import { html } from '@polymer/lit-element'
import { PageViewElement } from './page-view-element.js'

// These are the shared styles needed by this element.
import { PaperFontStyles, ViewStyles } from './shared-styles.js'

// Custom components
import '../components/device-tree-widget.js';
import '../components/info-window-widget.js';
import '../components/error-table-widget.js';
import '../components/history-log-widget.js';


class DashboardView extends PageViewElement {
  constructor () {
    super()
    // At startup, no device selected
    this.selectedDeviceInfo = {id: null, type:""}
  }

  render () {
    return html`
      ${PaperFontStyles}
      ${ViewStyles}
      <style>
      .dashboard-body {
        height: 80vh;
        overflow-y: scroll;
      }
      </style>
      <section>
        <div class="paper-font-display1 view-title">Dashboard</div>
        <div class="dashboard-body">
          <div class="flex-container">
            <div style="flex-grow: 6; height: 200%">
              <device-tree-widget @changed-selected-device="${this._onChangedSelectedDevice}"></device-tree-widget>
            </div>
            <div style="flex-grow: 1; height: 200%">
              <info-window-widget .deviceToRequest="${this.selectedDeviceInfo}"></info-window-widget>
            </div>
          </div>
          <div class="flex-container">
            <div style="flex-grow: 8">
              <error-table-widget @changed-selected-device="${this._onChangedSelectedDevice}"></error-table-widget>
            </div>
          </div>
          <div class="flex-container">
            <div style="flex-grow: 8">
              <history-log-widget></history-log-widget>
            </div>
          </div>
        </div>
      </section>
    `
  }

  _onChangedSelectedDevice(e){
    this.selectedDeviceInfo = e.detail
  }

  static get properties () {
    return {
      selectedDeviceInfo: { type: Object }
    }
  }
}

window.customElements.define('dashboard-view', DashboardView)
