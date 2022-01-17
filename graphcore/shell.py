# from GraphCore.model import GraphCoreModel
from graphcore.settings import GraphCoreSettings
from graphcore.thread_signal import GraphCoreThreadSignal
from networkml.network import NetworkClass, NetworkClassInstance, NetworkInstance
from networkml.network import ExtensibleWrappedAccessor
from networkml.lexer import NetworkParser
from networkml.interpreter import NetworkInterpreter
from networkml.interpretermanager import arm_interpreter
from networkml.network import MethodArmer
from networkml.specnetwork import SpecValidator
from graphcore.script_worker import get_script_worker
from graphcore.script_worker import ScriptWorker
import networkx as nx
import numpy as np
import time
import yaml
from graphcore.reporter import GraphCoreReporter
from PyQt5.QtCore import QThread, QMutex, pyqtSignal
import traceback


# yaml's presettings for load/dump
def represent_odict(dumper, instance):
    return dumper.represent_mapping('tag:yaml.org,2002:map', instance.items())

yaml.add_representer(dict, represent_odict)

def construct_odict(loader, node):
    return dict(loader.construct_pairs(node))

yaml.add_constructor('tag:yaml.org,2002:map', construct_odict)



# GraphCore's Context class
class GraphCoreContext(object):

    def __init__(self, G: nx.DiGraph, settings: GraphCoreSettings, reporter: GraphCoreReporter):
        self._G: nx.DiGraph = G
        self._settings = settings
        self._reporter = reporter
        self._variables = {}
        self._functions = {}
        self._filename = None
        self._dirty: bool = False
        scene_attrs = self.settings.setting('default-scene-attrs')
        for k in scene_attrs.keys():
            G.graph[k] = scene_attrs[k]
        if 'variables' not in self.graph.keys():
            self.graph['variables'] = {}
        if 'functions' not in self.graph.keys():
            self.graph['functions'] = {}
        if 'constraints' not in self.graph.keys():
            self.graph['constraints'] = {}
        if 'user-defined-functions' not in self.graph.keys():
            self.graph['user-defined-functions'] = {}

    @property
    def G(self):
        return self._G

    @property
    def settings(self) -> GraphCoreSettings:
        return self._settings

    @property
    def reporter(self) -> GraphCoreReporter:
        return self._reporter

    @property
    def graph(self):
        return self._G.graph

    @property
    def nodes(self):
        return self._G.nodes

    @property
    def edges(self):
        return self._G.edges

    @property
    def dirty(self):
        return self._dirty

    @dirty.setter
    def dirty(self, flag):
        self._dirty = flag

    @property
    def constraints(self):
        return self._G.graph['constraints']

    @property
    def groups(self):
        if 'groups' not in self._G.graph.keys():
            self._G.graph['groups'] = {}
        return self._G.graph['groups']

    @property
    def scripts(self):
        if 'scripts' not in self._G.graph.keys():
            self._G.graph['scripts'] = {}
            self.dirty = True
        return self._G.graph['scripts']

    @property
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, _filename):
        self._filename = _filename

    @property
    def variables(self):
        return self._variables

    @property
    def functions(self):
        return self._functions

    @property
    def user_defined_functions(self):
        return self.graph['user-defined-functions']

    # aid attributes
    def aid_attributes(self):
        if 'version' not in self.graph.keys():
            self.graph['version'] = "0.1.0"
            self.dirty = True
        attrs = self.settings.setting('default-scene-attrs')
        # types = sets.setting('scene-attr-types')
        for k in attrs.keys():
            if k not in self.graph.keys():
                self.graph[k] = attrs[k]
                self.dirty = True
        attrs = self.settings.setting('default-node-attrs')
        for n in self.nodes:
            t = self.nodes[n]['type']['value']
            a = attrs[t]
            for k in a.keys():
                if k not in self.nodes[n].keys():
                    self.nodes[n][k] = {}
                    self.nodes[n][k]['value'] = a[k]['value']
                    self.nodes[n][k]['type'] = a[k]['type']
                    self.nodes[n][k]['visible'] = a[k]['visible']
                    if 'list' in a[k].keys():
                        self.nodes[n][k]['list'] = a[k]['list']
                    self.dirty = True

        attrs = self.settings.setting('default-edge-attrs')
        for e in self.edges:
            t = self.edges[e[0], e[1]]['type']['value']
            a = attrs[t]
            for k in a.keys():
                if k not in self.edges[e[0], e[1]].keys():
                    self.edges[e[0], e[1]][k] = {}
                    self.edges[e[0], e[1]][k]['value'] = a[k]['value']
                    self.edges[e[0], e[1]][k]['type'] = a[k]['type']
                    self.edges[e[0], e[1]][k]['visible'] = a[k]['visible']
                    if 'list' in a[k].keys():
                        self.edges[e[0], e[1]]['list'] = a[k]['list']
                self.dirty = True
        if 'variables' not in self.graph.keys():
            self.graph['variables'] = {}
            self.dirty = True
        if 'functions' not in self.graph.keys():
            self.graph['functions'] = {}
            self.dirty = True
        if 'constraints' not in self.graph.keys():
            self.graph['constraints'] = {}
            self.dirty = True
        if 'user-defined-functions' not in self.graph.keys():
            self.graph['user-defined-functions'] = {}
            self.dirty = True

    # read_file
    def read_file(self, filename) -> None:
        try:
            with open(filename, "r") as f:
                G = yaml.load(f, Loader=yaml.Loader)
                # A = nx.nx_pydot.read_dot(filename)
                # G = nx.read_yaml(filename)
                if 'constraints' not in G.graph.keys():
                    G.graph['constraints'] = {}
                self._G = G
                self.aid_attributes()
        except Exception as ex:
            self.reporter.report("file open failed. no infection to current graph.")
            raise ex

    # open
    def open(self, filename):
        self.read_file(filename)
        self.filename = filename

    # save file
    def save(self, filename=None) -> None:
        if filename is None:
            if self.filename is None:
                self.reporter.report("filename not specified")
            else:
                # nx.write_yaml(self.G, self.filename)
                with open(filename,'w') as f:
                    yaml.dump(self.G, f)
                self.dirty = False
        else:
            # nx.write_yaml(self.G, filename)
            with open(filename,'w') as f:
                yaml.dump(self.G, f)
            self.filename = filename
            self.dirty = False

    # save as file
    def save_as(self, filename: str) -> None:
        self.save(filename)

    def function(self, name: str):
        return self._functions[name]

    def arity(self, name: str):
        return self._functions[name]['arity']

    def add_node(self, n):
        self._G.add_node(n)

    def remove_node(self, n):
        self._G.remove_node(n)

    def add_edge(self, u, v):
        self._G.add_edge(u, v)

    def remove_edge(self, u, v):
        self._G.remove_edge(u, v)

    def has_variable(self, var_name) -> bool:
        if var_name in self._variables.keys():
            return True
        return False

    def variable(self, name: str):
        return self._variables[name]

    def add_variable(self, name, var) -> None:
        self._variables[name] = var

    def remove_variable(self, name) -> None:
        self._variables.pop(name)

    def has_function(self, func_name) -> bool:
        if func_name in self._functions.keys():
            return True
        return False

    def add_function(self, name, func) -> None:
        self._functions[name] = func

    def remove_function(self, name) -> None:
        self._functions.pop(name)

    def has_constraint(self, constraint_name) -> bool:
        if constraint_name in self.graph['constraints'].keys():
            return True
        return False

    def add_constraint(self, name, constraint) -> None:
        self.graph['constraints'][name] = constraint

    def remove_constraint(self, name) -> None:
        self.graph['constraints'].pop(name)

    def check_constraint(self, constraint) -> bool:
        # FIXME
        return True

    def change_view(self, x, y, width, height):
        self.graph['x'] = x
        self.graph['y'] = y
        self.graph['w'] = width
        self.graph['h'] = height

    def collect_edges(self, n, node_is_source=True, node_is_target=True):
        edges = []
        for e in self.edges:
            if (node_is_source and n == e[0]) or (node_is_target and n == e[1]):
                edges.append(e)
        return edges


# GraphCore's shell class
class GraphCoreShell(object):

    HandlerPurged = 1
    HandlerChanged = 2
    HandlerNew = 3

    # initializer
    def __init__(self, settings: GraphCoreSettings):
        self._settings = settings
        self._graph = nx.DiGraph()
        self._default_reporter = GraphCoreReporter(lambda x: print(x))
        self._handler = None
        self._async_handler = None
        self._handlers = []
        self._reflection_map = {}
        self._reporters = []

    @property
    def settings(self) -> GraphCoreSettings:
        return self._settings

    @property
    def default_reporter(self) -> GraphCoreReporter:
        return self._default_reporter

    @property
    def handler(self):
        return self._handler

    @property
    def async_handler(self):
        return self._async_handler

    @property
    def handlers(self) -> list:
        return self._handlers

    def new_handler(self):
        context = GraphCoreContext(nx.DiGraph(), settings=self.settings, reporter=self.default_reporter)
        handler = GraphCoreContextHandler(context, self.default_reporter, self.settings)
        async_handler = GraphCoreAsyncContextHandler(context, self.default_reporter, self.settings)
        self.handlers.append((handler, async_handler))
        self._handler = handler
        self._async_handler = async_handler
        self.do_reflection(GraphCoreShell.HandlerNew, (handler, async_handler))

    def set_current_handler(self, _handler) -> None:
        for c in self.handlers:
            if c[0] == _handler or c[1] == _handler:
                self._handler = c[0]
                self._async_handler = c[1]
                self.do_reflection(GraphCoreShell.HandlerChanged, c)
                break

    def set_current_handler_by_name(self, filename: str) -> None:
        for pair in self.handlers:
            handler: GraphCoreContextHandler = pair[0]
            if handler.context.filename is not None and handler.context.filename == filename:
                self.set_current_handler(handler)
                break

    def purge_handler(self, _handler) -> None:
        handler_pair = None
        for c in self.handlers:
            if c[0] == _handler or c[1] == _handler:
                handler_pair = c
                break
        if handler_pair is not None:
            self.handlers.remove(c)
            self.do_reflection(GraphCoreShell.HandlerPurged, None)
        if len(self.handlers) != 0:
            self.do_reflection(GraphCoreShell.HandlerChanged, self.handlers[0])

    def set_reflection(self, event, func) -> None:
        self._reflection_map[event] = func

    def do_reflection(self, event, args) -> None:
        if event in self._reflection_map.keys():
            self._reflection_map[event](args)

    def remove_reflection(self, event) -> None:
        self._reflection_map.pop(event)

    def report(self, text) -> None:
        for r in self._reporters:
            r.report(text)

    def add_reporter(self, reporter: GraphCoreReporter) -> None:
        if reporter not in self._reporters:
            self._reporters.append(reporter)

    def remove_reporter(self, reporter) -> None:
        self._reporters.remove(reporter)

    # check if opened
    def opened(self, filename: str) -> bool:
        for pair in self.handlers:
            handler: GraphCoreContextHandler = pair[0]
            if handler.context.filename is not None and handler.context.filename == filename:
                return True
        return False

    # open file
    def open(self, filename) -> None:
        context = GraphCoreContext(nx.DiGraph(), settings=self.settings, reporter=self.default_reporter)
        context.open(filename)
        groups = context.groups
        for gid in groups.keys():
            SG = context.G.subgraph(groups[gid])
            groups[gid] = SG
        handler = GraphCoreContextHandler(context, settings=self.settings, reporter=self.default_reporter)
        async_handler = GraphCoreAsyncContextHandler(context, settings=self.settings, reporter=self.default_reporter)
        self.handlers.append((handler, async_handler))
        self.do_reflection(GraphCoreShell.HandlerNew, (handler, async_handler))


# GraphCore Shell Handler class
class GraphCoreContextHandler:
    NodeAdded = 1
    NodeUpdated = 2
    NodeRemoved = 3
    EdgeAdded = 4
    EdgeUpdated = 5
    EdgeRemoved = 6
    ViewUpdated = 7
    NodeSelected = 8
    NodeDeselected = 9
    EdgeSelected = 10
    EdgeDeselected = 11
    AllDeselected = 12
    ConstraintAdded = 13
    ConstraintUpdated = 14
    ConstraintRemoved = 15
    Loaded = 16
    UserDefinedFunctionAdded = 17
    UserDefinedFunctionUpdated = 18
    UserDefinedFunctionRemoved = 19
    UserScriptAdded = 20
    UserScriptDeleted = 21
    ElementsSelected = 22
    GroupCreated = 23
    GroupPurged = 24
    GroupRemoved = 25
    GroupSelected = 26
    GroupDeselected = 27
    ElementsAddSelect = 28

    def __init__(self, ctx: GraphCoreContext, reporter: GraphCoreReporter, settings: GraphCoreSettings):
        self._context = ctx
        self._reporter = reporter
        self._settings = settings
        self._reflection_map = {}
        self._selection = {}
        self._selected_constraints = []
        self._extras = {}
        self._meta = None
        self._clazz = None
        self._toplevel = None
        self._selected_elements = ()
        self._copy_buf = {"nodes": {}, "edges": {}, "groups": {}}
        self._script_handler = None
        self.setup_nml_objects()
        self.install_builtin_functions()

    @property
    def script_handler(self):
        return self._script_handler

    def set_script_handler(self, sh):
        self._script_handler = sh

    @property
    def element_to_item(self):
        return self.extras['element_to_item']

    def set_selected_elements(self, elems):
        self._selected_elements = elems

    @property
    def selected_elements(self):
        elems = []
        for e in self.element_to_item.keys():
            i = self.element_to_item[e]
            if i.is_selected:
                elems.append(e)
        return tuple(elems)

    @property
    def selected_nodes(self):
        from graphcore.graphicsitem import GraphCoreNodeItemInterface
        nodes = []
        for e in self.element_to_item.keys():
            i = self.element_to_item[e]
            if isinstance(i, GraphCoreNodeItemInterface) and i.is_selected:
                nodes.append(e)
        return tuple(nodes)

    @property
    def selected_edges(self):
        from graphcore.graphicsitem import GraphCoreEdgeItemInterface
        edges = []
        for e in self.element_to_item.keys():
            i = self.element_to_item[e]
            if isinstance(i, GraphCoreEdgeItemInterface) and i.is_selected:
                edges.append(e)
        return tuple(edges)

    @property
    def selected_groups(self):
        from graphcore.graphicsitem import GCItemGroup
        groups = []
        for e in self.element_to_item.keys():
            i = self.element_to_item[e]
            if isinstance(i, GCItemGroup):
                groups.append(e)
        return tuple(groups)

    @property
    def copy_buf(self) -> dict:
        return self._copy_buf

    def create_group(self):
        members = [_ for _ in self.selected_nodes]
        members.extend(self.selected_edges)
        self.add_group(members)

    def add_group(self, members):
        SG = self.context.G.subgraph(members)
        groups = self.context.groups
        gid = 1
        for i in range(len(groups.keys())):
            if str(i) not in groups.keys():
                gid = i
                break
        gid = "g{}".format(gid)
        groups[gid] = SG
        self.context.dirty = True
        self.do_reflection(GraphCoreContextHandler.GroupCreated, gid)

    def remove_group(self, gid):
        SG = self.context.G.graph['groups'][gid]
        self.context.G.graph['groups'].pop(gid)
        nodes = SG.nodes
        edges = SG.edges
        for n in nodes:
            self.remove_node(n)
        for e in edges:
            self.remove_edge(e[0], e[1])
        self.do_reflection(GraphCoreContextHandler.GroupRemoved, gid)

    def purge_group(self, gid=None):
        if gid is None:
            gids = self.selected_groups
        else:
            gids = (gid,)
        for g in gids:
            SG = self.context.groups[g]
            self.context.groups.pop(g)
            self.context.dirty = True
            self.do_reflection(GraphCoreContextHandler.GroupPurged, g)

    def copy(self):
        nodes = {}
        edges = {}
        for n in self.selected_nodes:
            if isinstance(n, str):
                nodes[n] = {}
                for k in self.context.G.nodes[n].keys():
                    nodes[n][k] = self.context.G.nodes[n][k]
            else:
                edges[n] = {}
                for k in self.context.G.edges[n[0], n[1]].keys():
                    edges[n][k] = self.context.G.edges[n[0], n[1]][k]
        self.copy_buf["nodes"] = nodes
        self.copy_buf["edges"] = edges

    def cut(self):
        self.copy()
        selected_elements = self.selected_elements
        self.set_selected_elements(())
        for n in selected_elements:
            if n is not tuple:
                self.remove_node(n)
            else:
                self.remove_edge(n[0], n[1])

    def paste(self):
        node_map = {}
        for v in self.copy_buf["nodes"].keys():
            node_map[v] = v
        for e in self.copy_buf["edges"].keys():
            node_map[e[0]] = e[0]
            node_map[e[1]] = e[1]
        for v in self.copy_buf["nodes"].keys():
            n = self.new_node(self.copy_buf["nodes"][v])
            node_map[v] = n
        for e in self.copy_buf["edges"].keys():
            u = node_map[e[0]]
            v = node_map[e[1]]
            self.add_edge(u, v, self.copy_buf["edges"][e])

    def setup_nml_objects(self):
        self._meta: NetworkClassInstance = NetworkClass(None, "GraphCore")
        clazz_sig = "{}[{}]".format("GraphCore", 1)
        embedded = ()
        args = ()
        self._meta.set_running(True)
        self._clazz: NetworkClassInstance = self._meta(self._meta, (clazz_sig, embedded, args))
        self._meta.set_running(False)
        sig = "{}.{}".format(self._clazz.signature, self._clazz.next_instance_id)
        initializer_args = ()
        embedded = [("G", self.context.G)]
        self._clazz.set_running(True)
        self._toplevel: NetworkInstance = self._clazz(self._clazz, (sig, embedded, initializer_args))
        self._clazz.set_running(False)
        self._toplevel.set_stack_enable(True)
        # validator/evaluator
        validator = SpecValidator(owner=self._toplevel)
        self._toplevel.set_validator(validator)
        arm_interpreter(self._toplevel)
        self._toplevel.set_running(True)
        # methods implementation
        self.implement_toplevel_methods()

    def implement_toplevel_methods(self):
        m = ExtensibleWrappedAccessor(self._toplevel, "sin", None,
                                      lambda ao, c, eo, ca, ea: np.sin(ca[0]), globally=True)
        self._toplevel.declare_method(m, globally=True)
        m = ExtensibleWrappedAccessor(self._toplevel, "cos", None,
                                      lambda ao, c, eo, ca, ea: np.cos(ca[0]), globally=True)
        self._toplevel.declare_method(m, globally=True)
        m = ExtensibleWrappedAccessor(self._toplevel, "tan", None,
                                      lambda ao, c, eo, ca, ea: np.tan(ca[0]), globally=True)
        self._toplevel.declare_method(m, globally=True)
        m = ExtensibleWrappedAccessor(self._toplevel, "arcsin", None,
                                      lambda ao, c, eo, ca, ea: np.arcsin(ca[0]), globally=True)
        self._toplevel.declare_method(m, globally=True)
        m = ExtensibleWrappedAccessor(self._toplevel, "arccos", None,
                                      lambda ao, c, eo, ca, ea: np.arccos(ca[0]), globally=True)
        self._toplevel.declare_method(m, globally=True)
        m = ExtensibleWrappedAccessor(self._toplevel, "arctan", None,
                                      lambda ao, c, eo, ca, ea: np.arctan(ca[0]), globally=True)
        self._toplevel.declare_method(m, globally=True)
        m = ExtensibleWrappedAccessor(self._toplevel, "exp", None,
                                      lambda ao, c, eo, ca, ea: np.exp(ca[0]), globally=True)
        self._toplevel.declare_method(m, globally=True)
        m = ExtensibleWrappedAccessor(self._toplevel, "log", None,
                                      lambda ao, c, eo, ca, ea: np.log(ca[0]), globally=True)
        self._toplevel.declare_method(m, globally=True)
        m = ExtensibleWrappedAccessor(self._toplevel, "pow", None,
                                      lambda ao, c, eo, ca, ea: np.power(ca[0], ca[1]), globally=True)
        self._toplevel.declare_method(m, globally=True)
        m = ExtensibleWrappedAccessor(self._toplevel, "sleep", None,
                                      lambda ao, c, eo, ca, ea: time.sleep(ca[0]), globally=True)
        self._toplevel.declare_method(m, globally=True)
        m = ExtensibleWrappedAccessor(self._toplevel, "print", self.reporter,
                                      lambda ao, c, eo, ca, ea: eo.report(" ".join([str(_) for _ in ca])),
                                      globally=True)
        self._toplevel.declare_method(m, globally=True)
        m = ExtensibleWrappedAccessor(self._toplevel, "append", None,
                                      lambda ao, c, eo, ca, ea: ca[0].append(ca[1]),
                                      globally=True)
        self._toplevel.declare_method(m, globally=True)
        m = ExtensibleWrappedAccessor(self._toplevel, "len", None,
                                      lambda ao, c, eo, ca, ea: len(ca[0]),
                                      globally=True)
        self._toplevel.declare_method(m, globally=True)
        m = ExtensibleWrappedAccessor(self._toplevel, "keys", None,
                                      lambda ao, c, eo, ca, ea: ca[0].keys())
        self._toplevel.declare_method(m, globally=True)
        m = ExtensibleWrappedAccessor(self._toplevel, "nodes", None,
                                      lambda ao, c, eo, ca, ea: [_ for _ in self.context.G.nodes],
                                      globally=True)
        m = ExtensibleWrappedAccessor(self._toplevel, "edges", None,
                                      lambda ao, c, eo, ca, ea: [_ for _ in self.context.G.edges],
                                      globally=True)
        self._toplevel.declare_method(m, globally=True)
        m = ExtensibleWrappedAccessor(self._toplevel, "node_attr_keys", None,
                                      lambda ao, c, eo, ca, ea: [_ for _ in self.context.G.nodes[ca[0]].keys()],
                                      globally=True)
        self._toplevel.declare_method(m, globally=True)
        m = ExtensibleWrappedAccessor(self._toplevel, "get_node_value", None,
                                      lambda ao, c, eo, ca, ea: self.node_attr(ca[0], ca[1]),
                                      globally=True)
        self._toplevel.declare_method(m, globally=True)
        m = ExtensibleWrappedAccessor(self._toplevel, "set_node_value", None,
                                      lambda ao, c, eo, ca, ea: self.change_node_attr(ca[0], *ca[1:]),
                                      globally=True)
        self._toplevel.declare_method(m, globally=True)
        m = ExtensibleWrappedAccessor(self._toplevel, "get_edge_value", None,
                                      lambda ao, c, eo, ca, ea: self.edge_attr(ca[0], ca[1], ca[2]),
                                      globally=True)
        self._toplevel.declare_method(m, globally=True)
        m = ExtensibleWrappedAccessor(self._toplevel, "set_edge_value", None,
                                      lambda ao, c, eo, ca, ea: self.change_edge_attr(ca[0], ca[1], ca[2], ca[3]),
                                      globally=True)
        self._toplevel.declare_method(m, globally=True)
        m = ExtensibleWrappedAccessor(self.toplevel, "run_system_script", None,
                                      lambda ao, c, eo, ca, ea: self.run_system_script(ca[0]),
                                      globally=True)
        self.toplevel.declare_method(m, globally=True)
        m = ExtensibleWrappedAccessor(self.toplevel, "run_user_script", None,
                                      lambda ao, c, eo, ca, ea: self.run_user_script(ca[0]),
                                      globally=True)
        self.toplevel.declare_method(m, globally=True)
        # armer = MethodArmer()
        # methods_config = self.settings.setting("system-methods")
        # for sig in methods_config.keys():
        #     armer.arm_method(sig, self._toplevel, self._clazz, self._meta, methods_config[sig])

    def emit_main_window_command(self, command_id, *args):
        pass

    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, ctx):
        self._context = ctx

    @property
    def reflection_map(self):
        return self._reflection_map

    @property
    def selected_constraints(self) -> list:
        return self._selected_constraints

    @property
    def reporter(self):
        return self._reporter

    @reporter.setter
    def reporter(self, _reporter):
        self._reporter = _reporter

    @property
    def settings(self) -> GraphCoreSettings:
        return self._settings

    @property
    def extras(self):
        return self._extras

    @property
    def toplevel(self) -> NetworkInstance:
        return self._toplevel

    # save context
    def save(self, filename=None):
        groups = self.context.groups
        gr = {}
        for gid in groups.keys():
            gr[gid] = groups[gid]
            groups[gid] = []
            for n in gr[gid].nodes:
                groups[gid].append(n)
            for e in gr[gid].edges:
                groups[gid].append(e)
        self.context.save(filename)
        for gid in groups.keys():
            groups[gid] = gr[gid]

    # clear user-defined variables and functions
    def clear_user_defined(self):
        self._context.variables.clear()
        self._context.user_defined_functions.clear()
        self.install_builtin_functions()

    # clear external action invoked from handler
    def clear_reflectios(self):
        self._reflection_map = {}

    # set external action invoked from shell
    def set_reflection(self, event, action):
        self._reflection_map[event] = action

    # remove external action invoked from shell
    def remove_reflection(self, event):
        self._reflection_map.pop(event)

    # do event action
    def do_reflection(self, event, obj):
        from graphcore.script_worker import GCScriptWorker
        script_handler: GCScriptWorker = self.script_handler
        if event in self.reflection_map.keys():
            # FIXME
            func = lambda x: self.reflection_map[event](obj)
            sig = GraphCoreThreadSignal(event, None, func, None)
            script_handler.main_thread_command.emit(sig)
            #self.reflection_map[event](obj)

    def node_id_to_data(self, n):
        return self.context.nodes[n]

    def node_data_to_id(self, data):
        nodes = self.context.nodes
        for n in nodes:
            node = nodes[n]
            # check attribute match
            unmatched = False
            for k in data.keys():
                if k in node.keys():
                    if data[k] != node[k]:
                        unmatched = True
                        break
                else:
                    unmatched = True
                    break
            if not unmatched:
                return n
        return None

    def edge_id_to_data(self, u, v):
        return self.context.edges[u, v]

    def edge_data_to_id(self, data):
        for e in self.context.edges:
            if self.context.edges[e[0], e[1]] == data:
                return e
        return None

    # get new node id
    def next_node_id(self):
        _id = 0
        for n in self.context.nodes:
            if int(n) > _id:
                _id = int(n)
        _id += 1
        return str(_id)

    def has_node(self, n):
        if n in self.context.nodes:
            return True
        return False

    def new_node(self, attrs=None):
        new_id = self.next_node_id()
        self.add_node(new_id, attrs)
        return new_id

    def add_node(self, n, attrs=None):
        self.context.add_node(n)
        if attrs is None:
            attrs = self.settings.setting('default-node-attrs')
        for k in attrs.keys():
            self.context.nodes[n][k] = attrs[k]
        self.context.dirty = True
        self.do_reflection(GraphCoreContextHandler.NodeAdded, n)

    def update_node(self, n):
        self.do_reflection(GraphCoreContextHandler.NodeUpdated, n)

    def remove_node(self, n):
        self.context.remove_node(n)
        self.context.dirty = True
        self.do_reflection(GraphCoreContextHandler.NodeRemoved, n)

    def has_edge(self, u, v):
        if (u, v) in self.context.edges:
            return True
        return False

    def add_edge(self, u, v, attrs=None):
        self.context.add_edge(u, v)
        if attrs is None:
            attrs = self.settings.setting('default-edge-attrs')
        for k in attrs.keys():
            self.context.edges[u, v][k] = attrs[k]
        self.context.dirty = True
        self.do_reflection(GraphCoreContextHandler.EdgeAdded, (u, v))

    def update_edge(self, u, v):
        self.do_reflection(GraphCoreContextHandler.EdgeUpdated, (u, v))

    def remove_edge(self, u, v):
        self.context.remove_edge(u, v)
        self.context.dirty = True
        self.do_reflection(GraphCoreContextHandler.EdgeRemoved, (u, v))

    def node_attr(self, n, a):
        return self.context.nodes[n][a]['value']

    def change_node_attr(self, n, *args):
        attrs_len = int(len(args)/2)
        for i in range(attrs_len):
            a = args[i*2]
            v = args[i*2+1]
            self.context.nodes[n][a]['value'] = v
        self.context.dirty = True
        # get_script_worker().main_window_command.emit(GraphCoreThreadSignal(GraphCoreContextHandler.NodeUpdated, n, None))
        self.do_reflection(GraphCoreContextHandler.NodeUpdated, n)

    def edge_attr(self, u, v, a):
        return self.context.edges[u, v][a]['value']

    def change_edge_attr(self, u, v, *args):
        arg_len = int(len(args)/2)
        for i in range(arg_len):
            a = args[i*2]
            v = args[i*2+1]
            self.context.edges[u, v][a]['value'] = v
            self.context.dirty = True
        self.do_reflection(GraphCoreContextHandler.EdgeUpdated, (u, v))

    def change_view(self, x, y, w, h):
        self.context.change_view(x, y, w, h)
        self.context.dirty = True
        self.do_reflection(GraphCoreContextHandler.ViewUpdated, (x, y, w, h))

    def change_script(self, sid, attr, value):
        self.context.scripts[sid][attr] = value
        self.context.dirty = True

    def loaded(self):
        for n in self.context.nodes:
            self.do_reflection(GraphCoreContextHandler.NodeAdded, n)
        for e in self.context.edges:
            self.do_reflection(GraphCoreContextHandler.EdgeAdded, e)
        for c in self.context.constraints:
            self.do_reflection(GraphCoreContextHandler.ConstraintAdded, c)
        for gid in self.context.groups.keys():
            self.do_reflection(GraphCoreContextHandler.GroupCreated, gid)
        x = self.context.graph['x']
        y = self.context.graph['y']
        w = self.context.graph['w']
        h = self.context.graph['h']
        self.do_reflection(GraphCoreContextHandler.ViewUpdated, (x, y, w, h))
        for f in self.context.user_defined_functions:
            script = self.context.user_defined_functions[f]
            self.do_reflection(GraphCoreContextHandler.UserDefinedFunctionAdded, (f, script))

    def new_user_defined_function_id(self):
        max_fid = 0
        for fid in self.context.user_defined_functions.keys():
            fid = int(fid[1:])
            if max_fid < fid:
                max_fid = fid
        max_fid += 1
        max_fid = "f{}".format(max_fid)
        return max_fid

    def add_user_defined_function(self, fid, script: str):
        x = self.context.user_defined_functions[fid] = str
        self.context.dirty = True
        self.do_reflection(GraphCoreContextHandler.UserDefinedFunctionAdded, (fid, script))

    def update_user_defined_function(self, fid, script: str):
        x = self.context.user_defined_functions[fid] = str
        self.context.dirty = True
        self.do_reflection(GraphCoreContextHandler.UserDefinedFunctionUpdated, (fid, script))

    def remove_user_defined_function(self, fid, script: str):
        x = self.context.user_defined_functions[fid] = str
        self.context.dirty = True
        self.do_reflection(GraphCoreContextHandler.UserDefinedFunctionRemoved, fid)

    def new_constraint(self):
        m: int = 0
        for k in self.context.constraints.keys():
            if m < int(k[1:]):
                m = int(k[1:])
        m += 1
        cid = "c{}".format(m)
        constraint = {
            'equation': '',
            'description': '',
            'enabled': False
        }
        self.context.add_constraint(cid, constraint)
        self.context.dirty = True
        self.do_reflection(GraphCoreContextHandler.ConstraintAdded, cid)

    def change_constraint(self, cid, attr, value):
        self.context.constraints[cid][attr] = value
        self.context.dirty = True
        self.do_reflection(GraphCoreContextHandler.ConstraintUpdated, cid)

    def remove_constraint(self, cid):
        self.context.constraints.pop(cid)
        self.context.dirty = True
        self.do_reflection(GraphCoreContextHandler.ConstraintRemoved, cid)

    def remove_selected_constraints(self):
        for cid in self.selected_constraints:
            self.remove_constraint(cid)

    def collect_edges(self, n, node_is_source=True, node_is_target=True):
        return self.context.collect_edges(n, node_is_source=node_is_source, node_is_target=node_is_target)

    def install_builtin_functions(self):
        # self._functions['reset'] = {
        #     'call': lambda x: self._shell.reset_context(),
        #     'arity': 0
        # }
        self._context.add_function('node_id', {
            'call': lambda x: self.node_data_to_id(x[0]),
            'arity': 1
        })
        self._context.add_function('node_data', {
            'call': lambda n: self.node_id_to_data(n[0]),
            'arity': 1
        })
        self._context.add_function('edge_id', {
            'call': lambda x: self.edge_data_to_id(x[0]),
            'arity': 1
        })
        self._context.add_function('edge_data', {
            'call': lambda e: self.edge_id_to_data(e[0]),
            'arity': 1
        })
        self._context.add_function('new_node', {
            'call': lambda x: self.new_node(),
            'arity': 0
        })
        self._context.add_function('add_node', {
            'call': lambda x: self.add_node(x[0]),
            'arity': 1
        })
        self._context.add_function('update_node', {
            'call': lambda x: self.update_node(x[0]),
            'arity': 3
        })
        self._context.add_function('change_node_attr', {
            'call': lambda x: self.change_node_attr(x[0], x[1], x[2]),
            'arity': 3
        })
        self._context.add_function('remove_node', {
            'call': lambda x: self.remove_node(x[0]),
            'arity': 1
        })
        self._context.add_function('add_edge', {
            'call': lambda x: self.add_edge(x[0], x[1]),
            'arity': 2
        })
        self._context.add_function('update_edge', {
            'call': lambda x: self.update_edge(x[0], x[1]),
            'arity': 3
        })
        self._context.add_function('change_edge_attr', {
            'call': lambda x: self.change_edge_attr(x[0], x[1], x[2], x[3]),
            'arity': 4
        })
        self._context.add_function('remove_edge', {
            'call': lambda x: self.remove_edge(x[0], x[1]),
            'arity': 2
        })
        self._context.add_function('change_view', {
            'call': lambda x: self.change_view(x[0], x[1], x[2], x[3]),
            'arity': 4
        })

    def call(self, func, args):
        function = self.context.function(func)
        return function['call'](args)

    def move_node_by(self, n, dx, dy):
        self.context.nodes[n]['x']['value'] += dx
        self.context.nodes[n]['y']['value'] += dy
        self.context.dirty = True
        self.do_reflection(GraphCoreContextHandler.NodeUpdated, n)

    def move_group_by(self, g, dx, dy):
        edges = []
        sg = self.context.groups[g]
        for n in sg.nodes:
            self.context.nodes[n]['x']['value'] += dx
            self.context.nodes[n]['y']['value'] += dy
            self.context.dirty = True
            for v in self.context.G.successors(n):
                if (n, v) not in edges:
                    edges.append((n, v))
            for v in self.context.G.predecessors(n):
                if (v, n) not in edges:
                    edges.append((v, n))
            # self.do_reflection(GraphCoreContextHandler.NodeUpdated, n)
        for e in edges:
            self.do_reflection(GraphCoreContextHandler.EdgeUpdated, e)

    def deselect_all(self):
        self.do_reflection(GraphCoreContextHandler.AllDeselected, None)

    def select_elements(self, es):
        self.do_reflection(GraphCoreContextHandler.ElementsSelected, es)

    def add_select_elements(self, es):
        self.do_reflection(GraphCoreContextHandler.ElementsAddSelect, es)

    def select_node(self, n):
        # print("select_node", n)
        self.do_reflection(GraphCoreContextHandler.NodeSelected, n)

    def deselect_node(self, n):
        self.set_selected_elements(())
        self.do_reflection(GraphCoreContextHandler.NodeDeselected, n)

    def select_edge(self, u, v):
        self.do_reflection(GraphCoreContextHandler.EdgeSelected, (u, v))

    def deselect_edge(self, u, v):
        self.set_selected_elements(())
        self.do_reflection(GraphCoreContextHandler.EdgeDeselected, (u, v))

    def select_group(self, g):
        self.do_reflection(GraphCoreContextHandler.ElementsSelected, (g))

    def deselect_group(self, g):
        self.set_selected_elements(())
        self.do_reflection(GraphCoreContextHandler.GroupDeselected, g)

    def select_constraint(self, cid):
        if cid not in self.selected_constraints:
            self.selected_constraints.append(cid)

    def run_system_script(self, sid):
        scripts = self.settings.setting('system-scripts')
        if sid not in scripts.keys():
            return
        enabled = scripts[sid]['enabled']
        if enabled:
            script = scripts[sid]['script']
            interpret = self.toplevel.get_method(self.toplevel, "interpret")
            interpret(self.toplevel, (script, "--safe=False"))

    def run_user_script(self, sid):
        scripts = self.context.graph['scripts']
        if sid not in scripts.keys():
            return
        enabled = scripts[sid]['enabled']
        if enabled:
            script = scripts[sid]['script']
            interpret = self.toplevel.get_method(self.toplevel, "interpret")
            interpret(self.toplevel, (script, "--safe=False"))

    def run(self, command):
        command()


# GraphCore's Asynchronous Handler Thread class
class GraphCoreAsyncContextHandlerThread(QThread):

    Signal: pyqtSignal = pyqtSignal(GraphCoreThreadSignal)

    Report: int = 1
    AsyncCall: int = 2
    # StateChanged: int = 3

    def __init__(self, handler: GraphCoreContextHandler, reporter: GraphCoreReporter, interval: int = 1000):
        super().__init__()
        self._handler = handler
        self._interval = interval
        self._reporter = reporter
        self._mutex = QMutex()
        self._command_queue = []

    def lock_command_queue(self):
        self._mutex.lock()

    def unlock_command_queue(self):
        self._mutex.unlock()

    def push_command(self, command):
        self.lock_command_queue()
        self._command_queue.append(command)
        self.unlock_command_queue()

    def pull_command(self):
        command = None
        self.lock_command_queue()
        if len(self._command_queue) > 0:
            command = self._command_queue[0]
            self._command_queue = self._command_queue[1:]
        self.unlock_command_queue()
        return command

    def run(self):
        while True:
            command = self.pull_command()
            if command is not None:
                command()
                # self._handler.execute_command(command, reporter=self._reporter)
            else:
                self.usleep(self._interval)
                # print("interval {}[milli sec] passed".format(self._interval))
        pass


# GraphCore Asynchronous Shell Handler
class GraphCoreAsyncContextHandler(GraphCoreContextHandler):
    def __init__(self, context: GraphCoreContext, reporter: GraphCoreReporter, settings: GraphCoreSettings):
        super().__init__(context, reporter, settings)
        self.install_builtin_functions()
        # self._thread_reporter: GraphCoreReporter = GraphCoreReporter()
        # self._thread_reporter.set_report_func(lambda x: self.report(str(x)))
        self._thread = GraphCoreAsyncContextHandlerThread(self, self.reporter)
        self._thread.Signal.connect(self.signal_notified)
        self._thread.start()

    def install_builtin_functions(self):
        super().install_builtin_functions()
        self.context.add_function('sleep', lambda x: self._thread.sleep(x))
        self.context.add_function('usleep', lambda x: self._thread.usleep(x))

    def async_call(self, func, args):
        function = self.context.function(func)
        sig = GraphCoreThreadSignal(GraphCoreAsyncContextHandlerThread.AsyncCall,
                                    data=args, func=function['call'], args=args)
        self._thread.Signal.emit(sig)
        return sig.result

    def call(self, func, args):
        return self.async_call(func, args)

    def run(self, command):
        self._thread.push_command(command)

    def signal_notified(self, sig: GraphCoreThreadSignal):
        # Async Update
        if sig.signal == GraphCoreAsyncContextHandlerThread.AsyncCall:
            result = sig.func(sig.args)
            sig.result = result

