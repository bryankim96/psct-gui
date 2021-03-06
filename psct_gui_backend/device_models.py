"""Module for OPC UA device mirroring classes."""
from abc import ABC, abstractmethod
import logging

logger = logging.getLogger(__name__)


class BaseDeviceModel(ABC):
    @abstractmethod
    def __init__(self, socketio_server=None):
        """Instantiate a BaseDeviceModel instance."""
        self._socketio_server = socketio_server

        self.children = {}
        self.parents = []

    @property
    @abstractmethod
    def data(self):
        """dict: Dictionary of data property names (str) and values."""
        pass

    @property
    @abstractmethod
    def errors(self):
        """dict: Dictionary of error property names (str) and values."""
        pass

    @property
    @abstractmethod
    def methods(self):
        """list: List of method names."""
        pass

    @property
    @abstractmethod
    def name(self):
        """str: Name of device."""
        pass

    @property
    @abstractmethod
    def id(self):
        """str: Unique device id."""
        pass

    @property
    @abstractmethod
    def type(self):
        """str: Name of this device's type."""
        pass

    @property
    @abstractmethod
    def position(self):
        """int: Position of the object (usually relative to parent)."""
        pass

    @property
    def position_info(self):
        """dict: Dictionary of extra position info relevant to the specific object type."""
        return {}

    @property
    @abstractmethod
    def serial(self):
        """str: Serial number of the device object."""
        pass

    @property
    def all_children(self):
        """list of BaseDeviceModels: Flat list of all children devices."""
        return [c for l in self.children.values() for c in l]

    @abstractmethod
    def set_data(self, name, value):
        pass

    @abstractmethod
    def set_error(self, name, value):
        pass

    @property
    def all_data(self):
        return {
            'id': self.id,
            'name': self.name,
            'type': self.type,
            'position': self.position,
            'extra_position_info': self.position_info,
            'serial': self.serial,
            'data': self.data,
            'errors': self.errors,
            'methods': self.methods,
            'children': {type: [model.id for model in self.children[type]]
                         for type in self.children},
            'parents': [model.id for model in self.parents]
        }

    def add_child(self, child):
        """Add a BaseDeviceModel as a child of this device.

        Parameters
        ----------
        child : psct_gui.backend.device_models.OPCUADeviceModel
            OPCUADeviceModel to add as a child.

        """
        if child.type not in self.children:
            self.children[child.type] = []
        self.children[child.type].append(child)
        child.parents.append(self)

    # Calls an object method and returns its return value
    @abstractmethod
    def call_method(self, method_name, *args):
        pass

    @abstractmethod
    def call_stop(self):
        pass
