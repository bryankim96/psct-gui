# pSCT Alignment Control GUI
Web GUI for pSCT mirror panel alignment monitoring/control. Built with a Python backend using OPC UA, socket.io, gevent, and Pyramid. The frontend implementation is with D3.js, Bootstrap 4, and DataTables for visualization/styling.

## Dependencies/Packages

* Python (backend)
  * [python-socketio](https://github.com/miguelgrinberg/python-socketio)
  * [python-opcua](https://github.com/FreeOpcUa/python-opcua)
  * [Pyramid](https://github.com/Pylons/pyramid)
* Javascript (frontend)
  * [D3.js](https://github.com/d3/d3)
  * [webpack](https://github.com/webpack/webpack)
  * [Bootstrap 4](https://github.com/twbs/bootstrap)
  * [jQuery](https://github.com/jquery/jquery)
  * [DataTables](https://github.com/DataTables/DataTables)
  * [Bootstrap-treeview](https://github.com/patternfly/patternfly-bootstrap-treeview)
* Other
  * libevent 2.1.8

## Installation and Setup

**TODO**

## Major Features/To Do:

 - [x] Web server functionality
    - [x] Base Pyramid server functionality (views)
    - [x] Gevent/greenlet server (using gunicorn)
 - [ ] User Authentication/Management
    - [x] Database support (local SQLite)
    - [ ] Database support (integrate with pSCT MySQL database)
    - [x] Login/logout/forbidden views
    - [x] Two-level permissions (User + Admin) w/ password hashing
    - [ ] Implement active/read-only mode
    - [ ] Restrict UI access based on permissions
 - [x] Core
    - [x] socket.io namespaces
    - [x] DeviceModel (Python object-based data model/ OPC UA -> socket.io connector)
    - [x] TelescopeModel
    - [x] MirrorModel
    - [x] EdgeModel
    - [x] ActuatorModel
    - [x] PanelModel
    - [x] MPESModel
    - [x] Method calling
    - [ ] Method interrupt/stop
    - [x] Master initialization function (traverse OPC UA tree and initialize all models)
 - [ ] Error Handling
    - [x] Error Log Table View (DataTables)
    - [ ] Error Modals/Alerts
    - [ ] Auto stop/interrupt on error
 - [x] Device Tree View (Bootstrap-treeview)
    - [x] Support for flat and tree view
    - [x] Status badges
    - [x] Clickable links to detailed device info
 - [x] Device Info Panel View
 - [ ] History Logging
    - [ ] Backend (server-side in-memory or DB)
    - [ ] History Log Table View (DataTables)
  - [ ] Mirror-level view/interface (D3.js)
    - [x] Display mirror panels as D3 objects
    - [ ] Display edges, MPES, actuators
    - [ ] Display component status via color
    - [x] On-hover tooltips
    - [ ] Detailed info on-click (go to children)
    - [ ] Side info window
    
## Approximate Timeline:

- [x] (~ 9/25/2018) Complete core functionality (all DeviceModels, initialization function for device tree)
- [x] (~ 9/28/2018) Complete Device Tree functionality (Model + Front-end)
- [x] (~ 10/5/2018) Complete Info window functionality (Model + Front-end)
- [ ] (~ 10/12/2018) Complete Error Log and alerts functionality (Model + Front-end)
- [ ] (~ 10/19/2018) Complete Telescope Mirror View functionality (Model + Front-end)
- [ ] (~ 10/28/2018) Complete User authentication and history log functionality

## Known Issues/Troubleshooting

## References

* CTA Operator GUI Prototype (@ DESY): [https://github.com/IftachSadeh/ctaOperatorGUI](https://github.com/IftachSadeh/ctaOperatorGUI)
  * [Paper 1](https://arxiv.org/abs/1608.03595)
  * [Paper 2](https://arxiv.org/abs/1710.07117)

* Python-socketio Documentation: [https://python-socketio.readthedocs.io/en/latest/](https://python-socketio.readthedocs.io/en/latest/)
* Python OPC UA Documentation: [https://python-opcua.readthedocs.io/en/latest/](https://python-opcua.readthedocs.io/en/latest/)
* Pyramid Web Framework Documentation: [https://docs.pylonsproject.org/projects/pyramid/en/latest/](https://docs.pylonsproject.org/projects/pyramid/en/latest/)

* D3.js wiki: [https://github.com/d3/d3/wiki](https://github.com/d3/d3/wiki)
* Webpack Documentation: [https://webpack.js.org/concepts/](https://webpack.js.org/concepts/)
* Bootstrap 4 Documentation: [https://getbootstrap.com/docs/4.1/getting-started/introduction/](https://getbootstrap.com/docs/4.1/getting-started/introduction/)
* jQuery Documentation: [https://api.jquery.com/](https://api.jquery.com/)
* DataTables Documentation: [https://datatables.net/manual/](https://datatables.net/manual/)