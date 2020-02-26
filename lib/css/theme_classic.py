#  https://base64.guru/converter/encode/image/gif
theme_classic = """.x-size-monitored {
    position: relative
}



.x-size-monitors {
    position: absolute;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    visibility: hidden;
    overflow: hidden
}

.x-size-monitors > * {
    width: 100%;
    height: 100%;
    overflow: hidden
}

.x-size-monitors.scroll > *.shrink::after {
    content: '';
    display: block;
    width: 200%;
    height: 200%;
    min-width: 1px;
    min-height: 1px
}

.x-size-monitors.scroll > *.expand::after {
    content: '';
    display: block;
    width: 100000px;
    height: 100000px
}

.x-size-monitors.overflowchanged > *.shrink > * {
    width: 100%;
    height: 100%
}

.x-size-monitors.overflowchanged > *.expand > * {
    width: 200%;
    height: 200%
}

.x-size-change-detector {
    visibility: hidden;
    position: absolute;
    left: 0;
    top: 0;
    z-index: -1;
    width: 100%;
    height: 100%;
    overflow: hidden
}

.x-size-change-detector > * {
    visibility: hidden
}

.x-size-change-detector-shrink > * {
    width: 200%;
    height: 200%
}

.x-size-change-detector-expand > * {
    width: 100000px;
    height: 100000px
}

@-webkit-keyframes x-paint-monitor-helper {
    from {
        zoom: 1
    }
    to {
        zoom: 1
    }
}

@keyframes x-paint-monitor-helper {
    from {
        zoom: 1
    }
    to {
        zoom: 1
    }
}

.x-paint-monitored {
    position: relative
}

.x-paint-monitor {
    width: 0 !important;
    height: 0 !important;
    visibility: hidden
}

.x-paint-monitor.cssanimation {
    -webkit-animation-duration: 0.0001ms;
    -webkit-animation-name: x-paint-monitor-helper;
    animation-duration: 0.0001ms;
    animation-name: x-paint-monitor-helper
}

.x-paint-monitor.overflowchange {
    overflow: hidden
}

.x-paint-monitor.overflowchange::after {
    content: '';
    display: block;
    width: 1px !important;
    height: 1px !important
}

.x-progress {
    overflow: hidden;
    position: relative
}

.x-progress-bar {
    height: 100%;
    width: 0
}

.x-progress-text {
    overflow: hidden
}

.x-progress-bar {
    overflow: hidden;
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0
}

.x-scroller {
    -webkit-overflow-scrolling: touch
}

.x-scroller-spacer {
    position: absolute;
    top: 0;
    overflow: hidden;
    height: 1px;
    width: 1px;
    font-size: 0;
    line-height: 0;
    pointer-events: none
}

.x-scroller-snappable {
    -ms-scroll-snap-type: mandatory;
    -webkit-scroll-snap-type: mandatory;
    scroll-snap-type: mandatory
}

.x-no-scrollbars {
    -ms-overflow-style: none
}

.x-no-scrollbars::-webkit-scrollbar {
    width: 0
}

.x-touch-action-pan-y {
    overflow-x: hidden !important
}

.x-touch-action-pan-x {
    overflow-y: hidden !important
}

.x-drag-body {
    cursor: default
}

.x-drag-body * {
    -webkit-user-select: none;
    -moz-user-select: none;
    user-select: none
}

.x-drag-dragging {
    z-index: 1000000 !important;
    pointer-events: none
}

.x-treelist {
    background-color: #fff;
    background-position: 16px 0%;
    overflow: hidden;
    padding: 0 0 0 0
}

.x-big .x-treelist {
    background-position: 0%
}

.x-treelist-container, .x-treelist-root-container {
    width: 100%
}

.x-treelist-toolstrip {
    display: none
}

.x-treelist-micro > .x-treelist-toolstrip {
    display: inline-block
}

.x-treelist-micro > .x-treelist-root-container {
    display: none
}

.x-treelist-item, .x-treelist-container, .x-treelist-root-container {
    overflow: hidden;
    list-style: none;
    padding: 0;
    margin: 0
}

.x-treelist-item-tool, .x-treelist-row, .x-treelist-item-wrap {
    position: relative
}

.x-treelist-item-icon, .x-treelist-item-expander {
    display: none;
    position: absolute;
    top: 0
}

.x-treelist-item-expander {
    right: 0;
    cursor: pointer
}

.x-treelist-expander-only .x-treelist-item-expandable > * > .x-treelist-item-wrap > * {
    cursor: pointer
}

.x-treelist-item-text {
    cursor: default;
    white-space: nowrap;
    overflow: hidden
}

.x-treelist-item-collapsed > .x-treelist-container {
    display: none
}

.x-treelist-item-expandable > * > * > .x-treelist-item-expander, .x-treelist-item-icon {
    display: block
}

.x-treelist-item-floated > * > * > .x-treelist-item-expander, .x-treelist-item-floated > * > * > .x-treelist-item-icon {
    display: none
}

.x-treelist-expander-first .x-treelist-item-expander {
    left: 0;
    right: auto
}

.x-treelist-toolstrip {
    background-color: #f8f8f8
}

.x-treelist-item-selected > .x-treelist-row {
    background-color: #dfe8f6
}

.x-treelist-item-selected > .x-treelist-row-over {
    background-color: #dfe8f6
}

.x-treelist-item-tool {
    padding-left: 0;
    padding-right: 6px
}

.x-treelist-item-icon:before, .x-treelist-item-tool:before, .x-treelist-item-expander {
    line-height: 20px
}

.x-treelist-item-icon, .x-treelist-item-tool, .x-treelist-item-expander {
    text-align: center;
    background-repeat: no-repeat;
    background-position: 0 center
}

.x-treelist-item-loading .x-treelist-item-icon {
    /* background-image: url("data:image/gif;R0lGODlhEAAQALMMAKqooJGOhp2bk7e1rZ2bkre1rJCPhqqon8PBudDOxXd1bISCef///wAAAAAAAAAAACH/C05FVFNDQVBFMi4wAwEAAAAh+QQFAAAMACwAAAAAEAAQAAAET5DJyYyhmAZ7sxQEs1nMsmACGJKmSaVEOLXnK1PuBADepCiMg/DQ+/2GRI8RKOxJfpTCIJNIYArS6aRajWYZCASDa41Ow+Fx2YMWOyfpTAQAIfkEBQAADAAsAAAAABAAEAAABE6QyckEoZgKe7MEQMUxhoEd6FFdQWlOqTq15SlT9VQM3rQsjMKO5/n9hANixgjc9SQ/CgKRUSgw0ynFapVmGYkEg3v1gsPibg8tfk7CnggAIfkEBQAADAAsAAAAABAAEAAABE2QycnOoZjaA/IsRWV1goCBoMiUJTW8A0XMBPZmM4Ug3hQEjN2uZygahDyP0RBMEpmTRCKzWGCkUkq1SsFOFQrG1tr9gsPc3jnco4A9EQAh+QQFAAAMACwAAAAAEAAQAAAETpDJyUqhmFqbJ0LMIA7McWDfF5LmAVApOLUvLFMmlSTdJAiM3a73+wl5HYKSEET2lBSFIhMIYKRSimFriGIZiwWD2/WCw+Jt7xxeU9qZCAAh+QQFAAAMACwAAAAAEAAQAAAETZDJyRCimFqbZ0rVxgwF9n3hSJbeSQ2rCWIkpSjddBzMfee7nQ/XCfJ+OQYAQFksMgQBxumkEKLSCfVpMDCugqyW2w18xZmuwZycdDsRACH5BAUAAAwALAAAAAAQABAAAARNkMnJUqKYWpunUtXGIAj2feFIlt5JrWybkdSydNNQMLaND7pC79YBFnY+HENHMRgyhwPGaQhQotGm00oQMLBSLYPQ9QIASrLAq5x0OxEAIfkEBQAADAAsAAAAABAAEAAABE2QycmUopham+da1cYkCfZ94UiW3kmtbJuRlGF0E4Iwto3rut6tA9wFAjiJjkIgZAYDTLNJgUIpgqyAcTgwCuACJssAdL3gpLmbpLAzEQA7"); */
    background-image: url(data:image/gif;base64,R0lGODlhEAAQALMMAKqooJGOhp2bk7e1rZ2bkre1rJCPhqqon8PBudDOxXd1bISCef///wAAAAAAAAAAACH/C05FVFNDQVBFMi4wAwEAAAAh+QQFAAAMACwAAAAAEAAQAAAET5DJyYyhmAZ7sxQEs1nMsmACGJKmSaVEOLXnK1PuBADepCiMg/DQ+/2GRI8RKOxJfpTCIJNIYArS6aRajWYZCASDa41Ow+Fx2YMWOyfpTAQAIfkEBQAADAAsAAAAABAAEAAABE6QyckEoZgKe7MEQMUxhoEd6FFdQWlOqTq15SlT9VQM3rQsjMKO5/n9hANixgjc9SQ/CgKRUSgw0ynFapVmGYkEg3v1gsPibg8tfk7CnggAIfkEBQAADAAsAAAAABAAEAAABE2QycnOoZjaA/IsRWV1goCBoMiUJTW8A0XMBPZmM4Ug3hQEjN2uZygahDyP0RBMEpmTRCKzWGCkUkq1SsFOFQrG1tr9gsPc3jnco4A9EQAh+QQFAAAMACwAAAAAEAAQAAAETpDJyUqhmFqbJ0LMIA7McWDfF5LmAVApOLUvLFMmlSTdJAiM3a73+wl5HYKSEET2lBSFIhMIYKRSimFriGIZiwWD2/WCw+Jt7xxeU9qZCAAh+QQFAAAMACwAAAAAEAAQAAAETZDJyRCimFqbZ0rVxgwF9n3hSJbeSQ2rCWIkpSjddBzMfee7nQ/XCfJ+OQYAQFksMgQBxumkEKLSCfVpMDCugqyW2w18xZmuwZycdDsRACH5BAUAAAwALAAAAAAQABAAAARNkMnJUqKYWpunUtXGIAj2feFIlt5JrWybkdSydNNQMLaND7pC79YBFnY+HENHMRgyhwPGaQhQotGm00oQMLBSLYPQ9QIASrLAq5x0OxEAIfkEBQAADAAsAAAAABAAEAAABE2QycmUopham+da1cYkCfZ94UiW3kmtbJuRlGF0E4Iwto3rut6tA9wFAjiJjkIgZAYDTLNJgUIpgqyAcTgwCuACJssAdL3gpLmbpLAzEQA7)
    color: transparent
}

.x-treelist-item-icon, .x-treelist-item-tool {
    color: grey;
    font-size: 16px;
    width: 16px
}

.x-treelist-item-tool {
    width: 22px
}

.x-treelist-item-expander {
    color: grey;
    font-size: 16px;
    width: 16px
}

.x-treelist-item-expander:after {
    content: "\\f0da";
    font: 16px/1 FontAwesome
}

.x-treelist-item-expanded > * > * > .x-treelist-item-expander:after {
    content: "\\f0d7";
    font: 16px/1 FontAwesome
}

.x-treelist-item-text {
    color: #000;
    margin-left: 19px;
    margin-right: 16px;
    font-size: 11px;
    line-height: 20px;
    text-overflow: ellipsis
}

.x-treelist-row {
    padding-left: 0;
    padding-right: 6px
}

.x-treelist-item-floated .x-treelist-container {
    width: auto
}

.x-treelist-item-floated > .x-treelist-row {
    background-color: #f8f8f8
}

.x-treelist-item-floated > .x-treelist-container {
    margin-left: -16px
}

.x-big .x-treelist-item-floated > .x-treelist-container {
    margin-left: 0
}

.x-treelist-item-floated > * > * > .x-treelist-item-text {
    margin-left: 0
}

.x-treelist-item-floated > * .x-treelist-row {
    padding-left: 0
}

.x-treelist-item-floated .x-treelist-row:before {
    width: 0
}

.x-treelist-item-floated > .x-treelist-row-over {
    background-color: #f8f8f8
}

.x-treelist-item-floated > .x-treelist-row-over > * > .x-treelist-item-text {
    color: #000
}

.x-treelist-item-expanded > .x-treelist-item-expander:after {
    content: "\\f0d7";
    font: 16px/1 FontAwesome
}

.x-treelist-item-collapsed > * > .x-treelist-item-expander:after {
    content: "\\f0da";
    font: 16px/1 FontAwesome
}

&
.x-treelist-highlight-path .x-treelist-item-over > * > .x-treelist-item-icon {
    color: grey;
    transition: color 0.5s
}

&
.x-treelist-highlight-path .x-treelist-item-over > * > .x-treelist-item-text {
    color: #000;
    transition: color 0.5s
}

&
.x-treelist-highlight-path .x-treelist-item-over > * > .x-treelist-item-expander {
    color: grey;
    transition: color 0.5s
}

.x-treelist-row-over {
    background-color: #efefef
}

.x-treelist-row-over > * > .x-treelist-item-icon {
    color: grey;
    transition: color 0.5s
}

.x-treelist-row-over > * > .x-treelist-item-text {
    color: #000;
    transition: color 0.5s
}

.x-treelist-row-over > * > .x-treelist-item-expander {
    color: grey;
    transition: color 0.5s
}

.x-treelist-expander-first .x-treelist-item-icon {
    left: 16px
}

.x-treelist-expander-first .x-treelist-item-text {
    margin-left: 35px;
    margin-right: 0
}

.x-treelist-expander-first .x-treelist-item-hide-icon > * > * > .x-treelist-item-text {
    margin-left: 19px
}

.x-treelist-item-hide-icon > * > * > .x-treelist-item-text {
    margin-left: 3px
}

.x-translatable {
    position: absolute !important;
    top: 500000px !important;
    left: 500000px !important;
    overflow: visible !important;
    z-index: 1
}

.x-translatable-hboxfix {
    position: absolute;
    min-width: 100%;
    top: 0;
    left: 0
}

.x-translatable-hboxfix > .x-translatable {
    position: relative !important
}

.x-translatable-container {
    overflow: hidden;
    width: auto;
    height: auto;
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0
}

.x-translatable-container::before {
    content: '';
    display: block;
    width: 1000000px;
    height: 1000000px;
    visibility: hidden
}

.x-body {
    margin: 0;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale
}

@-ms-viewport {
    width: device-width
}

img {
    border: 0
}

.x-border-box, .x-border-box * {
    box-sizing: border-box;
    -moz-box-sizing: border-box;
    -ms-box-sizing: border-box;
    -webkit-box-sizing: border-box
}

.x-ltr {
    direction: ltr
}

.x-clear {
    overflow: hidden;
    clear: both;
    font-size: 0;
    line-height: 0;
    display: table
}

.x-layer {
    position: absolute !important;
    top: 0;
    left: 0;
    overflow: hidden
}

.x-fixed-layer {
    position: fixed !important;
    overflow: hidden
}

.x-shim {
    position: absolute;
    left: 0;
    top: 0;
    overflow: hidden;
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=0)";
    opacity: 0
}

.x-hidden-display {
    display: none !important
}

.x-hidden-visibility {
    visibility: hidden !important
}

.x-hidden, .x-hidden-offsets {
    display: block !important;
    visibility: hidden !important;
    position: absolute !important;
    top: -10000px !important
}

.x-hidden-clip {
    position: absolute !important;
    clip: rect(0, 0, 0, 0)
}

.x-masked-relative {
    position: relative
}

.x-ie-shadow {
    background-color: #777;
    position: absolute;
    overflow: hidden
}

.x-unselectable {
    user-select: none;
    -o-user-select: none;
    -ms-user-select: none;
    -moz-user-select: -moz-none;
    -webkit-user-select: none;
    -webkit-tap-highlight-color: transparent;
    -webkit-user-drag: none;
    cursor: default
}

.x-selectable {
    cursor: auto;
    -moz-user-select: text;
    -webkit-user-select: text;
    -ms-user-select: text;
    user-select: text;
    -o-user-select: text
}

.x-list-plain {
    list-style-type: none;
    margin: 0;
    padding: 0
}

.x-table-plain {
    border-collapse: collapse;
    border-spacing: 0;
    font-size: 1em
}

.x-frame-tl, .x-frame-tr, .x-frame-tc, .x-frame-bl, .x-frame-br, .x-frame-bc {
    overflow: hidden;
    background-repeat: no-repeat
}

.x-frame-tc, .x-frame-bc {
    background-repeat: repeat-x
}

td.x-frame-tl, td.x-frame-tr, td.x-frame-bl, td.x-frame-br {
    width: 1px
}

.x-frame-mc {
    background-repeat: repeat-x;
    overflow: hidden
}

.x-proxy-el {
    position: absolute;
    background: #b4b4b4;
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=80)";
    opacity: 0.8
}

.x-css-shadow {
    position: absolute;
    -webkit-border-radius: 5px;
    -moz-border-radius: 5px;
    -ms-border-radius: 5px;
    -o-border-radius: 5px;
    border-radius: 5px
}

.x-item-disabled, .x-item-disabled * {
    cursor: default;
    pointer-events: none
}

.x-component, .x-container {
    position: relative
}

:focus {
    outline: none
}

.x-body .x-sync-repaint:before, .x-body .x-sync-repaint:after {
    content: none !important
}

.x-position-relative {
    position: relative !important
}

.x-tab-guard {
    position: absolute;
    clip: rect(0, 0, 0, 0)
}

.x-box-item {
    position: absolute !important;
    left: 0;
    top: 0
}

.x-autocontainer-outerCt {
    display: table;
    transform: translateZ(0)
}

.x-clipped .x-autocontainer-outerCt {
    transform: initial
}

.x-autocontainer-innerCt {
    display: table-cell;
    height: 100%;
    vertical-align: top
}

.x-mask {
    z-index: 100;
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    outline: none !important
}

.x-ie8 .x-mask {
    background-image: url(data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
}

.x-mask-fixed {
    position: fixed
}

.x-mask-msg {
    position: absolute
}

.x-progress {
    border-style: solid
}

.x-btn {
    display: inline-block;
    outline: 0;
    cursor: pointer;
    white-space: nowrap;
    text-decoration: none;
    vertical-align: top;
    overflow: hidden;
    position: relative
}

.x-btn > .x-frame {
    height: 100%;
    width: 100%
}

.x-btn-wrap {
    height: 100%;
    width: 100%;
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-align: stretch;
    -ms-flex-align: stretch;
    align-items: stretch
}

.x-btn-wrap.x-btn-arrow-bottom, .x-btn-wrap.x-btn-split-bottom {
    -webkit-box-orient: vertical;
    -ms-flex-direction: column;
    flex-direction: column
}

.x-ie9m .x-btn-wrap {
    display: table;
    border-spacing: 0
}

.x-btn-button {
    white-space: nowrap;
    line-height: 0;
    position: relative;
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-align: center;
    -ms-flex-align: center;
    align-items: center;
    -webkit-box-flex: 1;
    -ms-flex: 1 1 auto;
    flex: 1 1 auto;
    min-width: 0
}

.x-btn-button.x-btn-icon-top, .x-btn-button.x-btn-icon-bottom {
    -webkit-box-orient: vertical;
    -ms-flex-direction: column;
    flex-direction: column;
    -webkit-box-align: stretch;
    -ms-flex-align: stretch;
    align-items: stretch;
    -webkit-box-pack: center;
    -ms-flex-pack: center;
    justify-content: center
}

.x-ie9m .x-btn-button {
    display: table-cell;
    vertical-align: middle
}

.x-btn-inner {
    overflow: hidden;
    text-overflow: ellipsis;
    -ms-flex-negative: 1;
    display: block
}

.x-ie9m .x-btn-inner {
    display: inline-block;
    vertical-align: middle
}

.x-btn-icon.x-btn-no-text > .x-btn-inner {
    display: none
}

.x-btn-icon-el {
    display: none;
    vertical-align: middle;
    text-align: center;
    background-position: center center;
    background-repeat: no-repeat
}

.x-btn-icon > .x-btn-icon-el {
    display: block
}

.x-ie9m .x-btn-icon-left > .x-btn-icon-el, .x-ie9m .x-btn-icon-right > .x-btn-icon-el {
    display: inline-block
}

.x-btn-button-center {
    text-align: center;
    -webkit-box-pack: center;
    -ms-flex-pack: center;
    justify-content: center
}

.x-btn-button-left {
    text-align: left;
    -webkit-box-pack: start;
    -ms-flex-pack: start;
    justify-content: flex-start
}

.x-btn-button-right {
    text-align: right;
    -webkit-box-pack: end;
    -ms-flex-pack: end;
    justify-content: flex-end
}

.x-btn-arrow:after, .x-btn-split:after {
    display: block;
    background-repeat: no-repeat;
    content: '';
    box-sizing: border-box;
    -moz-box-sizing: border-box;
    -ms-box-sizing: border-box;
    -webkit-box-sizing: border-box;
    text-align: center
}

.x-btn-arrow-right:after, .x-btn-split-right:after {
    background-position: right center;
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-align: center;
    -ms-flex-align: center;
    align-items: center;
    -webkit-box-pack: center;
    -ms-flex-pack: center;
    justify-content: center
}

.x-ie9m .x-btn-arrow-right:after, .x-ie9m .x-btn-split-right:after {
    display: table-cell;
    vertical-align: middle
}

.x-btn-arrow-bottom:after, .x-btn-split-bottom:after {
    background-position: center bottom;
    content: '\\00a0';
    line-height: 0
}

.x-ie9m .x-btn-arrow-bottom:after, .x-ie9m .x-btn-split-bottom:after {
    display: table-row
}

.x-btn-split-right > .x-btn-button:after {
    position: absolute;
    display: block;
    top: -100%;
    right: 0;
    height: 300%;
    content: ''
}

.x-btn-split-bottom > .x-btn-button:after {
    position: absolute;
    display: block;
    bottom: 0;
    left: -100%;
    font-size: 0;
    width: 300%;
    content: ''
}

.x-btn-mc {
    overflow: visible
}

.x-segmented-button {
    display: table;
    table-layout: fixed
}

.x-segmented-button-item {
    display: table-cell;
    vertical-align: top
}

.x-segmented-button-item > .x-frame {
    width: 100%;
    height: 100%
}

.x-segmented-button-item .x-btn-mc {
    width: 100%
}

.x-segmented-button-item-horizontal {
    display: table-cell;
    height: 100%
}

.x-segmented-button-item-horizontal.x-segmented-button-first {
    border-top-right-radius: 0;
    border-bottom-right-radius: 0
}

.x-segmented-button-item-horizontal.x-segmented-button-first .x-btn-tr, .x-segmented-button-item-horizontal.x-segmented-button-first .x-btn-mr, .x-segmented-button-item-horizontal.x-segmented-button-first .x-btn-br {
    display: none
}

.x-segmented-button-item-horizontal.x-segmented-button-middle {
    border-radius: 0;
    border-left: 0
}

.x-segmented-button-item-horizontal.x-segmented-button-middle .x-btn-tl, .x-segmented-button-item-horizontal.x-segmented-button-middle .x-btn-tr, .x-segmented-button-item-horizontal.x-segmented-button-middle .x-btn-ml, .x-segmented-button-item-horizontal.x-segmented-button-middle .x-btn-mr, .x-segmented-button-item-horizontal.x-segmented-button-middle .x-btn-bl, .x-segmented-button-item-horizontal.x-segmented-button-middle .x-btn-br {
    display: none
}

.x-segmented-button-item-horizontal.x-segmented-button-last {
    border-left: 0;
    border-top-left-radius: 0;
    border-bottom-left-radius: 0
}

.x-segmented-button-item-horizontal.x-segmented-button-last .x-btn-tl, .x-segmented-button-item-horizontal.x-segmented-button-last .x-btn-ml, .x-segmented-button-item-horizontal.x-segmented-button-last .x-btn-bl {
    display: none
}

.x-segmented-button-row {
    display: table-row
}

.x-segmented-button-item-vertical.x-segmented-button-first {
    border-bottom-right-radius: 0;
    border-bottom-left-radius: 0
}

.x-segmented-button-item-vertical.x-segmented-button-first .x-btn-bl, .x-segmented-button-item-vertical.x-segmented-button-first .x-btn-bc, .x-segmented-button-item-vertical.x-segmented-button-first .x-btn-br {
    display: none
}

.x-segmented-button-item-vertical.x-segmented-button-middle {
    border-radius: 0;
    border-top: 0
}

.x-segmented-button-item-vertical.x-segmented-button-middle .x-btn-tl, .x-segmented-button-item-vertical.x-segmented-button-middle .x-btn-tc, .x-segmented-button-item-vertical.x-segmented-button-middle .x-btn-tr, .x-segmented-button-item-vertical.x-segmented-button-middle .x-btn-bl, .x-segmented-button-item-vertical.x-segmented-button-middle .x-btn-bc, .x-segmented-button-item-vertical.x-segmented-button-middle .x-btn-br {
    display: none
}

.x-segmented-button-item-vertical.x-segmented-button-last {
    border-top: 0;
    border-top-right-radius: 0;
    border-top-left-radius: 0
}

.x-segmented-button-item-vertical.x-segmented-button-last .x-btn-tl, .x-segmented-button-item-vertical.x-segmented-button-last .x-btn-tc, .x-segmented-button-item-vertical.x-segmented-button-last .x-btn-tr {
    display: none
}

.x-title-icon {
    background-repeat: no-repeat;
    background-position: 0 0;
    vertical-align: middle;
    line-height: 1;
    text-align: center
}

.x-title {
    display: table;
    table-layout: fixed
}

.x-title-text {
    display: table-cell;
    overflow: hidden;
    white-space: nowrap;
    -o-text-overflow: ellipsis;
    text-overflow: ellipsis;
    vertical-align: middle
}

.x-title-align-left {
    text-align: left
}

.x-title-align-center {
    text-align: center
}

.x-title-align-right {
    text-align: right
}

.x-title-rotate-right {
    -webkit-transform: rotate(90deg);
    -webkit-transform-origin: 0 0;
    -moz-transform: rotate(90deg);
    -moz-transform-origin: 0 0;
    -ms-transform: rotate(90deg);
    -ms-transform-origin: 0 0;
    transform: rotate(90deg);
    transform-origin: 0 0
}

.x-ie8 .x-title-rotate-right {
    -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=1)"
}

.x-title-rotate-left {
    -webkit-transform: rotate(270deg);
    -webkit-transform-origin: 100% 0;
    -moz-transform: rotate(270deg);
    -moz-transform-origin: 100% 0;
    -ms-transform: rotate(270deg);
    -ms-transform-origin: 100% 0;
    transform: rotate(270deg);
    transform-origin: 100% 0
}

.x-ie8 .x-title-rotate-left {
    -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=3)"
}

.x-horizontal.x-header .x-title-rotate-right.x-title-align-left > .x-title-item {
    vertical-align: bottom
}

.x-horizontal.x-header .x-title-rotate-right.x-title-align-center > .x-title-item {
    vertical-align: middle
}

.x-horizontal.x-header .x-title-rotate-right.x-title-align-right > .x-title-item {
    vertical-align: top
}

.x-horizontal.x-header .x-title-rotate-left.x-title-align-left > .x-title-item {
    vertical-align: top
}

.x-horizontal.x-header .x-title-rotate-left.x-title-align-center > .x-title-item {
    vertical-align: middle
}

.x-horizontal.x-header .x-title-rotate-left.x-title-align-right > .x-title-item {
    vertical-align: bottom
}

.x-vertical.x-header .x-title-rotate-none.x-title-align-left > .x-title-item {
    vertical-align: top
}

.x-vertical.x-header .x-title-rotate-none.x-title-align-center > .x-title-item {
    vertical-align: middle
}

.x-vertical.x-header .x-title-rotate-none.x-title-align-right > .x-title-item {
    vertical-align: bottom
}

.x-title-icon-wrap {
    display: table-cell;
    text-align: center;
    vertical-align: middle;
    line-height: 0
}

.x-title-icon-wrap.x-title-icon-top, .x-title-icon-wrap.x-title-icon-bottom {
    display: table-row
}

.x-title-icon {
    display: inline-block;
    vertical-align: middle;
    background-position: center;
    background-repeat: no-repeat
}

.x-tool {
    font-size: 15px;
    line-height: 1
}

.x-header > .x-box-inner, .x-panel-header-mc > .x-box-inner, .x-window-header-mc > .x-box-inner {
    overflow: visible
}

.x-splitter {
    font-size: 1px
}

.x-splitter-horizontal {
    cursor: e-resize;
    cursor: row-resize
}

.x-splitter-vertical {
    cursor: e-resize;
    cursor: col-resize
}

.x-splitter-collapsed, .x-splitter-horizontal-noresize, .x-splitter-vertical-noresize {
    cursor: default
}

.x-splitter-active {
    z-index: 4
}

.x-collapse-el {
    position: absolute;
    background-repeat: no-repeat
}

.x-splitter-focus {
    z-index: 4
}

.x-box-layout-ct {
    overflow: hidden
}

.x-box-target {
    position: absolute;
    width: 20000px;
    top: 0;
    left: 0;
    min-height: 1px
}

.x-box-inner {
    overflow: hidden;
    position: relative;
    left: 0;
    top: 0
}

.x-box-scroller {
    position: absolute;
    background-repeat: no-repeat;
    background-position: center;
    line-height: 0;
    font-size: 0;
    text-align: center
}

.x-box-scroller-top {
    top: 0
}

.x-box-scroller-right {
    right: 0
}

.x-box-scroller-bottom {
    bottom: 0
}

.x-box-scroller-left {
    left: 0
}

.x-box-menu-body-horizontal {
    float: left
}

.x-box-menu-after {
    position: relative;
    float: left
}

.x-toolbar-text {
    white-space: nowrap
}

.x-toolbar-separator {
    display: block;
    font-size: 1px;
    overflow: hidden;
    cursor: default;
    border: 0;
    width: 0;
    height: 0;
    line-height: 0px
}

.x-toolbar-scroller {
    padding-left: 0
}

.x-toolbar-plain {
    border: 0
}

.x-dd-drag-proxy, .x-dd-drag-current {
    z-index: 1000000 !important;
    pointer-events: none
}

.x-dd-drag-proxy {
    display: table
}

.x-dd-drag-repair .x-dd-drag-ghost {
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=60)";
    opacity: 0.6
}

.x-dd-drag-repair .x-dd-drop-icon {
    display: none
}

.x-dd-drag-ghost, .x-dd-drop-icon {
    display: table-cell;
    vertical-align: middle
}

.x-dd-drag-ghost {
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=85)";
    opacity: 0.85;
    white-space: nowrap
}

.x-dd-drop-icon {
    height: 26px;
    width: 26px;
    background-color: transparent;
    background-position: center;
    background-repeat: no-repeat
}

.x-docked {
    position: absolute !important;
    z-index: 2
}

.x-docked-vertical {
    position: static
}

.x-docked-top {
    border-bottom-width: 0 !important
}

.x-docked-bottom {
    border-top-width: 0 !important
}

.x-docked-left {
    border-right-width: 0 !important
}

.x-docked-right {
    border-left-width: 0 !important
}

.x-docked-noborder-top {
    border-top-width: 0 !important
}

.x-docked-noborder-right {
    border-right-width: 0 !important
}

.x-docked-noborder-bottom {
    border-bottom-width: 0 !important
}

.x-docked-noborder-left {
    border-left-width: 0 !important
}

.x-noborder-l {
    border-left-width: 0 !important
}

.x-noborder-b {
    border-bottom-width: 0 !important
}

.x-noborder-bl {
    border-bottom-width: 0 !important;
    border-left-width: 0 !important
}

.x-noborder-r {
    border-right-width: 0 !important
}

.x-noborder-rl {
    border-right-width: 0 !important;
    border-left-width: 0 !important
}

.x-noborder-rb {
    border-right-width: 0 !important;
    border-bottom-width: 0 !important
}

.x-noborder-rbl {
    border-right-width: 0 !important;
    border-bottom-width: 0 !important;
    border-left-width: 0 !important
}

.x-noborder-t {
    border-top-width: 0 !important
}

.x-noborder-tl {
    border-top-width: 0 !important;
    border-left-width: 0 !important
}

.x-noborder-tb {
    border-top-width: 0 !important;
    border-bottom-width: 0 !important
}

.x-noborder-tbl {
    border-top-width: 0 !important;
    border-bottom-width: 0 !important;
    border-left-width: 0 !important
}

.x-noborder-tr {
    border-top-width: 0 !important;
    border-right-width: 0 !important
}

.x-noborder-trl {
    border-top-width: 0 !important;
    border-right-width: 0 !important;
    border-left-width: 0 !important
}

.x-noborder-trb {
    border-top-width: 0 !important;
    border-right-width: 0 !important;
    border-bottom-width: 0 !important
}

.x-noborder-trbl {
    border-width: 0 !important
}

.x-panel, .x-plain {
    overflow: hidden;
    position: relative
}

.x-panel {
    outline: none
}

td.x-frame-mc {
    vertical-align: top
}

.x-panel-bodyWrap {
    overflow: hidden;
    position: static;
    height: 100%;
    width: 100%
}

.x-panel-body {
    overflow: hidden;
    position: relative
}

.x-panel-header-plain, .x-panel-body-plain {
    border: 0;
    padding: 0
}

.x-panel-collapsed-mini {
    visibility: hidden
}

.x-viewport > .x-body.x-panel > .x-panel-bodyWrap {
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0
}

.x-table-layout {
    font-size: 1em
}

.x-btn-group {
    position: relative;
    overflow: hidden
}

.x-btn-group-body {
    position: relative
}

.x-btn-group-body .x-table-layout-cell {
    vertical-align: top
}

.x-viewport, .x-viewport > .x-body {
    margin: 0;
    padding: 0;
    border: 0 none;
    position: static
}

.x-viewport {
    height: 100%
}

.x-viewport > .x-body {
    min-height: 100%
}

.x-column {
    float: left
}

.x-resizable-overlay {
    position: absolute;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    display: none;
    z-index: 200000;
    background-color: #fff;
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=0)";
    opacity: 0
}

.x-window {
    outline: none;
    overflow: hidden
}

.x-window .x-window-wrap {
    position: relative
}

.x-window-body {
    position: relative;
    overflow: hidden
}

.x-form-item {
    display: table;
    table-layout: fixed;
    border-spacing: 0;
    border-collapse: separate
}

.x-form-item-label {
    overflow: hidden
}

.x-form-item.x-form-item-no-label > .x-form-item-label {
    display: none
}

.x-form-item-label, .x-form-item-body {
    display: table-cell
}

.x-form-item-body {
    vertical-align: middle;
    height: 100%
}

.x-form-item-label-inner {
    display: inline-block
}

.x-form-item-label-top {
    display: table-row;
    height: 1px
}

.x-form-item-label-top > .x-form-item-label-inner {
    display: table-cell
}

.x-form-item-label-top-side-error:after {
    display: table-cell;
    content: ''
}

.x-form-item-label-right {
    text-align: right
}

.x-form-error-wrap-side {
    display: table-cell;
    vertical-align: middle
}

.x-form-error-wrap-under {
    display: table-row;
    height: 1px
}

.x-form-error-wrap-under > .x-form-error-msg {
    display: table-cell
}

.x-form-error-wrap-under-side-label:before {
    display: table-cell;
    content: '';
    pointer-events: none
}

.x-form-invalid-icon {
    overflow: hidden
}

.x-form-invalid-icon ul {
    display: none
}

.x-form-trigger-wrap {
    display: table;
    width: 100%;
    height: 100%
}

.x-gecko .x-form-trigger-wrap {
    display: -moz-inline-box;
    display: inline-flex;
    vertical-align: top
}

.x-form-text-wrap {
    display: table-cell;
    overflow: hidden;
    height: 100%;
    position: relative
}

.x-gecko .x-form-text-wrap {
    display: block;
    -moz-box-flex: 1;
    flex: 1
}

.x-form-text-wrap .x-placeholder-label {
    position: absolute;
    top: 0;
    left: 0;
    cursor: text;
    white-space: nowrap;
    overflow: hidden
}

.x-form-item-body.x-form-text-grow {
    min-width: inherit;
    max-width: inherit
}

.x-form-text {
    border: 0;
    margin: 0;
    -webkit-border-radius: 0;
    -moz-border-radius: 0;
    -ms-border-radius: 0;
    -o-border-radius: 0;
    border-radius: 0;
    display: block;
    background: repeat-x 0 0;
    width: 100%;
    height: 100%
}

.x-webkit .x-form-text {
    height: calc(100% + 3px)
}

.x-form-trigger {
    display: table-cell;
    vertical-align: top;
    cursor: pointer;
    overflow: hidden;
    background-repeat: no-repeat;
    text-align: center;
    line-height: 0;
    white-space: nowrap
}

.x-item-disabled .x-form-trigger {
    cursor: default
}

.x-form-trigger.x-form-trigger-cmp {
    background: none;
    border: 0
}

.x-gecko .x-form-trigger {
    display: block
}

.x-form-textarea {
    overflow: auto;
    resize: none
}

div.x-form-text-grow .x-form-textarea {
    min-height: inherit
}

.x-message-box .x-form-display-field {
    height: auto
}

.x-ie8 .x-form-fieldcontainer > .x-form-item-body.x-field-container-body-vertical {
    display: table-row
}

.x-form-cb-wrap {
    vertical-align: top
}

.x-form-cb-wrap-inner {
    position: relative
}

.x-form-cb {
    position: absolute;
    left: 0;
    right: auto;
    vertical-align: top;
    overflow: hidden;
    padding: 0;
    border: 0
}

.x-form-cb::-moz-focus-inner {
    padding: 0;
    border: 0
}

.x-form-cb-input {
    position: absolute;
    margin: 0;
    padding: 0;
    border: 0;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=0)";
    opacity: 0
}

.x-form-cb-after {
    left: auto;
    right: 0
}

.x-form-cb-label {
    display: inline-block
}

.x-form-cb-label.x-form-cb-no-box-label {
    display: none
}

.x-fieldset {
    display: block;
    position: relative;
    overflow: hidden
}

.x-fieldset-header {
    overflow: hidden
}

.x-fieldset-header .x-form-item, .x-fieldset-header .x-tool {
    float: left
}

.x-fieldset-header .x-fieldset-header-text {
    float: left
}

.x-fieldset-header .x-form-cb-wrap {
    font-size: 0;
    line-height: 0;
    min-height: 0;
    height: auto
}

.x-fieldset-header .x-form-cb {
    margin: 0;
    position: static;
    display: inherit
}

.x-fieldset-body {
    overflow: hidden
}

.x-fieldset-collapsed {
    padding-bottom: 0 !important
}

.x-fieldset-collapsed > .x-fieldset-body {
    display: none
}

.x-fieldset-header-text-collapsible {
    cursor: pointer
}

.x-view-item-focused {
    outline: 1px dashed #c0d4ed !important;
    outline-offset: -1px
}

.x-ie9 .x-boundlist-list-ct {
    min-height: 0%
}

.x-datepicker {
    position: relative
}

.x-datepicker .x-monthpicker {
    left: 0;
    top: 0;
    display: block
}

.x-datepicker .x-monthpicker-months, .x-datepicker .x-monthpicker-years {
    height: 100%
}

.x-datepicker-inner {
    table-layout: fixed;
    width: 100%;
    border-collapse: separate
}

.x-datepicker-cell {
    padding: 0
}

.x-datepicker-header {
    position: relative
}

.x-datepicker-arrow {
    position: absolute;
    outline: none;
    font-size: 0
}

.x-datepicker-column-header {
    padding: 0
}

.x-datepicker-date {
    display: block;
    text-decoration: none
}

.x-monthpicker {
    display: table
}

.x-monthpicker-body {
    height: 100%;
    position: relative
}

.x-monthpicker-months, .x-monthpicker-years {
    float: left
}

.x-monthpicker-item {
    float: left
}

.x-monthpicker-item-inner {
    display: block;
    text-decoration: none
}

.x-monthpicker-yearnav-button-ct {
    float: left;
    text-align: center
}

.x-monthpicker-yearnav-button {
    display: inline-block;
    outline: none;
    font-size: 0
}

.x-monthpicker-buttons {
    width: 100%
}

.x-datepicker .x-monthpicker-buttons {
    position: absolute;
    bottom: 0
}

.x-datepicker-month .x-btn-split > .x-btn-button:after {
    content: none
}

.x-form-display-field-body {
    vertical-align: top
}

.x-form-file-btn {
    overflow: hidden;
    position: relative
}

.x-form-file-input {
    border: 0;
    position: absolute;
    cursor: pointer;
    top: 0;
    right: 0;
    width: 100%;
    height: 100%;
    overflow: hidden;
    text-indent: -10000px;
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=0)";
    opacity: 0;
    font-size: 1000px
}

.x-form-item-hidden {
    margin: 0
}

.x-tip {
    position: absolute;
    overflow: visible
}

.x-tip-body {
    overflow: hidden;
    position: relative
}

.x-tip-anchor {
    position: absolute;
    border-style: solid;
    height: 0;
    width: 0
}

.x-color-picker-item {
    float: left;
    text-decoration: none
}

.x-color-picker-item-inner {
    display: block;
    font-size: 1px
}

.x-html-editor-tb .x-toolbar {
    position: static !important
}

.x-htmleditor-iframe, .x-htmleditor-textarea {
    display: block;
    overflow: auto;
    width: 100%;
    height: 100%;
    border: 0
}

.x-tagfield-body {
    vertical-align: top
}

.x-tagfield {
    height: auto !important;
    cursor: text;
    overflow-y: auto
}

.x-tagfield .x-tagfield-list {
    padding: 0;
    margin: 0
}

.x-tagfield-list.x-tagfield-singleselect {
    white-space: nowrap;
    overflow: hidden
}

.x-tagfield-input, .x-tagfield-item {
    vertical-align: top;
    display: inline-block;
    position: relative
}

.x-tagfield-input-field {
    font: inherit;
    border: 0;
    margin: 0;
    background: none;
    width: 100%
}

.x-tagfield-stacked .x-tagfield-item {
    display: block
}

.x-tagfield-item {
    cursor: default
}

.x-tagfield-item-close {
    cursor: pointer;
    position: absolute
}

.x-tagfield-arialist {
    list-style-type: none;
    position: absolute;
    clip: rect(0, 0, 0, 0)
}

.x-tagfield-arialist-item {
    list-style-type: none
}

.x-fit-item {
    position: relative
}

.x-grid-view {
    overflow: hidden;
    position: relative
}

.x-grid-row-table {
    width: 0;
    table-layout: fixed;
    border: 0 none;
    border-collapse: separate;
    border-spacing: 0
}

.x-grid-item {
    table-layout: fixed;
    outline: none;
    position: relative
}

.x-grid-row {
    outline: none
}

.x-grid-td {
    overflow: hidden;
    border-width: 0;
    vertical-align: top
}

.x-grid-cell-inner {
    overflow: hidden;
    white-space: nowrap
}

.x-wrap-cell .x-grid-cell-inner {
    white-space: normal
}

.x-grid-resize-marker {
    position: absolute;
    z-index: 5;
    top: 0
}

.x-grid-item-container {
    min-height: 1px;
    position: relative
}

.x-col-move-top, .x-col-move-bottom {
    position: absolute;
    top: 0;
    line-height: 0;
    font-size: 0;
    overflow: hidden;
    z-index: 20000;
    background: no-repeat center top transparent
}

.x-grid-header-ct {
    cursor: default
}

.x-column-header {
    position: absolute;
    overflow: hidden;
    background-repeat: repeat-x
}

.x-column-header-inner {
    white-space: nowrap;
    position: relative;
    overflow: hidden
}

.x-leaf-column-header {
    height: 100%
}

.x-leaf-column-header .x-column-header-text-container {
    height: 100%
}

.x-column-header-text-container {
    width: 100%;
    display: table;
    table-layout: fixed
}

.x-column-header-text-container.x-column-header-text-container-auto {
    table-layout: auto
}

.x-column-header-text-wrapper {
    display: table-cell;
    vertical-align: middle
}

.x-column-header-text {
    display: block;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap
}

.x-column-header-text-inner {
    background-repeat: no-repeat
}

.x-column-header-inner-empty .x-column-header-text-inner {
    display: none
}

.x-column-header-inner-empty .x-column-header-text-container {
    line-height: 0
}

.x-column-header-trigger {
    display: none;
    height: 100%;
    background-repeat: no-repeat;
    position: absolute;
    right: 0;
    top: 0;
    text-align: center
}

.x-ie9m .x-column-header-trigger {
    z-index: 6
}

.x-column-header-over .x-column-header-trigger, .x-column-header-open .x-column-header-trigger {
    display: block
}

.x-column-header-align-right {
    text-align: right
}

.x-column-header-align-left {
    text-align: left
}

.x-column-header-align-center {
    text-align: center
}

.x-grid-cell-inner-action-col {
    line-height: 0;
    font-size: 0
}

.x-grid-cell-inner-action-col :focus {
    outline: 1px dotted #464646
}

.x-action-col-icon {
    display: inline-block;
    line-height: 1
}

.x-column-header-checkbox .x-column-header-text {
    margin-bottom: 0.4em
}

.x-column-header-checkbox .x-column-header-inner-empty .x-column-header-text {
    margin-bottom: 0
}

.x-grid-checkcolumn-cell-inner {
    line-height: 0
}

.x-grid-checkcolumn-cell-inner :focus {
    outline: 1px dotted #464646
}

.x-group-hd-container {
    overflow: hidden
}

.x-grid-group-hd {
    white-space: nowrap;
    outline: none
}

.x-grid-group-title {
    position: relative
}

.x-grid-row-body-hidden, .x-grid-group-collapsed {
    display: none
}

.x-grid-row-body-hidden {
    display: none
}

.x-menu {
    outline: none
}

.x-menu-body {
    position: relative
}

.x-menu-item {
    white-space: nowrap;
    overflow: hidden;
    border-color: transparent;
    border-style: solid
}

.x-menu-item-cmp .x-field-label-cell {
    vertical-align: middle
}

.x-menu-icon-separator {
    position: absolute;
    top: 0px;
    z-index: 0;
    height: 100%;
    overflow: hidden
}

.x-menu-plain .x-menu-icon-separator {
    display: none
}

.x-menu-item-link {
    -webkit-tap-highlight-color: transparent;
    -webkit-touch-callout: none;
    text-decoration: none;
    outline: 0;
    display: block
}

.x-menu-item-link-href {
    -webkit-touch-callout: default
}

.x-menu-item-text {
    display: inline-block
}

.x-menu-item-icon, .x-menu-item-icon-right, .x-menu-item-arrow {
    font-size: 0;
    position: absolute;
    text-align: center;
    background-repeat: no-repeat
}

.x-grid-scroll-container {
    position: absolute;
    z-index: 1
}

.x-grid-scrollbar-clipper-floated, .x-grid-scrollbar-floated {
    z-index: 2
}

.x-grid-scroll-body {
    width: 100%;
    position: relative
}

.x-grid-scrollbar-clipper {
    overflow: hidden;
    position: absolute;
    top: 0;
    left: 0
}

.x-grid-scrollbar-clipper > .x-grid-view, .x-grid-scrollbar-clipper > .x-tree-view {
    overflow-y: hidden !important
}

.x-grid-with-col-lines .x-grid-scrollbar-clipper-locked .x-grid-cell-last {
    border-right-width: 0
}

.x-grid-scrollbar {
    position: absolute;
    bottom: 0;
    left: 0;
    display: none
}

.x-grid-scrollbar-visible {
    display: block
}

.x-grid-locking-body > .x-grid {
    z-index: 2;
    pointer-events: none
}

.x-grid-locking-body > .x-grid .x-docked {
    pointer-events: auto
}

.x-grid-locking-body .x-grid-body {
    background: transparent
}

.x-grid-locking-body > .x-splitter {
    z-index: 2
}

.x-grid-locking-body > .x-splitter-active {
    z-index: 4
}

.x-grid-locking-body > .x-splitter-focus {
    z-index: 4
}

.x-grid-inner-locked.x-border-region-slide-in {
    z-index: 3
}

.x-grid-inner-locked.x-border-region-slide-in > .x-panel-bodyWrap > .x-grid-body > .x-grid-view, .x-grid-inner-locked.x-border-region-slide-in > .x-panel-bodyWrap > .x-grid-body > .x-tree-view {
    overflow-y: hidden !important
}

.x-grid-editor .x-form-cb-wrap {
    text-align: center
}

.x-grid-editor .x-form-cb {
    position: static;
    display: inline-block
}

.x-grid-editor .x-form-display-field {
    margin: 0;
    white-space: nowrap;
    overflow: hidden
}

.x-grid-editor div.x-form-action-col-field {
    line-height: 0
}

.x-grid-row-editor-wrap {
    position: absolute;
    overflow: visible;
    z-index: 2
}

.x-grid-row-editor {
    position: absolute;
    z-index: 0
}

.x-grid-row-editor-buttons {
    position: absolute;
    white-space: nowrap
}

.x-grid-row-expander {
    font-size: 0;
    line-height: 0;
    text-align: center
}

.x-grid-row-expander:focus {
    outline: 1px dotted #464646
}

.x-grid-hide-row-expander-spacer .x-grid-row-expander-spacer {
    display: none
}

.x-grid-row-expander-spacer {
    border: 0 none
}

.x-ssm-row-numberer-hd {
    cursor: se-resize !important
}

.x-ssm-row-numberer-cell {
    cursor: e-resize
}

.x-ssm-column-select .x-column-header {
    cursor: s-resize
}

.x-ssm-extender-drag-handle {
    position: absolute;
    z-index: 1;
    cursor: crosshair
}

.x-ssm-extender-mask {
    position: absolute;
    z-index: 1;
    pointer-events: none
}

.x-abs-layout-ct {
    position: relative
}

.x-abs-layout-item {
    position: absolute !important
}

.x-border-layout-ct {
    overflow: hidden
}

.x-border-layout-ct {
    position: relative
}

.x-border-region-slide-in {
    z-index: 5
}

.x-region-collapsed-placeholder {
    z-index: 4
}

.x-center-layout-item {
    position: absolute
}

.x-center-target {
    position: relative
}

.x-form-layout-wrap {
    display: table;
    width: 100%;
    border-collapse: separate
}

.x-form-layout-colgroup {
    display: table-column-group
}

.x-form-layout-column {
    display: table-column
}

.x-form-layout-auto-label > * > .x-form-item-label {
    width: auto !important
}

.x-form-layout-auto-label > * > .x-form-item-label > .x-form-item-label-inner {
    width: auto !important;
    white-space: nowrap
}

.x-form-layout-auto-label > * > .x-form-layout-label-column {
    width: 1px
}

.x-form-layout-sized-label > * > .x-form-item-label {
    width: auto !important
}

.x-form-form-item {
    display: table-row
}

.x-form-form-item > .x-form-item-label {
    padding-left: 0 !important;
    padding-right: 0 !important;
    padding-bottom: 0 !important
}

.x-form-form-item > .x-form-item-body {
    max-width: none
}

.x-form-form-item.x-form-item-no-label:before {
    content: ' ';
    display: table-cell;
    pointer-events: none
}

.x-resizable-wrapped {
    box-sizing: border-box;
    -moz-box-sizing: border-box;
    -ms-box-sizing: border-box;
    -webkit-box-sizing: border-box
}

.x-slider {
    outline: none;
    position: relative
}

.x-slider-inner {
    position: relative;
    left: 0;
    top: 0;
    overflow: visible
}

.x-slider-vert .x-slider-inner {
    background: repeat-y 0 0
}

.x-slider-thumb {
    position: absolute;
    background: no-repeat 0 0;
    cursor: default;
    -webkit-user-callout: none
}

.x-slider-horz .x-slider-thumb {
    left: 0
}

.x-slider-vert .x-slider-thumb {
    bottom: 0
}

.x-tab {
    display: block;
    outline: 0;
    cursor: pointer;
    white-space: nowrap;
    text-decoration: none;
    vertical-align: top;
    overflow: hidden;
    position: relative
}

.x-tab > .x-frame {
    height: 100%;
    width: 100%
}

.x-tab-wrap {
    height: 100%;
    width: 100%;
    display: table;
    border-spacing: 0
}

.x-tab-button {
    white-space: nowrap;
    line-height: 0;
    position: relative;
    display: table-cell;
    vertical-align: middle
}

.x-tab-inner {
    overflow: hidden;
    text-overflow: ellipsis;
    display: inline-block;
    vertical-align: middle
}

.x-tab-icon.x-tab-no-text > .x-tab-inner {
    display: none
}

.x-tab-icon-el {
    display: none;
    vertical-align: middle;
    text-align: center;
    background-position: center center;
    background-repeat: no-repeat
}

.x-tab-icon > .x-tab-icon-el {
    display: inline-block
}

.x-tab-icon-top > .x-tab-icon-el, .x-tab-icon-bottom > .x-tab-icon-el {
    display: block
}

.x-tab-button-center {
    text-align: center
}

.x-tab-button-left {
    text-align: left
}

.x-tab-button-right {
    text-align: right
}

.x-tab-mc {
    overflow: visible
}

.x-tab {
    z-index: 1
}

.x-tab-active {
    z-index: 3
}

.x-tab-button {
    position: relative
}

.x-tab-close-btn {
    display: block;
    position: absolute;
    overflow: hidden;
    font-size: 0;
    line-height: 0
}

.x-tab-rotate-left {
    -webkit-transform: rotate(270deg);
    -webkit-transform-origin: 100% 0;
    -moz-transform: rotate(270deg);
    -moz-transform-origin: 100% 0;
    -ms-transform: rotate(270deg);
    -ms-transform-origin: 100% 0;
    transform: rotate(270deg);
    transform-origin: 100% 0
}

.x-ie8 .x-tab-rotate-left {
    -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=3)"
}

.x-tab-rotate-right {
    -webkit-transform: rotate(90deg);
    -webkit-transform-origin: 0 0;
    -moz-transform: rotate(90deg);
    -moz-transform-origin: 0 0;
    -ms-transform: rotate(90deg);
    -ms-transform-origin: 0 0;
    transform: rotate(90deg);
    transform-origin: 0 0
}

.x-ie8 .x-tab-rotate-right {
    -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=1)"
}

.x-tab-tr, .x-tab-br, .x-tab-mr, .x-tab-tl, .x-tab-bl, .x-tab-ml {
    width: 1px
}

.x-tab-bar {
    z-index: 0;
    position: relative
}

.x-tab-bar-strip {
    position: absolute;
    line-height: 0;
    font-size: 0;
    z-index: 2
}

.x-tab-bar-top > .x-tab-bar-strip {
    bottom: 0
}

.x-tab-bar-bottom > .x-tab-bar-strip {
    top: 0
}

.x-tab-bar-left > .x-tab-bar-strip {
    right: 0
}

.x-tab-bar-right > .x-tab-bar-strip {
    left: 0
}

.x-tab-bar-horizontal .x-tab-bar-strip {
    width: 100%;
    left: 0
}

.x-tab-bar-vertical {
    display: table-cell
}

.x-tab-bar-vertical .x-tab-bar-strip {
    height: 100%;
    top: 0
}

.x-tab-bar-plain {
    background: transparent !important
}

.x-box-scroller-plain {
    background-color: transparent !important
}

.x-breadcrumb-btn .x-box-target:first-child {
    margin: 0
}

.x-breadcrumb-btn > .x-btn-split-right > .x-btn-button:after {
    content: none
}

.x-breadcrumb-btn.x-btn-over > .x-btn-split-right > .x-btn-button:after, .x-breadcrumb-btn.x-btn-menu-active > .x-btn-split-right > .x-btn-button:after {
    content: ''
}

.x-autowidth-table .x-grid-item-container {
    overflow: visible
}

.x-autowidth-table .x-grid-item {
    table-layout: auto;
    width: auto !important
}

.x-tree-view {
    overflow: hidden
}

.x-tree-elbow-img, .x-tree-icon {
    display: inline-block;
    text-align: center;
    background-repeat: no-repeat;
    background-position: 0 center;
    vertical-align: top
}

.x-tree-checkbox {
    display: inline-block;
    vertical-align: top;
    position: relative
}

.x-tree-animator-wrap {
    overflow: hidden
}

.x-body {
    color: #000;
    font-size: 12px;
    font-family: tahoma, arial, verdana, sans-serif
}

.x-animating-size, .x-collapsed {
    overflow: hidden !important
}

.x-animating-size {
    z-index: 10000
}

.x-editor .x-form-item-body {
    padding-bottom: 0
}

.x-mask {
    background-image: none;
    background-color: rgba(204, 204, 204, 0.5);
    cursor: default;
    border-style: solid;
    border-width: 1px;
    border-color: transparent
}

.x-ie8 .x-mask {
    -ms-filter: "progid:DXImageTransform.Microsoft.gradient(startColorstr=#80cccccc, endColorstr=#80cccccc)";
    zoom: 1
}

.x-mask.x-focus {
    border-style: solid;
    border-width: 1px;
    border-color: #c0d4ed
}

.x-mask-msg {
    padding: 2px;
    border-style: solid;
    border-width: 1px;
    border-color: #99bce8;
    background: #dfe9f6
}

.x-mask-msg-inner {
    padding: 0 5px;
    border-style: solid;
    border-width: 1px;
    border-color: #a3bad9;
    background-color: #eee;
    color: #222;
    font: normal 11px tahoma, arial, verdana, sans-serif
}

.x-mask-msg-text {
    padding: 5px 5px 5px 20px;
    /* background-image: url("data:image/gif;R0lGODlhEAAQALMMAKqooJGOhp2bk7e1rZ2bkre1rJCPhqqon8PBudDOxXd1bISCef///wAAAAAAAAAAACH/C05FVFNDQVBFMi4wAwEAAAAh+QQFAAAMACwAAAAAEAAQAAAET5DJyYyhmAZ7sxQEs1nMsmACGJKmSaVEOLXnK1PuBADepCiMg/DQ+/2GRI8RKOxJfpTCIJNIYArS6aRajWYZCASDa41Ow+Fx2YMWOyfpTAQAIfkEBQAADAAsAAAAABAAEAAABE6QyckEoZgKe7MEQMUxhoEd6FFdQWlOqTq15SlT9VQM3rQsjMKO5/n9hANixgjc9SQ/CgKRUSgw0ynFapVmGYkEg3v1gsPibg8tfk7CnggAIfkEBQAADAAsAAAAABAAEAAABE2QycnOoZjaA/IsRWV1goCBoMiUJTW8A0XMBPZmM4Ug3hQEjN2uZygahDyP0RBMEpmTRCKzWGCkUkq1SsFOFQrG1tr9gsPc3jnco4A9EQAh+QQFAAAMACwAAAAAEAAQAAAETpDJyUqhmFqbJ0LMIA7McWDfF5LmAVApOLUvLFMmlSTdJAiM3a73+wl5HYKSEET2lBSFIhMIYKRSimFriGIZiwWD2/WCw+Jt7xxeU9qZCAAh+QQFAAAMACwAAAAAEAAQAAAETZDJyRCimFqbZ0rVxgwF9n3hSJbeSQ2rCWIkpSjddBzMfee7nQ/XCfJ+OQYAQFksMgQBxumkEKLSCfVpMDCugqyW2w18xZmuwZycdDsRACH5BAUAAAwALAAAAAAQABAAAARNkMnJUqKYWpunUtXGIAj2feFIlt5JrWybkdSydNNQMLaND7pC79YBFnY+HENHMRgyhwPGaQhQotGm00oQMLBSLYPQ9QIASrLAq5x0OxEAIfkEBQAADAAsAAAAABAAEAAABE2QycmUopham+da1cYkCfZ94UiW3kmtbJuRlGF0E4Iwto3rut6tA9wFAjiJjkIgZAYDTLNJgUIpgqyAcTgwCuACJssAdL3gpLmbpLAzEQA7"); */
    background-image: url(data:image/gif;base64,R0lGODlhEAAQALMMAKqooJGOhp2bk7e1rZ2bkre1rJCPhqqon8PBudDOxXd1bISCef///wAAAAAAAAAAACH/C05FVFNDQVBFMi4wAwEAAAAh+QQFAAAMACwAAAAAEAAQAAAET5DJyYyhmAZ7sxQEs1nMsmACGJKmSaVEOLXnK1PuBADepCiMg/DQ+/2GRI8RKOxJfpTCIJNIYArS6aRajWYZCASDa41Ow+Fx2YMWOyfpTAQAIfkEBQAADAAsAAAAABAAEAAABE6QyckEoZgKe7MEQMUxhoEd6FFdQWlOqTq15SlT9VQM3rQsjMKO5/n9hANixgjc9SQ/CgKRUSgw0ynFapVmGYkEg3v1gsPibg8tfk7CnggAIfkEBQAADAAsAAAAABAAEAAABE2QycnOoZjaA/IsRWV1goCBoMiUJTW8A0XMBPZmM4Ug3hQEjN2uZygahDyP0RBMEpmTRCKzWGCkUkq1SsFOFQrG1tr9gsPc3jnco4A9EQAh+QQFAAAMACwAAAAAEAAQAAAETpDJyUqhmFqbJ0LMIA7McWDfF5LmAVApOLUvLFMmlSTdJAiM3a73+wl5HYKSEET2lBSFIhMIYKRSimFriGIZiwWD2/WCw+Jt7xxeU9qZCAAh+QQFAAAMACwAAAAAEAAQAAAETZDJyRCimFqbZ0rVxgwF9n3hSJbeSQ2rCWIkpSjddBzMfee7nQ/XCfJ+OQYAQFksMgQBxumkEKLSCfVpMDCugqyW2w18xZmuwZycdDsRACH5BAUAAAwALAAAAAAQABAAAARNkMnJUqKYWpunUtXGIAj2feFIlt5JrWybkdSydNNQMLaND7pC79YBFnY+HENHMRgyhwPGaQhQotGm00oQMLBSLYPQ9QIASrLAq5x0OxEAIfkEBQAADAAsAAAAABAAEAAABE2QycmUopham+da1cYkCfZ94UiW3kmtbJuRlGF0E4Iwto3rut6tA9wFAjiJjkIgZAYDTLNJgUIpgqyAcTgwCuACJssAdL3gpLmbpLAzEQA7)
    background-repeat: no-repeat;
    background-position: 0 center
}

.x-progress-default {
    background-color: #e0e8f3;
    border-width: 1px;
    height: 20px;
    border-color: #6594cf;
    border-style: solid
}

.x-progress-default .x-progress-bar-default {
    background-image: none;
    background-color: #73a3e0;
    background-image: -webkit-gradient(linear, top, bottom, color-stop(0%, #b2ccee), color-stop(50%, #88b1e5), color-stop(51%, #73a3e0), color-stop(0%, #5e96db));
    background-image: -webkit-linear-gradient(top, #b2ccee, #88b1e5 50%, #73a3e0 51%, #5e96db);
    background-image: -moz-linear-gradient(top, #b2ccee, #88b1e5 50%, #73a3e0 51%, #5e96db);
    background-image: -o-linear-gradient(top, #b2ccee, #88b1e5 50%, #73a3e0 51%, #5e96db);
    background-image: -ms-linear-gradient(top, #b2ccee, #88b1e5 50%, #73a3e0 51%, #5e96db);
    background-image: linear-gradient(top, #b2ccee, #88b1e5 50%, #73a3e0 51%, #5e96db)
}

.x-nlg .x-progress-default .x-progress-bar-default {
    background: repeat-x;
    /* background-image: url("data:image/gif;R0lGODlhAQAgA/QAAF+W22GY22SZ3Gab3Wic3Wue3m2f3m+h33Ki34qy5Y+15pO455i76J2+6aHB6qbE66vH7K/K7f///1+W21+W21+W21+W21+W21+W21+W21+W21+W21+W21+W21+W21+W2yH5BAEAABIALAAAAAABACADRAhFACMkCACgoMGDCBMqXMiwocOHEBM2KBCxosWLGDE+WHBgQMaPIEOKHEmypEUIDhgoQGCAgACTMGPKnEmzps2bOHPqLBgQADs=") */
    background-image: url(data:image/gif;base64,R0lGODlhAQAgA/QAAF+W22GY22SZ3Gab3Wic3Wue3m2f3m+h33Ki34qy5Y+15pO455i76J2+6aHB6qbE66vH7K/K7f///1+W21+W21+W21+W21+W21+W21+W21+W21+W21+W21+W21+W21+W2yH5BAEAABIALAAAAAABACADRAhFACMkCACgoMGDCBMqXMiwocOHEBM2KBCxosWLGDE+WHBgQMaPIEOKHEmypEUIDhgoQGCAgACTMGPKnEmzps2bOHPqLBgQADs=)
}

.x-progress-default .x-progress-text {
    color: #fff;
    font-weight: bold;
    font-size: 11px;
    font-family: tahoma, arial, verdana, sans-serif;
    text-align: center;
    line-height: 18px
}

.x-progress-default .x-progress-text-back {
    color: #396295;
    line-height: 18px
}

.x-progress-default.x-progress-focus:after {
    position: absolute;
    content: ' ';
    top: 0px;
    right: 0px;
    bottom: 0px;
    left: 0px;
    border: 1px solid #6594cf;
    pointer-events: none
}

.x-cmd-slicer.x-progress-bar-default:before {
    display: none;
    content: "x-slicer:, bg:url("data:image/gif;R0lGODlhAQAgA/QAAF+W22GY22SZ3Gab3Wic3Wue3m2f3m+h33Ki34qy5Y+15pO455i76J2+6aHB6qbE66vH7K/K7f///1+W21+W21+W21+W21+W21+W21+W21+W21+W21+W21+W21+W21+W2yH5BAEAABIALAAAAAABACADRAhFACMkCACgoMGDCBMqXMiwocOHEBM2KBCxosWLGDE+WHBgQMaPIEOKHEmypEUIDhgoQGCAgACTMGPKnEmzps2bOHPqLBgQADs="), stretch:bottom" !important
}

.x-progressbar-default-cell > .x-grid-cell-inner, .x-progress-default-cell > .x-grid-cell-inner, .x-progressbarwidget-default-cell > .x-grid-cell-inner {
    padding-top: 0px;
    padding-bottom: 0px
}

.x-progressbar-default-cell > .x-grid-cell-inner .x-progress-default, .x-progress-default-cell > .x-grid-cell-inner .x-progress-default, .x-progressbarwidget-default-cell > .x-grid-cell-inner .x-progress-default {
    height: 18px
}

.x-btn-default-small {
    -webkit-border-radius: 3px;
    -moz-border-radius: 3px;
    -ms-border-radius: 3px;
    -o-border-radius: 3px;
    border-radius: 3px;
    padding: 2px 2px 2px 2px;
    border-width: 1px;
    border-style: solid;
    background-image: none;
    background-color: #fff;
    background-image: -webkit-gradient(linear, top, bottom, color-stop(0%, #fff), color-stop(48%, #f9f9f9), color-stop(52%, #e2e2e2), color-stop(0%, #e7e7e7));
    background-image: -webkit-linear-gradient(top, #fff, #f9f9f9 48%, #e2e2e2 52%, #e7e7e7);
    background-image: -moz-linear-gradient(top, #fff, #f9f9f9 48%, #e2e2e2 52%, #e7e7e7);
    background-image: -o-linear-gradient(top, #fff, #f9f9f9 48%, #e2e2e2 52%, #e7e7e7);
    background-image: -ms-linear-gradient(top, #fff, #f9f9f9 48%, #e2e2e2 52%, #e7e7e7);
    background-image: linear-gradient(top, #fff, #f9f9f9 48%, #e2e2e2 52%, #e7e7e7)
}

.x-btn-default-small-mc {
    /* background-image: url("data:image/gif;R0lGODlhAQAgA/MAAOLi4uPj4+Tk5OXl5fn5+fr6+vv7+/z8/P39/f///+Li4uLi4uLi4uLi4uLi4uLi4iH5BAEAAAkALAAAAAABACADQwhCABEAGECwoMGDCBMqXMiwocOHCQsIgEixosWLFw8QCICxo8ePIEOKHGnxgIECBAAEmEiypcuXMGPKnEmzps2bBAMCADs=");*/
    background-image: url(data:image/gif;base64,R0lGODlhAQAgA/MAAOLi4uPj4+Tk5OXl5fn5+fr6+vv7+/z8/P39/f///+Li4uLi4uLi4uLi4uLi4uLi4iH5BAEAAAkALAAAAAABACADQwhCABEAGECwoMGDCBMqXMiwocOHCQsIgEixosWLFw8QCICxo8ePIEOKHGnxgIECBAAEmEiypcuXMGPKnEmzps2bBAMCADs=)
    background-position: 0 top;
    background-color: #fff
}

.x-nbr .x-btn-default-small {
    padding: 0 !important;
    border-width: 0 !important;
    -webkit-border-radius: 0px;
    -moz-border-radius: 0px;
    -ms-border-radius: 0px;
    -o-border-radius: 0px;
    border-radius: 0px;
    background-color: transparent !important;
    background-image: none;
    box-shadow: none !important
}

.x-btn-default-small-frameInfo {
    font-family: th-3-3-3-3-1-1-1-1-2-2-2-2
}

.x-btn-default-small-tl {
    background-position: 0 -6px
}

.x-btn-default-small-tr {
    background-position: right -9px
}

.x-btn-default-small-bl {
    background-position: 0 -12px
}

.x-btn-default-small-br {
    background-position: right -15px
}

.x-btn-default-small-ml {
    background-position: 0 top
}

.x-btn-default-small-mr {
    background-position: right top
}

.x-btn-default-small-tc {
    background-position: 0 0
}

.x-btn-default-small-bc {
    background-position: 0 -3px
}

.x-btn-default-small-tr, .x-btn-default-small-br, .x-btn-default-small-mr {
    padding-right: 3px
}

.x-btn-default-small-tl, .x-btn-default-small-bl, .x-btn-default-small-ml {
    padding-left: 3px
}

.x-btn-default-small-tc {
    height: 3px
}

.x-btn-default-small-bc {
    height: 3px
}

.x-btn-default-small-tl, .x-btn-default-small-bl, .x-btn-default-small-tr, .x-btn-default-small-br, .x-btn-default-small-tc, .x-btn-default-small-bc, .x-btn-default-small-ml, .x-btn-default-small-mr {
    /* background-image: url("data:image/gif;R0lGODlhAwASAPMAANHR0dXV1dbW1tjY2N/f3+Tk5Obm5vr6+v7+/v///wAAANHR0dHR0dHR0dHR0dHR0SH5BAEAAAkALAAAAAADABIAQwgyAAEIDHAAQYEBBhIaCFDAAIKHCRYeIGAgooCHCBQKBGCAwIEAFREcEGBgQMMCAkgmCAgAOw==")*/
    background-image: url(data:image/gif;base64,R0lGODlhAwASAPMAANHR0dXV1dbW1tjY2N/f3+Tk5Obm5vr6+v7+/v///wAAANHR0dHR0dHR0dHR0dHR0SH5BAEAAAkALAAAAAADABIAQwgyAAEIDHAAQYEBBhIaCFDAAIKHCRYeIGAgooCHCBQKBGCAwIEAFREcEGBgQMMCAkgmCAgAOw==)
}

.x-btn-default-small-ml, .x-btn-default-small-mr {
    /* background-image: url("data:image/gif;R0lGODlhBgAgA/MAANHR0eLi4uPj4+Tk5OXl5fn5+fr6+vv7+/z8/P39/f///9HR0dHR0dHR0dHR0dHR0SH5BAEAAAoALAAAAAAGACADQwj/AAEkGJgAAIAACAMYJMCQwMKGDxlGdAigIUWLEzNWhLhRYseLHDF+1CiyZMiTHk2mRAlypcuWMEmylPmSZsyROFXe1GmzZ86ZP2sG3QmU51CfRpMWXSpUaVOmRJ9KjUoVKVSDBrIaMDig6wCrU8FWPUrW6VizYtOWvbo2bNuzbNG+VSu3bty7bu3mxQt3r9++gNUiGIzAYIHDBQwKWCyALl/HfyEHnktZ72TLkjNXfrw5cufLnDF/1iy6dOjTnk2nRg16tevWsEmzlv2aduzRuFXf1m27N1nChQEcGH4Aq1bDiA0mVAiAcWMAXr/mnj29dvXd1Hlf9629e/bv1r2HQgePfbz58ui5k1d/nn367fDFv5fvvn789ffb55+Pn/5++/4F2N+A+glYIIH8HahgggwCiKCDC0LY4H8UGjihhRkFBAA7")*/
    background-image: url(data:image/gif;base64,R0lGODlhBgAgA/MAANHR0eLi4uPj4+Tk5OXl5fn5+fr6+vv7+/z8/P39/f///9HR0dHR0dHR0dHR0dHR0SH5BAEAAAoALAAAAAAGACADQwj/AAEkGJgAAIAACAMYJMCQwMKGDxlGdAigIUWLEzNWhLhRYseLHDF+1CiyZMiTHk2mRAlypcuWMEmylPmSZsyROFXe1GmzZ86ZP2sG3QmU51CfRpMWXSpUaVOmRJ9KjUoVKVSDBrIaMDig6wCrU8FWPUrW6VizYtOWvbo2bNuzbNG+VSu3bty7bu3mxQt3r9++gNUiGIzAYIHDBQwKWCyALl/HfyEHnktZ72TLkjNXfrw5cufLnDF/1iy6dOjTnk2nRg16tevWsEmzlv2aduzRuFXf1m27N1nChQEcGH4Aq1bDiA0mVAiAcWMAXr/mnj29dvXd1Hlf9629e/bv1r2HQgePfbz58ui5k1d/nn367fDFv5fvvn789ffb55+Pn/5++/4F2N+A+glYIIH8HahgggwCiKCDC0LY4H8UGjihhRkFBAA7)
}

.x-btn-default-small-mc {
    padding: 0px 0px 0px 0px
}

.x-cmd-slicer.x-btn-default-small:before {
    display: none;
    /* content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, frame-bg:url("data:image/gif;R0lGODlhAQAgA/MAAOLi4uPj4+Tk5OXl5fn5+fr6+vv7+/z8/P39/f///+Li4uLi4uLi4uLi4uLi4uLi4iH5BAEAAAkALAAAAAABACADQwhCABEAGECwoMGDCBMqXMiwocOHCQsIgEixosWLFw8QCICxo8ePIEOKHGnxgIECBAAEmEiypcuXMGPKnEmzps2bBAMCADs="), corners:url("data:image/gif;R0lGODlhAwASAPMAANHR0dXV1dbW1tjY2N/f3+Tk5Obm5vr6+v7+/v///wAAANHR0dHR0dHR0dHR0dHR0SH5BAEAAAkALAAAAAADABIAQwgyAAEIDHAAQYEBBhIaCFDAAIKHCRYeIGAgooCHCBQKBGCAwIEAFREcEGBgQMMCAkgmCAgAOw=="), sides:url("data:image/gif;R0lGODlhBgAgA/MAANHR0eLi4uPj4+Tk5OXl5fn5+fr6+vv7+/z8/P39/f///9HR0dHR0dHR0dHR0dHR0SH5BAEAAAoALAAAAAAGACADQwj/AAEkGJgAAIAACAMYJMCQwMKGDxlGdAigIUWLEzNWhLhRYseLHDF+1CiyZMiTHk2mRAlypcuWMEmylPmSZsyROFXe1GmzZ86ZP2sG3QmU51CfRpMWXSpUaVOmRJ9KjUoVKVSDBrIaMDig6wCrU8FWPUrW6VizYtOWvbo2bNuzbNG+VSu3bty7bu3mxQt3r9++gNUiGIzAYIHDBQwKWCyALl/HfyEHnktZ72TLkjNXfrw5cufLnDF/1iy6dOjTnk2nRg16tevWsEmzlv2aduzRuFXf1m27N1nChQEcGH4Aq1bDiA0mVAiAcWMAXr/mnj29dvXd1Hlf9629e/bv1r2HQgePfbz58ui5k1d/nn367fDFv5fvvn789ffb55+Pn/5++/4F2N+A+glYIIH8HahgggwCiKCDC0LY4H8UGjihhRkFBAA7")" !important*/
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, frame-bg:url(data:image/gif;base64,R0lGODlhAQAgA/MAAOLi4uPj4+Tk5OXl5fn5+fr6+vv7+/z8/P39/f///+Li4uLi4uLi4uLi4uLi4uLi4iH5BAEAAAkALAAAAAABACADQwhCABEAGECwoMGDCBMqXMiwocOHCQsIgEixosWLFw8QCICxo8ePIEOKHGnxgIECBAAEmEiypcuXMGPKnEmzps2bBAMCADs=), corners:url(data:image/gif;base64,R0lGODlhAwASAPMAANHR0dXV1dbW1tjY2N/f3+Tk5Obm5vr6+v7+/v///wAAANHR0dHR0dHR0dHR0dHR0SH5BAEAAAkALAAAAAADABIAQwgyAAEIDHAAQYEBBhIaCFDAAIKHCRYeIGAgooCHCBQKBGCAwIEAFREcEGBgQMMCAkgmCAgAOw==), sides:url(data:image/gif;base64,R0lGODlhBgAgA/MAANHR0eLi4uPj4+Tk5OXl5fn5+fr6+vv7+/z8/P39/f///9HR0dHR0dHR0dHR0dHR0SH5BAEAAAoALAAAAAAGACADQwj/AAEkGJgAAIAACAMYJMCQwMKGDxlGdAigIUWLEzNWhLhRYseLHDF+1CiyZMiTHk2mRAlypcuWMEmylPmSZsyROFXe1GmzZ86ZP2sG3QmU51CfRpMWXSpUaVOmRJ9KjUoVKVSDBrIaMDig6wCrU8FWPUrW6VizYtOWvbo2bNuzbNG+VSu3bty7bu3mxQt3r9++gNUiGIzAYIHDBQwKWCyALl/HfyEHnktZ72TLkjNXfrw5cufLnDF/1iy6dOjTnk2nRg16tevWsEmzlv2aduzRuFXf1m27N1nChQEcGH4Aq1bDiA0mVAiAcWMAXr/mnj29dvXd1Hlf9629e/bv1r2HQgePfbz58ui5k1d/nn367fDFv5fvvn789ffb55+Pn/5++/4F2N+A+glYIIH8HahgggwCiKCDC0LY4H8UGjihhRkFBAA7)" !important
}

.x-btn-default-small {
    border-color: #d1d1d1
}

.x-btn-button-default-small {
    min-height: 16px
}

.x-ie9m .x-btn-button-default-small {
    min-height: auto;
    height: 16px
}

.x-btn-inner-default-small {
    font: normal 11px/16px tahoma, arial, verdana, sans-serif;
    color: #333;
    padding: 0 4px;
    max-width: 100%
}

.x-btn-icon-right > .x-btn-inner-default-small, .x-btn-icon-left > .x-btn-inner-default-small {
    max-width: calc(100% - 16px)
}

.x-ie10p .x-btn-inner-default-small {
    max-width: none
}

.x-btn-icon-el-default-small {
    font-size: 16px;
    height: 16px;
    color: #333;
    line-height: 16px
}

.x-btn-icon-left > .x-btn-icon-el-default-small, .x-btn-icon-right > .x-btn-icon-el-default-small {
    width: 16px
}

.x-btn-icon-top > .x-btn-icon-el-default-small, .x-btn-icon-bottom > .x-btn-icon-el-default-small {
    min-width: 16px
}

.x-btn-icon-el-default-small.x-btn-glyph {
    opacity: 0.5
}

.x-ie8 .x-btn-icon-el-default-small.x-btn-glyph {
    color: #999
}

.x-btn-text.x-btn-icon-left > .x-btn-icon-el-default-small {
    margin-right: 0px
}

.x-btn-text.x-btn-icon-right > .x-btn-icon-el-default-small {
    margin-left: 0px
}

.x-btn-text.x-btn-icon-top > .x-btn-icon-el-default-small {
    margin-bottom: 4px
}

.x-btn-text.x-btn-icon-bottom > .x-btn-icon-el-default-small {
    margin-top: 4px
}

.x-btn-arrow-right > .x-btn-icon.x-btn-no-text.x-btn-button-default-small {
    padding-right: 4px
}

.x-btn-arrow-right > .x-btn-text.x-btn-icon-right > .x-btn-icon-el-default-small {
    margin-right: 4px
}

.x-btn-arrow-bottom > .x-btn-button-default-small, .x-btn-split-bottom > .x-btn-button-default-small {
    padding-bottom: 2px
}

.x-btn-wrap-default-small.x-btn-arrow-right:after {
    width: 8px;
    background-image: url(data:image/gif;base64,R0lGODlhCgAKAIcAAAAAAP///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAAEALAAAAAAKAAoAAAgZAAMIHEiwoMGDCA0CWLhQYcODABJKnFgwIAA7);
    padding-right: 8px
}

.x-btn-wrap-default-small.x-btn-arrow-bottom:after {
    height: 8px;
    background-image:url(data:image/gif;base64,R0lGODlhCgAKAIcAAAAAAP///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAAEALAAAAAAKAAoAAAgZAAMIHEiwoMGDCA0CWLhQYcODABJKnFgwIAA7)
}

.x-btn-wrap-default-small.x-btn-split-right:after {
    width: 14px;
    background-image: url(data:image/gif;base64,R0lGODlhDgBIAMIEAAAAAMnJycLa9vX19f///////////////yH5BAEKAAIALAAAAAAOAEgAAANcGCPczupJEaerFq6sefdYFlrjVErnk14btzbv57YiTdomjuoqz3oUH0woqwFjwSMxCVoinzSAVDp8TH/WnnLb5M68xq74Ow6Tz+b0Dbwut9FvdY49d9fhd/kOmAAAOw==);
    padding-right: 14px
}

.x-btn-wrap-default-small.x-btn-split-bottom:after {
    height: 14px;
    background-image: url(data:image/gif;base64,R0lGODlhyAAOAMIDAAAAAMTExMLa9v///////////////////yH5BAEKAAIALAAAAADIAA4AAANdGLrc/jDKSau9OOsth/9gKI5kaZ5oqq5s676mIM90bd94ru987//AoHBILBqPyKRyyWw6n9CodEqtWq/YrHbL7XqBgHD4Sy6bZeKzeq0FsN/wuHxOr9vv+Lx+v04AADs=)
}

.x-btn-over > .x-btn-wrap-default-small.x-btn-split-right:after {
    /* background-image: url("data:image/gif;R0lGODlhDgBIAMIEAAAAAKrI8cLa9tru/////////////////yH5BAEKAAIALAAAAAAOAEgAAANcGCPczupJEaerFq6sefdYFlrjVErnk14btzbv57YiTdomjuoqz3oUH0woqwFjwSMxCVoinzSAVDp8TH/WnnLb5M68xq74Ow6Tz+b0Dbwut9FvdY49d9fhd/kOmAAAOw==")*/
     background-image: url(data:image/gif;base64,R0lGODlhDgBIAMIEAAAAAKrI8cLa9tru/////////////////yH5BAEKAAIALAAAAAAOAEgAAANcGCPczupJEaerFq6sefdYFlrjVErnk14btzbv57YiTdomjuoqz3oUH0woqwFjwSMxCVoinzSAVDp8TH/WnnLb5M68xq74Ow6Tz+b0Dbwut9FvdY49d9fhd/kOmAAAOw==)
}

.x-btn-over > .x-btn-wrap-default-small.x-btn-split-bottom:after {
    /* background-image: url("data:image/gif;R0lGODlhyAAOAKEDAAAAAKrI8e/4/////yH5BAEKAAMALAAAAADIAA4AAAJbjI+py+0Po5y02uuE3rz7D4biSJbmiabqKg7uC8fyTNf2jef6zvf+DwwKh8Si8YhMKpfMpvMJjUqn1Kr1is1qeYBudwsOi13esflsBaDX7Lb7DY/L5/S6/X4uAAA7") */
    background-image: url(data:image/gif;base64,R0lGODlhDgBIAMIEAAAAAKrI8cLa9tru/////////////////yH5BAEKAAIALAAAAAAOAEgAAANcGCPczupJEaerFq6sefdYFlrjVErnk14btzbv57YiTdomjuoqz3oUH0woqwFjwSMxCVoinzSAVDp8TH/WnnLb5M68xq74Ow6Tz+b0Dbwut9FvdY49d9fhd/kOmAAAOw==) 
}

.x-btn-split-right > .x-btn-icon.x-btn-no-text.x-btn-button-default-small {
    padding-right: 4px
}

.x-btn-split-right > .x-btn-text.x-btn-icon-right > .x-btn-icon-el-default-small {
    margin-right: 4px
}

.x-btn-focus.x-btn-default-small {
    border-color: #b0ccf2;
    background-image: none;
    background-color: #fff;
    background-image: -webkit-gradient(linear, top, bottom, color-stop(0%, #fff), color-stop(48%, #f9f9f9), color-stop(52%, #e7e7e7), color-stop(0%, #ececec));
    background-image: -webkit-linear-gradient(top, #fff, #f9f9f9 48%, #e7e7e7 52%, #ececec);
    background-image: -moz-linear-gradient(top, #fff, #f9f9f9 48%, #e7e7e7 52%, #ececec);
    background-image: -o-linear-gradient(top, #fff, #f9f9f9 48%, #e7e7e7 52%, #ececec);
    background-image: -ms-linear-gradient(top, #fff, #f9f9f9 48%, #e7e7e7 52%, #ececec);
    background-image: linear-gradient(top, #fff, #f9f9f9 48%, #e7e7e7 52%, #ececec)
}

.x-btn-focus.x-btn-default-small .x-btn-wrap {
    outline: 1px dotted #333
}

.x-btn-default-small .x-btn-arrow-el {
    position: absolute;
    top: 0;
    right: 0;
    height: 100%;
    width: 16px;
    pointer-events: none
}

.x-btn-over.x-btn-default-small {
    border-color: #b0ccf2;
    background-image: none;
    background-color: #e4f3ff;
    background-image: -webkit-gradient(linear, top, bottom, color-stop(0%, #e4f3ff), color-stop(48%, #d9edff), color-stop(52%, #c2d8f2), color-stop(0%, #c6dcf6));
    background-image: -webkit-linear-gradient(top, #e4f3ff, #d9edff 48%, #c2d8f2 52%, #c6dcf6);
    background-image: -moz-linear-gradient(top, #e4f3ff, #d9edff 48%, #c2d8f2 52%, #c6dcf6);
    background-image: -o-linear-gradient(top, #e4f3ff, #d9edff 48%, #c2d8f2 52%, #c6dcf6);
    background-image: -ms-linear-gradient(top, #e4f3ff, #d9edff 48%, #c2d8f2 52%, #c6dcf6);
    background-image: linear-gradient(top, #e4f3ff, #d9edff 48%, #c2d8f2 52%, #c6dcf6)
}

.x-btn.x-btn-menu-active.x-btn-default-small, .x-btn.x-btn-pressed.x-btn-default-small {
    border-color: #9ebae1;
    background-image: none;
    background-color: #b6cbe4;
    background-image: -webkit-gradient(linear, top, bottom, color-stop(0%, #b6cbe4), color-stop(48%, #bfd2e6), color-stop(52%, #8dc0f5), color-stop(0%, #98c5f5));
    background-image: -webkit-linear-gradient(top, #b6cbe4, #bfd2e6 48%, #8dc0f5 52%, #98c5f5);
    background-image: -moz-linear-gradient(top, #b6cbe4, #bfd2e6 48%, #8dc0f5 52%, #98c5f5);
    background-image: -o-linear-gradient(top, #b6cbe4, #bfd2e6 48%, #8dc0f5 52%, #98c5f5);
    background-image: -ms-linear-gradient(top, #b6cbe4, #bfd2e6 48%, #8dc0f5 52%, #98c5f5);
    background-image: linear-gradient(top, #b6cbe4, #bfd2e6 48%, #8dc0f5 52%, #98c5f5)
}

.x-btn.x-btn-disabled.x-btn-default-small {
    border-color: #e1e1e1;
    background-image: none;
    background-color: #f7f7f7;
    background-image: -webkit-gradient(linear, top, bottom, color-stop(0%, #f7f7f7), color-stop(48%, #f1f1f1), color-stop(52%, #dadada), color-stop(0%, #dfdfdf));
    background-image: -webkit-linear-gradient(top, #f7f7f7, #f1f1f1 48%, #dadada 52%, #dfdfdf);
    background-image: -moz-linear-gradient(top, #f7f7f7, #f1f1f1 48%, #dadada 52%, #dfdfdf);
    background-image: -o-linear-gradient(top, #f7f7f7, #f1f1f1 48%, #dadada 52%, #dfdfdf);
    background-image: -ms-linear-gradient(top, #f7f7f7, #f1f1f1 48%, #dadada 52%, #dfdfdf);
    background-image: linear-gradient(top, #f7f7f7, #f1f1f1 48%, #dadada 52%, #dfdfdf)
}

.x-btn-focus .x-btn-default-small-tl, .x-btn-focus .x-btn-default-small-bl, .x-btn-focus .x-btn-default-small-tr, .x-btn-focus .x-btn-default-small-br, .x-btn-focus .x-btn-default-small-tc, .x-btn-focus .x-btn-default-small-bc {
    /*background-image: url("data:image/gif;R0lGODlhAwASAPMAALDM8rfQ87fR88LV8Mjb9tTi9+bo7Ovr6/f5/f7+/v///wAAALDM8rDM8rDM8rDM8iH5BAEAAAoALAAAAAADABIAQwgzAAEIDIAggYEBBQ4oDGDgQIKHCgoQJFAgooCHCRQeEAigAAEEASomQCCgwICGBgSUVBAQADs=")*/
    background-image: url(data:image/gif;base64,R0lGODlhAwASAPMAALDM8rfQ87fR88LV8Mjb9tTi9+bo7Ovr6/f5/f7+/v///wAAALDM8rDM8rDM8rDM8iH5BAEAAAoALAAAAAADABIAQwgzAAEIDIAggYEBBQ4oDGDgQIKHCgoQJFAgooCHCRQeEAigAAEEASomQCCgwICGBgSUVBAQADs=)
}

.x-btn-focus .x-btn-default-small-ml, .x-btn-focus .x-btn-default-small-mr {
    /* background-image: url("data:image/gif;R0lGODlhBgAgA/MAALDM8ufn5+jo6Onp6erq6vn5+fr6+vv7+/z8/P39/f///7DM8rDM8rDM8rDM8rDM8iH5BAEAAAoALAAAAAAGACADQwj/AAEkGJgAAIAACAMYJMCQwMKGDxlGdAigIUWLEzNWhLhRYseLHDF+1CiyZMiTHk2mRAlypcuWMEmylPmSZsyROFXe1GmzZ86ZP2sG3QmU51CfRpMWXSpUaVOmRJ9KjUoVKVSDBrIaMDig6wCrU8FWPUrW6VizYtOWvbo2bNuzbNG+VSu3bty7bu3mxQt3r9++gNUiGIzAYIHDBQwKWCyALl/HfyEHnktZ72TLkjNXfrw5cufLnDF/1iy6dOjTnk2nRg16tevWsEmzlv2aduzRuFXf1m27N1nChQEcGH4Aq1bDiA0mVAiAcWMAXr/mnj29dvXd1Hlf9629e/bv1r2HQgePfbz58ui5k1d/nn367fDFv5fvvn789ffb55+Pn/5++/4F2N+A+glYIIH8HahgggwCiKCDC0LY4H8UGjihhRkFBAA7")*/
     background-image: url(data:image/gif;base64,R0lGODlhAwASAPMAALDM8rfQ87fR88LV8Mjb9tTi9+bo7Ovr6/f5/f7+/v///wAAALDM8rDM8rDM8rDM8iH5BAEAAAoALAAAAAADABIAQwgzAAEIDIAggYEBBQ4oDGDgQIKHCgoQJFAgooCHCRQeEAigAAEEASomQCCgwICGBgSUVBAQADs=)
    
}

.x-btn-focus .x-btn-default-small-mc {
    background-color: #fff;
    /*background-image: url("data:image/gif;R0lGODlhAQAgA/MAAOfn5+jo6Onp6erq6vn5+fr6+vv7+/z8/P39/f///+fn5+fn5+fn5+fn5+fn5+fn5yH5BAEAAAkALAAAAAABACADQwhCABEAGECwoMGDCBMqXMiwocOHCQsIgEixosWLFw8QCICxo8ePIEOKHGnxgIECBAAEmEiypcuXMGPKnEmzps2bBAMCADs=")*/
    background-image: url(data:image/gif;base64,R0lGODlhAQAgA/MAAOfn5+jo6Onp6erq6vn5+fr6+vv7+/z8/P39/f///+fn5+fn5+fn5+fn5+fn5+fn5yH5BAEAAAkALAAAAAABACADQwhCABEAGECwoMGDCBMqXMiwocOHCQsIgEixosWLFw8QCICxo8ePIEOKHGnxgIECBAAEmEiypcuXMGPKnEmzps2bBAMCADs=)
}

.x-btn-over .x-btn-default-small-tl, .x-btn-over .x-btn-default-small-bl, .x-btn-over .x-btn-default-small-tr, .x-btn-over .x-btn-default-small-br, .x-btn-over .x-btn-default-small-tc, .x-btn-over .x-btn-default-small-bc {
 /*   background-image: url("data:image/gif;R0lGODlhAwASAPMAALDM8rfQ87fR88DX9sPZ9cXb9dTi997u/t/u/uLy/+Py/////wAAALDM8rDM8rDM8iH5BAEAAAsALAAAAAADABIAQwgzAAEIDHAgAYEABgooDECgQIKHCwwEQDDAQEQBCjIqLCAQgIEBCBAuSHBAgMSGBASYXBAQADs=")*/
    background-image: url(data:image/gif;base64,R0lGODlhAwASAPMAALDM8rfQ87fR88DX9sPZ9cXb9dTi997u/t/u/uLy/+Py/////wAAALDM8rDM8rDM8iH5BAEAAAsALAAAAAADABIAQwgzAAEIDHAgAYEABgooDECgQIKHCwwEQDDAQEQBCjIqLCAQgIEBCBAuSHBAgMSGBASYXBAQADs=)
}

.x-btn-over .x-btn-default-small-ml, .x-btn-over .x-btn-default-small-mr {
/*    background-image: url("data:image/gif;R0lGODlhBgAgA/MAALDM8sLY8sPZ88Ta9Nnt/9rt/9vu/9zu/93v/97w/+Dw/+Hx/////7DM8rDM8rDM8iH5BAEAAAwALAAAAAAGACADQwj/AAEsGLgAAIAACAMYHMBwwMKGDxlGdAigIUWLEzNWhLhRYseLHDF+1CiyZMiTHk2mRAlypcuWMEmylPmSZsyROFXe1GmzZ86ZP2sG3QmU51CfRpMWXSpUaVOmRJ9KjUoVKVSDB7IeMCigqwCrU8FWPUrW6VizYtOWvbo2bNuzbNG+VSu3bty7bu3mxQt3r9++gNUmGJzAYIHDBQwmVDi3sd7AjvnSlRz572TLlSE/vqyZ8ubMnEODHv25tOfTmE2nRt15tevWsEWrjk2atWzbtV/f1p0bsoLfCgwiGI7AoIHjBgwSWE5AcUKuXnfTni29em/r1K9rz84dd3fe36d7QR8Pnrz48ujPq8dunn169+u3t5f/nn788PDz29ePf7///gDOF2B9A94n4IEEImhgggwu6CB/CkLYoIQP/hfhSAEBADs=") */
    background-image: url(data:image/gif;base64,R0lGODlhBgAgA/MAALDM8sLY8sPZ88Ta9Nnt/9rt/9vu/9zu/93v/97w/+Dw/+Hx/////7DM8rDM8rDM8iH5BAEAAAwALAAAAAAGACADQwj/AAEsGLgAAIAACAMYHMBwwMKGDxlGdAigIUWLEzNWhLhRYseLHDF+1CiyZMiTHk2mRAlypcuWMEmylPmSZsyROFXe1GmzZ86ZP2sG3QmU51CfRpMWXSpUaVOmRJ9KjUoVKVSDB7IeMCigqwCrU8FWPUrW6VizYtOWvbo2bNuzbNG+VSu3bty7bu3mxQt3r9++gNUmGJzAYIHDBQwmVDi3sd7AjvnSlRz572TLlSE/vqyZ8ubMnEODHv25tOfTmE2nRt15tevWsEWrjk2atWzbtV/f1p0bsoLfCgwiGI7AoIHjBgwSWE5AcUKuXnfTni29em/r1K9rz84dd3fe36d7QR8Pnrz48ujPq8dunn169+u3t5f/nn788PDz29ePf7///gDOF2B9A94n4IEEImhgggwu6CB/CkLYoIQP/hfhSAEBADs=)
}

.x-btn-over .x-btn-default-small-mc {
    background-color: #e4f3ff;
    /* background-image: url("data:image/gif;R0lGODlhAQAgA/MAAMLY8sPZ88Ta9Nnt/9rt/9vu/9zu/93v/97w/+Dw/+Hx/////8LY8sLY8sLY8sLY8iH5BAEAAAsALAAAAAABACADQwhBABUAEECwoMGDCBMqXMiwocOHCQ0EgEixosWLFxEQGIixo8ePIEOKHFkxwYECAwBMJMmypcuXMGPKnEmzps2CAQEAOw==") */
    background-image: url(data:image/gif;base64,R0lGODlhAQAgA/MAAMLY8sPZ88Ta9Nnt/9rt/9vu/9zu/93v/97w/+Dw/+Hx/////8LY8sLY8sLY8sLY8iH5BAEAAAsALAAAAAABACADQwhBABUAEECwoMGDCBMqXMiwocOHCQ0EgEixosWLFxEQGIixo8ePIEOKHFkxwYECAwBMJMmypcuXMGPKnEmzps2CAQEAOw==)
}

.x-btn-focus.x-btn-over .x-btn-default-small-tl, .x-btn-focus.x-btn-over .x-btn-default-small-bl, .x-btn-focus.x-btn-over .x-btn-default-small-tr, .x-btn-focus.x-btn-over .x-btn-default-small-br, .x-btn-focus.x-btn-over .x-btn-default-small-tc, .x-btn-focus.x-btn-over .x-btn-default-small-bc {
    /* background-image: url("data:image/gif;R0lGODlhAwASAPMAALDM8rfQ87fR88DX9sPZ9cXb9dTi997u/t/u/uLy/+Py/////wAAALDM8rDM8rDM8iH5BAEAAAsALAAAAAADABIAQwgzAAEIDHAgAYEABgooDECgQIKHCwwEQDDAQEQBCjIqLCAQgIEBCBAuSHBAgMSGBASYXBAQADs=")*/ 
    background-image: url(data:image/gif;base64,R0lGODlhAwASAPMAALDM8rfQ87fR88DX9sPZ9cXb9dTi997u/t/u/uLy/+Py/////wAAALDM8rDM8rDM8iH5BAEAAAsALAAAAAADABIAQwgzAAEIDHAgAYEABgooDECgQIKHCwwEQDDAQEQBCjIqLCAQgIEBCBAuSHBAgMSGBASYXBAQADs=)
}

.x-btn-focus.x-btn-over .x-btn-default-small-ml, .x-btn-focus.x-btn-over .x-btn-default-small-mr {
    /* background-image: url("data:image/gif;R0lGODlhBgAgA/MAALDM8sLY8sPZ88Ta9Nnt/9rt/9vu/9zu/93v/97w/+Dw/+Hx/////7DM8rDM8rDM8iH5BAEAAAwALAAAAAAGACADQwj/AAEsGLgAAIAACAMYHMBwwMKGDxlGdAigIUWLEzNWhLhRYseLHDF+1CiyZMiTHk2mRAlypcuWMEmylPmSZsyROFXe1GmzZ86ZP2sG3QmU51CfRpMWXSpUaVOmRJ9KjUoVKVSDB7IeMCigqwCrU8FWPUrW6VizYtOWvbo2bNuzbNG+VSu3bty7bu3mxQt3r9++gNUmGJzAYIHDBQwmVDi3sd7AjvnSlRz572TLlSE/vqyZ8ubMnEODHv25tOfTmE2nRt15tevWsEWrjk2atWzbtV/f1p0bsoLfCgwiGI7AoIHjBgwSWE5AcUKuXnfTni29em/r1K9rz84dd3fe36d7QR8Pnrz48ujPq8dunn169+u3t5f/nn788PDz29ePf7///gDOF2B9A94n4IEEImhgggwu6CB/CkLYoIQP/hfhSAEBADs=") */
    background-image: url(data:image/gif;base64,R0lGODlhBgAgA/MAALDM8sLY8sPZ88Ta9Nnt/9rt/9vu/9zu/93v/97w/+Dw/+Hx/////7DM8rDM8rDM8iH5BAEAAAwALAAAAAAGACADQwj/AAEsGLgAAIAACAMYHMBwwMKGDxlGdAigIUWLEzNWhLhRYseLHDF+1CiyZMiTHk2mRAlypcuWMEmylPmSZsyROFXe1GmzZ86ZP2sG3QmU51CfRpMWXSpUaVOmRJ9KjUoVKVSDB7IeMCigqwCrU8FWPUrW6VizYtOWvbo2bNuzbNG+VSu3bty7bu3mxQt3r9++gNUmGJzAYIHDBQwmVDi3sd7AjvnSlRz572TLlSE/vqyZ8ubMnEODHv25tOfTmE2nRt15tevWsEWrjk2atWzbtV/f1p0bsoLfCgwiGI7AoIHjBgwSWE5AcUKuXnfTni29em/r1K9rz84dd3fe36d7QR8Pnrz48ujPq8dunn169+u3t5f/nn788PDz29ePf7///gDOF2B9A94n4IEEImhgggwu6CB/CkLYoIQP/hfhSAEBADs=)
}

.x-btn-focus.x-btn-over .x-btn-default-small-mc {
    background-color: #e4f3ff;
    /*  background-image: url("data:image/gif;R0lGODlhAQAgA/MAAMLY8sPZ88Ta9Nnt/9rt/9vu/9zu/93v/97w/+Dw/+Hx/////8LY8sLY8sLY8sLY8iH5BAEAAAsALAAAAAABACADQwhBABUAEECwoMGDCBMqXMiwocOHCQ0EgEixosWLFxEQGIixo8ePIEOKHFkxwYECAwBMJMmypcuXMGPKnEmzps2CAQEAOw==")*/
    background-image: url(data:image/gif;base64,R0lGODlhAQAgA/MAAMLY8sPZ88Ta9Nnt/9rt/9vu/9zu/93v/97w/+Dw/+Hx/////8LY8sLY8sLY8sLY8iH5BAEAAAsALAAAAAABACADQwhBABUAEECwoMGDCBMqXMiwocOHCQ0EgEixosWLFxEQGIixo8ePIEOKHFkxwYECAwBMJMmypcuXMGPKnEmzps2CAQEAOw==)
}

.x-btn.x-btn-menu-active .x-btn-default-small-tl, .x-btn.x-btn-menu-active .x-btn-default-small-bl, .x-btn.x-btn-menu-active .x-btn-default-small-tr, .x-btn.x-btn-menu-active .x-btn-default-small-br, .x-btn.x-btn-menu-active .x-btn-default-small-tc, .x-btn.x-btn-menu-active .x-btn-default-small-bc, .x-btn.x-btn-pressed .x-btn-default-small-tl, .x-btn.x-btn-pressed .x-btn-default-small-bl, .x-btn.x-btn-pressed .x-btn-default-small-tr, .x-btn.x-btn-pressed .x-btn-default-small-br, .x-btn.x-btn-pressed .x-btn-default-small-tc, .x-btn.x-btn-pressed .x-btn-default-small-bc {
    /*background-image: url("data:image/gif;R0lGODlhAwASAPMAAJbD85bE9ZfD85fE9Zy955664aXA4qe/46jA47TK47TL47bL5LfM5Mva7v///wAAACH5BAEAAA4ALAAAAAADABIAQwg1AAsIPKCAgQACDQYoPAAgAIOHDhocSGCgQUQECzIG2CiwQAMDCQ5YZKAAQQMCAgIAQGDSQUAAOw==")*/
    background-image: url(data:image/gif;base64,R0lGODlhAwASAPMAAJbD85bE9ZfD85fE9Zy955664aXA4qe/46jA47TK47TL47bL5LfM5Mva7v///wAAACH5BAEAAA4ALAAAAAADABIAQwg1AAsIPKCAgQACDQYoPAAgAIOHDhocSGCgQUQECzIG2CiwQAMDCQ5YZKAAQQMCAgIAQGDSQUAAOw==)
}

.x-btn.x-btn-menu-active .x-btn-default-small-ml, .x-btn.x-btn-menu-active .x-btn-default-small-mr, .x-btn.x-btn-pressed .x-btn-default-small-ml, .x-btn.x-btn-pressed .x-btn-default-small-mr {
    /* background-image: url("data:image/gif;R0lGODlhBgAgA/QAAI3A9Y7A9Y/B9ZDB9ZHC9ZLC9ZTD9ZXD9Z664bjM5LnN5LrO5LvP5bzP5b3Q5b3R5b7R5f///43A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9SH5BAEAABEALAAAAAAGACADRAj/ABEkGJgAAQIACAEYPMDwwMKGDxlGdIigIUWLEzNWhLhRYseLHDF+1CiyZMiTHk2mRAlypcuWMEmylPmSZsyROFXe1GmzZ86ZP2sG3QmU51CfRpMWXSpUaVOmRJ9KjUoVKVSDDbI2MEigKwGrU8FWPUrW6VizYtOWvbo2bNuzbNG+VSu3bty7bu3mxQt3r9++gNUuGLzA4IPDDwwKWCzAoIHHBujylfyXcuC5mPVe1my5c+bJnyuH3gya82jPplOXXi1adWvWpF/Ljk0bNWzbs3HXPs3b9W7fuoPjVEBcgUEGyBkYdMDcgUEI0CEYDEA9gMEB2AcYLMC9gHDgvW+HUc89/rd48OjPqyefnv168+7jw5///X19+ffpl8/Pf7//9voB2J+A/9lXIH4HBmgggQwu6CCCDUL4oIISVkjhhQNOmKGFG2KYYIcgfihihA4FBAA7")*/
    background-image: url(data:image/gif;base64,R0lGODlhBgAgA/QAAI3A9Y7A9Y/B9ZDB9ZHC9ZLC9ZTD9ZXD9Z664bjM5LnN5LrO5LvP5bzP5b3Q5b3R5b7R5f///43A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9SH5BAEAABEALAAAAAAGACADRAj/ABEkGJgAAQIACAEYPMDwwMKGDxlGdIigIUWLEzNWhLhRYseLHDF+1CiyZMiTHk2mRAlypcuWMEmylPmSZsyROFXe1GmzZ86ZP2sG3QmU51CfRpMWXSpUaVOmRJ9KjUoVKVSDDbI2MEigKwGrU8FWPUrW6VizYtOWvbo2bNuzbNG+VSu3bty7bu3mxQt3r9++gNUuGLzA4IPDDwwKWCzAoIHHBujylfyXcuC5mPVe1my5c+bJnyuH3gya82jPplOXXi1adWvWpF/Ljk0bNWzbs3HXPs3b9W7fuoPjVEBcgUEGyBkYdMDcgUEI0CEYDEA9gMEB2AcYLMC9gHDgvW+HUc89/rd48OjPqyefnv168+7jw5///X19+ffpl8/Pf7//9voB2J+A/9lXIH4HBmgggQwu6CCCDUL4oIISVkjhhQNOmKGFG2KYYIcgfihihA4FBAA7)
}

.x-btn.x-btn-menu-active .x-btn-default-small-mc, .x-btn.x-btn-pressed .x-btn-default-small-mc {
    background-color: #b6cbe4;
    /* background-image: url("data:image/gif;R0lGODlhAQAgA/QAAI3A9Y7A9Y/B9ZDB9ZHC9ZLC9ZTD9ZXD9bjM5LnN5LrO5LvP5bzP5b3Q5b3R5b7R5f///43A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9SH5BAEAABAALAAAAAABACADRAhDABEAOECwoMGDCBMqXMiwocOHCRkQgEixosWLFxU4EGAAo8ePIEOKHEmyYoIFDR4EGFCgpMuXMGPKnEmzps2bOAsGBAA7")*/
    background-image: url(data:image/gif;base64,R0lGODlhAQAgA/QAAI3A9Y7A9Y/B9ZDB9ZHC9ZLC9ZTD9ZXD9bjM5LnN5LrO5LvP5bzP5b3Q5b3R5b7R5f///43A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9SH5BAEAABAALAAAAAABACADRAhDABEAOECwoMGDCBMqXMiwocOHCRkQgEixosWLFxU4EGAAo8ePIEOKHEmyYoIFDR4EGFCgpMuXMGPKnEmzps2bOAsGBAA7)
}

.x-btn-focus.x-btn-menu-active .x-btn-default-small-tl, .x-btn-focus.x-btn-menu-active .x-btn-default-small-bl, .x-btn-focus.x-btn-menu-active .x-btn-default-small-tr, .x-btn-focus.x-btn-menu-active .x-btn-default-small-br, .x-btn-focus.x-btn-menu-active .x-btn-default-small-tc, .x-btn-focus.x-btn-menu-active .x-btn-default-small-bc, .x-btn-focus.x-btn-pressed .x-btn-default-small-tl, .x-btn-focus.x-btn-pressed .x-btn-default-small-bl, .x-btn-focus.x-btn-pressed .x-btn-default-small-tr, .x-btn-focus.x-btn-pressed .x-btn-default-small-br, .x-btn-focus.x-btn-pressed .x-btn-default-small-tc, .x-btn-focus.x-btn-pressed .x-btn-default-small-bc {
    /* background-image: url("data:image/gif;R0lGODlhAwASAPMAAJbD85bE9ZfD85fE9Zy955664aXA4qe/46jA47TK47TL47bL5LfM5Mva7v///wAAACH5BAEAAA4ALAAAAAADABIAQwg1AAsIPKCAgQACDQYoPAAgAIOHDhocSGCgQUQECzIG2CiwQAMDCQ5YZKAAQQMCAgIAQGDSQUAAOw==")*/ 
    background-image: url(data:image/gif;base64,R0lGODlhAwASAPMAAJbD85bE9ZfD85fE9Zy955664aXA4qe/46jA47TK47TL47bL5LfM5Mva7v///wAAACH5BAEAAA4ALAAAAAADABIAQwg1AAsIPKCAgQACDQYoPAAgAIOHDhocSGCgQUQECzIG2CiwQAMDCQ5YZKAAQQMCAgIAQGDSQUAAOw==)
}

.x-btn-focus.x-btn-menu-active .x-btn-default-small-ml, .x-btn-focus.x-btn-menu-active .x-btn-default-small-mr, .x-btn-focus.x-btn-pressed .x-btn-default-small-ml, .x-btn-focus.x-btn-pressed .x-btn-default-small-mr {
    background-image: url("data:image/gif;R0lGODlhBgAgA/QAAI3A9Y7A9Y/B9ZDB9ZHC9ZLC9ZTD9ZXD9Z664bjM5LnN5LrO5LvP5bzP5b3Q5b3R5b7R5f///43A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9SH5BAEAABEALAAAAAAGACADRAj/ABEkGJgAAQIACAEYPMDwwMKGDxlGdIigIUWLEzNWhLhRYseLHDF+1CiyZMiTHk2mRAlypcuWMEmylPmSZsyROFXe1GmzZ86ZP2sG3QmU51CfRpMWXSpUaVOmRJ9KjUoVKVSDDbI2MEigKwGrU8FWPUrW6VizYtOWvbo2bNuzbNG+VSu3bty7bu3mxQt3r9++gNUuGLzA4IPDDwwKWCzAoIHHBujylfyXcuC5mPVe1my5c+bJnyuH3gya82jPplOXXi1adWvWpF/Ljk0bNWzbs3HXPs3b9W7fuoPjVEBcgUEGyBkYdMDcgUEI0CEYDEA9gMEB2AcYLMC9gHDgvW+HUc89/rd48OjPqyefnv168+7jw5///X19+ffpl8/Pf7//9voB2J+A/9lXIH4HBmgggQwu6CCCDUL4oIISVkjhhQNOmKGFG2KYYIcgfihihA4FBAA7")
}

.x-btn-focus.x-btn-menu-active .x-btn-default-small-mc, .x-btn-focus.x-btn-pressed .x-btn-default-small-mc {
    background-color: #b6cbe4;
    background-image: url("data:image/gif;R0lGODlhAQAgA/QAAI3A9Y7A9Y/B9ZDB9ZHC9ZLC9ZTD9ZXD9bjM5LnN5LrO5LvP5bzP5b3Q5b3R5b7R5f///43A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9SH5BAEAABAALAAAAAABACADRAhDABEAOECwoMGDCBMqXMiwocOHCRkQgEixosWLFxU4EGAAo8ePIEOKHEmyYoIFDR4EGFCgpMuXMGPKnEmzps2bOAsGBAA7")
}

.x-btn.x-btn-disabled .x-btn-default-small-tl, .x-btn.x-btn-disabled .x-btn-default-small-bl, .x-btn.x-btn-disabled .x-btn-default-small-tr, .x-btn.x-btn-disabled .x-btn-default-small-br, .x-btn.x-btn-disabled .x-btn-default-small-tc, .x-btn.x-btn-disabled .x-btn-default-small-bc {
    background-image: url("data:image/gif;R0lGODlhAwASAPMAAN7e3uDg4OHh4ePj4+fn5+7u7vT09Pb29v///wAAAN7e3t7e3t7e3t7e3t7e3t7e3iH5BAEAAAgALAAAAAADABIAQwgwAAUIHGDgAIAABQAoHKDwgEMEBQgSKABxgEODCgUKKEDAwACKBzwWCKAQwICPCAICADs=")
}

.x-btn.x-btn-disabled .x-btn-default-small-ml, .x-btn.x-btn-disabled .x-btn-default-small-mr {
    background-image: url("data:image/gif;R0lGODlhBgAgA/MAANra2tvb29zc3N3d3eHh4fHx8fLy8vPz8/T09PX19f///9ra2tra2tra2tra2tra2iH5BAEAAAoALAAAAAAGACADQwj/AAkkGJiAAAEACAEYHMBwwMKGDxlGdEigIUWLEzNWhLhRYseLHDF+1CiyZMiTHk2mRAlypcuWMEmylPmSZsyROFXe1GmzZ86ZP2sG3QmU51CfRpMWXSpUaVOmRJ9KjUoVKVSDBrIaMCigqwCrU8FWPUrW6VizYtOWvbo2bNuzbNG+VSu3bty7bu3mxQt3r9++gNUiGIzAYIHDBQwGWByALl/HfyEHnktZ72TLkjNXfrw5cufLnDF/1iy6dOjTnk2nRg16tevWsEmzlv2aduzRuFXf1m27N1nChQkcGH4Aq1bDiA0mVEiAcWMCXr/mnj29dvXd1Hlf9629e/bv1r2HQgePfbz58ui5k1d/nn367fDFv5fvvn789ffb55+Pn/5++/4F2N+A+glYIIH8HahgggwCiKCDC0LY4H8UGjihhRkFBAA7")
}

.x-btn.x-btn-disabled .x-btn-default-small-mc {
    background-color: #f7f7f7;
    background-image: url("data:image/gif;R0lGODlhAQAgA/MAANra2tvb29zc3N3d3fHx8fLy8vPz8/T09PX19f///9ra2tra2tra2tra2tra2tra2iH5BAEAAAkALAAAAAABACADQwhCABEAGECwoMGDCBMqXMiwocOHCQsIgEixosWLFw8QCICxo8ePIEOKHGnxgIECBAAEmEiypcuXMGPKnEmzps2bBAMCADs=")
}

.x-nbr .x-btn-default-small {
    background-image: none
}

.x-btn-disabled.x-btn-default-small .x-btn-inner, .x-btn-disabled.x-btn-default-small .x-btn-icon-el {
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=50)";
    opacity: 0.5
}

.x-nbr .x-segmented-button-item-horizontal.x-btn-default-small.x-segmented-button-first {
    border-right-width: 1px !important
}

.x-nbr .x-segmented-button-item-horizontal.x-btn-default-small.x-segmented-button-first .x-btn-default-small-mc {
    padding-right: 2px !important
}

.x-nbr .x-segmented-button-item-horizontal.x-btn-default-small.x-segmented-button-middle {
    border-right-width: 1px !important
}

.x-nbr .x-segmented-button-item-horizontal.x-btn-default-small.x-segmented-button-middle .x-btn-default-small-mc {
    padding-right: 2px !important;
    padding-left: 2px !important
}

.x-nbr .x-segmented-button-item-horizontal.x-btn-default-small.x-segmented-button-last .x-btn-default-small-mc {
    padding-left: 2px !important
}

.x-nbr .x-segmented-button-item-vertical.x-btn-default-small.x-segmented-button-first {
    border-bottom-width: 1px !important
}

.x-nbr .x-segmented-button-item-vertical.x-btn-default-small.x-segmented-button-first .x-btn-default-small-mc {
    padding-bottom: 2px !important
}

.x-nbr .x-segmented-button-item-vertical.x-btn-default-small.x-segmented-button-middle {
    border-bottom-width: 1px !important
}

.x-nbr .x-segmented-button-item-vertical.x-btn-default-small.x-segmented-button-middle .x-btn-default-small-mc {
    padding-top: 2px !important;
    padding-bottom: 2px !important
}

.x-nbr .x-segmented-button-item-vertical.x-btn-default-small.x-segmented-button-last .x-btn-default-small-mc {
    padding-top: 2px !important
}

.x-nbr .x-segmented-button-item.x-btn-default-small:after {
    content: ' ';
    border-style: solid;
    border-width: 0;
    position: absolute
}

.x-nbr .x-segmented-button-item-horizontal.x-btn-default-small:after {
    top: 1px;
    right: 0;
    bottom: 1px;
    left: 0
}

.x-nbr .x-segmented-button-item-horizontal.x-btn-default-small.x-segmented-button-first:after {
    left: 1px
}

.x-nbr .x-segmented-button-item-horizontal.x-btn-default-small.x-segmented-button-last:after {
    right: 1px
}

.x-nbr .x-segmented-button-item-vertical.x-btn-default-small:after {
    top: 0;
    right: 1px;
    bottom: 0;
    left: 1px
}

.x-nbr .x-segmented-button-item-vertical.x-btn-default-small.x-segmented-button-first:after {
    top: 1px
}

.x-nbr .x-segmented-button-item-vertical.x-btn-default-small.x-segmented-button-last:after {
    bottom: 1px
}

.x-cmd-slicer.x-btn-focus.x-btn-default-small:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url("data:image/gif;R0lGODlhAwASAPMAALDM8rfQ87fR88LV8Mjb9tTi9+bo7Ovr6/f5/f7+/v///wAAALDM8rDM8rDM8rDM8iH5BAEAAAoALAAAAAADABIAQwgzAAEIDIAggYEBBQ4oDGDgQIKHCgoQJFAgooCHCRQeEAigAAEEASomQCCgwICGBgSUVBAQADs="), sides:url("data:image/gif;R0lGODlhBgAgA/MAALDM8ufn5+jo6Onp6erq6vn5+fr6+vv7+/z8/P39/f///7DM8rDM8rDM8rDM8rDM8iH5BAEAAAoALAAAAAAGACADQwj/AAEkGJgAAIAACAMYJMCQwMKGDxlGdAigIUWLEzNWhLhRYseLHDF+1CiyZMiTHk2mRAlypcuWMEmylPmSZsyROFXe1GmzZ86ZP2sG3QmU51CfRpMWXSpUaVOmRJ9KjUoVKVSDBrIaMDig6wCrU8FWPUrW6VizYtOWvbo2bNuzbNG+VSu3bty7bu3mxQt3r9++gNUiGIzAYIHDBQwKWCyALl/HfyEHnktZ72TLkjNXfrw5cufLnDF/1iy6dOjTnk2nRg16tevWsEmzlv2aduzRuFXf1m27N1nChQEcGH4Aq1bDiA0mVAiAcWMAXr/mnj29dvXd1Hlf9629e/bv1r2HQgePfbz58ui5k1d/nn367fDFv5fvvn789ffb55+Pn/5++/4F2N+A+glYIIH8HahgggwCiKCDC0LY4H8UGjihhRkFBAA7"), frame-bg:url("data:image/gif;R0lGODlhAQAgA/MAAOfn5+jo6Onp6erq6vn5+fr6+vv7+/z8/P39/f///+fn5+fn5+fn5+fn5+fn5+fn5yH5BAEAAAkALAAAAAABACADQwhCABEAGECwoMGDCBMqXMiwocOHCQsIgEixosWLFw8QCICxo8ePIEOKHGnxgIECBAAEmEiypcuXMGPKnEmzps2bBAMCADs=")" !important
}

.x-cmd-slicer.x-btn-over.x-btn-default-small:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url("data:image/gif;R0lGODlhAwASAPMAALDM8rfQ87fR88DX9sPZ9cXb9dTi997u/t/u/uLy/+Py/////wAAALDM8rDM8rDM8iH5BAEAAAsALAAAAAADABIAQwgzAAEIDHAgAYEABgooDECgQIKHCwwEQDDAQEQBCjIqLCAQgIEBCBAuSHBAgMSGBASYXBAQADs="), sides:url("data:image/gif;R0lGODlhBgAgA/MAALDM8sLY8sPZ88Ta9Nnt/9rt/9vu/9zu/93v/97w/+Dw/+Hx/////7DM8rDM8rDM8iH5BAEAAAwALAAAAAAGACADQwj/AAEsGLgAAIAACAMYHMBwwMKGDxlGdAigIUWLEzNWhLhRYseLHDF+1CiyZMiTHk2mRAlypcuWMEmylPmSZsyROFXe1GmzZ86ZP2sG3QmU51CfRpMWXSpUaVOmRJ9KjUoVKVSDB7IeMCigqwCrU8FWPUrW6VizYtOWvbo2bNuzbNG+VSu3bty7bu3mxQt3r9++gNUmGJzAYIHDBQwmVDi3sd7AjvnSlRz572TLlSE/vqyZ8ubMnEODHv25tOfTmE2nRt15tevWsEWrjk2atWzbtV/f1p0bsoLfCgwiGI7AoIHjBgwSWE5AcUKuXnfTni29em/r1K9rz84dd3fe36d7QR8Pnrz48ujPq8dunn169+u3t5f/nn788PDz29ePf7///gDOF2B9A94n4IEEImhgggwu6CB/CkLYoIQP/hfhSAEBADs="), frame-bg:url("data:image/gif;R0lGODlhAQAgA/MAAMLY8sPZ88Ta9Nnt/9rt/9vu/9zu/93v/97w/+Dw/+Hx/////8LY8sLY8sLY8sLY8iH5BAEAAAsALAAAAAABACADQwhBABUAEECwoMGDCBMqXMiwocOHCQ0EgEixosWLFxEQGIixo8ePIEOKHFkxwYECAwBMJMmypcuXMGPKnEmzps2CAQEAOw==")" !important
}

.x-cmd-slicer.x-btn-focus.x-btn-over.x-btn-default-small:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url("data:image/gif;R0lGODlhAwASAPMAALDM8rfQ87fR88DX9sPZ9cXb9dTi997u/t/u/uLy/+Py/////wAAALDM8rDM8rDM8iH5BAEAAAsALAAAAAADABIAQwgzAAEIDHAgAYEABgooDECgQIKHCwwEQDDAQEQBCjIqLCAQgIEBCBAuSHBAgMSGBASYXBAQADs="), sides:url("data:image/gif;R0lGODlhBgAgA/MAALDM8sLY8sPZ88Ta9Nnt/9rt/9vu/9zu/93v/97w/+Dw/+Hx/////7DM8rDM8rDM8iH5BAEAAAwALAAAAAAGACADQwj/AAEsGLgAAIAACAMYHMBwwMKGDxlGdAigIUWLEzNWhLhRYseLHDF+1CiyZMiTHk2mRAlypcuWMEmylPmSZsyROFXe1GmzZ86ZP2sG3QmU51CfRpMWXSpUaVOmRJ9KjUoVKVSDB7IeMCigqwCrU8FWPUrW6VizYtOWvbo2bNuzbNG+VSu3bty7bu3mxQt3r9++gNUmGJzAYIHDBQwmVDi3sd7AjvnSlRz572TLlSE/vqyZ8ubMnEODHv25tOfTmE2nRt15tevWsEWrjk2atWzbtV/f1p0bsoLfCgwiGI7AoIHjBgwSWE5AcUKuXnfTni29em/r1K9rz84dd3fe36d7QR8Pnrz48ujPq8dunn169+u3t5f/nn788PDz29ePf7///gDOF2B9A94n4IEEImhgggwu6CB/CkLYoIQP/hfhSAEBADs="), frame-bg:url("data:image/gif;R0lGODlhAQAgA/MAAMLY8sPZ88Ta9Nnt/9rt/9vu/9zu/93v/97w/+Dw/+Hx/////8LY8sLY8sLY8sLY8iH5BAEAAAsALAAAAAABACADQwhBABUAEECwoMGDCBMqXMiwocOHCQ0EgEixosWLFxEQGIixo8ePIEOKHFkxwYECAwBMJMmypcuXMGPKnEmzps2CAQEAOw==")" !important
}

.x-cmd-slicer.x-btn-pressed.x-btn-default-small:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url("data:image/gif;R0lGODlhAwASAPMAAJbD85bE9ZfD85fE9Zy955664aXA4qe/46jA47TK47TL47bL5LfM5Mva7v///wAAACH5BAEAAA4ALAAAAAADABIAQwg1AAsIPKCAgQACDQYoPAAgAIOHDhocSGCgQUQECzIG2CiwQAMDCQ5YZKAAQQMCAgIAQGDSQUAAOw=="), sides:url("data:image/gif;R0lGODlhBgAgA/QAAI3A9Y7A9Y/B9ZDB9ZHC9ZLC9ZTD9ZXD9Z664bjM5LnN5LrO5LvP5bzP5b3Q5b3R5b7R5f///43A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9SH5BAEAABEALAAAAAAGACADRAj/ABEkGJgAAQIACAEYPMDwwMKGDxlGdIigIUWLEzNWhLhRYseLHDF+1CiyZMiTHk2mRAlypcuWMEmylPmSZsyROFXe1GmzZ86ZP2sG3QmU51CfRpMWXSpUaVOmRJ9KjUoVKVSDDbI2MEigKwGrU8FWPUrW6VizYtOWvbo2bNuzbNG+VSu3bty7bu3mxQt3r9++gNUuGLzA4IPDDwwKWCzAoIHHBujylfyXcuC5mPVe1my5c+bJnyuH3gya82jPplOXXi1adWvWpF/Ljk0bNWzbs3HXPs3b9W7fuoPjVEBcgUEGyBkYdMDcgUEI0CEYDEA9gMEB2AcYLMC9gHDgvW+HUc89/rd48OjPqyefnv168+7jw5///X19+ffpl8/Pf7//9voB2J+A/9lXIH4HBmgggQwu6CCCDUL4oIISVkjhhQNOmKGFG2KYYIcgfihihA4FBAA7"), frame-bg:url("data:image/gif;R0lGODlhAQAgA/QAAI3A9Y7A9Y/B9ZDB9ZHC9ZLC9ZTD9ZXD9bjM5LnN5LrO5LvP5bzP5b3Q5b3R5b7R5f///43A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9SH5BAEAABAALAAAAAABACADRAhDABEAOECwoMGDCBMqXMiwocOHCRkQgEixosWLFxU4EGAAo8ePIEOKHEmyYoIFDR4EGFCgpMuXMGPKnEmzps2bOAsGBAA7")" !important
}

.x-cmd-slicer.x-btn-focus.x-btn-pressed.x-btn-default-small:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url("data:image/gif;R0lGODlhAwASAPMAAJbD85bE9ZfD85fE9Zy955664aXA4qe/46jA47TK47TL47bL5LfM5Mva7v///wAAACH5BAEAAA4ALAAAAAADABIAQwg1AAsIPKCAgQACDQYoPAAgAIOHDhocSGCgQUQECzIG2CiwQAMDCQ5YZKAAQQMCAgIAQGDSQUAAOw=="), sides:url("data:image/gif;R0lGODlhBgAgA/QAAI3A9Y7A9Y/B9ZDB9ZHC9ZLC9ZTD9ZXD9Z664bjM5LnN5LrO5LvP5bzP5b3Q5b3R5b7R5f///43A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9SH5BAEAABEALAAAAAAGACADRAj/ABEkGJgAAQIACAEYPMDwwMKGDxlGdIigIUWLEzNWhLhRYseLHDF+1CiyZMiTHk2mRAlypcuWMEmylPmSZsyROFXe1GmzZ86ZP2sG3QmU51CfRpMWXSpUaVOmRJ9KjUoVKVSDDbI2MEigKwGrU8FWPUrW6VizYtOWvbo2bNuzbNG+VSu3bty7bu3mxQt3r9++gNUuGLzA4IPDDwwKWCzAoIHHBujylfyXcuC5mPVe1my5c+bJnyuH3gya82jPplOXXi1adWvWpF/Ljk0bNWzbs3HXPs3b9W7fuoPjVEBcgUEGyBkYdMDcgUEI0CEYDEA9gMEB2AcYLMC9gHDgvW+HUc89/rd48OjPqyefnv168+7jw5///X19+ffpl8/Pf7//9voB2J+A/9lXIH4HBmgggQwu6CCCDUL4oIISVkjhhQNOmKGFG2KYYIcgfihihA4FBAA7"), frame-bg:url("data:image/gif;R0lGODlhAQAgA/QAAI3A9Y7A9Y/B9ZDB9ZHC9ZLC9ZTD9ZXD9bjM5LnN5LrO5LvP5bzP5b3Q5b3R5b7R5f///43A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9SH5BAEAABAALAAAAAABACADRAhDABEAOECwoMGDCBMqXMiwocOHCRkQgEixosWLFxU4EGAAo8ePIEOKHEmyYoIFDR4EGFCgpMuXMGPKnEmzps2bOAsGBAA7")" !important
}

.x-cmd-slicer.x-btn-disabled.x-btn-default-small:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url("data:image/gif;R0lGODlhAwASAPMAAN7e3uDg4OHh4ePj4+fn5+7u7vT09Pb29v///wAAAN7e3t7e3t7e3t7e3t7e3t7e3iH5BAEAAAgALAAAAAADABIAQwgwAAUIHGDgAIAABQAoHKDwgEMEBQgSKABxgEODCgUKKEDAwACKBzwWCKAQwICPCAICADs="), sides:url("data:image/gif;R0lGODlhBgAgA/MAANra2tvb29zc3N3d3eHh4fHx8fLy8vPz8/T09PX19f///9ra2tra2tra2tra2tra2iH5BAEAAAoALAAAAAAGACADQwj/AAkkGJiAAAEACAEYHMBwwMKGDxlGdEigIUWLEzNWhLhRYseLHDF+1CiyZMiTHk2mRAlypcuWMEmylPmSZsyROFXe1GmzZ86ZP2sG3QmU51CfRpMWXSpUaVOmRJ9KjUoVKVSDBrIaMCigqwCrU8FWPUrW6VizYtOWvbo2bNuzbNG+VSu3bty7bu3mxQt3r9++gNUiGIzAYIHDBQwGWByALl/HfyEHnktZ72TLkjNXfrw5cufLnDF/1iy6dOjTnk2nRg16tevWsEmzlv2aduzRuFXf1m27N1nChQkcGH4Aq1bDiA0mVEiAcWMCXr/mnj29dvXd1Hlf9629e/bv1r2HQgePfbz58ui5k1d/nn367fDFv5fvvn789ffb55+Pn/5++/4F2N+A+glYIIH8HahgggwCiKCDC0LY4H8UGjihhRkFBAA7"), frame-bg:url("data:image/gif;R0lGODlhAQAgA/MAANra2tvb29zc3N3d3fHx8fLy8vPz8/T09PX19f///9ra2tra2tra2tra2tra2tra2iH5BAEAAAkALAAAAAABACADQwhCABEAGECwoMGDCBMqXMiwocOHCQsIgEixosWLFw8QCICxo8ePIEOKHGnxgIECBAAEmEiypcuXMGPKnEmzps2bBAMCADs=")" !important
}

.x-button-default-small-cell > .x-grid-cell-inner {
    padding-top: 0;
    padding-bottom: 0
}

.x-button-default-small-cell > .x-grid-cell-inner > .x-btn-default-small {
    vertical-align: top
}

.x-btn-default-medium {
    -webkit-border-radius: 3px;
    -moz-border-radius: 3px;
    -ms-border-radius: 3px;
    -o-border-radius: 3px;
    border-radius: 3px;
    padding: 3px 3px 3px 3px;
    border-width: 1px;
    border-style: solid;
    background-image: none;
    background-color: #fff;
    background-image: -webkit-gradient(linear, top, bottom, color-stop(0%, #fff), color-stop(48%, #f9f9f9), color-stop(52%, #e2e2e2), color-stop(0%, #e7e7e7));
    background-image: -webkit-linear-gradient(top, #fff, #f9f9f9 48%, #e2e2e2 52%, #e7e7e7);
    background-image: -moz-linear-gradient(top, #fff, #f9f9f9 48%, #e2e2e2 52%, #e7e7e7);
    background-image: -o-linear-gradient(top, #fff, #f9f9f9 48%, #e2e2e2 52%, #e7e7e7);
    background-image: -ms-linear-gradient(top, #fff, #f9f9f9 48%, #e2e2e2 52%, #e7e7e7);
    background-image: linear-gradient(top, #fff, #f9f9f9 48%, #e2e2e2 52%, #e7e7e7)
}

.x-btn-default-medium-mc {
    background-image: url("data:image/gif;R0lGODlhAQAgA/MAAOLi4uPj4+Tk5OXl5ebm5vf39/n5+fr6+vv7+/z8/P39/f///+Li4uLi4uLi4uLi4iH5BAEAAAsALAAAAAABACADQwhLABUcCDCAgMGDCBMqXMiwocOHECMmTFBAgMSLGDNqzKgAgQEABDeKHEmypMmTKCUqSIAAwQEDAUAKEFAwpc2bOHPq3Mmzp8+fPQMCADs=");
    background-position: 0 top;
    background-color: #fff
}

.x-nbr .x-btn-default-medium {
    padding: 0 !important;
    border-width: 0 !important;
    -webkit-border-radius: 0px;
    -moz-border-radius: 0px;
    -ms-border-radius: 0px;
    -o-border-radius: 0px;
    border-radius: 0px;
    background-color: transparent !important;
    background-image: none;
    box-shadow: none !important
}

.x-btn-default-medium-frameInfo {
    font-family: th-3-3-3-3-1-1-1-1-3-3-3-3
}

.x-btn-default-medium-tl {
    background-position: 0 -6px
}

.x-btn-default-medium-tr {
    background-position: right -9px
}

.x-btn-default-medium-bl {
    background-position: 0 -12px
}

.x-btn-default-medium-br {
    background-position: right -15px
}

.x-btn-default-medium-ml {
    background-position: 0 top
}

.x-btn-default-medium-mr {
    background-position: right top
}

.x-btn-default-medium-tc {
    background-position: 0 0
}

.x-btn-default-medium-bc {
    background-position: 0 -3px
}

.x-btn-default-medium-tr, .x-btn-default-medium-br, .x-btn-default-medium-mr {
    padding-right: 3px
}

.x-btn-default-medium-tl, .x-btn-default-medium-bl, .x-btn-default-medium-ml {
    padding-left: 3px
}

.x-btn-default-medium-tc {
    height: 3px
}

.x-btn-default-medium-bc {
    height: 3px
}

.x-btn-default-medium-tl, .x-btn-default-medium-bl, .x-btn-default-medium-tr, .x-btn-default-medium-br, .x-btn-default-medium-tc, .x-btn-default-medium-bc, .x-btn-default-medium-ml, .x-btn-default-medium-mr {
    background-image: url("data:image/gif;R0lGODlhAwASAPMAANHR0dXV1dbW1tjY2N/f3+Tk5Obm5vr6+v7+/v///wAAANHR0dHR0dHR0dHR0dHR0SH5BAEAAAkALAAAAAADABIAQwgyAAEIDHAAQYEBBhIaCFDAAIKHCRYeIGAgooCHCBQKBGCAwIEAFREcEGBgQMMCAkgmCAgAOw==")
}

.x-btn-default-medium-ml, .x-btn-default-medium-mr {
    background-image: url("data:image/gif;R0lGODlhBgAgA/MAANHR0eLi4uPj4+Tk5OXl5ebm5vf39/n5+fr6+vv7+/z8/P39/f///9HR0dHR0dHR0SH5BAEAAAwALAAAAAAGACADQwj/AAEsGLgAAAAECBEYFMBQgEECEAkYLECxwMSKFylmtAigIkePG0N2xDhSY8mPJEGeFKmyZcqXJl3GhIlyps2aOFnS1HmTZ86VQGX+FOqzaNCdR3smHYqU6FKjTqM2napUalWqTK9qzcoVKkkFYBUYNEDWgMEBaAd43bq269O3Vt3GbUsXLta6c+2y1Sv3Ll+8fvMKDkx472DDhfsiXuyWYEEACSInMHig8gGDATIHWNjwYUTAjEErHi269N/Th0mjTmw6dWvWq0PHVu169mvZtXPD1o17t+/ewGn/Fh78NvHjxpPbXs4bOfPhIh0bDCsWsmSDkicfTEjZMmeGmDV/YHcIIK3a8mk9Q1TenD3058XhO28v3318+vjf57+vvz////P5FyCA9g1oYIEI1qfgfgcuKGCCDEL4oIMEUthghBZKWCGGHE7Y4YYehgjiiBeKWCKJGp6oYoosZujih6QFBAA7")
}

.x-btn-default-medium-mc {
    padding: 1px 1px 1px 1px
}

.x-cmd-slicer.x-btn-default-medium:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, frame-bg:url("data:image/gif;R0lGODlhAQAgA/MAAOLi4uPj4+Tk5OXl5ebm5vf39/n5+fr6+vv7+/z8/P39/f///+Li4uLi4uLi4uLi4iH5BAEAAAsALAAAAAABACADQwhLABUcCDCAgMGDCBMqXMiwocOHECMmTFBAgMSLGDNqzKgAgQEABDeKHEmypMmTKCUqSIAAwQEDAUAKEFAwpc2bOHPq3Mmzp8+fPQMCADs="), corners:url("data:image/gif;R0lGODlhAwASAPMAANHR0dXV1dbW1tjY2N/f3+Tk5Obm5vr6+v7+/v///wAAANHR0dHR0dHR0dHR0dHR0SH5BAEAAAkALAAAAAADABIAQwgyAAEIDHAAQYEBBhIaCFDAAIKHCRYeIGAgooCHCBQKBGCAwIEAFREcEGBgQMMCAkgmCAgAOw=="), sides:url("data:image/gif;R0lGODlhBgAgA/MAANHR0eLi4uPj4+Tk5OXl5ebm5vf39/n5+fr6+vv7+/z8/P39/f///9HR0dHR0dHR0SH5BAEAAAwALAAAAAAGACADQwj/AAEsGLgAAAAECBEYFMBQgEECEAkYLECxwMSKFylmtAigIkePG0N2xDhSY8mPJEGeFKmyZcqXJl3GhIlyps2aOFnS1HmTZ86VQGX+FOqzaNCdR3smHYqU6FKjTqM2napUalWqTK9qzcoVKkkFYBUYNEDWgMEBaAd43bq269O3Vt3GbUsXLta6c+2y1Sv3Ll+8fvMKDkx472DDhfsiXuyWYEEACSInMHig8gGDATIHWNjwYUTAjEErHi269N/Th0mjTmw6dWvWq0PHVu169mvZtXPD1o17t+/ewGn/Fh78NvHjxpPbXs4bOfPhIh0bDCsWsmSDkicfTEjZMmeGmDV/YHcIIK3a8mk9Q1TenD3058XhO28v3318+vjf57+vvz////P5FyCA9g1oYIEI1qfgfgcuKGCCDEL4oIMEUthghBZKWCGGHE7Y4YYehgjiiBeKWCKJGp6oYoosZujih6QFBAA7")" !important
}

.x-btn-default-medium {
    border-color: #d1d1d1
}

.x-btn-button-default-medium {
    min-height: 24px
}

.x-ie9m .x-btn-button-default-medium {
    min-height: auto;
    height: 24px
}

.x-btn-inner-default-medium {
    font: normal 11px/16px tahoma, arial, verdana, sans-serif;
    color: #333;
    padding: 0 4px;
    max-width: 100%
}

.x-btn-icon-right > .x-btn-inner-default-medium, .x-btn-icon-left > .x-btn-inner-default-medium {
    max-width: calc(100% - 24px)
}

.x-ie10p .x-btn-inner-default-medium {
    max-width: none
}

.x-btn-icon-el-default-medium {
    font-size: 24px;
    height: 24px;
    color: #333;
    line-height: 24px
}

.x-btn-icon-left > .x-btn-icon-el-default-medium, .x-btn-icon-right > .x-btn-icon-el-default-medium {
    width: 24px
}

.x-btn-icon-top > .x-btn-icon-el-default-medium, .x-btn-icon-bottom > .x-btn-icon-el-default-medium {
    min-width: 24px
}

.x-btn-icon-el-default-medium.x-btn-glyph {
    opacity: 0.5
}

.x-ie8 .x-btn-icon-el-default-medium.x-btn-glyph {
    color: #999
}

.x-btn-text.x-btn-icon-left > .x-btn-icon-el-default-medium {
    margin-right: 0px
}

.x-btn-text.x-btn-icon-right > .x-btn-icon-el-default-medium {
    margin-left: 0px
}

.x-btn-text.x-btn-icon-top > .x-btn-icon-el-default-medium {
    margin-bottom: 4px
}

.x-btn-text.x-btn-icon-bottom > .x-btn-icon-el-default-medium {
    margin-top: 4px
}

.x-btn-arrow-right > .x-btn-icon.x-btn-no-text.x-btn-button-default-medium {
    padding-right: 4px
}

.x-btn-arrow-right > .x-btn-text.x-btn-icon-right > .x-btn-icon-el-default-medium {
    margin-right: 4px
}

.x-btn-arrow-bottom > .x-btn-button-default-medium, .x-btn-split-bottom > .x-btn-button-default-medium {
    padding-bottom: 3px
}

.x-btn-wrap-default-medium.x-btn-arrow-right:after {
    width: 8px;
    background-image: url("data:image/gif;R0lGODlhCgAKAIcAAAAAAP///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAAEALAAAAAAKAAoAAAgZAAMIHEiwoMGDCA0CWLhQYcODABJKnFgwIAA7");
    padding-right: 8px
}

.x-btn-wrap-default-medium.x-btn-arrow-bottom:after {
    height: 8px;
    background-image: url("data:image/gif;R0lGODlhCgAKAIcAAAAAAP///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAAEALAAAAAAKAAoAAAgZAAMIHEiwoMGDCA0CWLhQYcODABJKnFgwIAA7")
}

.x-btn-wrap-default-medium.x-btn-split-right:after {
    width: 14px;
    background-image: url("data:image/gif;R0lGODlhDgBIAMIEAAAAAMnJycLa9vX19f///////////////yH5BAEKAAIALAAAAAAOAEgAAANcGCPczupJEaerFq6sefdYFlrjVErnk14btzbv57YiTdomjuoqz3oUH0woqwFjwSMxCVoinzSAVDp8TH/WnnLb5M68xq74Ow6Tz+b0Dbwut9FvdY49d9fhd/kOmAAAOw==");
    padding-right: 14px
}

.x-btn-wrap-default-medium.x-btn-split-bottom:after {
    height: 14px;
    background-image: url("data:image/gif;R0lGODlhyAAOAMIDAAAAAMTExMLa9v///////////////////yH5BAEKAAIALAAAAADIAA4AAANdGLrc/jDKSau9OOsth/9gKI5kaZ5oqq5s676mIM90bd94ru987//AoHBILBqPyKRyyWw6n9CodEqtWq/YrHbL7XqBgHD4Sy6bZeKzeq0FsN/wuHxOr9vv+Lx+v04AADs=")
}

.x-btn-over > .x-btn-wrap-default-medium.x-btn-split-right:after {
    background-image: url("data:image/gif;R0lGODlhDgBIAMIEAAAAAKrI8cLa9tru/////////////////yH5BAEKAAIALAAAAAAOAEgAAANcGCPczupJEaerFq6sefdYFlrjVErnk14btzbv57YiTdomjuoqz3oUH0woqwFjwSMxCVoinzSAVDp8TH/WnnLb5M68xq74Ow6Tz+b0Dbwut9FvdY49d9fhd/kOmAAAOw==")
}

.x-btn-over > .x-btn-wrap-default-medium.x-btn-split-bottom:after {
    background-image: url("data:image/gif;R0lGODlhyAAOAKEDAAAAAKrI8e/4/////yH5BAEKAAMALAAAAADIAA4AAAJbjI+py+0Po5y02uuE3rz7D4biSJbmiabqKg7uC8fyTNf2jef6zvf+DwwKh8Si8YhMKpfMpvMJjUqn1Kr1is1qeYBudwsOi13esflsBaDX7Lb7DY/L5/S6/X4uAAA7")
}

.x-btn-split-right > .x-btn-icon.x-btn-no-text.x-btn-button-default-medium {
    padding-right: 4px
}

.x-btn-split-right > .x-btn-text.x-btn-icon-right > .x-btn-icon-el-default-medium {
    margin-right: 4px
}

.x-btn-focus.x-btn-default-medium {
    border-color: #b0ccf2;
    background-image: none;
    background-color: #fff;
    background-image: -webkit-gradient(linear, top, bottom, color-stop(0%, #fff), color-stop(48%, #f9f9f9), color-stop(52%, #e7e7e7), color-stop(0%, #ececec));
    background-image: -webkit-linear-gradient(top, #fff, #f9f9f9 48%, #e7e7e7 52%, #ececec);
    background-image: -moz-linear-gradient(top, #fff, #f9f9f9 48%, #e7e7e7 52%, #ececec);
    background-image: -o-linear-gradient(top, #fff, #f9f9f9 48%, #e7e7e7 52%, #ececec);
    background-image: -ms-linear-gradient(top, #fff, #f9f9f9 48%, #e7e7e7 52%, #ececec);
    background-image: linear-gradient(top, #fff, #f9f9f9 48%, #e7e7e7 52%, #ececec)
}

.x-btn-focus.x-btn-default-medium .x-btn-wrap {
    outline: 1px dotted #333
}

.x-btn-default-medium .x-btn-arrow-el {
    position: absolute;
    top: 0;
    right: 0;
    height: 100%;
    width: 17px;
    pointer-events: none
}

.x-btn-over.x-btn-default-medium {
    border-color: #b0ccf2;
    background-image: none;
    background-color: #e4f3ff;
    background-image: -webkit-gradient(linear, top, bottom, color-stop(0%, #e4f3ff), color-stop(48%, #d9edff), color-stop(52%, #c2d8f2), color-stop(0%, #c6dcf6));
    background-image: -webkit-linear-gradient(top, #e4f3ff, #d9edff 48%, #c2d8f2 52%, #c6dcf6);
    background-image: -moz-linear-gradient(top, #e4f3ff, #d9edff 48%, #c2d8f2 52%, #c6dcf6);
    background-image: -o-linear-gradient(top, #e4f3ff, #d9edff 48%, #c2d8f2 52%, #c6dcf6);
    background-image: -ms-linear-gradient(top, #e4f3ff, #d9edff 48%, #c2d8f2 52%, #c6dcf6);
    background-image: linear-gradient(top, #e4f3ff, #d9edff 48%, #c2d8f2 52%, #c6dcf6)
}

.x-btn.x-btn-menu-active.x-btn-default-medium, .x-btn.x-btn-pressed.x-btn-default-medium {
    border-color: #9ebae1;
    background-image: none;
    background-color: #b6cbe4;
    background-image: -webkit-gradient(linear, top, bottom, color-stop(0%, #b6cbe4), color-stop(48%, #bfd2e6), color-stop(52%, #8dc0f5), color-stop(0%, #98c5f5));
    background-image: -webkit-linear-gradient(top, #b6cbe4, #bfd2e6 48%, #8dc0f5 52%, #98c5f5);
    background-image: -moz-linear-gradient(top, #b6cbe4, #bfd2e6 48%, #8dc0f5 52%, #98c5f5);
    background-image: -o-linear-gradient(top, #b6cbe4, #bfd2e6 48%, #8dc0f5 52%, #98c5f5);
    background-image: -ms-linear-gradient(top, #b6cbe4, #bfd2e6 48%, #8dc0f5 52%, #98c5f5);
    background-image: linear-gradient(top, #b6cbe4, #bfd2e6 48%, #8dc0f5 52%, #98c5f5)
}

.x-btn.x-btn-disabled.x-btn-default-medium {
    border-color: #e1e1e1;
    background-image: none;
    background-color: #f7f7f7;
    background-image: -webkit-gradient(linear, top, bottom, color-stop(0%, #f7f7f7), color-stop(48%, #f1f1f1), color-stop(52%, #dadada), color-stop(0%, #dfdfdf));
    background-image: -webkit-linear-gradient(top, #f7f7f7, #f1f1f1 48%, #dadada 52%, #dfdfdf);
    background-image: -moz-linear-gradient(top, #f7f7f7, #f1f1f1 48%, #dadada 52%, #dfdfdf);
    background-image: -o-linear-gradient(top, #f7f7f7, #f1f1f1 48%, #dadada 52%, #dfdfdf);
    background-image: -ms-linear-gradient(top, #f7f7f7, #f1f1f1 48%, #dadada 52%, #dfdfdf);
    background-image: linear-gradient(top, #f7f7f7, #f1f1f1 48%, #dadada 52%, #dfdfdf)
}

.x-btn-focus .x-btn-default-medium-tl, .x-btn-focus .x-btn-default-medium-bl, .x-btn-focus .x-btn-default-medium-tr, .x-btn-focus .x-btn-default-medium-br, .x-btn-focus .x-btn-default-medium-tc, .x-btn-focus .x-btn-default-medium-bc {
    background-image: url("data:image/gif;R0lGODlhAwASAPMAALDM8rfQ87fR88LV8Mjb9tTi9+bo7Ovr6/f5/f7+/v///wAAALDM8rDM8rDM8rDM8iH5BAEAAAoALAAAAAADABIAQwgzAAEIDIAggYEBBQ4oDGDgQIKHCgoQJFAgooCHCRQeEAigAAEEASomQCCgwICGBgSUVBAQADs=")
}

.x-btn-focus .x-btn-default-medium-ml, .x-btn-focus .x-btn-default-medium-mr {
    background-image: url("data:image/gif;R0lGODlhBgAgA/MAALDM8ufn5+jo6Onp6erq6uvr6/f39/n5+fr6+vv7+/z8/P39/f///7DM8rDM8rDM8iH5BAEAAAwALAAAAAAGACADQwj/AAEsGLgAAAAECBEYFMBQgEECEAkYLECxwMSKFylmtAigIkePG0N2xDhSY8mPJEGeFKmyZcqXJl3GhIlyps2aOFnS1HmTZ86VQGX+FOqzaNCdR3smHYqU6FKjTqM2napUalWqTK9qzcoVKkkFYBUYNEDWgMEBaAd43bq269O3Vt3GbUsXLta6c+2y1Sv3Ll+8fvMKDkx472DDhfsiXuyWYEEACSInMHig8gGDATIHWNjwYUTAjEErHi269N/Th0mjTmw6dWvWq0PHVu169mvZtXPD1o17t+/ewGn/Fh78NvHjxpPbXs4bOfPhIh0bDCsWsmSDkicfTEjZMmeGmDV/YHcIIK3a8mk9Q1TenD3058XhO28v3318+vjf57+vvz////P5FyCA9g1oYIEI1qfgfgcuKGCCDEL4oIMEUthghBZKWCGGHE7Y4YYehgjiiBeKWCKJGp6oYoosZujih6QFBAA7")
}

.x-btn-focus .x-btn-default-medium-mc {
    background-color: #fff;
    background-image: url("data:image/gif;R0lGODlhAQAgA/MAAOfn5+jo6Onp6erq6uvr6/f39/n5+fr6+vv7+/z8/P39/f///+fn5+fn5+fn5+fn5yH5BAEAAAsALAAAAAABACADQwhLABUcCDCAgMGDCBMqXMiwocOHECMmTFBAgMSLGDNqzKgAgQEABDeKHEmypMmTKCUqSIAAwQEDAUAKEFAwpc2bOHPq3Mmzp8+fPQMCADs=")
}

.x-btn-over .x-btn-default-medium-tl, .x-btn-over .x-btn-default-medium-bl, .x-btn-over .x-btn-default-medium-tr, .x-btn-over .x-btn-default-medium-br, .x-btn-over .x-btn-default-medium-tc, .x-btn-over .x-btn-default-medium-bc {
    background-image: url("data:image/gif;R0lGODlhAwASAPMAALDM8rfQ87fR88DX9sPZ9cXb9dTi997u/t/u/uLy/+Py/////wAAALDM8rDM8rDM8iH5BAEAAAsALAAAAAADABIAQwgzAAEIDHAgAYEABgooDECgQIKHCwwEQDDAQEQBCjIqLCAQgIEBCBAuSHBAgMSGBASYXBAQADs=")
}

.x-btn-over .x-btn-default-medium-ml, .x-btn-over .x-btn-default-medium-mr {
    background-image: url("data:image/gif;R0lGODlhBgAgA/QAALDM8sLY8sPZ8sPZ88Ta9MXb9dfr/tnt/9rt/9vu/9zv/93v/97v/9/w/+Dx/+Hx/+Lx/////7DM8rDM8rDM8rDM8rDM8rDM8rDM8rDM8rDM8rDM8rDM8rDM8rDM8rDM8iH5BAEAABEALAAAAAAGACADRAj/AAFAGAgBAIAECBMYDMAwgMECEAs8jDgRYkWJACJi1HixY0aKHy2G3AiS40iPJlOWXClSZUuWJF/KjEkTJUybM3HWPMnT5U6fOoP2vDk0Z9GfRIEeFaq0adKnRp1GhYp0qtWqWJkSbcC1gUEDYA0YHEB2gNarZ7MuXStVbdu0cNlSjftWLlq7bufipau3rt++gO/+FRw4L+HDah0odmBwgeMFBhFIRrCw4diyBgloJsAXcWfDoD+L3kt6cOjShUebVp0atWfXp1fDZv1atu3Wt2vj3q27d2zev33TDk58uPHZyHMXTw7c44PnDwx29QqAgXUGBhVoV2AwoUIAB8IfaTAooLyAygwvk1VvFsBmzu43H1c+vzlz4feX089fH//+//YB6F+ABA5ooH4FInhgfwo2yOCD/EUooIMSJgjhhBdaWOGCG1KIYYcZcvjhiBqSKGKJKJ6ooocpsrhiiC7GCOOMINZoYmgBAQA7")
}

.x-btn-over .x-btn-default-medium-mc {
    background-color: #e4f3ff;
    background-image: url("data:image/gif;R0lGODlhAQAgA/QAAMLY8sPZ8sPZ88Ta9MXb9dfr/tnt/9rt/9vu/9zv/93v/97v/9/w/+Dx/+Hx/+Lx/////8LY8sLY8sLY8sLY8sLY8sLY8sLY8sLY8sLY8sLY8sLY8sLY8sLY8sLY8sLY8iH5BAEAABAALAAAAAABACADRAhKAB8gAECgoMGDCBMqXMiwocOHEBMyKCAgosWLGDNibKDgAAABAzSKHEmypMmTKCM6YLAgAQIDAT6CDJmyps2bOHPq3Mmzp0+eAQEAOw==")
}

.x-btn-focus.x-btn-over .x-btn-default-medium-tl, .x-btn-focus.x-btn-over .x-btn-default-medium-bl, .x-btn-focus.x-btn-over .x-btn-default-medium-tr, .x-btn-focus.x-btn-over .x-btn-default-medium-br, .x-btn-focus.x-btn-over .x-btn-default-medium-tc, .x-btn-focus.x-btn-over .x-btn-default-medium-bc {
    background-image: url("data:image/gif;R0lGODlhAwASAPMAALDM8rfQ87fR88DX9sPZ9cXb9dTi997u/t/u/uLy/+Py/////wAAALDM8rDM8rDM8iH5BAEAAAsALAAAAAADABIAQwgzAAEIDHAgAYEABgooDECgQIKHCwwEQDDAQEQBCjIqLCAQgIEBCBAuSHBAgMSGBASYXBAQADs=")
}

.x-btn-focus.x-btn-over .x-btn-default-medium-ml, .x-btn-focus.x-btn-over .x-btn-default-medium-mr {
    background-image: url("data:image/gif;R0lGODlhBgAgA/QAALDM8sLY8sPZ8sPZ88Ta9MXb9dfr/tnt/9rt/9vu/9zv/93v/97v/9/w/+Dx/+Hx/+Lx/////7DM8rDM8rDM8rDM8rDM8rDM8rDM8rDM8rDM8rDM8rDM8rDM8rDM8rDM8iH5BAEAABEALAAAAAAGACADRAj/AAFAGAgBAIAECBMYDMAwgMECEAs8jDgRYkWJACJi1HixY0aKHy2G3AiS40iPJlOWXClSZUuWJF/KjEkTJUybM3HWPMnT5U6fOoP2vDk0Z9GfRIEeFaq0adKnRp1GhYp0qtWqWJkSbcC1gUEDYA0YHEB2gNarZ7MuXStVbdu0cNlSjftWLlq7bufipau3rt++gO/+FRw4L+HDah0odmBwgeMFBhFIRrCw4diyBgloJsAXcWfDoD+L3kt6cOjShUebVp0atWfXp1fDZv1atu3Wt2vj3q27d2zev33TDk58uPHZyHMXTw7c44PnDwx29QqAgXUGBhVoV2AwoUIAB8IfaTAooLyAygwvk1VvFsBmzu43H1c+vzlz4feX089fH//+//YB6F+ABA5ooH4FInhgfwo2yOCD/EUooIMSJgjhhBdaWOGCG1KIYYcZcvjhiBqSKGKJKJ6ooocpsrhiiC7GCOOMINZoYmgBAQA7")
}

.x-btn-focus.x-btn-over .x-btn-default-medium-mc {
    background-color: #e4f3ff;
    background-image: url("data:image/gif;R0lGODlhAQAgA/QAAMLY8sPZ8sPZ88Ta9MXb9dfr/tnt/9rt/9vu/9zv/93v/97v/9/w/+Dx/+Hx/+Lx/////8LY8sLY8sLY8sLY8sLY8sLY8sLY8sLY8sLY8sLY8sLY8sLY8sLY8sLY8sLY8iH5BAEAABAALAAAAAABACADRAhKAB8gAECgoMGDCBMqXMiwocOHEBMyKCAgosWLGDNibKDgAAABAzSKHEmypMmTKCM6YLAgAQIDAT6CDJmyps2bOHPq3Mmzp0+eAQEAOw==")
}

.x-btn.x-btn-menu-active .x-btn-default-medium-tl, .x-btn.x-btn-menu-active .x-btn-default-medium-bl, .x-btn.x-btn-menu-active .x-btn-default-medium-tr, .x-btn.x-btn-menu-active .x-btn-default-medium-br, .x-btn.x-btn-menu-active .x-btn-default-medium-tc, .x-btn.x-btn-menu-active .x-btn-default-medium-bc, .x-btn.x-btn-pressed .x-btn-default-medium-tl, .x-btn.x-btn-pressed .x-btn-default-medium-bl, .x-btn.x-btn-pressed .x-btn-default-medium-tr, .x-btn.x-btn-pressed .x-btn-default-medium-br, .x-btn.x-btn-pressed .x-btn-default-medium-tc, .x-btn.x-btn-pressed .x-btn-default-medium-bc {
    background-image: url("data:image/gif;R0lGODlhAwASAPMAAJbD85bE9ZfD85fE9Zy955664aXA4qe/46jA47TK47bL5Mva7v///wAAAJbD85bD8yH5BAEAAAwALAAAAAADABIAQwg0AAsIPJBAgQACCwYoPAAggIKHDBYQNLAgIoKHCgJoFFhggYEEByoqSIBgAQEBAQAgKMkgIAA7")
}

.x-btn.x-btn-menu-active .x-btn-default-medium-ml, .x-btn.x-btn-menu-active .x-btn-default-medium-mr, .x-btn.x-btn-pressed .x-btn-default-medium-ml, .x-btn.x-btn-pressed .x-btn-default-medium-mr {
    background-image: url("data:image/gif;R0lGODlhBgAgA/QAAI3A9Y7A9Y/B9ZDB85DB9ZHC9ZLC9ZPC9ZPD9ZTD9ZXD9ZbE9Z664bfM5LjM5LjN5LnN5LrO5LrO5bvP5bvQ57zQ5b3Q5b3R5b7R5f///43A9Y3A9Y3A9Y3A9Y3A9Y3A9SH5BAEAABkALAAAAAAGACADRAj/ABk0GNiAAYMKCCsYFMBQgEEFEBUYXEBxwcSKFylmtMigIkePG0N2xDhSY8mPJEGeFKmyZcqXJl3GhIlyps2aOFnS1HmTZ86VQGX+FOqzaNCdR3smHYqU6FKjTqM2napUalWqTK9qzcoVKskIYCMYpECWgkEDaA143bq269O3Vt3GbUsXLta6c+2y1Sv3Ll+8fvMKDkx472DDhfsiXuz2geMHBidInmDwguULBgFoBmCQgGcCBhGIRgCYcWnFqE+r/sv6cOrWiVe7lh0btmnbr2fjpn1bt+/av3sDHy68eG7ix43zTs58ufPd0IM3j45cpIPrDgxC2A7BoITvEiJPezZoobwFgxjSYzA4oP0AgwHiB1jY0GCB+wUMHth/wGCC/wk8J52A1VGnnIHTDYgggQcq6GCBDzYI4YQSVpgghRdayGCGHG7o4YIgRthhiBh+KKKJJZKooYojnsgiiiu6KGOKM8ZI44025tgijjvqCGOPQP4o5ItE1phaQAA7")
}

.x-btn.x-btn-menu-active .x-btn-default-medium-mc, .x-btn.x-btn-pressed .x-btn-default-medium-mc {
    background-color: #b6cbe4;
    background-image: url("data:image/gif;R0lGODlhAQAgA/QAAI3A9Y7A9Y/B9ZDB85DB9ZHC9ZLC9ZPC9ZPD9ZTD9ZXD9ZbE9bfM5LjM5LjN5LnN5LrO5LrO5bvP5bvQ57zQ5b3Q5b3R5b7R5f///43A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9SH5BAEAABgALAAAAAABACADRAhNABlQEKBggcGDCBMqXMiwocOHECMmhDDBgMSLGDNqzOhAggUABBBsHEmypMmTKFNKbPAggoQKFwYEEFDgQAKVOHPq3Mmzp8+fQIMCDQgAOw==")
}

.x-btn-focus.x-btn-menu-active .x-btn-default-medium-tl, .x-btn-focus.x-btn-menu-active .x-btn-default-medium-bl, .x-btn-focus.x-btn-menu-active .x-btn-default-medium-tr, .x-btn-focus.x-btn-menu-active .x-btn-default-medium-br, .x-btn-focus.x-btn-menu-active .x-btn-default-medium-tc, .x-btn-focus.x-btn-menu-active .x-btn-default-medium-bc, .x-btn-focus.x-btn-pressed .x-btn-default-medium-tl, .x-btn-focus.x-btn-pressed .x-btn-default-medium-bl, .x-btn-focus.x-btn-pressed .x-btn-default-medium-tr, .x-btn-focus.x-btn-pressed .x-btn-default-medium-br, .x-btn-focus.x-btn-pressed .x-btn-default-medium-tc, .x-btn-focus.x-btn-pressed .x-btn-default-medium-bc {
    background-image: url("data:image/gif;R0lGODlhAwASAPMAAJbD85bE9ZfD85fE9Zy955664aXA4qe/46jA47TK47bL5Mva7v///wAAAJbD85bD8yH5BAEAAAwALAAAAAADABIAQwg0AAsIPJBAgQACCwYoPAAggIKHDBYQNLAgIoKHCgJoFFhggYEEByoqSIBgAQEBAQAgKMkgIAA7")
}

.x-btn-focus.x-btn-menu-active .x-btn-default-medium-ml, .x-btn-focus.x-btn-menu-active .x-btn-default-medium-mr, .x-btn-focus.x-btn-pressed .x-btn-default-medium-ml, .x-btn-focus.x-btn-pressed .x-btn-default-medium-mr {
    background-image: url("data:image/gif;R0lGODlhBgAgA/QAAI3A9Y7A9Y/B9ZDB85DB9ZHC9ZLC9ZPC9ZPD9ZTD9ZXD9ZbE9Z664bfM5LjM5LjN5LnN5LrO5LrO5bvP5bvQ57zQ5b3Q5b3R5b7R5f///43A9Y3A9Y3A9Y3A9Y3A9Y3A9SH5BAEAABkALAAAAAAGACADRAj/ABk0GNiAAYMKCCsYFMBQgEEFEBUYXEBxwcSKFylmtMigIkePG0N2xDhSY8mPJEGeFKmyZcqXJl3GhIlyps2aOFnS1HmTZ86VQGX+FOqzaNCdR3smHYqU6FKjTqM2napUalWqTK9qzcoVKskIYCMYpECWgkEDaA143bq269O3Vt3GbUsXLta6c+2y1Sv3Ll+8fvMKDkx472DDhfsiXuz2geMHBidInmDwguULBgFoBmCQgGcCBhGIRgCYcWnFqE+r/sv6cOrWiVe7lh0btmnbr2fjpn1bt+/av3sDHy68eG7ix43zTs58ufPd0IM3j45cpIPrDgxC2A7BoITvEiJPezZoobwFgxjSYzA4oP0AgwHiB1jY0GCB+wUMHth/wGCC/wk8J52A1VGnnIHTDYgggQcq6GCBDzYI4YQSVpgghRdayGCGHG7o4YIgRthhiBh+KKKJJZKooYojnsgiiiu6KGOKM8ZI44025tgijjvqCGOPQP4o5ItE1phaQAA7")
}

.x-btn-focus.x-btn-menu-active .x-btn-default-medium-mc, .x-btn-focus.x-btn-pressed .x-btn-default-medium-mc {
    background-color: #b6cbe4;
    background-image: url("data:image/gif;R0lGODlhAQAgA/QAAI3A9Y7A9Y/B9ZDB85DB9ZHC9ZLC9ZPC9ZPD9ZTD9ZXD9ZbE9bfM5LjM5LjN5LnN5LrO5LrO5bvP5bvQ57zQ5b3Q5b3R5b7R5f///43A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9SH5BAEAABgALAAAAAABACADRAhNABlQEKBggcGDCBMqXMiwocOHECMmhDDBgMSLGDNqzOhAggUABBBsHEmypMmTKFNKbPAggoQKFwYEEFDgQAKVOHPq3Mmzp8+fQIMCDQgAOw==")
}

.x-btn.x-btn-disabled .x-btn-default-medium-tl, .x-btn.x-btn-disabled .x-btn-default-medium-bl, .x-btn.x-btn-disabled .x-btn-default-medium-tr, .x-btn.x-btn-disabled .x-btn-default-medium-br, .x-btn.x-btn-disabled .x-btn-default-medium-tc, .x-btn.x-btn-disabled .x-btn-default-medium-bc {
    background-image: url("data:image/gif;R0lGODlhAwASAPMAAN7e3uDg4OHh4ePj4+fn5+7u7vT09Pb29v///wAAAN7e3t7e3t7e3t7e3t7e3t7e3iH5BAEAAAgALAAAAAADABIAQwgwAAUIHGDgAIAABQAoHKDwgEMEBQgSKABxgEODCgUKKEDAwACKBzwWCKAQwICPCAICADs=")
}

.x-btn.x-btn-disabled .x-btn-default-medium-ml, .x-btn.x-btn-disabled .x-btn-default-medium-mr {
    background-image: url("data:image/gif;R0lGODlhBgAgA/MAANra2tvb29zc3N3d3d7e3uHh4e/v7/Hx8fLy8vPz8/T09PX19f///9ra2tra2tra2iH5BAEAAAwALAAAAAAGACADQwj/AAssGLigQAEECBEYDMAwgMEBEAcYJECRwMSKFylmtFigIkePG0N2xDhSY8mPJEGeFKmyZcqXJl3GhIlyps2aOFnS1HmTZ86VQGX+FOqzaNCdR3smHYqU6FKjTqM2napUalWqTK9qzcoVKkkFYBUYNEDWgEEBaAV43bq269O3Vt3GbUsXLta6c+2y1Sv3Ll+8fvMKDkx472DDhfsiXuyWYMECCSInMHig8gGDADIDWNjwYUTAjEErHi269N/Th0mjTmw6dWvWq0PHVu169mvZtXPD1o17t+/ewGn/Fh78NvHjxpPbXs4bOfPhIh0bDCsWsmSDkicfTEjZMmeGmDV/YHdYIK3a8mk9Q1TenD3058XhO28v3318+vjf57+vvz////P5FyCA9g1oYIEI1qfgfgcuKGCCDEL4oIMEUthghBZKWCGGHE7Y4YYehgjiiBeKWCKJGp6oYoosZujih6QFBAA7")
}

.x-btn.x-btn-disabled .x-btn-default-medium-mc {
    background-color: #f7f7f7;
    background-image: url("data:image/gif;R0lGODlhAQAgA/MAANra2tvb29zc3N3d3d7e3u/v7/Hx8fLy8vPz8/T09PX19f///9ra2tra2tra2tra2iH5BAEAAAsALAAAAAABACADQwhLABUcCDCAgMGDCBMqXMiwocOHECMmTFBAgMSLGDNqzKgAgQEABDeKHEmypMmTKCUqSIAAwQEDAUAKEFAwpc2bOHPq3Mmzp8+fPQMCADs=")
}

.x-nbr .x-btn-default-medium {
    background-image: none
}

.x-btn-disabled.x-btn-default-medium .x-btn-inner, .x-btn-disabled.x-btn-default-medium .x-btn-icon-el {
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=50)";
    opacity: 0.5
}

.x-nbr .x-segmented-button-item-horizontal.x-btn-default-medium.x-segmented-button-first {
    border-right-width: 1px !important
}

.x-nbr .x-segmented-button-item-horizontal.x-btn-default-medium.x-segmented-button-first .x-btn-default-medium-mc {
    padding-right: 3px !important
}

.x-nbr .x-segmented-button-item-horizontal.x-btn-default-medium.x-segmented-button-middle {
    border-right-width: 1px !important
}

.x-nbr .x-segmented-button-item-horizontal.x-btn-default-medium.x-segmented-button-middle .x-btn-default-medium-mc {
    padding-right: 3px !important;
    padding-left: 3px !important
}

.x-nbr .x-segmented-button-item-horizontal.x-btn-default-medium.x-segmented-button-last .x-btn-default-medium-mc {
    padding-left: 3px !important
}

.x-nbr .x-segmented-button-item-vertical.x-btn-default-medium.x-segmented-button-first {
    border-bottom-width: 1px !important
}

.x-nbr .x-segmented-button-item-vertical.x-btn-default-medium.x-segmented-button-first .x-btn-default-medium-mc {
    padding-bottom: 3px !important
}

.x-nbr .x-segmented-button-item-vertical.x-btn-default-medium.x-segmented-button-middle {
    border-bottom-width: 1px !important
}

.x-nbr .x-segmented-button-item-vertical.x-btn-default-medium.x-segmented-button-middle .x-btn-default-medium-mc {
    padding-top: 3px !important;
    padding-bottom: 3px !important
}

.x-nbr .x-segmented-button-item-vertical.x-btn-default-medium.x-segmented-button-last .x-btn-default-medium-mc {
    padding-top: 3px !important
}

.x-nbr .x-segmented-button-item.x-btn-default-medium:after {
    content: ' ';
    border-style: solid;
    border-width: 0;
    position: absolute
}

.x-nbr .x-segmented-button-item-horizontal.x-btn-default-medium:after {
    top: 1px;
    right: 0;
    bottom: 1px;
    left: 0
}

.x-nbr .x-segmented-button-item-horizontal.x-btn-default-medium.x-segmented-button-first:after {
    left: 1px
}

.x-nbr .x-segmented-button-item-horizontal.x-btn-default-medium.x-segmented-button-last:after {
    right: 1px
}

.x-nbr .x-segmented-button-item-vertical.x-btn-default-medium:after {
    top: 0;
    right: 1px;
    bottom: 0;
    left: 1px
}

.x-nbr .x-segmented-button-item-vertical.x-btn-default-medium.x-segmented-button-first:after {
    top: 1px
}

.x-nbr .x-segmented-button-item-vertical.x-btn-default-medium.x-segmented-button-last:after {
    bottom: 1px
}

.x-cmd-slicer.x-btn-focus.x-btn-default-medium:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url("data:image/gif;R0lGODlhAwASAPMAALDM8rfQ87fR88LV8Mjb9tTi9+bo7Ovr6/f5/f7+/v///wAAALDM8rDM8rDM8rDM8iH5BAEAAAoALAAAAAADABIAQwgzAAEIDIAggYEBBQ4oDGDgQIKHCgoQJFAgooCHCRQeEAigAAEEASomQCCgwICGBgSUVBAQADs="), sides:url("data:image/gif;R0lGODlhBgAgA/MAALDM8ufn5+jo6Onp6erq6uvr6/f39/n5+fr6+vv7+/z8/P39/f///7DM8rDM8rDM8iH5BAEAAAwALAAAAAAGACADQwj/AAEsGLgAAAAECBEYFMBQgEECEAkYLECxwMSKFylmtAigIkePG0N2xDhSY8mPJEGeFKmyZcqXJl3GhIlyps2aOFnS1HmTZ86VQGX+FOqzaNCdR3smHYqU6FKjTqM2napUalWqTK9qzcoVKkkFYBUYNEDWgMEBaAd43bq269O3Vt3GbUsXLta6c+2y1Sv3Ll+8fvMKDkx472DDhfsiXuyWYEEACSInMHig8gGDATIHWNjwYUTAjEErHi269N/Th0mjTmw6dWvWq0PHVu169mvZtXPD1o17t+/ewGn/Fh78NvHjxpPbXs4bOfPhIh0bDCsWsmSDkicfTEjZMmeGmDV/YHcIIK3a8mk9Q1TenD3058XhO28v3318+vjf57+vvz////P5FyCA9g1oYIEI1qfgfgcuKGCCDEL4oIMEUthghBZKWCGGHE7Y4YYehgjiiBeKWCKJGp6oYoosZujih6QFBAA7"), frame-bg:url("data:image/gif;R0lGODlhAQAgA/MAAOfn5+jo6Onp6erq6uvr6/f39/n5+fr6+vv7+/z8/P39/f///+fn5+fn5+fn5+fn5yH5BAEAAAsALAAAAAABACADQwhLABUcCDCAgMGDCBMqXMiwocOHECMmTFBAgMSLGDNqzKgAgQEABDeKHEmypMmTKCUqSIAAwQEDAUAKEFAwpc2bOHPq3Mmzp8+fPQMCADs=")" !important
}

.x-cmd-slicer.x-btn-over.x-btn-default-medium:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url("data:image/gif;R0lGODlhAwASAPMAALDM8rfQ87fR88DX9sPZ9cXb9dTi997u/t/u/uLy/+Py/////wAAALDM8rDM8rDM8iH5BAEAAAsALAAAAAADABIAQwgzAAEIDHAgAYEABgooDECgQIKHCwwEQDDAQEQBCjIqLCAQgIEBCBAuSHBAgMSGBASYXBAQADs="), sides:url("data:image/gif;R0lGODlhBgAgA/QAALDM8sLY8sPZ8sPZ88Ta9MXb9dfr/tnt/9rt/9vu/9zv/93v/97v/9/w/+Dx/+Hx/+Lx/////7DM8rDM8rDM8rDM8rDM8rDM8rDM8rDM8rDM8rDM8rDM8rDM8rDM8rDM8iH5BAEAABEALAAAAAAGACADRAj/AAFAGAgBAIAECBMYDMAwgMECEAs8jDgRYkWJACJi1HixY0aKHy2G3AiS40iPJlOWXClSZUuWJF/KjEkTJUybM3HWPMnT5U6fOoP2vDk0Z9GfRIEeFaq0adKnRp1GhYp0qtWqWJkSbcC1gUEDYA0YHEB2gNarZ7MuXStVbdu0cNlSjftWLlq7bufipau3rt++gO/+FRw4L+HDah0odmBwgeMFBhFIRrCw4diyBgloJsAXcWfDoD+L3kt6cOjShUebVp0atWfXp1fDZv1atu3Wt2vj3q27d2zev33TDk58uPHZyHMXTw7c44PnDwx29QqAgXUGBhVoV2AwoUIAB8IfaTAooLyAygwvk1VvFsBmzu43H1c+vzlz4feX089fH//+//YB6F+ABA5ooH4FInhgfwo2yOCD/EUooIMSJgjhhBdaWOGCG1KIYYcZcvjhiBqSKGKJKJ6ooocpsrhiiC7GCOOMINZoYmgBAQA7"), frame-bg:url("data:image/gif;R0lGODlhAQAgA/QAAMLY8sPZ8sPZ88Ta9MXb9dfr/tnt/9rt/9vu/9zv/93v/97v/9/w/+Dx/+Hx/+Lx/////8LY8sLY8sLY8sLY8sLY8sLY8sLY8sLY8sLY8sLY8sLY8sLY8sLY8sLY8sLY8iH5BAEAABAALAAAAAABACADRAhKAB8gAECgoMGDCBMqXMiwocOHEBMyKCAgosWLGDNibKDgAAABAzSKHEmypMmTKCM6YLAgAQIDAT6CDJmyps2bOHPq3Mmzp0+eAQEAOw==")" !important
}

.x-cmd-slicer.x-btn-focus.x-btn-over.x-btn-default-medium:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url("data:image/gif;R0lGODlhAwASAPMAALDM8rfQ87fR88DX9sPZ9cXb9dTi997u/t/u/uLy/+Py/////wAAALDM8rDM8rDM8iH5BAEAAAsALAAAAAADABIAQwgzAAEIDHAgAYEABgooDECgQIKHCwwEQDDAQEQBCjIqLCAQgIEBCBAuSHBAgMSGBASYXBAQADs="), sides:url("data:image/gif;R0lGODlhBgAgA/QAALDM8sLY8sPZ8sPZ88Ta9MXb9dfr/tnt/9rt/9vu/9zv/93v/97v/9/w/+Dx/+Hx/+Lx/////7DM8rDM8rDM8rDM8rDM8rDM8rDM8rDM8rDM8rDM8rDM8rDM8rDM8rDM8iH5BAEAABEALAAAAAAGACADRAj/AAFAGAgBAIAECBMYDMAwgMECEAs8jDgRYkWJACJi1HixY0aKHy2G3AiS40iPJlOWXClSZUuWJF/KjEkTJUybM3HWPMnT5U6fOoP2vDk0Z9GfRIEeFaq0adKnRp1GhYp0qtWqWJkSbcC1gUEDYA0YHEB2gNarZ7MuXStVbdu0cNlSjftWLlq7bufipau3rt++gO/+FRw4L+HDah0odmBwgeMFBhFIRrCw4diyBgloJsAXcWfDoD+L3kt6cOjShUebVp0atWfXp1fDZv1atu3Wt2vj3q27d2zev33TDk58uPHZyHMXTw7c44PnDwx29QqAgXUGBhVoV2AwoUIAB8IfaTAooLyAygwvk1VvFsBmzu43H1c+vzlz4feX089fH//+//YB6F+ABA5ooH4FInhgfwo2yOCD/EUooIMSJgjhhBdaWOGCG1KIYYcZcvjhiBqSKGKJKJ6ooocpsrhiiC7GCOOMINZoYmgBAQA7"), frame-bg:url("data:image/gif;R0lGODlhAQAgA/QAAMLY8sPZ8sPZ88Ta9MXb9dfr/tnt/9rt/9vu/9zv/93v/97v/9/w/+Dx/+Hx/+Lx/////8LY8sLY8sLY8sLY8sLY8sLY8sLY8sLY8sLY8sLY8sLY8sLY8sLY8sLY8sLY8iH5BAEAABAALAAAAAABACADRAhKAB8gAECgoMGDCBMqXMiwocOHEBMyKCAgosWLGDNibKDgAAABAzSKHEmypMmTKCM6YLAgAQIDAT6CDJmyps2bOHPq3Mmzp0+eAQEAOw==")" !important
}

.x-cmd-slicer.x-btn-pressed.x-btn-default-medium:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url("data:image/gif;R0lGODlhAwASAPMAAJbD85bE9ZfD85fE9Zy955664aXA4qe/46jA47TK47bL5Mva7v///wAAAJbD85bD8yH5BAEAAAwALAAAAAADABIAQwg0AAsIPJBAgQACCwYoPAAggIKHDBYQNLAgIoKHCgJoFFhggYEEByoqSIBgAQEBAQAgKMkgIAA7"), sides:url("data:image/gif;R0lGODlhBgAgA/QAAI3A9Y7A9Y/B9ZDB85DB9ZHC9ZLC9ZPC9ZPD9ZTD9ZXD9ZbE9Z664bfM5LjM5LjN5LnN5LrO5LrO5bvP5bvQ57zQ5b3Q5b3R5b7R5f///43A9Y3A9Y3A9Y3A9Y3A9Y3A9SH5BAEAABkALAAAAAAGACADRAj/ABk0GNiAAYMKCCsYFMBQgEEFEBUYXEBxwcSKFylmtMigIkePG0N2xDhSY8mPJEGeFKmyZcqXJl3GhIlyps2aOFnS1HmTZ86VQGX+FOqzaNCdR3smHYqU6FKjTqM2napUalWqTK9qzcoVKskIYCMYpECWgkEDaA143bq269O3Vt3GbUsXLta6c+2y1Sv3Ll+8fvMKDkx472DDhfsiXuz2geMHBidInmDwguULBgFoBmCQgGcCBhGIRgCYcWnFqE+r/sv6cOrWiVe7lh0btmnbr2fjpn1bt+/av3sDHy68eG7ix43zTs58ufPd0IM3j45cpIPrDgxC2A7BoITvEiJPezZoobwFgxjSYzA4oP0AgwHiB1jY0GCB+wUMHth/wGCC/wk8J52A1VGnnIHTDYgggQcq6GCBDzYI4YQSVpgghRdayGCGHG7o4YIgRthhiBh+KKKJJZKooYojnsgiiiu6KGOKM8ZI44025tgijjvqCGOPQP4o5ItE1phaQAA7"), frame-bg:url("data:image/gif;R0lGODlhAQAgA/QAAI3A9Y7A9Y/B9ZDB85DB9ZHC9ZLC9ZPC9ZPD9ZTD9ZXD9ZbE9bfM5LjM5LjN5LnN5LrO5LrO5bvP5bvQ57zQ5b3Q5b3R5b7R5f///43A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9SH5BAEAABgALAAAAAABACADRAhNABlQEKBggcGDCBMqXMiwocOHECMmhDDBgMSLGDNqzOhAggUABBBsHEmypMmTKFNKbPAggoQKFwYEEFDgQAKVOHPq3Mmzp8+fQIMCDQgAOw==")" !important
}

.x-cmd-slicer.x-btn-focus.x-btn-pressed.x-btn-default-medium:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url("data:image/gif;R0lGODlhAwASAPMAAJbD85bE9ZfD85fE9Zy955664aXA4qe/46jA47TK47bL5Mva7v///wAAAJbD85bD8yH5BAEAAAwALAAAAAADABIAQwg0AAsIPJBAgQACCwYoPAAggIKHDBYQNLAgIoKHCgJoFFhggYEEByoqSIBgAQEBAQAgKMkgIAA7"), sides:url("data:image/gif;R0lGODlhBgAgA/QAAI3A9Y7A9Y/B9ZDB85DB9ZHC9ZLC9ZPC9ZPD9ZTD9ZXD9ZbE9Z664bfM5LjM5LjN5LnN5LrO5LrO5bvP5bvQ57zQ5b3Q5b3R5b7R5f///43A9Y3A9Y3A9Y3A9Y3A9Y3A9SH5BAEAABkALAAAAAAGACADRAj/ABk0GNiAAYMKCCsYFMBQgEEFEBUYXEBxwcSKFylmtMigIkePG0N2xDhSY8mPJEGeFKmyZcqXJl3GhIlyps2aOFnS1HmTZ86VQGX+FOqzaNCdR3smHYqU6FKjTqM2napUalWqTK9qzcoVKskIYCMYpECWgkEDaA143bq269O3Vt3GbUsXLta6c+2y1Sv3Ll+8fvMKDkx472DDhfsiXuz2geMHBidInmDwguULBgFoBmCQgGcCBhGIRgCYcWnFqE+r/sv6cOrWiVe7lh0btmnbr2fjpn1bt+/av3sDHy68eG7ix43zTs58ufPd0IM3j45cpIPrDgxC2A7BoITvEiJPezZoobwFgxjSYzA4oP0AgwHiB1jY0GCB+wUMHth/wGCC/wk8J52A1VGnnIHTDYgggQcq6GCBDzYI4YQSVpgghRdayGCGHG7o4YIgRthhiBh+KKKJJZKooYojnsgiiiu6KGOKM8ZI44025tgijjvqCGOPQP4o5ItE1phaQAA7"), frame-bg:url("data:image/gif;R0lGODlhAQAgA/QAAI3A9Y7A9Y/B9ZDB85DB9ZHC9ZLC9ZPC9ZPD9ZTD9ZXD9ZbE9bfM5LjM5LjN5LnN5LrO5LrO5bvP5bvQ57zQ5b3Q5b3R5b7R5f///43A9Y3A9Y3A9Y3A9Y3A9Y3A9Y3A9SH5BAEAABgALAAAAAABACADRAhNABlQEKBggcGDCBMqXMiwocOHECMmhDDBgMSLGDNqzOhAggUABBBsHEmypMmTKFNKbPAggoQKFwYEEFDgQAKVOHPq3Mmzp8+fQIMCDQgAOw==")" !important
}

.x-cmd-slicer.x-btn-disabled.x-btn-default-medium:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url("data:image/gif;R0lGODlhAwASAPMAAN7e3uDg4OHh4ePj4+fn5+7u7vT09Pb29v///wAAAN7e3t7e3t7e3t7e3t7e3t7e3iH5BAEAAAgALAAAAAADABIAQwgwAAUIHGDgAIAABQAoHKDwgEMEBQgSKABxgEODCgUKKEDAwACKBzwWCKAQwICPCAICADs="), sides:url("data:image/gif;R0lGODlhBgAgA/MAANra2tvb29zc3N3d3d7e3uHh4e/v7/Hx8fLy8vPz8/T09PX19f///9ra2tra2tra2iH5BAEAAAwALAAAAAAGACADQwj/AAssGLigQAEECBEYDMAwgMEBEAcYJECRwMSKFylmtFigIkePG0N2xDhSY8mPJEGeFKmyZcqXJl3GhIlyps2aOFnS1HmTZ86VQGX+FOqzaNCdR3smHYqU6FKjTqM2napUalWqTK9qzcoVKkkFYBUYNEDWgEEBaAV43bq269O3Vt3GbUsXLta6c+2y1Sv3Ll+8fvMKDkx472DDhfsiXuyWYMECCSInMHig8gGDADIDWNjwYUTAjEErHi269N/Th0mjTmw6dWvWq0PHVu169mvZtXPD1o17t+/ewGn/Fh78NvHjxpPbXs4bOfPhIh0bDCsWsmSDkicfTEjZMmeGmDV/YHdYIK3a8mk9Q1TenD3058XhO28v3318+vjf57+vvz////P5FyCA9g1oYIEI1qfgfgcuKGCCDEL4oIMEUthghBZKWCGGHE7Y4YYehgjiiBeKWCKJGp6oYoosZujih6QFBAA7"), frame-bg:url("data:image/gif;R0lGODlhAQAgA/MAANra2tvb29zc3N3d3d7e3u/v7/Hx8fLy8vPz8/T09PX19f///9ra2tra2tra2tra2iH5BAEAAAsALAAAAAABACADQwhLABUcCDCAgMGDCBMqXMiwocOHECMmTFBAgMSLGDNqzKgAgQEABDeKHEmypMmTKCUqSIAAwQEDAUAKEFAwpc2bOHPq3Mmzp8+fPQMCADs=")" !important
}

.x-button-default-medium-cell > .x-grid-cell-inner {
    padding-top: 0;
    padding-bottom: 0
}

.x-button-default-medium-cell > .x-grid-cell-inner > .x-btn-default-medium {
    vertical-align: top
}

.x-btn-default-large {
    -webkit-border-radius: 3px;
    -moz-border-radius: 3px;
    -ms-border-radius: 3px;
    -o-border-radius: 3px;
    border-radius: 3px;
    padding: 3px 3px 3px 3px;
    border-width: 1px;
    border-style: solid;
    background-image: none;
    background-color: #fff;
    background-image: -webkit-gradient(linear, top, bottom, color-stop(0%, #fff), color-stop(48%, #f9f9f9), color-stop(52%, #e2e2e2), color-stop(0%, #e7e7e7));
    background-image: -webkit-linear-gradient(top, #fff, #f9f9f9 48%, #e2e2e2 52%, #e7e7e7);
    background-image: -moz-linear-gradient(top, #fff, #f9f9f9 48%, #e2e2e2 52%, #e7e7e7);
    background-image: -o-linear-gradient(top, #fff, #f9f9f9 48%, #e2e2e2 52%, #e7e7e7);
    background-image: -ms-linear-gradient(top, #fff, #f9f9f9 48%, #e2e2e2 52%, #e7e7e7);
    background-image: linear-gradient(top, #fff, #f9f9f9 48%, #e2e2e2 52%, #e7e7e7)
}

.x-btn-default-large-mc {
    background-image: url("data:image/gif;R0lGODlhAQAgA/MAAOLi4uPj4+Tk5OXl5ebm5vX19fn5+fr6+vv7+/z8/P39/f7+/v///+Li4uLi4uLi4iH5BAEAAAwALAAAAAABACADQwhPABcgKBCAgMGDCBMqXMiwocOHECMmTHAAgACJGDNq3JhRAUUDAAIIGMCxpMmTKFOqXAlRgUcECA4YMDAgpMiRJFnq3Mmzp8+fQIMKHdozIAA7");
    background-position: 0 top;
    background-color: #fff
}

.x-nbr .x-btn-default-large {
    padding: 0 !important;
    border-width: 0 !important;
    -webkit-border-radius: 0px;
    -moz-border-radius: 0px;
    -ms-border-radius: 0px;
    -o-border-radius: 0px;
    border-radius: 0px;
    background-color: transparent !important;
    background-image: none;
    box-shadow: none !important
}

.x-btn-default-large-frameInfo {
    font-family: th-3-3-3-3-1-1-1-1-3-3-3-3
}

.x-btn-default-large-tl {
    background-position: 0 -6px
}

.x-btn-default-large-tr {
    background-position: right -9px
}

.x-btn-default-large-bl {
    background-position: 0 -12px
}

.x-btn-default-large-br {
    background-position: right -15px
}

.x-btn-default-large-ml {
    background-position: 0 top
}

.x-btn-default-large-mr {
    background-position: right top
}

.x-btn-default-large-tc {
    background-position: 0 0
}

.x-btn-default-large-bc {
    background-position: 0 -3px
}

.x-btn-default-large-tr, .x-btn-default-large-br, .x-btn-default-large-mr {
    padding-right: 3px
}

.x-btn-default-large-tl, .x-btn-default-large-bl, .x-btn-default-large-ml {
    padding-left: 3px
}

.x-btn-default-large-tc {
    height: 3px
}

.x-btn-default-large-bc {
    height: 3px
}

.x-btn-default-large-tl, .x-btn-default-large-bl, .x-btn-default-large-tr, .x-btn-default-large-br, .x-btn-default-large-tc, .x-btn-default-large-bc, .x-btn-default-large-ml, .x-btn-default-large-mr {
    background-image: url("data:image/gif;R0lGODlhAwASAPMAANHR0dXV1dbW1tjY2N/f3+Tk5Obm5vr6+v7+/v///wAAANHR0dHR0dHR0dHR0dHR0SH5BAEAAAkALAAAAAADABIAQwgyAAEIDHAAQYEBBhIaCFDAAIKHCRYeIGAgooCHCBQKBGCAwIEAFREcEGBgQMMCAkgmCAgAOw==")
}

.x-btn-default-large-ml, .x-btn-default-large-mr {
    background-image: url("data:image/gif;R0lGODlhBgAgA/MAANHR0eLi4uPj4+Tk5OXl5ebm5vX19fn5+fr6+vv7+/z8/P39/f7+/v///9HR0dHR0SH5BAEAAA0ALAAAAAAGACADQwj/AAEwGMgAAIAECBMYNMDQgEEBEAUYLECxwMSKFylmtAigIkePG0N2xDhSY8mPJEGeFKmyZcqXJl3GhIlyps2aOFnS1HmTZ86VQGX+FOqzaNCdR3smHYqU6FKjTqM2napUalWqTK9qzcoVKkkFYBUYREAWgcEAaAMYHMB2gNetb7s+nWtVbt24eOlizXtXL1y/dvcC5iu4r+HCiP8eVpw4MOPHPxdIXmAwrFgAZc0COMD5wNm0DyOubWuQgGkChCGndsx6tevBsBe3jt34tWzbtWmr1j37Nm/cu30Lzz08OPHjxpP3Rr5cOfDm0J9L/029ePTquSdTBqC9cliDCRUedkw4tqzBzp43dy59+jPa0BDhSwTQ1i190gBOo87fHrtz/9dZN52AAA7InIH/EajggQU2uGCCDD4YYIQUQmjhhBciiOGGGnboYIUcfpihiCFK6KGJJJ4IooojoujiiinG+GKLMM5YYo040qjjjTuyyOOPPga5UkAAOw==")
}

.x-btn-default-large-mc {
    padding: 1px 1px 1px 1px
}

.x-cmd-slicer.x-btn-default-large:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, frame-bg:url("data:image/gif;R0lGODlhAQAgA/MAAOLi4uPj4+Tk5OXl5ebm5vX19fn5+fr6+vv7+/z8/P39/f7+/v///+Li4uLi4uLi4iH5BAEAAAwALAAAAAABACADQwhPABcgKBCAgMGDCBMqXMiwocOHECMmTHAAgACJGDNq3JhRAUUDAAIIGMCxpMmTKFOqXAlRgUcECA4YMDAgpMiRJFnq3Mmzp8+fQIMKHdozIAA7"), corners:url("data:image/gif;R0lGODlhAwASAPMAANHR0dXV1dbW1tjY2N/f3+Tk5Obm5vr6+v7+/v///wAAANHR0dHR0dHR0dHR0dHR0SH5BAEAAAkALAAAAAADABIAQwgyAAEIDHAAQYEBBhIaCFDAAIKHCRYeIGAgooCHCBQKBGCAwIEAFREcEGBgQMMCAkgmCAgAOw=="), sides:url("data:image/gif;R0lGODlhBgAgA/MAANHR0eLi4uPj4+Tk5OXl5ebm5vX19fn5+fr6+vv7+/z8/P39/f7+/v///9HR0dHR0SH5BAEAAA0ALAAAAAAGACADQwj/AAEwGMgAAIAECBMYNMDQgEEBEAUYLECxwMSKFylmtAigIkePG0N2xDhSY8mPJEGeFKmyZcqXJl3GhIlyps2aOFnS1HmTZ86VQGX+FOqzaNCdR3smHYqU6FKjTqM2napUalWqTK9qzcoVKkkFYBUYREAWgcEAaAMYHMB2gNetb7s+nWtVbt24eOlizXtXL1y/dvcC5iu4r+HCiP8eVpw4MOPHPxdIXmAwrFgAZc0COMD5wNm0DyOubWuQgGkChCGndsx6tevBsBe3jt34tWzbtWmr1j37Nm/cu30Lzz08OPHjxpP3Rr5cOfDm0J9L/029ePTquSdTBqC9cliDCRUedkw4tqzBzp43dy59+jPa0BDhSwTQ1i190gBOo87fHrtz/9dZN52AAA7InIH/EajggQU2uGCCDD4YYIQUQmjhhBciiOGGGnboYIUcfpihiCFK6KGJJJ4IooojoujiiinG+GKLMM5YYo040qjjjTuyyOOPPga5UkAAOw==")" !important
}

.x-btn-default-large {
    border-color: #d1d1d1
}

.x-btn-button-default-large {
    min-height: 32px
}

.x-ie9m .x-btn-button-default-large {
    min-height: auto;
    height: 32px
}

.x-btn-inner-default-large {
    font: normal 11px/16px tahoma, arial, verdana, sans-serif;
    color: #333;
    padding: 0 4px;
    max-width: 100%
}

.x-btn-icon-right > .x-btn-inner-default-large, .x-btn-icon-left > .x-btn-inner-default-large {
    max-width: calc(100% - 32px)
}

.x-ie10p .x-btn-inner-default-large {
    max-width: none
}

.x-btn-icon-el-default-large {
    font-size: 32px;
    height: 32px;
    color: #333;
    line-height: 32px
}

.x-btn-icon-left > .x-btn-icon-el-default-large, .x-btn-icon-right > .x-btn-icon-el-default-large {
    width: 32px
}

.x-btn-icon-top > .x-btn-icon-el-default-large, .x-btn-icon-bottom > .x-btn-icon-el-default-large {
    min-width: 32px
}

.x-btn-icon-el-default-large.x-btn-glyph {
    opacity: 0.5
}

.x-ie8 .x-btn-icon-el-default-large.x-btn-glyph {
    color: #999
}

.x-btn-text.x-btn-icon-left > .x-btn-icon-el-default-large {
    margin-right: 0px
}

.x-btn-text.x-btn-icon-right > .x-btn-icon-el-default-large {
    margin-left: 0px
}

.x-btn-text.x-btn-icon-top > .x-btn-icon-el-default-large {
    margin-bottom: 4px
}

.x-btn-text.x-btn-icon-bottom > .x-btn-icon-el-default-large {
    margin-top: 4px
}

.x-btn-arrow-right > .x-btn-icon.x-btn-no-text.x-btn-button-default-large {
    padding-right: 4px
}

.x-btn-arrow-right > .x-btn-text.x-btn-icon-right > .x-btn-icon-el-default-large {
    margin-right: 4px
}

.x-btn-arrow-bottom > .x-btn-button-default-large, .x-btn-split-bottom > .x-btn-button-default-large {
    padding-bottom: 3px
}

.x-btn-wrap-default-large.x-btn-arrow-right:after {
    width: 8px;
    background-image: url("data:image/gif;R0lGODlhCgAKAIcAAAAAAP///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAAEALAAAAAAKAAoAAAgZAAMIHEiwoMGDCA0CWLhQYcODABJKnFgwIAA7");
    padding-right: 8px
}

.x-btn-wrap-default-large.x-btn-arrow-bottom:after {
    height: 8px;
    background-image: url("data:image/gif;R0lGODlhCgAKAIcAAAAAAP///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAAEALAAAAAAKAAoAAAgZAAMIHEiwoMGDCA0CWLhQYcODABJKnFgwIAA7")
}

.x-btn-wrap-default-large.x-btn-split-right:after {
    width: 14px;
    background-image: url("data:image/gif;R0lGODlhDgBIAMIEAAAAAMnJycLa9vX19f///////////////yH5BAEKAAIALAAAAAAOAEgAAANcGCPczupJEaerFq6sefdYFlrjVErnk14btzbv57YiTdomjuoqz3oUH0woqwFjwSMxCVoinzSAVDp8TH/WnnLb5M68xq74Ow6Tz+b0Dbwut9FvdY49d9fhd/kOmAAAOw==");
    padding-right: 14px
}

.x-btn-wrap-default-large.x-btn-split-bottom:after {
    height: 14px;
    background-image: url("data:image/gif;R0lGODlhyAAOAMIDAAAAAMTExMLa9v///////////////////yH5BAEKAAIALAAAAADIAA4AAANdGLrc/jDKSau9OOsth/9gKI5kaZ5oqq5s676mIM90bd94ru987//AoHBILBqPyKRyyWw6n9CodEqtWq/YrHbL7XqBgHD4Sy6bZeKzeq0FsN/wuHxOr9vv+Lx+v04AADs=")
}

.x-btn-over > .x-btn-wrap-default-large.x-btn-split-right:after {
    background-image: url("data:image/gif;R0lGODlhDgBIAMIEAAAAAKrI8cLa9tru/////////////////yH5BAEKAAIALAAAAAAOAEgAAANcGCPczupJEaerFq6sefdYFlrjVErnk14btzbv57YiTdomjuoqz3oUH0woqwFjwSMxCVoinzSAVDp8TH/WnnLb5M68xq74Ow6Tz+b0Dbwut9FvdY49d9fhd/kOmAAAOw==")
}

.x-btn-over > .x-btn-wrap-default-large.x-btn-split-bottom:after {
    background-image: url("data:image/gif;R0lGODlhyAAOAKEDAAAAAKrI8e/4/////yH5BAEKAAMALAAAAADIAA4AAAJbjI+py+0Po5y02uuE3rz7D4biSJbmiabqKg7uC8fyTNf2jef6zvf+DwwKh8Si8YhMKpfMpvMJjUqn1Kr1is1qeYBudwsOi13esflsBaDX7Lb7DY/L5/S6/X4uAAA7")
}

.x-btn-split-right > .x-btn-icon.x-btn-no-text.x-btn-button-default-large {
    padding-right: 4px
}

.x-btn-split-right > .x-btn-text.x-btn-icon-right > .x-btn-icon-el-default-large {
    margin-right: 4px
}

.x-btn-focus.x-btn-default-large {
    border-color: #b0ccf2;
    background-image: none;
    background-color: #fff;
    background-image: -webkit-gradient(linear, top, bottom, color-stop(0%, #fff), color-stop(48%, #f9f9f9), color-stop(52%, #e7e7e7), color-stop(0%, #ececec));
    background-image: -webkit-linear-gradient(top, #fff, #f9f9f9 48%, #e7e7e7 52%, #ececec);
    background-image: -moz-linear-gradient(top, #fff, #f9f9f9 48%, #e7e7e7 52%, #ececec);
    background-image: -o-linear-gradient(top, #fff, #f9f9f9 48%, #e7e7e7 52%, #ececec);
    background-image: -ms-linear-gradient(top, #fff, #f9f9f9 48%, #e7e7e7 52%, #ececec);
    background-image: linear-gradient(top, #fff, #f9f9f9 48%, #e7e7e7 52%, #ececec)
}

.x-btn-focus.x-btn-default-large .x-btn-wrap {
    outline: 1px dotted #333
}

.x-btn-default-large .x-btn-arrow-el {
    position: absolute;
    top: 0;
    right: 0;
    height: 100%;
    width: 17px;
    pointer-events: none
}

.x-btn-over.x-btn-default-large {
    border-color: #b0ccf2;
    background-image: none;
    background-color: #e4f3ff;
    background-image: -webkit-gradient(linear, top, bottom, color-stop(0%, #e4f3ff), color-stop(48%, #d9edff), color-stop(52%, #c2d8f2), color-stop(0%, #c6dcf6));
    background-image: -webkit-linear-gradient(top, #e4f3ff, #d9edff 48%, #c2d8f2 52%, #c6dcf6);
    background-image: -moz-linear-gradient(top, #e4f3ff, #d9edff 48%, #c2d8f2 52%, #c6dcf6);
    background-image: -o-linear-gradient(top, #e4f3ff, #d9edff 48%, #c2d8f2 52%, #c6dcf6);
    background-image: -ms-linear-gradient(top, #e4f3ff, #d9edff 48%, #c2d8f2 52%, #c6dcf6);
    background-image: linear-gradient(top, #e4f3ff, #d9edff 48%, #c2d8f2 52%, #c6dcf6)
}

.x-btn.x-btn-menu-active.x-btn-default-large, .x-btn.x-btn-pressed.x-btn-default-large {
    border-color: #9ebae1;
    background-image: none;
    background-color: #b6cbe4;
    background-image: -webkit-gradient(linear, top, bottom, color-stop(0%, #b6cbe4), color-stop(48%, #bfd2e6), color-stop(52%, #8dc0f5), color-stop(0%, #98c5f5));
    background-image: -webkit-linear-gradient(top, #b6cbe4, #bfd2e6 48%, #8dc0f5 52%, #98c5f5);
    background-image: -moz-linear-gradient(top, #b6cbe4, #bfd2e6 48%, #8dc0f5 52%, #98c5f5);
    background-image: -o-linear-gradient(top, #b6cbe4, #bfd2e6 48%, #8dc0f5 52%, #98c5f5);
    background-image: -ms-linear-gradient(top, #b6cbe4, #bfd2e6 48%, #8dc0f5 52%, #98c5f5);
    background-image: linear-gradient(top, #b6cbe4, #bfd2e6 48%, #8dc0f5 52%, #98c5f5)
}

.x-btn.x-btn-disabled.x-btn-default-large {
    border-color: #e1e1e1;
    background-image: none;
    background-color: #f7f7f7;
    background-image: -webkit-gradient(linear, top, bottom, color-stop(0%, #f7f7f7), color-stop(48%, #f1f1f1), color-stop(52%, #dadada), color-stop(0%, #dfdfdf));
    background-image: -webkit-linear-gradient(top, #f7f7f7, #f1f1f1 48%, #dadada 52%, #dfdfdf);
    background-image: -moz-linear-gradient(top, #f7f7f7, #f1f1f1 48%, #dadada 52%, #dfdfdf);
    background-image: -o-linear-gradient(top, #f7f7f7, #f1f1f1 48%, #dadada 52%, #dfdfdf);
    background-image: -ms-linear-gradient(top, #f7f7f7, #f1f1f1 48%, #dadada 52%, #dfdfdf);
    background-image: linear-gradient(top, #f7f7f7, #f1f1f1 48%, #dadada 52%, #dfdfdf)
}

.x-btn-focus .x-btn-default-large-tl, .x-btn-focus .x-btn-default-large-bl, .x-btn-focus .x-btn-default-large-tr, .x-btn-focus .x-btn-default-large-br, .x-btn-focus .x-btn-default-large-tc, .x-btn-focus .x-btn-default-large-bc {
    background-image: url("data:image/gif;R0lGODlhAwASAPMAALDM8rfQ87fR88LV8Mjb9tTi9+bo7Ovr6/f5/f7+/v///wAAALDM8rDM8rDM8rDM8iH5BAEAAAoALAAAAAADABIAQwgzAAEIDIAggYEBBQ4oDGDgQIKHCgoQJFAgooCHCRQeEAigAAEEASomQCCgwICGBgSUVBAQADs=")
}

.x-btn-focus .x-btn-default-large-ml, .x-btn-focus .x-btn-default-large-mr {
    background-image: url("data:image/gif;R0lGODlhBgAgA/MAALDM8ufn5+jo6Onp6erq6uvr6/X19fn5+fr6+vv7+/z8/P39/f7+/v///7DM8rDM8iH5BAEAAA0ALAAAAAAGACADQwj/AAEwGMgAAIAECBMYNMDQgEEBEAUYLECxwMSKFylmtAigIkePG0N2xDhSY8mPJEGeFKmyZcqXJl3GhIlyps2aOFnS1HmTZ86VQGX+FOqzaNCdR3smHYqU6FKjTqM2napUalWqTK9qzcoVKkkFYBUYREAWgcEAaAMYHMB2gNetb7s+nWtVbt24eOlizXtXL1y/dvcC5iu4r+HCiP8eVpw4MOPHPxdIXmAwrFgAZc0COMD5wNm0DyOubWuQgGkChCGndsx6tevBsBe3jt34tWzbtWmr1j37Nm/cu30Lzz08OPHjxpP3Rr5cOfDm0J9L/029ePTquSdTBqC9cliDCRUedkw4tqzBzp43dy59+jPa0BDhSwTQ1i190gBOo87fHrtz/9dZN52AAA7InIH/EajggQU2uGCCDD4YYIQUQmjhhBciiOGGGnboYIUcfpihiCFK6KGJJJ4IooojoujiiinG+GKLMM5YYo040qjjjTuyyOOPPga5UkAAOw==")
}

.x-btn-focus .x-btn-default-large-mc {
    background-color: #fff;
    background-image: url("data:image/gif;R0lGODlhAQAgA/MAAOfn5+jo6Onp6erq6uvr6/X19fn5+fr6+vv7+/z8/P39/f7+/v///+fn5+fn5+fn5yH5BAEAAAwALAAAAAABACADQwhPABcgKBCAgMGDCBMqXMiwocOHECMmTHAAgACJGDNq3JhRAUUDAAIIGMCxpMmTKFOqXAlRgUcECA4YMDAgpMiRJFnq3Mmzp8+fQIMKHdozIAA7")
}

.x-btn-over .x-btn-default-large-tl, .x-btn-over .x-btn-default-large-bl, .x-btn-over .x-btn-default-large-tr, .x-btn-over .x-btn-default-large-br, .x-btn-over .x-btn-default-large-tc, .x-btn-over .x-btn-default-large-bc {
    background-image: url("data:image/gif;R0lGODlhAwASAPMAALDM8rfQ87fR88DX9sPZ9cXb9dTi99/u/uPy/////wAAALDM8rDM8rDM8rDM8rDM8iH5BAEAAAkALAAAAAADABIAQwgyAAEIDHAAAYEABgooDECgAIKHCQwQHGAgooCHCBQWEAjAwIADCBMgOCBAYkMCAkomCAgAOw==")
}

.x-btn-over .x-btn-default-large-ml, .x-btn-over .x-btn-default-large-mr {
    background-image: url("data:image/gif;R0lGODlhBgAgA/QAALDM8sLY8sPZ88Ta9MXb9MXb9dXp/Nnt/9rt/9vu/9zu/93v/97v/97w/9/w/+Dw/+Dx/+Hx/+Ly/////7DM8rDM8rDM8rDM8rDM8rDM8rDM8rDM8rDM8rDM8rDM8rDM8iH5BAEAABMALAAAAAAGACADRAj/AAFIGCgBAIAFCBcYNMDQgEEBEAUYLECxwMSKFylmtAigIkePG0N2xDhSY8mPJEGeFKmyZcqXJl3GhIlyps2aOFnS1HmTZ86VQGX+FOqzaNCdR3smHYqU6FKjTqM2napUalWqTK9qzcoVKskHYB8YTEA2gcEAaAMYHMB2gNetb7s+nWtVbt24eOlizXtXL1y/dvcC5iu4r+HCiP8eVpw4MOPHPyNIjmCwgeUGBhVoVmAQgWcEZ9M+jDga4tq2hCGndsx6tevBsBe3jt34tWzbtWmr1j37Nm/cu30Lzz08OPHjxpP3Rr5cOfDm0J9L/029ePTquSdTBgChOwSDDsI7gjDIoDwDgwkVAihrFsBn0AAOyD9gkIB9AqHR5lcLIKLE/qQB0JZbAqKGnXMHXmfddAsmyCBzDyLY4IQQOmghhRJWiKGCGnaY4YccghhhiCSOaOKFHpaIoogrqrjhiS+2CGOKM7IY4400yqgjjjbmyKOLPgbZ45BAElljkUgeqeRTAQEAOw==")
}

.x-btn-over .x-btn-default-large-mc {
    background-color: #e4f3ff;
    background-image: url("data:image/gif;R0lGODlhAQAgA/QAAMLY8sPZ88Ta9MXb9MXb9dXp/Nnt/9rt/9vu/9zu/93v/97v/97w/9/w/+Dw/+Dx/+Hx/+Ly/////8LY8sLY8sLY8sLY8sLY8sLY8sLY8sLY8sLY8sLY8sLY8sLY8sLY8iH5BAEAABIALAAAAAABACADRAhRACMoKBCAgMGDCBMqXMiwocOHECMmdIAAgACJGDNq3JgRAoMEBwAECHCRo8mTKFOqXMnyIYQHDRYoQHDAwAAAIkmWbMmzp8+fQIMKHUq06M+AADs=")
}

.x-btn-focus.x-btn-over .x-btn-default-large-tl, .x-btn-focus.x-btn-over .x-btn-default-large-bl, .x-btn-focus.x-btn-over .x-btn-default-large-tr, .x-btn-focus.x-btn-over .x-btn-default-large-br, .x-btn-focus.x-btn-over .x-btn-default-large-tc, .x-btn-focus.x-btn-over .x-btn-default-large-bc {
    background-image: url("data:image/gif;R0lGODlhAwASAPMAALDM8rfQ87fR88DX9sPZ9cXb9dTi99/u/uPy/////wAAALDM8rDM8rDM8rDM8rDM8iH5BAEAAAkALAAAAAADABIAQwgyAAEIDHAAAYEABgooDECgAIKHCQwQHGAgooCHCBQWEAjAwIADCBMgOCBAYkMCAkomCAgAOw==")
}

.x-btn-focus.x-btn-over .x-btn-default-large-ml, .x-btn-focus.x-btn-over .x-btn-default-large-mr {
    background-image: url("data:image/gif;R0lGODlhBgAgA/QAALDM8sLY8sPZ88Ta9MXb9MXb9dXp/Nnt/9rt/9vu/9zu/93v/97v/97w/9/w/+Dw/+Dx/+Hx/+Ly/////7DM8rDM8rDM8rDM8rDM8rDM8rDM8rDM8rDM8rDM8rDM8rDM8iH5BAEAABMALAAAAAAGACADRAj/AAFIGCgBAIAFCBcYNMDQgEEBEAUYLECxwMSKFylmtAigIkePG0N2xDhSY8mPJEGeFKmyZcqXJl3GhIlyps2aOFnS1HmTZ86VQGX+FOqzaNCdR3smHYqU6FKjTqM2napUalWqTK9qzcoVKskHYB8YTEA2gcEAaAMYHMB2gNetb7s+nWtVbt24eOlizXtXL1y/dvcC5iu4r+HCiP8eVpw4MOPHPyNIjmCwgeUGBhVoVmAQgWcEZ9M+jDga4tq2hCGndsx6tevBsBe3jt34tWzbtWmr1j37Nm/cu30Lzz08OPHjxpP3Rr5cOfDm0J9L/029ePTquSdTBgChOwSDDsI7gjDIoDwDgwkVAihrFsBn0AAOyD9gkIB9AqHR5lcLIKLE/qQB0JZbAqKGnXMHXmfddAsmyCBzDyLY4IQQOmghhRJWiKGCGnaY4YccghhhiCSOaOKFHpaIoogrqrjhiS+2CGOKM7IY4400yqgjjjbmyKOLPgbZ45BAElljkUgeqeRTAQEAOw==")
}

.x-btn-focus.x-btn-over .x-btn-default-large-mc {
    background-color: #e4f3ff;
    background-image: url("data:image/gif;R0lGODlhAQAgA/QAAMLY8sPZ88Ta9MXb9MXb9dXp/Nnt/9rt/9vu/9zu/93v/97v/97w/9/w/+Dw/+Dx/+Hx/+Ly/////8LY8sLY8sLY8sLY8sLY8sLY8sLY8sLY8sLY8sLY8sLY8sLY8sLY8iH5BAEAABIALAAAAAABACADRAhRACMoKBCAgMGDCBMqXMiwocOHECMmdIAAgACJGDNq3JgRAoMEBwAECHCRo8mTKFOqXMnyIYQHDRYoQHDAwAAAIkmWbMmzp8+fQIMKHUq06M+AADs=")
}

.x-btn.x-btn-menu-active .x-btn-default-large-tl, .x-btn.x-btn-menu-active .x-btn-default-large-bl, .x-btn.x-btn-menu-active .x-btn-default-large-tr, .x-btn.x-btn-menu-active .x-btn-default-large-br, .x-btn.x-btn-menu-active .x-btn-default-large-tc, .x-btn.x-btn-menu-active .x-btn-default-large-bc, .x-btn.x-btn-pressed .x-btn-default-large-tl, .x-btn.x-btn-pressed .x-btn-default-large-bl, .x-btn.x-btn-pressed .x-btn-default-large-tr, .x-btn.x-btn-pressed .x-btn-default-large-br, .x-btn.x-btn-pressed .x-btn-default-large-tc, .x-btn.x-btn-pressed .x-btn-default-large-bc {
    background-image: url("data:image/gif;R0lGODlhAwASAPMAAJfD85fE9Zy955664aXA4qe/46jA47TK47bL5Mva7v///wAAAJfD85fD85fD85fD8yH5BAEAAAoALAAAAAADABIAQwgzAAcILHAAAQABCQIoLAAgAIKHChIQJJAgooGHCBQGEDggAYEDBSoiOGAggYCGAAyUVBAQADs=")
}

.x-btn.x-btn-menu-active .x-btn-default-large-ml, .x-btn.x-btn-menu-active .x-btn-default-large-mr, .x-btn.x-btn-pressed .x-btn-default-large-ml, .x-btn.x-btn-pressed .x-btn-default-large-mr {
    background-image: url("data:image/gif;R0lGODlhBgAgA/QAAI3A9Y7A9Y/B9ZDB9ZHB9ZHC9ZLC9ZPC9ZTD9ZXD8pXD9ZXE9ZbE9Z664bbO6LfL5LfM5LjM5LjN5LnN5LrO5LrO5bvP5bzP5bzQ5b3Q5b7R5f///43A9Y3A9Y3A9Y3A9SH5BAEAABsALAAAAAAGACADRAj/ABs8GPigQQMLCC0YdMDQgUECEAkYXEBxgUEGGBlczLgRY0eNDTKCFPmxZEiOJz2mHImS5EqTLmO2nKlSZk2aLG/qzMkTJk6fO4H2fEnU5lCjQpMW/bk0aNOjTJE+VSq1atSrTq1mxQp1q9euYJVOGDvBYIazGQwGWBvA4IG3B6hylfuVbtipeLXe1Wu3b965f+sG3guY72C/hhMXXixYcWPGhB9LvhuhcgSDFDJTMHih8wWDGkJrMAigNACDAlILMGigtQGDCGIjQAyZ9mTbkXPj3n24t2PdvmsHvz0c+G/ex4sjF568OfPnxJ1Hh26c+vLp2Ktnv669O/fvysNLlPfeAIJ5CAYlqJdgkGzZBhXiVzCYUGEDDPgxmEULWrTBBAAmoBZbqKlm0AAIDmBQAQwWwJprsMlmkAIUKgDeeBdaJ56GGG64nYfkdSgihyR+OKKJJYaYYoYotqiiiyy+KGOMNIJY44kz2qgjjjeuuKOPPP4Io5A5BmkkkEgOeaSSSRbZZI9MRumklFBOaWWVWBKJZUAAOw==")
}

.x-btn.x-btn-menu-active .x-btn-default-large-mc, .x-btn.x-btn-pressed .x-btn-default-large-mc {
    background-color: #b6cbe4;
    background-image: url("data:image/gif;R0lGODlhAQAgA/QAAI3A9Y7A9Y/B9ZDB9ZHB9ZHC9ZLC9ZPC9ZTD9ZXD8pXD9ZXE9ZbE9bbO6LfL5LfM5LjM5LjN5LnN5LrO5LrO5bvP5bzP5bzQ5b3Q5b7R5f///43A9Y3A9Y3A9Y3A9Y3A9SH5BAEAABoALAAAAAABACADRAhVAB1UaEBgAYODCBMqXMiwocOHECNKTCgBQ4ADEzNq3MhRI4QJFjIAEGAAQceTKFOqXMmyZcQHESRQqHABQ4YEAQQMKFBSgcufQIMKHUq0qNGjSIcGBAA7")
}

.x-btn-focus.x-btn-menu-active .x-btn-default-large-tl, .x-btn-focus.x-btn-menu-active .x-btn-default-large-bl, .x-btn-focus.x-btn-menu-active .x-btn-default-large-tr, .x-btn-focus.x-btn-menu-active .x-btn-default-large-br, .x-btn-focus.x-btn-menu-active .x-btn-default-large-tc, .x-btn-focus.x-btn-menu-active .x-btn-default-large-bc, .x-btn-focus.x-btn-pressed .x-btn-default-large-tl, .x-btn-focus.x-btn-pressed .x-btn-default-large-bl, .x-btn-focus.x-btn-pressed .x-btn-default-large-tr, .x-btn-focus.x-btn-pressed .x-btn-default-large-br, .x-btn-focus.x-btn-pressed .x-btn-default-large-tc, .x-btn-focus.x-btn-pressed .x-btn-default-large-bc {
    background-image: url("data:image/gif;R0lGODlhAwASAPMAAJfD85fE9Zy955664aXA4qe/46jA47TK47bL5Mva7v///wAAAJfD85fD85fD85fD8yH5BAEAAAoALAAAAAADABIAQwgzAAcILHAAAQABCQIoLAAgAIKHChIQJJAgooGHCBQGEDggAYEDBSoiOGAggYCGAAyUVBAQADs=")
}

.x-btn-focus.x-btn-menu-active .x-btn-default-large-ml, .x-btn-focus.x-btn-menu-active .x-btn-default-large-mr, .x-btn-focus.x-btn-pressed .x-btn-default-large-ml, .x-btn-focus.x-btn-pressed .x-btn-default-large-mr {
    background-image: url("data:image/gif;R0lGODlhBgAgA/QAAI3A9Y7A9Y/B9ZDB9ZHB9ZHC9ZLC9ZPC9ZTD9ZXD8pXD9ZXE9ZbE9Z664bbO6LfL5LfM5LjM5LjN5LnN5LrO5LrO5bvP5bzP5bzQ5b3Q5b7R5f///43A9Y3A9Y3A9Y3A9SH5BAEAABsALAAAAAAGACADRAj/ABs8GPigQQMLCC0YdMDQgUECEAkYXEBxgUEGGBlczLgRY0eNDTKCFPmxZEiOJz2mHImS5EqTLmO2nKlSZk2aLG/qzMkTJk6fO4H2fEnU5lCjQpMW/bk0aNOjTJE+VSq1atSrTq1mxQp1q9euYJVOGDvBYIazGQwGWBvA4IG3B6hylfuVbtipeLXe1Wu3b965f+sG3guY72C/hhMXXixYcWPGhB9LvhuhcgSDFDJTMHih8wWDGkJrMAigNACDAlILMGigtQGDCGIjQAyZ9mTbkXPj3n24t2PdvmsHvz0c+G/ex4sjF568OfPnxJ1Hh26c+vLp2Ktnv669O/fvysNLlPfeAIJ5CAYlqJdgkGzZBhXiVzCYUGEDDPgxmEULWrTBBAAmoBZbqKlm0AAIDmBQAQwWwJprsMlmkAIUKgDeeBdaJ56GGG64nYfkdSgihyR+OKKJJYaYYoYotqiiiyy+KGOMNIJY44kz2qgjjjeuuKOPPP4Io5A5BmkkkEgOeaSSSRbZZI9MRumklFBOaWWVWBKJZUAAOw==")
}

.x-btn-focus.x-btn-menu-active .x-btn-default-large-mc, .x-btn-focus.x-btn-pressed .x-btn-default-large-mc {
    background-color: #b6cbe4;
    background-image: url("data:image/gif;R0lGODlhAQAgA/QAAI3A9Y7A9Y/B9ZDB9ZHB9ZHC9ZLC9ZPC9ZTD9ZXD8pXD9ZXE9ZbE9bbO6LfL5LfM5LjM5LjN5LnN5LrO5LrO5bvP5bzP5bzQ5b3Q5b7R5f///43A9Y3A9Y3A9Y3A9Y3A9SH5BAEAABoALAAAAAABACADRAhVAB1UaEBgAYODCBMqXMiwocOHECNKTCgBQ4ADEzNq3MhRI4QJFjIAEGAAQceTKFOqXMmyZcQHESRQqHABQ4YEAQQMKFBSgcufQIMKHUq0qNGjSIcGBAA7")
}

.x-btn.x-btn-disabled .x-btn-default-large-tl, .x-btn.x-btn-disabled .x-btn-default-large-bl, .x-btn.x-btn-disabled .x-btn-default-large-tr, .x-btn.x-btn-disabled .x-btn-default-large-br, .x-btn.x-btn-disabled .x-btn-default-large-tc, .x-btn.x-btn-disabled .x-btn-default-large-bc {
    background-image: url("data:image/gif;R0lGODlhAwASAPMAAN7e3uDg4OHh4ePj4+fn5+7u7vT09Pb29v///wAAAN7e3t7e3t7e3t7e3t7e3t7e3iH5BAEAAAgALAAAAAADABIAQwgwAAUIHGDgAIAABQAoHKDwgEMEBQgSKABxgEODCgUKKEDAwACKBzwWCKAQwICPCAICADs=")
}

.x-btn.x-btn-disabled .x-btn-default-large-ml, .x-btn.x-btn-disabled .x-btn-default-large-mr {
    background-image: url("data:image/gif;R0lGODlhBgAgA/MAANra2tvb29zc3N3d3d7e3uHh4e3t7fHx8fLy8vPz8/T09PX19fb29v///9ra2tra2iH5BAEAAA0ALAAAAAAGACADQwj/AAswGMigQIEECBMYNMDQgMEAEAMYJECRwMSKFylmtFigIkePG0N2xDhSY8mPJEGeFKmyZcqXJl3GhIlyps2aOFnS1HmTZ86VQGX+FOqzaNCdR3smHYqU6FKjTqM2napUalWqTK9qzcoVKkkFYBUYREAWgUEAaAEYFMBWgNetb7s+nWtVbt24eOlizXtXL1y/dvcC5iu4r+HCiP8eVpw4MOPHPxdIXmAwrNgCZc0WOMD5wNm0DyOubWtwgOkBhCGndsx6tevBsBe3jt34tWzbtWmr1j37Nm/cu30Lzz08OPHjxpP3Rr5cOfDm0J9L/029ePTquSdTLqC9cliDCRUedkw4tqzBzp43dy59+jPa0BDhSyzQ1i190gVOo87fHrtz/9dZN52AAA7InIH/EajggQU2uGCCDD4YYIQUQmjhhBciiOGGGnboYIUcfpihiCFK6KGJJJ4IooojoujiiinG+GKLMM5YYo040qjjjTuyyOOPPga5UkAAOw==")
}

.x-btn.x-btn-disabled .x-btn-default-large-mc {
    background-color: #f7f7f7;
    background-image: url("data:image/gif;R0lGODlhAQAgA/MAANra2tvb29zc3N3d3d7e3u3t7fHx8fLy8vPz8/T09PX19fb29v///9ra2tra2tra2iH5BAEAAAwALAAAAAABACADQwhPABcgKBCAgMGDCBMqXMiwocOHECMmTHAAgACJGDNq3JhRAUUDAAIIGMCxpMmTKFOqXAlRgUcECA4YMDAgpMiRJFnq3Mmzp8+fQIMKHdozIAA7")
}

.x-nbr .x-btn-default-large {
    background-image: none
}

.x-btn-disabled.x-btn-default-large .x-btn-inner, .x-btn-disabled.x-btn-default-large .x-btn-icon-el {
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=50)";
    opacity: 0.5
}

.x-nbr .x-segmented-button-item-horizontal.x-btn-default-large.x-segmented-button-first {
    border-right-width: 1px !important
}

.x-nbr .x-segmented-button-item-horizontal.x-btn-default-large.x-segmented-button-first .x-btn-default-large-mc {
    padding-right: 3px !important
}

.x-nbr .x-segmented-button-item-horizontal.x-btn-default-large.x-segmented-button-middle {
    border-right-width: 1px !important
}

.x-nbr .x-segmented-button-item-horizontal.x-btn-default-large.x-segmented-button-middle .x-btn-default-large-mc {
    padding-right: 3px !important;
    padding-left: 3px !important
}

.x-nbr .x-segmented-button-item-horizontal.x-btn-default-large.x-segmented-button-last .x-btn-default-large-mc {
    padding-left: 3px !important
}

.x-nbr .x-segmented-button-item-vertical.x-btn-default-large.x-segmented-button-first {
    border-bottom-width: 1px !important
}

.x-nbr .x-segmented-button-item-vertical.x-btn-default-large.x-segmented-button-first .x-btn-default-large-mc {
    padding-bottom: 3px !important
}

.x-nbr .x-segmented-button-item-vertical.x-btn-default-large.x-segmented-button-middle {
    border-bottom-width: 1px !important
}

.x-nbr .x-segmented-button-item-vertical.x-btn-default-large.x-segmented-button-middle .x-btn-default-large-mc {
    padding-top: 3px !important;
    padding-bottom: 3px !important
}

.x-nbr .x-segmented-button-item-vertical.x-btn-default-large.x-segmented-button-last .x-btn-default-large-mc {
    padding-top: 3px !important
}

.x-nbr .x-segmented-button-item.x-btn-default-large:after {
    content: ' ';
    border-style: solid;
    border-width: 0;
    position: absolute
}

.x-nbr .x-segmented-button-item-horizontal.x-btn-default-large:after {
    top: 1px;
    right: 0;
    bottom: 1px;
    left: 0
}

.x-nbr .x-segmented-button-item-horizontal.x-btn-default-large.x-segmented-button-first:after {
    left: 1px
}

.x-nbr .x-segmented-button-item-horizontal.x-btn-default-large.x-segmented-button-last:after {
    right: 1px
}

.x-nbr .x-segmented-button-item-vertical.x-btn-default-large:after {
    top: 0;
    right: 1px;
    bottom: 0;
    left: 1px
}

.x-nbr .x-segmented-button-item-vertical.x-btn-default-large.x-segmented-button-first:after {
    top: 1px
}

.x-nbr .x-segmented-button-item-vertical.x-btn-default-large.x-segmented-button-last:after {
    bottom: 1px
}

.x-cmd-slicer.x-btn-focus.x-btn-default-large:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url("data:image/gif;R0lGODlhAwASAPMAALDM8rfQ87fR88LV8Mjb9tTi9+bo7Ovr6/f5/f7+/v///wAAALDM8rDM8rDM8rDM8iH5BAEAAAoALAAAAAADABIAQwgzAAEIDIAggYEBBQ4oDGDgQIKHCgoQJFAgooCHCRQeEAigAAEEASomQCCgwICGBgSUVBAQADs="), sides:url("data:image/gif;R0lGODlhBgAgA/MAALDM8ufn5+jo6Onp6erq6uvr6/X19fn5+fr6+vv7+/z8/P39/f7+/v///7DM8rDM8iH5BAEAAA0ALAAAAAAGACADQwj/AAEwGMgAAIAECBMYNMDQgEEBEAUYLECxwMSKFylmtAigIkePG0N2xDhSY8mPJEGeFKmyZcqXJl3GhIlyps2aOFnS1HmTZ86VQGX+FOqzaNCdR3smHYqU6FKjTqM2napUalWqTK9qzcoVKkkFYBUYREAWgcEAaAMYHMB2gNetb7s+nWtVbt24eOlizXtXL1y/dvcC5iu4r+HCiP8eVpw4MOPHPxdIXmAwrFgAZc0COMD5wNm0DyOubWuQgGkChCGndsx6tevBsBe3jt34tWzbtWmr1j37Nm/cu30Lzz08OPHjxpP3Rr5cOfDm0J9L/029ePTquSdTBqC9cliDCRUedkw4tqzBzp43dy59+jPa0BDhSwTQ1i190gBOo87fHrtz/9dZN52AAA7InIH/EajggQU2uGCCDD4YYIQUQmjhhBciiOGGGnboYIUcfpihiCFK6KGJJJ4IooojoujiiinG+GKLMM5YYo040qjjjTuyyOOPPga5UkAAOw=="), frame-bg:url("data:image/gif;R0lGODlhAQAgA/MAAOfn5+jo6Onp6erq6uvr6/X19fn5+fr6+vv7+/z8/P39/f7+/v///+fn5+fn5+fn5yH5BAEAAAwALAAAAAABACADQwhPABcgKBCAgMGDCBMqXMiwocOHECMmTHAAgACJGDNq3JhRAUUDAAIIGMCxpMmTKFOqXAlRgUcECA4YMDAgpMiRJFnq3Mmzp8+fQIMKHdozIAA7")" !important
}

.x-cmd-slicer.x-btn-over.x-btn-default-large:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url("data:image/gif;R0lGODlhAwASAPMAALDM8rfQ87fR88DX9sPZ9cXb9dTi99/u/uPy/////wAAALDM8rDM8rDM8rDM8rDM8iH5BAEAAAkALAAAAAADABIAQwgyAAEIDHAAAYEABgooDECgAIKHCQwQHGAgooCHCBQWEAjAwIADCBMgOCBAYkMCAkomCAgAOw=="), sides:url("data:image/gif;R0lGODlhBgAgA/QAALDM8sLY8sPZ88Ta9MXb9MXb9dXp/Nnt/9rt/9vu/9zu/93v/97v/97w/9/w/+Dw/+Dx/+Hx/+Ly/////7DM8rDM8rDM8rDM8rDM8rDM8rDM8rDM8rDM8rDM8rDM8rDM8iH5BAEAABMALAAAAAAGACADRAj/AAFIGCgBAIAFCBcYNMDQgEEBEAUYLECxwMSKFylmtAigIkePG0N2xDhSY8mPJEGeFKmyZcqXJl3GhIlyps2aOFnS1HmTZ86VQGX+FOqzaNCdR3smHYqU6FKjTqM2napUalWqTK9qzcoVKskHYB8YTEA2gcEAaAMYHMB2gNetb7s+nWtVbt24eOlizXtXL1y/dvcC5iu4r+HCiP8eVpw4MOPHPyNIjmCwgeUGBhVoVmAQgWcEZ9M+jDga4tq2hCGndsx6tevBsBe3jt34tWzbtWmr1j37Nm/cu30Lzz08OPHjxpP3Rr5cOfDm0J9L/029ePTquSdTBgChOwSDDsI7gjDIoDwDgwkVAihrFsBn0AAOyD9gkIB9AqHR5lcLIKLE/qQB0JZbAqKGnXMHXmfddAsmyCBzDyLY4IQQOmghhRJWiKGCGnaY4YccghhhiCSOaOKFHpaIoogrqrjhiS+2CGOKM7IY4400yqgjjjbmyKOLPgbZ45BAElljkUgeqeRTAQEAOw=="), frame-bg:url("data:image/gif;R0lGODlhAQAgA/QAAMLY8sPZ88Ta9MXb9MXb9dXp/Nnt/9rt/9vu/9zu/93v/97v/97w/9/w/+Dw/+Dx/+Hx/+Ly/////8LY8sLY8sLY8sLY8sLY8sLY8sLY8sLY8sLY8sLY8sLY8sLY8sLY8iH5BAEAABIALAAAAAABACADRAhRACMoKBCAgMGDCBMqXMiwocOHECMmdIAAgACJGDNq3JgRAoMEBwAECHCRo8mTKFOqXMnyIYQHDRYoQHDAwAAAIkmWbMmzp8+fQIMKHUq06M+AADs=")" !important
}

.x-cmd-slicer.x-btn-focus.x-btn-over.x-btn-default-large:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url("data:image/gif;R0lGODlhAwASAPMAALDM8rfQ87fR88DX9sPZ9cXb9dTi99/u/uPy/////wAAALDM8rDM8rDM8rDM8rDM8iH5BAEAAAkALAAAAAADABIAQwgyAAEIDHAAAYEABgooDECgAIKHCQwQHGAgooCHCBQWEAjAwIADCBMgOCBAYkMCAkomCAgAOw=="), sides:url("data:image/gif;R0lGODlhBgAgA/QAALDM8sLY8sPZ88Ta9MXb9MXb9dXp/Nnt/9rt/9vu/9zu/93v/97v/97w/9/w/+Dw/+Dx/+Hx/+Ly/////7DM8rDM8rDM8rDM8rDM8rDM8rDM8rDM8rDM8rDM8rDM8rDM8iH5BAEAABMALAAAAAAGACADRAj/AAFIGCgBAIAFCBcYNMDQgEEBEAUYLECxwMSKFylmtAigIkePG0N2xDhSY8mPJEGeFKmyZcqXJl3GhIlyps2aOFnS1HmTZ86VQGX+FOqzaNCdR3smHYqU6FKjTqM2napUalWqTK9qzcoVKskHYB8YTEA2gcEAaAMYHMB2gNetb7s+nWtVbt24eOlizXtXL1y/dvcC5iu4r+HCiP8eVpw4MOPHPyNIjmCwgeUGBhVoVmAQgWcEZ9M+jDga4tq2hCGndsx6tevBsBe3jt34tWzbtWmr1j37Nm/cu30Lzz08OPHjxpP3Rr5cOfDm0J9L/029ePTquSdTBgChOwSDDsI7gjDIoDwDgwkVAihrFsBn0AAOyD9gkIB9AqHR5lcLIKLE/qQB0JZbAqKGnXMHXmfddAsmyCBzDyLY4IQQOmghhRJWiKGCGnaY4YccghhhiCSOaOKFHpaIoogrqrjhiS+2CGOKM7IY4400yqgjjjbmyKOLPgbZ45BAElljkUgeqeRTAQEAOw=="), frame-bg:url("data:image/gif;R0lGODlhAQAgA/QAAMLY8sPZ88Ta9MXb9MXb9dXp/Nnt/9rt/9vu/9zu/93v/97v/97w/9/w/+Dw/+Dx/+Hx/+Ly/////8LY8sLY8sLY8sLY8sLY8sLY8sLY8sLY8sLY8sLY8sLY8sLY8sLY8iH5BAEAABIALAAAAAABACADRAhRACMoKBCAgMGDCBMqXMiwocOHECMmdIAAgACJGDNq3JgRAoMEBwAECHCRo8mTKFOqXMnyIYQHDRYoQHDAwAAAIkmWbMmzp8+fQIMKHUq06M+AADs=")" !important
}

.x-cmd-slicer.x-btn-pressed.x-btn-default-large:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url("data:image/gif;R0lGODlhAwASAPMAAJfD85fE9Zy955664aXA4qe/46jA47TK47bL5Mva7v///wAAAJfD85fD85fD85fD8yH5BAEAAAoALAAAAAADABIAQwgzAAcILHAAAQABCQIoLAAgAIKHChIQJJAgooGHCBQGEDggAYEDBSoiOGAggYCGAAyUVBAQADs="), sides:url("data:image/gif;R0lGODlhBgAgA/QAAI3A9Y7A9Y/B9ZDB9ZHB9ZHC9ZLC9ZPC9ZTD9ZXD8pXD9ZXE9ZbE9Z664bbO6LfL5LfM5LjM5LjN5LnN5LrO5LrO5bvP5bzP5bzQ5b3Q5b7R5f///43A9Y3A9Y3A9Y3A9SH5BAEAABsALAAAAAAGACADRAj/ABs8GPigQQMLCC0YdMDQgUECEAkYXEBxgUEGGBlczLgRY0eNDTKCFPmxZEiOJz2mHImS5EqTLmO2nKlSZk2aLG/qzMkTJk6fO4H2fEnU5lCjQpMW/bk0aNOjTJE+VSq1atSrTq1mxQp1q9euYJVOGDvBYIazGQwGWBvA4IG3B6hylfuVbtipeLXe1Wu3b965f+sG3guY72C/hhMXXixYcWPGhB9LvhuhcgSDFDJTMHih8wWDGkJrMAigNACDAlILMGigtQGDCGIjQAyZ9mTbkXPj3n24t2PdvmsHvz0c+G/ex4sjF568OfPnxJ1Hh26c+vLp2Ktnv669O/fvysNLlPfeAIJ5CAYlqJdgkGzZBhXiVzCYUGEDDPgxmEULWrTBBAAmoBZbqKlm0AAIDmBQAQwWwJprsMlmkAIUKgDeeBdaJ56GGG64nYfkdSgihyR+OKKJJYaYYoYotqiiiyy+KGOMNIJY44kz2qgjjjeuuKOPPP4Io5A5BmkkkEgOeaSSSRbZZI9MRumklFBOaWWVWBKJZUAAOw=="), frame-bg:url("data:image/gif;R0lGODlhAQAgA/QAAI3A9Y7A9Y/B9ZDB9ZHB9ZHC9ZLC9ZPC9ZTD9ZXD8pXD9ZXE9ZbE9bbO6LfL5LfM5LjM5LjN5LnN5LrO5LrO5bvP5bzP5bzQ5b3Q5b7R5f///43A9Y3A9Y3A9Y3A9Y3A9SH5BAEAABoALAAAAAABACADRAhVAB1UaEBgAYODCBMqXMiwocOHECNKTCgBQ4ADEzNq3MhRI4QJFjIAEGAAQceTKFOqXMmyZcQHESRQqHABQ4YEAQQMKFBSgcufQIMKHUq0qNGjSIcGBAA7")" !important
}

.x-cmd-slicer.x-btn-focus.x-btn-pressed.x-btn-default-large:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url("data:image/gif;R0lGODlhAwASAPMAAJfD85fE9Zy955664aXA4qe/46jA47TK47bL5Mva7v///wAAAJfD85fD85fD85fD8yH5BAEAAAoALAAAAAADABIAQwgzAAcILHAAAQABCQIoLAAgAIKHChIQJJAgooGHCBQGEDggAYEDBSoiOGAggYCGAAyUVBAQADs="), sides:url("data:image/gif;R0lGODlhBgAgA/QAAI3A9Y7A9Y/B9ZDB9ZHB9ZHC9ZLC9ZPC9ZTD9ZXD8pXD9ZXE9ZbE9Z664bbO6LfL5LfM5LjM5LjN5LnN5LrO5LrO5bvP5bzP5bzQ5b3Q5b7R5f///43A9Y3A9Y3A9Y3A9SH5BAEAABsALAAAAAAGACADRAj/ABs8GPigQQMLCC0YdMDQgUECEAkYXEBxgUEGGBlczLgRY0eNDTKCFPmxZEiOJz2mHImS5EqTLmO2nKlSZk2aLG/qzMkTJk6fO4H2fEnU5lCjQpMW/bk0aNOjTJE+VSq1atSrTq1mxQp1q9euYJVOGDvBYIazGQwGWBvA4IG3B6hylfuVbtipeLXe1Wu3b965f+sG3guY72C/hhMXXixYcWPGhB9LvhuhcgSDFDJTMHih8wWDGkJrMAigNACDAlILMGigtQGDCGIjQAyZ9mTbkXPj3n24t2PdvmsHvz0c+G/ex4sjF568OfPnxJ1Hh26c+vLp2Ktnv669O/fvysNLlPfeAIJ5CAYlqJdgkGzZBhXiVzCYUGEDDPgxmEULWrTBBAAmoBZbqKlm0AAIDmBQAQwWwJprsMlmkAIUKgDeeBdaJ56GGG64nYfkdSgihyR+OKKJJYaYYoYotqiiiyy+KGOMNIJY44kz2qgjjjeuuKOPPP4Io5A5BmkkkEgOeaSSSRbZZI9MRumklFBOaWWVWBKJZUAAOw=="), frame-bg:url("data:image/gif;R0lGODlhAQAgA/QAAI3A9Y7A9Y/B9ZDB9ZHB9ZHC9ZLC9ZPC9ZTD9ZXD8pXD9ZXE9ZbE9bbO6LfL5LfM5LjM5LjN5LnN5LrO5LrO5bvP5bzP5bzQ5b3Q5b7R5f///43A9Y3A9Y3A9Y3A9Y3A9SH5BAEAABoALAAAAAABACADRAhVAB1UaEBgAYODCBMqXMiwocOHECNKTCgBQ4ADEzNq3MhRI4QJFjIAEGAAQceTKFOqXMmyZcQHESRQqHABQ4YEAQQMKFBSgcufQIMKHUq0qNGjSIcGBAA7")" !important
}

.x-cmd-slicer.x-btn-disabled.x-btn-default-large:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url("data:image/gif;R0lGODlhAwASAPMAAN7e3uDg4OHh4ePj4+fn5+7u7vT09Pb29v///wAAAN7e3t7e3t7e3t7e3t7e3t7e3iH5BAEAAAgALAAAAAADABIAQwgwAAUIHGDgAIAABQAoHKDwgEMEBQgSKABxgEODCgUKKEDAwACKBzwWCKAQwICPCAICADs="), sides:url("data:image/gif;R0lGODlhBgAgA/MAANra2tvb29zc3N3d3d7e3uHh4e3t7fHx8fLy8vPz8/T09PX19fb29v///9ra2tra2iH5BAEAAA0ALAAAAAAGACADQwj/AAswGMigQIEECBMYNMDQgMEAEAMYJECRwMSKFylmtFigIkePG0N2xDhSY8mPJEGeFKmyZcqXJl3GhIlyps2aOFnS1HmTZ86VQGX+FOqzaNCdR3smHYqU6FKjTqM2napUalWqTK9qzcoVKkkFYBUYREAWgUEAaAEYFMBWgNetb7s+nWtVbt24eOlizXtXL1y/dvcC5iu4r+HCiP8eVpw4MOPHPxdIXmAwrNgCZc0WOMD5wNm0DyOubWtwgOkBhCGndsx6tevBsBe3jt34tWzbtWmr1j37Nm/cu30Lzz08OPHjxpP3Rr5cOfDm0J9L/029ePTquSdTLqC9cliDCRUedkw4tqzBzp43dy59+jPa0BDhSyzQ1i190gVOo87fHrtz/9dZN52AAA7InIH/EajggQU2uGCCDD4YYIQUQmjhhBciiOGGGnboYIUcfpihiCFK6KGJJJ4IooojoujiiinG+GKLMM5YYo040qjjjTuyyOOPPga5UkAAOw=="), frame-bg:url("data:image/gif;R0lGODlhAQAgA/MAANra2tvb29zc3N3d3d7e3u3t7fHx8fLy8vPz8/T09PX19fb29v///9ra2tra2tra2iH5BAEAAAwALAAAAAABACADQwhPABcgKBCAgMGDCBMqXMiwocOHECMmTHAAgACJGDNq3JhRAUUDAAIIGMCxpMmTKFOqXAlRgUcECA4YMDAgpMiRJFnq3Mmzp8+fQIMKHdozIAA7")" !important
}

.x-button-default-large-cell > .x-grid-cell-inner {
    padding-top: 0;
    padding-bottom: 0
}

.x-button-default-large-cell > .x-grid-cell-inner > .x-btn-default-large {
    vertical-align: top
}

.x-btn-default-toolbar-small {
    -webkit-border-radius: 3px;
    -moz-border-radius: 3px;
    -ms-border-radius: 3px;
    -o-border-radius: 3px;
    border-radius: 3px;
    padding: 2px 2px 2px 2px;
    border-width: 1px;
    border-style: solid;
    background-color: transparent
}

.x-btn-default-toolbar-small-mc {
    background-color: transparent
}

.x-nbr .x-btn-default-toolbar-small {
    padding: 0 !important;
    border-width: 0 !important;
    -webkit-border-radius: 0px;
    -moz-border-radius: 0px;
    -ms-border-radius: 0px;
    -o-border-radius: 0px;
    border-radius: 0px;
    background-color: transparent !important;
    box-shadow: none !important
}

.x-btn-default-toolbar-small-frameInfo {
    font-family: th-3-3-3-3-1-1-1-1-2-2-2-2
}

.x-btn-default-toolbar-small-tl {
    background-position: 0 -6px
}

.x-btn-default-toolbar-small-tr {
    background-position: right -9px
}

.x-btn-default-toolbar-small-bl {
    background-position: 0 -12px
}

.x-btn-default-toolbar-small-br {
    background-position: right -15px
}

.x-btn-default-toolbar-small-ml {
    background-position: 0 top
}

.x-btn-default-toolbar-small-mr {
    background-position: right top
}

.x-btn-default-toolbar-small-tc {
    background-position: 0 0
}

.x-btn-default-toolbar-small-bc {
    background-position: 0 -3px
}

.x-btn-default-toolbar-small-tr, .x-btn-default-toolbar-small-br, .x-btn-default-toolbar-small-mr {
    padding-right: 3px
}

.x-btn-default-toolbar-small-tl, .x-btn-default-toolbar-small-bl, .x-btn-default-toolbar-small-ml {
    padding-left: 3px
}

.x-btn-default-toolbar-small-tc {
    height: 3px
}

.x-btn-default-toolbar-small-bc {
    height: 3px
}

.x-btn-default-toolbar-small-mc {
    padding: 0px 0px 0px 0px
}

.x-cmd-slicer.x-btn-default-toolbar-small:before {
    display: none;
    content: "x-slicer:, frame:3px 3px 3px 3px" !important
}

.x-btn-default-toolbar-small {
    border-color: transparent
}

.x-btn-button-default-toolbar-small {
    min-height: 16px
}

.x-ie9m .x-btn-button-default-toolbar-small {
    min-height: auto;
    height: 16px
}

.x-btn-inner-default-toolbar-small {
    font: normal 11px/16px tahoma, arial, verdana, sans-serif;
    color: #333;
    padding: 0 4px;
    max-width: 100%
}

.x-btn-icon-right > .x-btn-inner-default-toolbar-small, .x-btn-icon-left > .x-btn-inner-default-toolbar-small {
    max-width: calc(100% - 16px)
}

.x-ie10p .x-btn-inner-default-toolbar-small {
    max-width: none
}

.x-btn-icon-el-default-toolbar-small {
    font-size: 16px;
    height: 16px;
    color: #333;
    line-height: 16px
}

.x-btn-icon-left > .x-btn-icon-el-default-toolbar-small, .x-btn-icon-right > .x-btn-icon-el-default-toolbar-small {
    width: 16px
}

.x-btn-icon-top > .x-btn-icon-el-default-toolbar-small, .x-btn-icon-bottom > .x-btn-icon-el-default-toolbar-small {
    min-width: 16px
}

.x-btn-icon-el-default-toolbar-small.x-btn-glyph {
    opacity: 0.5
}

.x-ie8 .x-btn-icon-el-default-toolbar-small.x-btn-glyph {
    color: #999
}

.x-btn-text.x-btn-icon-left > .x-btn-icon-el-default-toolbar-small {
    margin-right: 0px
}

.x-btn-text.x-btn-icon-right > .x-btn-icon-el-default-toolbar-small {
    margin-left: 0px
}

.x-btn-text.x-btn-icon-top > .x-btn-icon-el-default-toolbar-small {
    margin-bottom: 4px
}

.x-btn-text.x-btn-icon-bottom > .x-btn-icon-el-default-toolbar-small {
    margin-top: 4px
}

.x-btn-arrow-right > .x-btn-icon.x-btn-no-text.x-btn-button-default-toolbar-small {
    padding-right: 4px
}

.x-btn-arrow-right > .x-btn-text.x-btn-icon-right > .x-btn-icon-el-default-toolbar-small {
    margin-right: 4px
}

.x-btn-arrow-bottom > .x-btn-button-default-toolbar-small, .x-btn-split-bottom > .x-btn-button-default-toolbar-small {
    padding-bottom: 2px
}

.x-btn-wrap-default-toolbar-small.x-btn-arrow-right:after {
    width: 8px;
    background-image: url("data:image/gif;R0lGODlhCgAKAIcAAAAAAP///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAAEALAAAAAAKAAoAAAgZAAMIHEiwoMGDCA0CWLhQYcODABJKnFgwIAA7");
    padding-right: 8px
}

.x-btn-wrap-default-toolbar-small.x-btn-arrow-bottom:after {
    height: 8px;
    background-image: url("data:image/gif;R0lGODlhCgAKAIcAAAAAAP///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAAEALAAAAAAKAAoAAAgZAAMIHEiwoMGDCA0CWLhQYcODABJKnFgwIAA7")
}

.x-btn-wrap-default-toolbar-small.x-btn-split-right:after {
    width: 14px;
    background-image: url("data:image/gif;R0lGODlhDgBIAIcAAAAAAMnJycLa9vX19QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAMAAAIALAAAAAAOAEgAAAg8AAUIHEiwoMGDCBMqXMiwocOHECNKnEixosWLGDNq3Mixo8ePAEKGVCiSIYCPKFOqXMmypcuXMGPKnBkQADs=");
    padding-right: 14px
}

.x-btn-wrap-default-toolbar-small.x-btn-split-bottom:after {
    height: 14px;
    background-image: url("data:image/gif;R0lGODlhyAAOAIcAAAAAAMTExMLa9v///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAMAAAIALAAAAADIAA4AAAhfAAUIHEiwoMGDCBMqXMiwocOHECNKnEixosWLGDNq3Mixo8ePIEOKHEmypMmTKFOqXMmypcuXMGPKnEmzpk2GAHLmvMmzJ0edPoMKrQhgqNGjSJMqXcq0qdOnUKN2DAgAOw==")
}

.x-btn-over > .x-btn-wrap-default-toolbar-small.x-btn-split-right:after {
    background-image: url("data:image/gif;R0lGODlhDgBIAMIEAAAAAKrI8cLa9tru/////////////////yH5BAEKAAIALAAAAAAOAEgAAANcGCPczupJEaerFq6sefdYFlrjVErnk14btzbv57YiTdomjuoqz3oUH0woqwFjwSMxCVoinzSAVDp8TH/WnnLb5M68xq74Ow6Tz+b0Dbwut9FvdY49d9fhd/kOmAAAOw==")
}

.x-btn-over > .x-btn-wrap-default-toolbar-small.x-btn-split-bottom:after {
    background-image: url("data:image/gif;R0lGODlhyAAOAKEDAAAAAKrI8e/4/////yH5BAEKAAMALAAAAADIAA4AAAJbjI+py+0Po5y02uuE3rz7D4biSJbmiabqKg7uC8fyTNf2jef6zvf+DwwKh8Si8YhMKpfMpvMJjUqn1Kr1is1qeYBudwsOi13esflsBaDX7Lb7DY/L5/S6/X4uAAA7")
}

.x-btn-split-right > .x-btn-icon.x-btn-no-text.x-btn-button-default-toolbar-small {
    padding-right: 4px
}

.x-btn-split-right > .x-btn-text.x-btn-icon-right > .x-btn-icon-el-default-toolbar-small {
    margin-right: 4px
}

.x-btn-focus.x-btn-default-toolbar-small {
    background-image: none;
    background-color: transparent
}

.x-btn-focus.x-btn-default-toolbar-small .x-btn-wrap {
    outline: 1px dotted #333
}

.x-btn-default-toolbar-small .x-btn-arrow-el {
    position: absolute;
    top: 0;
    right: 0;
    height: 100%;
    width: 16px;
    pointer-events: none
}

.x-btn-over.x-btn-default-toolbar-small {
    border-color: #81a4d0;
    background-image: none;
    background-color: #dbeeff;
    background-image: -webkit-gradient(linear, top, bottom, color-stop(0%, #dbeeff), color-stop(48%, #d0e7ff), color-stop(52%, #bbd2f0), color-stop(0%, #bed6f5));
    background-image: -webkit-linear-gradient(top, #dbeeff, #d0e7ff 48%, #bbd2f0 52%, #bed6f5);
    background-image: -moz-linear-gradient(top, #dbeeff, #d0e7ff 48%, #bbd2f0 52%, #bed6f5);
    background-image: -o-linear-gradient(top, #dbeeff, #d0e7ff 48%, #bbd2f0 52%, #bed6f5);
    background-image: -ms-linear-gradient(top, #dbeeff, #d0e7ff 48%, #bbd2f0 52%, #bed6f5);
    background-image: linear-gradient(top, #dbeeff, #d0e7ff 48%, #bbd2f0 52%, #bed6f5)
}

.x-btn.x-btn-menu-active.x-btn-default-toolbar-small, .x-btn.x-btn-pressed.x-btn-default-toolbar-small {
    border-color: #7a9ac4;
    background-image: none;
    background-color: #bccfe5;
    background-image: -webkit-gradient(linear, top, bottom, color-stop(0%, #bccfe5), color-stop(48%, #c5d6e7), color-stop(52%, #95c4f4), color-stop(0%, #9fc9f5));
    background-image: -webkit-linear-gradient(top, #bccfe5, #c5d6e7 48%, #95c4f4 52%, #9fc9f5);
    background-image: -moz-linear-gradient(top, #bccfe5, #c5d6e7 48%, #95c4f4 52%, #9fc9f5);
    background-image: -o-linear-gradient(top, #bccfe5, #c5d6e7 48%, #95c4f4 52%, #9fc9f5);
    background-image: -ms-linear-gradient(top, #bccfe5, #c5d6e7 48%, #95c4f4 52%, #9fc9f5);
    background-image: linear-gradient(top, #bccfe5, #c5d6e7 48%, #95c4f4 52%, #9fc9f5)
}

.x-btn.x-btn-disabled.x-btn-default-toolbar-small {
    border-color: #e1e1e1;
    background-image: none;
    background-color: transparent
}

.x-btn.x-btn-disabled.x-btn-default-toolbar-small .x-btn-inner {
    color: #8c8c8c
}

.x-btn-focus .x-btn-default-toolbar-small-tl, .x-btn-focus .x-btn-default-toolbar-small-bl, .x-btn-focus .x-btn-default-toolbar-small-tr, .x-btn-focus .x-btn-default-toolbar-small-br, .x-btn-focus .x-btn-default-toolbar-small-tc, .x-btn-focus .x-btn-default-toolbar-small-bc {
    background-image: url(images/btn/btn-default-toolbar-small-focus-corners.gif)
}

.x-btn-focus .x-btn-default-toolbar-small-ml, .x-btn-focus .x-btn-default-toolbar-small-mr {
    background-image: url(images/btn/btn-default-toolbar-small-focus-sides.gif)
}

.x-btn-focus .x-btn-default-toolbar-small-mc {
    background-color: transparent;
    background-image: url(images/btn/btn-default-toolbar-small-focus-fbg.gif)
}

.x-btn-over .x-btn-default-toolbar-small-tl, .x-btn-over .x-btn-default-toolbar-small-bl, .x-btn-over .x-btn-default-toolbar-small-tr, .x-btn-over .x-btn-default-toolbar-small-br, .x-btn-over .x-btn-default-toolbar-small-tc, .x-btn-over .x-btn-default-toolbar-small-bc {
    background-image: url("data:image/gif;R0lGODlhAwASAPMAAIGk0Iys1I2s1JOy25y63rjR8brN5r3V9NHm+9Ln+9ns/9rt/////wAAAIGk0IGk0CH5BAEAAAwALAAAAAADABIAQwg0AAEIDIBAQYEBBg4oDFDggIKHDAwESEDAQEQBCzIqPCAQgAECCQJYVIBAgIEBDQsIMMkgIAA7")
}

.x-btn-over .x-btn-default-toolbar-small-ml, .x-btn-over .x-btn-default-toolbar-small-mr {
    background-image: url("data:image/gif;R0lGODlhBgAgA/QAAIGk0LvS8LvS8bvT8bzT8rzU8rzU873U89Dn/9Hn/9Lo/9Pp/9Tp/9Xq/9fr/9js/////4Gk0IGk0IGk0IGk0IGk0IGk0IGk0IGk0IGk0IGk0IGk0IGk0IGk0IGk0IGk0CH5BAEAABAALAAAAAAGACADRAj/AAE8GPgAAIAACAMYPMDwwMKGDxlGdAigIUWLEzNWhLhRYseLHDF+1CiyZMiTHk2mRAlypcuWMEmylPmSZsyROFXe1GmzZ86ZP2sG3QmU51CfRpMWXSpUaVOmRJ9KjUoVKVSDC7IuMEigKwGrU8FWPUrW6VizYtOWvbo2bNuzbNG+VSu3bty7bu3mxQt3r9++gNU2GNzAYILDCQwKWCzAoIHHBujylfyXcuC5mPVe1my5c+bJnyuH3gya82jPplOXXi1adWvWpF/Ljk0bNWzbs3HXPs3b9W7fuoPjdEDcgUEGyBkYVMBcgUEE0BEYTKgQwIDrAwwW2F5AOPDet8HnUBb/O/z38+bTj0e/Xn359vDfy/funn58+/PJ49+vvz/7/P/xF6B/9RF4n4EAFjjgggo2eCCDDzqYYIQUTmihgBJiWKGGFyLI4YcehgihQwEBADs=")
}

.x-btn-over .x-btn-default-toolbar-small-mc {
    background-color: #dbeeff;
    background-image: url("data:image/gif;R0lGODlhAQAgA/MAALvS8LvS8bvT8bzT8rzU8rzU873U89Dn/9Hn/9Lo/9Pp/9Tp/9Xq/9fr/9js/////yH5BAEAAA8ALAAAAAABACADQwhDAB0AMECwoMGDCBMqXMiwocOHCRUMgEixosWLFxkgCFAAo8ePIEOKHEmyYoMFCQ4AEECgpMuXMGPKnEmzps2bOAsGBAA7")
}

.x-btn-focus.x-btn-over .x-btn-default-toolbar-small-tl, .x-btn-focus.x-btn-over .x-btn-default-toolbar-small-bl, .x-btn-focus.x-btn-over .x-btn-default-toolbar-small-tr, .x-btn-focus.x-btn-over .x-btn-default-toolbar-small-br, .x-btn-focus.x-btn-over .x-btn-default-toolbar-small-tc, .x-btn-focus.x-btn-over .x-btn-default-toolbar-small-bc {
    background-image: url("data:image/gif;R0lGODlhAwASAPMAAIGk0Iys1I2s1JOy25y63rjR8brN5r3V9NHm+9Ln+9ns/9rt/////wAAAIGk0IGk0CH5BAEAAAwALAAAAAADABIAQwg0AAEIDIBAQYEBBg4oDFDggIKHDAwESEDAQEQBCzIqPCAQgAECCQJYVIBAgIEBDQsIMMkgIAA7")
}

.x-btn-focus.x-btn-over .x-btn-default-toolbar-small-ml, .x-btn-focus.x-btn-over .x-btn-default-toolbar-small-mr {
    background-image: url("data:image/gif;R0lGODlhBgAgA/QAAIGk0LvS8LvS8bvT8bzT8rzU8rzU873U89Dn/9Hn/9Lo/9Pp/9Tp/9Xq/9fr/9js/////4Gk0IGk0IGk0IGk0IGk0IGk0IGk0IGk0IGk0IGk0IGk0IGk0IGk0IGk0IGk0CH5BAEAABAALAAAAAAGACADRAj/AAE8GPgAAIAACAMYPMDwwMKGDxlGdAigIUWLEzNWhLhRYseLHDF+1CiyZMiTHk2mRAlypcuWMEmylPmSZsyROFXe1GmzZ86ZP2sG3QmU51CfRpMWXSpUaVOmRJ9KjUoVKVSDC7IuMEigKwGrU8FWPUrW6VizYtOWvbo2bNuzbNG+VSu3bty7bu3mxQt3r9++gNU2GNzAYILDCQwKWCzAoIHHBujylfyXcuC5mPVe1my5c+bJnyuH3gya82jPplOXXi1adWvWpF/Ljk0bNWzbs3HXPs3b9W7fuoPjdEDcgUEGyBkYVMBcgUEE0BEYTKgQwIDrAwwW2F5AOPDet8HnUBb/O/z38+bTj0e/Xn359vDfy/funn58+/PJ49+vvz/7/P/xF6B/9RF4n4EAFjjgggo2eCCDDzqYYIQUTmihgBJiWKGGFyLI4YcehgihQwEBADs=")
}

.x-btn-focus.x-btn-over .x-btn-default-toolbar-small-mc {
    background-color: #dbeeff;
    background-image: url("data:image/gif;R0lGODlhAQAgA/MAALvS8LvS8bvT8bzT8rzU8rzU873U89Dn/9Hn/9Lo/9Pp/9Tp/9Xq/9fr/9js/////yH5BAEAAA8ALAAAAAABACADQwhDAB0AMECwoMGDCBMqXMiwocOHCRUMgEixosWLFxkgCFAAo8ePIEOKHEmyYoMFCQ4AEECgpMuXMGPKnEmzps2bOAsGBAA7")
}

.x-btn.x-btn-menu-active .x-btn-default-toolbar-small-tl, .x-btn.x-btn-menu-active .x-btn-default-toolbar-small-bl, .x-btn.x-btn-menu-active .x-btn-default-toolbar-small-tr, .x-btn.x-btn-menu-active .x-btn-default-toolbar-small-br, .x-btn.x-btn-menu-active .x-btn-default-toolbar-small-tc, .x-btn.x-btn-menu-active .x-btn-default-toolbar-small-bc, .x-btn.x-btn-pressed .x-btn-default-toolbar-small-tl, .x-btn.x-btn-pressed .x-btn-default-toolbar-small-bl, .x-btn.x-btn-pressed .x-btn-default-toolbar-small-tr, .x-btn.x-btn-pressed .x-btn-default-toolbar-small-br, .x-btn.x-btn-pressed .x-btn-default-toolbar-small-tc, .x-btn.x-btn-pressed .x-btn-default-toolbar-small-bc {
    background-image: url("data:image/gif;R0lGODlhAwASAPMAAHqaxIWo04ejyYekyY6qzprE8JvE8J3I9J7I9LbK4rfH37fL4rzP5b3Q5f///wAAACH5BAEAAA4ALAAAAAADABIAQwg1AAEIHLCggYEAChAoHFDgQIOHDhQMSEBAQUQBDDIe2CgQgAICCQZYbLBAgIIABg4UEGDSQUAAOw==")
}

.x-btn.x-btn-menu-active .x-btn-default-toolbar-small-ml, .x-btn.x-btn-menu-active .x-btn-default-toolbar-small-mr, .x-btn.x-btn-pressed .x-btn-default-toolbar-small-ml, .x-btn.x-btn-pressed .x-btn-default-toolbar-small-mr {
    background-image: url("data:image/gif;R0lGODlhBgAgA/QAAHqaxJXE9JbE9JfF9JjF9JnG9JrG9JvH9JzH9L7Q5b/R5cDS5cHT5sLT5sPU5sPV5sTV5v///3qaxHqaxHqaxHqaxHqaxHqaxHqaxHqaxHqaxHqaxHqaxHqaxHqaxHqaxCH5BAEAABEALAAAAAAGACADRAj/AAEkGJgAAIAACAMYRMAQwcKGDxlGdAigIUWLEzNWhLhRYseLHDF+1CiyZMiTHk2mRAlypcuWMEmylPmSZsyROFXe1GmzZ86ZP2sG3QmU51CfRpMWXSpUaVOmRJ9KjUoVKVSDDbI2MFigawGrU8FWPUrW6VizYtOWvbo2bNuzbNG+VSu3bty7bu3mxQt3r9++gNUuGLzA4IPDDwwOWDzA4IHHB+jylfyXcuC5mPVe1my5c+bJnyuH3gya82jPplOXXi1adWvWpF/Ljk0bNWzbs3HXPs3b9W7fuoPjVEBcgUEGyBkYdMDcgUEI0CEYFEBdgEEC2AkYNMDdgHDgvW+HUc89/rd48OjPqyefnv168+7jw5///X19+ffpl8/Pf7//9voB2J+A/9lXIH4HBmgggQwu6CCCDUL4oIISVkjhhQNOmKGFG2KYYIcgfihihA4FBAA7")
}

.x-btn.x-btn-menu-active .x-btn-default-toolbar-small-mc, .x-btn.x-btn-pressed .x-btn-default-toolbar-small-mc {
    background-color: #bccfe5;
    background-image: url("data:image/gif;R0lGODlhAQAgA/QAAJXE9JbE9JfF9JjF9JnG9JrG9JvH9JzH9L7Q5b/R5cDS5cHT5sLT5sPU5sPV5sTV5v///5XE9JXE9JXE9JXE9JXE9JXE9JXE9JXE9JXE9JXE9JXE9JXE9JXE9JXE9JXE9CH5BAEAABAALAAAAAABACADRAhDABEAOECwoMGDCBMqXMiwocOHCRkQgEixosWLFxU4EGAAo8ePIEOKHEmyYoIFDR4EGFCgpMuXMGPKnEmzps2bOAsGBAA7")
}

.x-btn-focus.x-btn-menu-active .x-btn-default-toolbar-small-tl, .x-btn-focus.x-btn-menu-active .x-btn-default-toolbar-small-bl, .x-btn-focus.x-btn-menu-active .x-btn-default-toolbar-small-tr, .x-btn-focus.x-btn-menu-active .x-btn-default-toolbar-small-br, .x-btn-focus.x-btn-menu-active .x-btn-default-toolbar-small-tc, .x-btn-focus.x-btn-menu-active .x-btn-default-toolbar-small-bc, .x-btn-focus.x-btn-pressed .x-btn-default-toolbar-small-tl, .x-btn-focus.x-btn-pressed .x-btn-default-toolbar-small-bl, .x-btn-focus.x-btn-pressed .x-btn-default-toolbar-small-tr, .x-btn-focus.x-btn-pressed .x-btn-default-toolbar-small-br, .x-btn-focus.x-btn-pressed .x-btn-default-toolbar-small-tc, .x-btn-focus.x-btn-pressed .x-btn-default-toolbar-small-bc {
    background-image: url("data:image/gif;R0lGODlhAwASAPMAAHqaxIWo04ejyYekyY6qzprE8JvE8J3I9J7I9LbK4rfH37fL4rzP5b3Q5f///wAAACH5BAEAAA4ALAAAAAADABIAQwg1AAEIHLCggYEAChAoHFDgQIOHDhQMSEBAQUQBDDIe2CgQgAICCQZYbLBAgIIABg4UEGDSQUAAOw==")
}

.x-btn-focus.x-btn-menu-active .x-btn-default-toolbar-small-ml, .x-btn-focus.x-btn-menu-active .x-btn-default-toolbar-small-mr, .x-btn-focus.x-btn-pressed .x-btn-default-toolbar-small-ml, .x-btn-focus.x-btn-pressed .x-btn-default-toolbar-small-mr {
    background-image: url("data:image/gif;R0lGODlhBgAgA/QAAHqaxJXE9JbE9JfF9JjF9JnG9JrG9JvH9JzH9L7Q5b/R5cDS5cHT5sLT5sPU5sPV5sTV5v///3qaxHqaxHqaxHqaxHqaxHqaxHqaxHqaxHqaxHqaxHqaxHqaxHqaxHqaxCH5BAEAABEALAAAAAAGACADRAj/AAEkGJgAAIAACAMYRMAQwcKGDxlGdAigIUWLEzNWhLhRYseLHDF+1CiyZMiTHk2mRAlypcuWMEmylPmSZsyROFXe1GmzZ86ZP2sG3QmU51CfRpMWXSpUaVOmRJ9KjUoVKVSDDbI2MFigawGrU8FWPUrW6VizYtOWvbo2bNuzbNG+VSu3bty7bu3mxQt3r9++gNUuGLzA4IPDDwwOWDzA4IHHB+jylfyXcuC5mPVe1my5c+bJnyuH3gya82jPplOXXi1adWvWpF/Ljk0bNWzbs3HXPs3b9W7fuoPjVEBcgUEGyBkYdMDcgUEI0CEYFEBdgEEC2AkYNMDdgHDgvW+HUc89/rd48OjPqyefnv168+7jw5///X19+ffpl8/Pf7//9voB2J+A/9lXIH4HBmgggQwu6CCCDUL4oIISVkjhhQNOmKGFG2KYYIcgfihihA4FBAA7")
}

.x-btn-focus.x-btn-menu-active .x-btn-default-toolbar-small-mc, .x-btn-focus.x-btn-pressed .x-btn-default-toolbar-small-mc {
    background-color: #bccfe5;
    background-image: url("data:image/gif;R0lGODlhAQAgA/QAAJXE9JbE9JfF9JjF9JnG9JrG9JvH9JzH9L7Q5b/R5cDS5cHT5sLT5sPU5sPV5sTV5v///5XE9JXE9JXE9JXE9JXE9JXE9JXE9JXE9JXE9JXE9JXE9JXE9JXE9JXE9JXE9CH5BAEAABAALAAAAAABACADRAhDABEAOECwoMGDCBMqXMiwocOHCRkQgEixosWLFxU4EGAAo8ePIEOKHEmyYoIFDR4EGFCgpMuXMGPKnEmzps2bOAsGBAA7")
}

.x-btn.x-btn-disabled .x-btn-default-toolbar-small-tl, .x-btn.x-btn-disabled .x-btn-default-toolbar-small-bl, .x-btn.x-btn-disabled .x-btn-default-toolbar-small-tr, .x-btn.x-btn-disabled .x-btn-default-toolbar-small-br, .x-btn.x-btn-disabled .x-btn-default-toolbar-small-tc, .x-btn.x-btn-disabled .x-btn-default-toolbar-small-bc {
    background-image: url("data:image/gif;R0lGODlhAwASAPIAAPDw8PHx8fT09Pb29v///wAAAPDw8PDw8CH5BAEAAAQALAAAAAADABIAQggnAAEIDECgoIABBQkQTFhwAMGDBBwyLCgQwAABChEWDHAxYQCOBAICADs=")
}

.x-btn.x-btn-disabled .x-btn-default-toolbar-small-ml, .x-btn.x-btn-disabled .x-btn-default-toolbar-small-mr {
    background-image: url("data:image/gif;R0lGODlhBgAgA/EAAPDw8P///wAAAPDw8CH5BAEAAAEALAAAAAAGACADQQj/AAEEGBgAgECCBgkWPDgwIUKGCxU6bAhxYsSHEitqzMgRo0eKHUF+vCiyJMmTFlNuHKkyJMqVJluyhPnSpcyYNG/WnGkzp8+eQHkKxRmU6NCdRpMiXaqz6c+jTosyfao0KlSqU6VarYp1a9arWruKDUsWrFmuZdGe/aq2Ldu3XuOOXSs3Ldy5buvSxXvXrt68fP/23es3sOHCiAkrBpyY8eLBjiNDniy48uHHlhtTviw5M2bOmzV77gx6dOjPokurTs0atWvSrWG/Pi27Nu3bpnOvnq07Nu7dtnvzBv7bt/DgxI8XH248ufPm0JlLRx6d+vTl1rNj3668+/Pr3qtzDP+uPTx48uPFm28YEAA7")
}

.x-btn.x-btn-disabled .x-btn-default-toolbar-small-mc {
    background-color: transparent;
    background-image: url("data:image/gif;R0lGODlhAQAgA/AAAP///wAAACH5BAEAAAAALAAAAAABACADQAgwAAEIHEiwoMGDCBMqXMiwocOHECNKnEixosWLGDNq3Mixo8ePIEOKHEmypMmTFAMCADs=")
}

.x-nbr .x-btn-default-toolbar-small {
    background-image: none
}

.x-btn-disabled.x-btn-default-toolbar-small {
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=50)";
    opacity: 0.5
}

.x-nbr .x-segmented-button-item-horizontal.x-btn-default-toolbar-small.x-segmented-button-first {
    border-right-width: 1px !important
}

.x-nbr .x-segmented-button-item-horizontal.x-btn-default-toolbar-small.x-segmented-button-first .x-btn-default-toolbar-small-mc {
    padding-right: 2px !important
}

.x-nbr .x-segmented-button-item-horizontal.x-btn-default-toolbar-small.x-segmented-button-middle {
    border-right-width: 1px !important
}

.x-nbr .x-segmented-button-item-horizontal.x-btn-default-toolbar-small.x-segmented-button-middle .x-btn-default-toolbar-small-mc {
    padding-right: 2px !important;
    padding-left: 2px !important
}

.x-nbr .x-segmented-button-item-horizontal.x-btn-default-toolbar-small.x-segmented-button-last .x-btn-default-toolbar-small-mc {
    padding-left: 2px !important
}

.x-nbr .x-segmented-button-item-vertical.x-btn-default-toolbar-small.x-segmented-button-first {
    border-bottom-width: 1px !important
}

.x-nbr .x-segmented-button-item-vertical.x-btn-default-toolbar-small.x-segmented-button-first .x-btn-default-toolbar-small-mc {
    padding-bottom: 2px !important
}

.x-nbr .x-segmented-button-item-vertical.x-btn-default-toolbar-small.x-segmented-button-middle {
    border-bottom-width: 1px !important
}

.x-nbr .x-segmented-button-item-vertical.x-btn-default-toolbar-small.x-segmented-button-middle .x-btn-default-toolbar-small-mc {
    padding-top: 2px !important;
    padding-bottom: 2px !important
}

.x-nbr .x-segmented-button-item-vertical.x-btn-default-toolbar-small.x-segmented-button-last .x-btn-default-toolbar-small-mc {
    padding-top: 2px !important
}

.x-nbr .x-segmented-button-item.x-btn-default-toolbar-small:after {
    content: ' ';
    border-style: solid;
    border-width: 0;
    position: absolute
}

.x-nbr .x-segmented-button-item-horizontal.x-btn-default-toolbar-small:after {
    top: 1px;
    right: 0;
    bottom: 1px;
    left: 0
}

.x-nbr .x-segmented-button-item-horizontal.x-btn-default-toolbar-small.x-segmented-button-first:after {
    left: 1px
}

.x-nbr .x-segmented-button-item-horizontal.x-btn-default-toolbar-small.x-segmented-button-last:after {
    right: 1px
}

.x-nbr .x-segmented-button-item-vertical.x-btn-default-toolbar-small:after {
    top: 0;
    right: 1px;
    bottom: 0;
    left: 1px
}

.x-nbr .x-segmented-button-item-vertical.x-btn-default-toolbar-small.x-segmented-button-first:after {
    top: 1px
}

.x-nbr .x-segmented-button-item-vertical.x-btn-default-toolbar-small.x-segmented-button-last:after {
    bottom: 1px
}

.x-cmd-slicer.x-btn-focus.x-btn-default-toolbar-small:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url(images/btn/btn-default-toolbar-small-focus-corners.gif), sides:url(images/btn/btn-default-toolbar-small-focus-sides.gif), frame-bg:url(images/btn/btn-default-toolbar-small-focus-fbg.gif)" !important
}

.x-cmd-slicer.x-btn-over.x-btn-default-toolbar-small:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url("data:image/gif;R0lGODlhAwASAPMAAIGk0Iys1I2s1JOy25y63rjR8brN5r3V9NHm+9Ln+9ns/9rt/////wAAAIGk0IGk0CH5BAEAAAwALAAAAAADABIAQwg0AAEIDIBAQYEBBg4oDFDggIKHDAwESEDAQEQBCzIqPCAQgAECCQJYVIBAgIEBDQsIMMkgIAA7"), sides:url("data:image/gif;R0lGODlhBgAgA/QAAIGk0LvS8LvS8bvT8bzT8rzU8rzU873U89Dn/9Hn/9Lo/9Pp/9Tp/9Xq/9fr/9js/////4Gk0IGk0IGk0IGk0IGk0IGk0IGk0IGk0IGk0IGk0IGk0IGk0IGk0IGk0IGk0CH5BAEAABAALAAAAAAGACADRAj/AAE8GPgAAIAACAMYPMDwwMKGDxlGdAigIUWLEzNWhLhRYseLHDF+1CiyZMiTHk2mRAlypcuWMEmylPmSZsyROFXe1GmzZ86ZP2sG3QmU51CfRpMWXSpUaVOmRJ9KjUoVKVSDC7IuMEigKwGrU8FWPUrW6VizYtOWvbo2bNuzbNG+VSu3bty7bu3mxQt3r9++gNU2GNzAYILDCQwKWCzAoIHHBujylfyXcuC5mPVe1my5c+bJnyuH3gya82jPplOXXi1adWvWpF/Ljk0bNWzbs3HXPs3b9W7fuoPjdEDcgUEGyBkYVMBcgUEE0BEYTKgQwIDrAwwW2F5AOPDet8HnUBb/O/z38+bTj0e/Xn359vDfy/funn58+/PJ49+vvz/7/P/xF6B/9RF4n4EAFjjgggo2eCCDDzqYYIQUTmihgBJiWKGGFyLI4YcehgihQwEBADs="), frame-bg:url("data:image/gif;R0lGODlhAQAgA/MAALvS8LvS8bvT8bzT8rzU8rzU873U89Dn/9Hn/9Lo/9Pp/9Tp/9Xq/9fr/9js/////yH5BAEAAA8ALAAAAAABACADQwhDAB0AMECwoMGDCBMqXMiwocOHCRUMgEixosWLFxkgCFAAo8ePIEOKHEmyYoMFCQ4AEECgpMuXMGPKnEmzps2bOAsGBAA7")" !important
}

.x-cmd-slicer.x-btn-focus.x-btn-over.x-btn-default-toolbar-small:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url("data:image/gif;R0lGODlhAwASAPMAAIGk0Iys1I2s1JOy25y63rjR8brN5r3V9NHm+9Ln+9ns/9rt/////wAAAIGk0IGk0CH5BAEAAAwALAAAAAADABIAQwg0AAEIDIBAQYEBBg4oDFDggIKHDAwESEDAQEQBCzIqPCAQgAECCQJYVIBAgIEBDQsIMMkgIAA7"), sides:url("data:image/gif;R0lGODlhBgAgA/QAAIGk0LvS8LvS8bvT8bzT8rzU8rzU873U89Dn/9Hn/9Lo/9Pp/9Tp/9Xq/9fr/9js/////4Gk0IGk0IGk0IGk0IGk0IGk0IGk0IGk0IGk0IGk0IGk0IGk0IGk0IGk0IGk0CH5BAEAABAALAAAAAAGACADRAj/AAE8GPgAAIAACAMYPMDwwMKGDxlGdAigIUWLEzNWhLhRYseLHDF+1CiyZMiTHk2mRAlypcuWMEmylPmSZsyROFXe1GmzZ86ZP2sG3QmU51CfRpMWXSpUaVOmRJ9KjUoVKVSDC7IuMEigKwGrU8FWPUrW6VizYtOWvbo2bNuzbNG+VSu3bty7bu3mxQt3r9++gNU2GNzAYILDCQwKWCzAoIHHBujylfyXcuC5mPVe1my5c+bJnyuH3gya82jPplOXXi1adWvWpF/Ljk0bNWzbs3HXPs3b9W7fuoPjdEDcgUEGyBkYVMBcgUEE0BEYTKgQwIDrAwwW2F5AOPDet8HnUBb/O/z38+bTj0e/Xn359vDfy/funn58+/PJ49+vvz/7/P/xF6B/9RF4n4EAFjjgggo2eCCDDzqYYIQUTmihgBJiWKGGFyLI4YcehgihQwEBADs="), frame-bg:url("data:image/gif;R0lGODlhAQAgA/MAALvS8LvS8bvT8bzT8rzU8rzU873U89Dn/9Hn/9Lo/9Pp/9Tp/9Xq/9fr/9js/////yH5BAEAAA8ALAAAAAABACADQwhDAB0AMECwoMGDCBMqXMiwocOHCRUMgEixosWLFxkgCFAAo8ePIEOKHEmyYoMFCQ4AEECgpMuXMGPKnEmzps2bOAsGBAA7")" !important
}

.x-cmd-slicer.x-btn-pressed.x-btn-default-toolbar-small:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url("data:image/gif;R0lGODlhAwASAPMAAHqaxIWo04ejyYekyY6qzprE8JvE8J3I9J7I9LbK4rfH37fL4rzP5b3Q5f///wAAACH5BAEAAA4ALAAAAAADABIAQwg1AAEIHLCggYEAChAoHFDgQIOHDhQMSEBAQUQBDDIe2CgQgAICCQZYbLBAgIIABg4UEGDSQUAAOw=="), sides:url("data:image/gif;R0lGODlhBgAgA/QAAHqaxJXE9JbE9JfF9JjF9JnG9JrG9JvH9JzH9L7Q5b/R5cDS5cHT5sLT5sPU5sPV5sTV5v///3qaxHqaxHqaxHqaxHqaxHqaxHqaxHqaxHqaxHqaxHqaxHqaxHqaxHqaxCH5BAEAABEALAAAAAAGACADRAj/AAEkGJgAAIAACAMYRMAQwcKGDxlGdAigIUWLEzNWhLhRYseLHDF+1CiyZMiTHk2mRAlypcuWMEmylPmSZsyROFXe1GmzZ86ZP2sG3QmU51CfRpMWXSpUaVOmRJ9KjUoVKVSDDbI2MFigawGrU8FWPUrW6VizYtOWvbo2bNuzbNG+VSu3bty7bu3mxQt3r9++gNUuGLzA4IPDDwwOWDzA4IHHB+jylfyXcuC5mPVe1my5c+bJnyuH3gya82jPplOXXi1adWvWpF/Ljk0bNWzbs3HXPs3b9W7fuoPjVEBcgUEGyBkYdMDcgUEI0CEYFEBdgEEC2AkYNMDdgHDgvW+HUc89/rd48OjPqyefnv168+7jw5///X19+ffpl8/Pf7//9voB2J+A/9lXIH4HBmgggQwu6CCCDUL4oIISVkjhhQNOmKGFG2KYYIcgfihihA4FBAA7"), frame-bg:url("data:image/gif;R0lGODlhAQAgA/QAAJXE9JbE9JfF9JjF9JnG9JrG9JvH9JzH9L7Q5b/R5cDS5cHT5sLT5sPU5sPV5sTV5v///5XE9JXE9JXE9JXE9JXE9JXE9JXE9JXE9JXE9JXE9JXE9JXE9JXE9JXE9JXE9CH5BAEAABAALAAAAAABACADRAhDABEAOECwoMGDCBMqXMiwocOHCRkQgEixosWLFxU4EGAAo8ePIEOKHEmyYoIFDR4EGFCgpMuXMGPKnEmzps2bOAsGBAA7")" !important
}

.x-cmd-slicer.x-btn-focus.x-btn-pressed.x-btn-default-toolbar-small:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url("data:image/gif;R0lGODlhAwASAPMAAHqaxIWo04ejyYekyY6qzprE8JvE8J3I9J7I9LbK4rfH37fL4rzP5b3Q5f///wAAACH5BAEAAA4ALAAAAAADABIAQwg1AAEIHLCggYEAChAoHFDgQIOHDhQMSEBAQUQBDDIe2CgQgAICCQZYbLBAgIIABg4UEGDSQUAAOw=="), sides:url("data:image/gif;R0lGODlhBgAgA/QAAHqaxJXE9JbE9JfF9JjF9JnG9JrG9JvH9JzH9L7Q5b/R5cDS5cHT5sLT5sPU5sPV5sTV5v///3qaxHqaxHqaxHqaxHqaxHqaxHqaxHqaxHqaxHqaxHqaxHqaxHqaxHqaxCH5BAEAABEALAAAAAAGACADRAj/AAEkGJgAAIAACAMYRMAQwcKGDxlGdAigIUWLEzNWhLhRYseLHDF+1CiyZMiTHk2mRAlypcuWMEmylPmSZsyROFXe1GmzZ86ZP2sG3QmU51CfRpMWXSpUaVOmRJ9KjUoVKVSDDbI2MFigawGrU8FWPUrW6VizYtOWvbo2bNuzbNG+VSu3bty7bu3mxQt3r9++gNUuGLzA4IPDDwwOWDzA4IHHB+jylfyXcuC5mPVe1my5c+bJnyuH3gya82jPplOXXi1adWvWpF/Ljk0bNWzbs3HXPs3b9W7fuoPjVEBcgUEGyBkYdMDcgUEI0CEYFEBdgEEC2AkYNMDdgHDgvW+HUc89/rd48OjPqyefnv168+7jw5///X19+ffpl8/Pf7//9voB2J+A/9lXIH4HBmgggQwu6CCCDUL4oIISVkjhhQNOmKGFG2KYYIcgfihihA4FBAA7"), frame-bg:url("data:image/gif;R0lGODlhAQAgA/QAAJXE9JbE9JfF9JjF9JnG9JrG9JvH9JzH9L7Q5b/R5cDS5cHT5sLT5sPU5sPV5sTV5v///5XE9JXE9JXE9JXE9JXE9JXE9JXE9JXE9JXE9JXE9JXE9JXE9JXE9JXE9JXE9CH5BAEAABAALAAAAAABACADRAhDABEAOECwoMGDCBMqXMiwocOHCRkQgEixosWLFxU4EGAAo8ePIEOKHEmyYoIFDR4EGFCgpMuXMGPKnEmzps2bOAsGBAA7")" !important
}

.x-cmd-slicer.x-btn-disabled.x-btn-default-toolbar-small:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url("data:image/gif;R0lGODlhAwASAPIAAPDw8PHx8fT09Pb29v///wAAAPDw8PDw8CH5BAEAAAQALAAAAAADABIAQggnAAEIDECgoIABBQkQTFhwAMGDBBwyLCgQwAABChEWDHAxYQCOBAICADs="), sides:url("data:image/gif;R0lGODlhBgAgA/EAAPDw8P///wAAAPDw8CH5BAEAAAEALAAAAAAGACADQQj/AAEEGBgAgECCBgkWPDgwIUKGCxU6bAhxYsSHEitqzMgRo0eKHUF+vCiyJMmTFlNuHKkyJMqVJluyhPnSpcyYNG/WnGkzp8+eQHkKxRmU6NCdRpMiXaqz6c+jTosyfao0KlSqU6VarYp1a9arWruKDUsWrFmuZdGe/aq2Ldu3XuOOXSs3Ldy5buvSxXvXrt68fP/23es3sOHCiAkrBpyY8eLBjiNDniy48uHHlhtTviw5M2bOmzV77gx6dOjPokurTs0atWvSrWG/Pi27Nu3bpnOvnq07Nu7dtnvzBv7bt/DgxI8XH248ufPm0JlLRx6d+vTl1rNj3668+/Pr3qtzDP+uPTx48uPFm28YEAA7"), frame-bg:url("data:image/gif;R0lGODlhAQAgA/AAAP///wAAACH5BAEAAAAALAAAAAABACADQAgwAAEIHEiwoMGDCBMqXMiwocOHECNKnEixosWLGDNq3Mixo8ePIEOKHEmypMmTFAMCADs=")" !important
}

.x-button-default-toolbar-small-cell > .x-grid-cell-inner {
    padding-top: 0;
    padding-bottom: 0
}

.x-button-default-toolbar-small-cell > .x-grid-cell-inner > .x-btn-default-toolbar-small {
    vertical-align: top
}

.x-btn-default-toolbar-medium {
    -webkit-border-radius: 3px;
    -moz-border-radius: 3px;
    -ms-border-radius: 3px;
    -o-border-radius: 3px;
    border-radius: 3px;
    padding: 3px 3px 3px 3px;
    border-width: 1px;
    border-style: solid;
    background-color: transparent
}

.x-btn-default-toolbar-medium-mc {
    background-color: transparent
}

.x-nbr .x-btn-default-toolbar-medium {
    padding: 0 !important;
    border-width: 0 !important;
    -webkit-border-radius: 0px;
    -moz-border-radius: 0px;
    -ms-border-radius: 0px;
    -o-border-radius: 0px;
    border-radius: 0px;
    background-color: transparent !important;
    box-shadow: none !important
}

.x-btn-default-toolbar-medium-frameInfo {
    font-family: th-3-3-3-3-1-1-1-1-3-3-3-3
}

.x-btn-default-toolbar-medium-tl {
    background-position: 0 -6px
}

.x-btn-default-toolbar-medium-tr {
    background-position: right -9px
}

.x-btn-default-toolbar-medium-bl {
    background-position: 0 -12px
}

.x-btn-default-toolbar-medium-br {
    background-position: right -15px
}

.x-btn-default-toolbar-medium-ml {
    background-position: 0 top
}

.x-btn-default-toolbar-medium-mr {
    background-position: right top
}

.x-btn-default-toolbar-medium-tc {
    background-position: 0 0
}

.x-btn-default-toolbar-medium-bc {
    background-position: 0 -3px
}

.x-btn-default-toolbar-medium-tr, .x-btn-default-toolbar-medium-br, .x-btn-default-toolbar-medium-mr {
    padding-right: 3px
}

.x-btn-default-toolbar-medium-tl, .x-btn-default-toolbar-medium-bl, .x-btn-default-toolbar-medium-ml {
    padding-left: 3px
}

.x-btn-default-toolbar-medium-tc {
    height: 3px
}

.x-btn-default-toolbar-medium-bc {
    height: 3px
}

.x-btn-default-toolbar-medium-mc {
    padding: 1px 1px 1px 1px
}

.x-cmd-slicer.x-btn-default-toolbar-medium:before {
    display: none;
    content: "x-slicer:, frame:3px 3px 3px 3px" !important
}

.x-btn-default-toolbar-medium {
    border-color: transparent
}

.x-btn-button-default-toolbar-medium {
    min-height: 24px
}

.x-ie9m .x-btn-button-default-toolbar-medium {
    min-height: auto;
    height: 24px
}

.x-btn-inner-default-toolbar-medium {
    font: normal 11px/16px tahoma, arial, verdana, sans-serif;
    color: #333;
    padding: 0 4px;
    max-width: 100%
}

.x-btn-icon-right > .x-btn-inner-default-toolbar-medium, .x-btn-icon-left > .x-btn-inner-default-toolbar-medium {
    max-width: calc(100% - 24px)
}

.x-ie10p .x-btn-inner-default-toolbar-medium {
    max-width: none
}

.x-btn-icon-el-default-toolbar-medium {
    font-size: 24px;
    height: 24px;
    color: #333;
    line-height: 24px
}

.x-btn-icon-left > .x-btn-icon-el-default-toolbar-medium, .x-btn-icon-right > .x-btn-icon-el-default-toolbar-medium {
    width: 24px
}

.x-btn-icon-top > .x-btn-icon-el-default-toolbar-medium, .x-btn-icon-bottom > .x-btn-icon-el-default-toolbar-medium {
    min-width: 24px
}

.x-btn-icon-el-default-toolbar-medium.x-btn-glyph {
    opacity: 0.5
}

.x-ie8 .x-btn-icon-el-default-toolbar-medium.x-btn-glyph {
    color: #999
}

.x-btn-text.x-btn-icon-left > .x-btn-icon-el-default-toolbar-medium {
    margin-right: 0px
}

.x-btn-text.x-btn-icon-right > .x-btn-icon-el-default-toolbar-medium {
    margin-left: 0px
}

.x-btn-text.x-btn-icon-top > .x-btn-icon-el-default-toolbar-medium {
    margin-bottom: 4px
}

.x-btn-text.x-btn-icon-bottom > .x-btn-icon-el-default-toolbar-medium {
    margin-top: 4px
}

.x-btn-arrow-right > .x-btn-icon.x-btn-no-text.x-btn-button-default-toolbar-medium {
    padding-right: 4px
}

.x-btn-arrow-right > .x-btn-text.x-btn-icon-right > .x-btn-icon-el-default-toolbar-medium {
    margin-right: 4px
}

.x-btn-arrow-bottom > .x-btn-button-default-toolbar-medium, .x-btn-split-bottom > .x-btn-button-default-toolbar-medium {
    padding-bottom: 3px
}

.x-btn-wrap-default-toolbar-medium.x-btn-arrow-right:after {
    width: 8px;
    background-image: url("data:image/gif;R0lGODlhCgAKAIcAAAAAAP///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAAEALAAAAAAKAAoAAAgZAAMIHEiwoMGDCA0CWLhQYcODABJKnFgwIAA7");
    padding-right: 8px
}

.x-btn-wrap-default-toolbar-medium.x-btn-arrow-bottom:after {
    height: 8px;
    background-image: url("data:image/gif;R0lGODlhCgAKAIcAAAAAAP///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAAEALAAAAAAKAAoAAAgZAAMIHEiwoMGDCA0CWLhQYcODABJKnFgwIAA7")
}

.x-btn-wrap-default-toolbar-medium.x-btn-split-right:after {
    width: 14px;
    background-image: url("data:image/gif;R0lGODlhDgBIAIcAAAAAAMnJycLa9vX19QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAMAAAIALAAAAAAOAEgAAAg8AAUIHEiwoMGDCBMqXMiwocOHECNKnEixosWLGDNq3Mixo8ePAEKGVCiSIYCPKFOqXMmypcuXMGPKnBkQADs=");
    padding-right: 14px
}

.x-btn-wrap-default-toolbar-medium.x-btn-split-bottom:after {
    height: 14px;
    background-image: url("data:image/gif;R0lGODlhyAAOAIcAAAAAAMTExMLa9v///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAMAAAIALAAAAADIAA4AAAhfAAUIHEiwoMGDCBMqXMiwocOHECNKnEixosWLGDNq3Mixo8ePIEOKHEmypMmTKFOqXMmypcuXMGPKnEmzpk2GAHLmvMmzJ0edPoMKrQhgqNGjSJMqXcq0qdOnUKN2DAgAOw==")
}

.x-btn-over > .x-btn-wrap-default-toolbar-medium.x-btn-split-right:after {
    background-image: url("data:image/gif;R0lGODlhDgBIAMIEAAAAAKrI8cLa9tru/////////////////yH5BAEKAAIALAAAAAAOAEgAAANcGCPczupJEaerFq6sefdYFlrjVErnk14btzbv57YiTdomjuoqz3oUH0woqwFjwSMxCVoinzSAVDp8TH/WnnLb5M68xq74Ow6Tz+b0Dbwut9FvdY49d9fhd/kOmAAAOw==")
}

.x-btn-over > .x-btn-wrap-default-toolbar-medium.x-btn-split-bottom:after {
    background-image: url("data:image/gif;R0lGODlhyAAOAKEDAAAAAKrI8e/4/////yH5BAEKAAMALAAAAADIAA4AAAJbjI+py+0Po5y02uuE3rz7D4biSJbmiabqKg7uC8fyTNf2jef6zvf+DwwKh8Si8YhMKpfMpvMJjUqn1Kr1is1qeYBudwsOi13esflsBaDX7Lb7DY/L5/S6/X4uAAA7")
}

.x-btn-split-right > .x-btn-icon.x-btn-no-text.x-btn-button-default-toolbar-medium {
    padding-right: 4px
}

.x-btn-split-right > .x-btn-text.x-btn-icon-right > .x-btn-icon-el-default-toolbar-medium {
    margin-right: 4px
}

.x-btn-focus.x-btn-default-toolbar-medium {
    background-image: none;
    background-color: transparent
}

.x-btn-focus.x-btn-default-toolbar-medium .x-btn-wrap {
    outline: 1px dotted #333
}

.x-btn-default-toolbar-medium .x-btn-arrow-el {
    position: absolute;
    top: 0;
    right: 0;
    height: 100%;
    width: 17px;
    pointer-events: none
}

.x-btn-over.x-btn-default-toolbar-medium {
    border-color: #81a4d0;
    background-image: none;
    background-color: #dbeeff;
    background-image: -webkit-gradient(linear, top, bottom, color-stop(0%, #dbeeff), color-stop(48%, #d0e7ff), color-stop(52%, #bbd2f0), color-stop(0%, #bed6f5));
    background-image: -webkit-linear-gradient(top, #dbeeff, #d0e7ff 48%, #bbd2f0 52%, #bed6f5);
    background-image: -moz-linear-gradient(top, #dbeeff, #d0e7ff 48%, #bbd2f0 52%, #bed6f5);
    background-image: -o-linear-gradient(top, #dbeeff, #d0e7ff 48%, #bbd2f0 52%, #bed6f5);
    background-image: -ms-linear-gradient(top, #dbeeff, #d0e7ff 48%, #bbd2f0 52%, #bed6f5);
    background-image: linear-gradient(top, #dbeeff, #d0e7ff 48%, #bbd2f0 52%, #bed6f5)
}

.x-btn.x-btn-menu-active.x-btn-default-toolbar-medium, .x-btn.x-btn-pressed.x-btn-default-toolbar-medium {
    border-color: #7a9ac4;
    background-image: none;
    background-color: #bccfe5;
    background-image: -webkit-gradient(linear, top, bottom, color-stop(0%, #bccfe5), color-stop(48%, #c5d6e7), color-stop(52%, #95c4f4), color-stop(0%, #9fc9f5));
    background-image: -webkit-linear-gradient(top, #bccfe5, #c5d6e7 48%, #95c4f4 52%, #9fc9f5);
    background-image: -moz-linear-gradient(top, #bccfe5, #c5d6e7 48%, #95c4f4 52%, #9fc9f5);
    background-image: -o-linear-gradient(top, #bccfe5, #c5d6e7 48%, #95c4f4 52%, #9fc9f5);
    background-image: -ms-linear-gradient(top, #bccfe5, #c5d6e7 48%, #95c4f4 52%, #9fc9f5);
    background-image: linear-gradient(top, #bccfe5, #c5d6e7 48%, #95c4f4 52%, #9fc9f5)
}

.x-btn.x-btn-disabled.x-btn-default-toolbar-medium {
    border-color: #e1e1e1;
    background-image: none;
    background-color: transparent
}

.x-btn.x-btn-disabled.x-btn-default-toolbar-medium .x-btn-inner {
    color: #8c8c8c
}

.x-btn-focus .x-btn-default-toolbar-medium-tl, .x-btn-focus .x-btn-default-toolbar-medium-bl, .x-btn-focus .x-btn-default-toolbar-medium-tr, .x-btn-focus .x-btn-default-toolbar-medium-br, .x-btn-focus .x-btn-default-toolbar-medium-tc, .x-btn-focus .x-btn-default-toolbar-medium-bc {
    background-image: url(images/btn/btn-default-toolbar-medium-focus-corners.gif)
}

.x-btn-focus .x-btn-default-toolbar-medium-ml, .x-btn-focus .x-btn-default-toolbar-medium-mr {
    background-image: url(images/btn/btn-default-toolbar-medium-focus-sides.gif)
}

.x-btn-focus .x-btn-default-toolbar-medium-mc {
    background-color: transparent;
    background-image: url(images/btn/btn-default-toolbar-medium-focus-fbg.gif)
}

.x-btn-over .x-btn-default-toolbar-medium-tl, .x-btn-over .x-btn-default-toolbar-medium-bl, .x-btn-over .x-btn-default-toolbar-medium-tr, .x-btn-over .x-btn-default-toolbar-medium-br, .x-btn-over .x-btn-default-toolbar-medium-tc, .x-btn-over .x-btn-default-toolbar-medium-bc {
    background-image: url("data:image/gif;R0lGODlhAwASAPMAAIGk0Iys1I2s1JOy25y63rjR8brN5r3V9NHn+9Ln+9nt/9rt/////wAAAIGk0IGk0CH5BAEAAAwALAAAAAADABIAQwg0AAEIDIBAQYEBBg4oDFDggIKHDAwESEDAQEQBCzIqPCAQgAECCQJYVIBAgIEBDQsIMMkgIAA7")
}

.x-btn-over .x-btn-default-toolbar-medium-ml, .x-btn-over .x-btn-default-toolbar-medium-mr {
    background-image: url("data:image/gif;R0lGODlhBgAgA/QAAIGk0LvS8LvS8bvT8bzT8bzT8rzU8rzU873U873V873V9M7l/dDn/9Hn/9Lo/9Pp/9Tp/9Xq/9bq/9br/9fr/9js/9ns/////4Gk0IGk0IGk0IGk0IGk0IGk0IGk0IGk0CH5BAEAABcALAAAAAAGACADRAj/AAFYGGgBAAAHCB0YFMBQgMEEEBMYVEBRwcSKFylmtAigIkePG0N2xDhSY8mPJEGeFKmyZcqXJl3GhIlyps2aOFnS1HmTZ86VQGX+FOqzaNCdR3smHYqU6FKjTqM2napUalWqTK9qzcoVKkkJYCUYXEB2gcECaAt43bq269O3Vt3GbUsXLta6c+2y1Sv3Ll+8fvMKDkx472DDhfsiXuyWgmMKBiFIhmCwgeUGBgNoDmCQgGcCBg+IPgCYcWnFqE+r/sv6cOrWiVe7lh0btmnbr2fjpn1bt+/av3sDHy68eG7ix43zTs58ufPd0IM3j45cZIXrFQxO2D7BYITvEQw+eBj/wGBChQAYqGfQ+XPmzQYHyB9wNq1BA/gNGETAH8Fz6f9VR51yA04HYIEBEnjgggIyqGCDED4ooYERUjhhghZmiOGGCHbooIYeVsjhhyOKGOKFJ4JIYoolorjiiybC6GKMNM5oo4o14nhjizr2yOOPLAYpY2oBAQA7")
}

.x-btn-over .x-btn-default-toolbar-medium-mc {
    background-color: #dbeeff;
    background-image: url("data:image/gif;R0lGODlhAQAgA/QAALvS8LvS8bvT8bzT8bzT8rzU8rzU873U873V873V9M7l/dDn/9Hn/9Lo/9Pp/9Tp/9Xq/9bq/9br/9fr/9js/9ns/////7vS8LvS8LvS8LvS8LvS8LvS8LvS8LvS8LvS8CH5BAEAABYALAAAAAABACADRAhNACs0CIAggcGDCBMqXMiwocOHECMmjKCAgMSLGDNqzDjhAQMAAwxsHEmypMmTKFNKpCABgoMGCwYAEECgwAGVOHPq3Mmzp8+fQIMCDQgAOw==")
}

.x-btn-focus.x-btn-over .x-btn-default-toolbar-medium-tl, .x-btn-focus.x-btn-over .x-btn-default-toolbar-medium-bl, .x-btn-focus.x-btn-over .x-btn-default-toolbar-medium-tr, .x-btn-focus.x-btn-over .x-btn-default-toolbar-medium-br, .x-btn-focus.x-btn-over .x-btn-default-toolbar-medium-tc, .x-btn-focus.x-btn-over .x-btn-default-toolbar-medium-bc {
    background-image: url("data:image/gif;R0lGODlhAwASAPMAAIGk0Iys1I2s1JOy25y63rjR8brN5r3V9NHn+9Ln+9nt/9rt/////wAAAIGk0IGk0CH5BAEAAAwALAAAAAADABIAQwg0AAEIDIBAQYEBBg4oDFDggIKHDAwESEDAQEQBCzIqPCAQgAECCQJYVIBAgIEBDQsIMMkgIAA7")
}

.x-btn-focus.x-btn-over .x-btn-default-toolbar-medium-ml, .x-btn-focus.x-btn-over .x-btn-default-toolbar-medium-mr {
    background-image: url("data:image/gif;R0lGODlhBgAgA/QAAIGk0LvS8LvS8bvT8bzT8bzT8rzU8rzU873U873V873V9M7l/dDn/9Hn/9Lo/9Pp/9Tp/9Xq/9bq/9br/9fr/9js/9ns/////4Gk0IGk0IGk0IGk0IGk0IGk0IGk0IGk0CH5BAEAABcALAAAAAAGACADRAj/AAFYGGgBAAAHCB0YFMBQgMEEEBMYVEBRwcSKFylmtAigIkePG0N2xDhSY8mPJEGeFKmyZcqXJl3GhIlyps2aOFnS1HmTZ86VQGX+FOqzaNCdR3smHYqU6FKjTqM2napUalWqTK9qzcoVKkkJYCUYXEB2gcECaAt43bq269O3Vt3GbUsXLta6c+2y1Sv3Ll+8fvMKDkx472DDhfsiXuyWgmMKBiFIhmCwgeUGBgNoDmCQgGcCBg+IPgCYcWnFqE+r/sv6cOrWiVe7lh0btmnbr2fjpn1bt+/av3sDHy68eG7ix43zTs58ufPd0IM3j45cZIXrFQxO2D7BYITvEQw+eBj/wGBChQAYqGfQ+XPmzQYHyB9wNq1BA/gNGETAH8Fz6f9VR51yA04HYIEBEnjgggIyqGCDED4ooYERUjhhghZmiOGGCHbooIYeVsjhhyOKGOKFJ4JIYoolorjiiybC6GKMNM5oo4o14nhjizr2yOOPLAYpY2oBAQA7")
}

.x-btn-focus.x-btn-over .x-btn-default-toolbar-medium-mc {
    background-color: #dbeeff;
    background-image: url("data:image/gif;R0lGODlhAQAgA/QAALvS8LvS8bvT8bzT8bzT8rzU8rzU873U873V873V9M7l/dDn/9Hn/9Lo/9Pp/9Tp/9Xq/9bq/9br/9fr/9js/9ns/////7vS8LvS8LvS8LvS8LvS8LvS8LvS8LvS8LvS8CH5BAEAABYALAAAAAABACADRAhNACs0CIAggcGDCBMqXMiwocOHECMmjKCAgMSLGDNqzDjhAQMAAwxsHEmypMmTKFNKpCABgoMGCwYAEECgwAGVOHPq3Mmzp8+fQIMCDQgAOw==")
}

.x-btn.x-btn-menu-active .x-btn-default-toolbar-medium-tl, .x-btn.x-btn-menu-active .x-btn-default-toolbar-medium-bl, .x-btn.x-btn-menu-active .x-btn-default-toolbar-medium-tr, .x-btn.x-btn-menu-active .x-btn-default-toolbar-medium-br, .x-btn.x-btn-menu-active .x-btn-default-toolbar-medium-tc, .x-btn.x-btn-menu-active .x-btn-default-toolbar-medium-bc, .x-btn.x-btn-pressed .x-btn-default-toolbar-medium-tl, .x-btn.x-btn-pressed .x-btn-default-toolbar-medium-bl, .x-btn.x-btn-pressed .x-btn-default-toolbar-medium-tr, .x-btn.x-btn-pressed .x-btn-default-toolbar-medium-br, .x-btn.x-btn-pressed .x-btn-default-toolbar-medium-tc, .x-btn.x-btn-pressed .x-btn-default-toolbar-medium-bc {
    background-image: url("data:image/gif;R0lGODlhAwASAPMAAHqaxIWo04ejyYekyY6qzprE8JvE8J3I9J7I9LbK4rfH37zP5f///wAAAHqaxHqaxCH5BAEAAAwALAAAAAADABIAQwg0AAEIHJBggYEAChAoHFDgwIKHDBQQJKAgooCHCw5oFAhAAYEEAyouSCBAQQADBwoIKMkgIAA7")
}

.x-btn.x-btn-menu-active .x-btn-default-toolbar-medium-ml, .x-btn.x-btn-menu-active .x-btn-default-toolbar-medium-mr, .x-btn.x-btn-pressed .x-btn-default-toolbar-medium-ml, .x-btn.x-btn-pressed .x-btn-default-toolbar-medium-mr {
    background-image: url("data:image/gif;R0lGODlhBgAgA/QAAHqaxJXE9JbE9JfF9JjF85jF9JnG9JrG9JvH9JzH9J3I9L3Q5b7Q5b7R5b/R5cDS5cDS5sHT5sHU58LU5sPU5sPV5sTV5v///3qaxHqaxHqaxHqaxHqaxHqaxHqaxHqaxCH5BAEAABcALAAAAAAGACADRAj/AAEsGLgAAIAJCCcYHMBwgMEEEBMYVEBRwcSKFylmtAigIkePG0N2xDhSY8mPJEGeFKmyZcqXJl3GhIlyps2aOFnS1HmTZ86VQGX+FOqzaNCdR3smHYqU6FKjTqM2napUalWqTK9qzcoVKskHYB8YlEBWgkEDaA143bq269O3Vt3GbUsXLta6c+2y1Sv3Ll+8fvMKDkx472DDhfsiXuy2geMGBiNIjmCwguUKBgNoDmCwgOcCBhGIRgCYcWnFqE+r/sv6cOrWiVe7lh0btmnbr2fjpn1bt+/av3sDHy68eG7ix43zTs58ufPd0IM3j45cJIPrDAw62O7AIITvECJPdjZIoTwFgxbSWzBIoD0BgwLiC1jY8GxagwfyHwg9+rl0/9VRp5yA0/1HIIADGqhggAsmyOCDDkZYIIQTSohghRheqOGBHDaYYYcUbuihiCGCaKGJH46IIoknquhiiS+2COOMMtaYIo032shijjzu6OOKQMaYWkAAOw==")
}

.x-btn.x-btn-menu-active .x-btn-default-toolbar-medium-mc, .x-btn.x-btn-pressed .x-btn-default-toolbar-medium-mc {
    background-color: #bccfe5;
    background-image: url("data:image/gif;R0lGODlhAQAgA/QAAJXE9JbE9JfF9JjF85jF9JnG9JrG9JvH9JzH9J3I9L3Q5b7Q5b7R5b/R5cDS5cDS5sHT5sHU58LU5sPU5sPV5sTV5v///5XE9JXE9JXE9JXE9JXE9JXE9JXE9JXE9JXE9CH5BAEAABYALAAAAAABACADRAhNABVIEIAggcGDCBMqXMiwocOHECMmdBChgMSLGDNqzMgAAgUABA5sHEmypMmTKFNKXNDgAYQJFQYEEFDAgEiVOHPq3Mmzp8+fQIP+DAgAOw==")
}

.x-btn-focus.x-btn-menu-active .x-btn-default-toolbar-medium-tl, .x-btn-focus.x-btn-menu-active .x-btn-default-toolbar-medium-bl, .x-btn-focus.x-btn-menu-active .x-btn-default-toolbar-medium-tr, .x-btn-focus.x-btn-menu-active .x-btn-default-toolbar-medium-br, .x-btn-focus.x-btn-menu-active .x-btn-default-toolbar-medium-tc, .x-btn-focus.x-btn-menu-active .x-btn-default-toolbar-medium-bc, .x-btn-focus.x-btn-pressed .x-btn-default-toolbar-medium-tl, .x-btn-focus.x-btn-pressed .x-btn-default-toolbar-medium-bl, .x-btn-focus.x-btn-pressed .x-btn-default-toolbar-medium-tr, .x-btn-focus.x-btn-pressed .x-btn-default-toolbar-medium-br, .x-btn-focus.x-btn-pressed .x-btn-default-toolbar-medium-tc, .x-btn-focus.x-btn-pressed .x-btn-default-toolbar-medium-bc {
    background-image: url("data:image/gif;R0lGODlhAwASAPMAAHqaxIWo04ejyYekyY6qzprE8JvE8J3I9J7I9LbK4rfH37zP5f///wAAAHqaxHqaxCH5BAEAAAwALAAAAAADABIAQwg0AAEIHJBggYEAChAoHFDgwIKHDBQQJKAgooCHCw5oFAhAAYEEAyouSCBAQQADBwoIKMkgIAA7")
}

.x-btn-focus.x-btn-menu-active .x-btn-default-toolbar-medium-ml, .x-btn-focus.x-btn-menu-active .x-btn-default-toolbar-medium-mr, .x-btn-focus.x-btn-pressed .x-btn-default-toolbar-medium-ml, .x-btn-focus.x-btn-pressed .x-btn-default-toolbar-medium-mr {
    background-image: url("data:image/gif;R0lGODlhBgAgA/QAAHqaxJXE9JbE9JfF9JjF85jF9JnG9JrG9JvH9JzH9J3I9L3Q5b7Q5b7R5b/R5cDS5cDS5sHT5sHU58LU5sPU5sPV5sTV5v///3qaxHqaxHqaxHqaxHqaxHqaxHqaxHqaxCH5BAEAABcALAAAAAAGACADRAj/AAEsGLgAAIAJCCcYHMBwgMEEEBMYVEBRwcSKFylmtAigIkePG0N2xDhSY8mPJEGeFKmyZcqXJl3GhIlyps2aOFnS1HmTZ86VQGX+FOqzaNCdR3smHYqU6FKjTqM2napUalWqTK9qzcoVKskHYB8YlEBWgkEDaA143bq269O3Vt3GbUsXLta6c+2y1Sv3Ll+8fvMKDkx472DDhfsiXuy2geMGBiNIjmCwguUKBgNoDmCwgOcCBhGIRgCYcWnFqE+r/sv6cOrWiVe7lh0btmnbr2fjpn1bt+/av3sDHy68eG7ix43zTs58ufPd0IM3j45cJIPrDAw62O7AIITvECJPdjZIoTwFgxbSWzBIoD0BgwLiC1jY8GxagwfyHwg9+rl0/9VRp5yA0/1HIIADGqhggAsmyOCDDkZYIIQTSohghRheqOGBHDaYYYcUbuihiCGCaKGJH46IIoknquhiiS+2COOMMtaYIo032shijjzu6OOKQMaYWkAAOw==")
}

.x-btn-focus.x-btn-menu-active .x-btn-default-toolbar-medium-mc, .x-btn-focus.x-btn-pressed .x-btn-default-toolbar-medium-mc {
    background-color: #bccfe5;
    background-image: url("data:image/gif;R0lGODlhAQAgA/QAAJXE9JbE9JfF9JjF85jF9JnG9JrG9JvH9JzH9J3I9L3Q5b7Q5b7R5b/R5cDS5cDS5sHT5sHU58LU5sPU5sPV5sTV5v///5XE9JXE9JXE9JXE9JXE9JXE9JXE9JXE9JXE9CH5BAEAABYALAAAAAABACADRAhNABVIEIAggcGDCBMqXMiwocOHECMmdBChgMSLGDNqzMgAAgUABA5sHEmypMmTKFNKXNDgAYQJFQYEEFDAgEiVOHPq3Mmzp8+fQIP+DAgAOw==")
}

.x-btn.x-btn-disabled .x-btn-default-toolbar-medium-tl, .x-btn.x-btn-disabled .x-btn-default-toolbar-medium-bl, .x-btn.x-btn-disabled .x-btn-default-toolbar-medium-tr, .x-btn.x-btn-disabled .x-btn-default-toolbar-medium-br, .x-btn.x-btn-disabled .x-btn-default-toolbar-medium-tc, .x-btn.x-btn-disabled .x-btn-default-toolbar-medium-bc {
    background-image: url("data:image/gif;R0lGODlhAwASAPIAAPDw8PHx8fT09Pb29v///wAAAPDw8PDw8CH5BAEAAAQALAAAAAADABIAQggnAAEIDECgoIABBQkQTFhwAMGDBBwyLCgQwAABChEWDHAxYQCOBAICADs=")
}

.x-btn.x-btn-disabled .x-btn-default-toolbar-medium-ml, .x-btn.x-btn-disabled .x-btn-default-toolbar-medium-mr {
    background-image: url("data:image/gif;R0lGODlhBgAgA/EAAPDw8P///wAAAPDw8CH5BAEAAAEALAAAAAAGACADQQj/AAEEGBgAgECCBgkWPDgwIUKGCxU6bAhxYsSHEitqzMgRo0eKHUF+vCiyJMmTFlNuHKkyJMqVJluyhPnSpcyYNG/WnGkzp8+eQHkKxRmU6NCdRpMiXaqz6c+jTosyfao0KlSqU6VarYp1a9arWruKDUsWrFmuZdGe/aq2Ldu3XuOOXSs3Ldy5buvSxXvXrt68fP/23es3sOHCiAkrBpyY8eLBjiNDniy48uHHlhtTviw5M2bOmzV77gx6dOjPokurTs0atWvSrWG/Pi27Nu3bpnOvnq07Nu7dtnvzBv7bt/DgxI8XH248ufPm0JlLRx6d+vTl1rNj3668+/Pr3qtzDP+uPTx48uPFm28YEAA7")
}

.x-btn.x-btn-disabled .x-btn-default-toolbar-medium-mc {
    background-color: transparent;
    background-image: url("data:image/gif;R0lGODlhAQAgA/AAAP///wAAACH5BAEAAAAALAAAAAABACADQAgwAAEIHEiwoMGDCBMqXMiwocOHECNKnEixosWLGDNq3Mixo8ePIEOKHEmypMmTFAMCADs=")
}

.x-nbr .x-btn-default-toolbar-medium {
    background-image: none
}

.x-btn-disabled.x-btn-default-toolbar-medium {
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=50)";
    opacity: 0.5
}

.x-nbr .x-segmented-button-item-horizontal.x-btn-default-toolbar-medium.x-segmented-button-first {
    border-right-width: 1px !important
}

.x-nbr .x-segmented-button-item-horizontal.x-btn-default-toolbar-medium.x-segmented-button-first .x-btn-default-toolbar-medium-mc {
    padding-right: 3px !important
}

.x-nbr .x-segmented-button-item-horizontal.x-btn-default-toolbar-medium.x-segmented-button-middle {
    border-right-width: 1px !important
}

.x-nbr .x-segmented-button-item-horizontal.x-btn-default-toolbar-medium.x-segmented-button-middle .x-btn-default-toolbar-medium-mc {
    padding-right: 3px !important;
    padding-left: 3px !important
}

.x-nbr .x-segmented-button-item-horizontal.x-btn-default-toolbar-medium.x-segmented-button-last .x-btn-default-toolbar-medium-mc {
    padding-left: 3px !important
}

.x-nbr .x-segmented-button-item-vertical.x-btn-default-toolbar-medium.x-segmented-button-first {
    border-bottom-width: 1px !important
}

.x-nbr .x-segmented-button-item-vertical.x-btn-default-toolbar-medium.x-segmented-button-first .x-btn-default-toolbar-medium-mc {
    padding-bottom: 3px !important
}

.x-nbr .x-segmented-button-item-vertical.x-btn-default-toolbar-medium.x-segmented-button-middle {
    border-bottom-width: 1px !important
}

.x-nbr .x-segmented-button-item-vertical.x-btn-default-toolbar-medium.x-segmented-button-middle .x-btn-default-toolbar-medium-mc {
    padding-top: 3px !important;
    padding-bottom: 3px !important
}

.x-nbr .x-segmented-button-item-vertical.x-btn-default-toolbar-medium.x-segmented-button-last .x-btn-default-toolbar-medium-mc {
    padding-top: 3px !important
}

.x-nbr .x-segmented-button-item.x-btn-default-toolbar-medium:after {
    content: ' ';
    border-style: solid;
    border-width: 0;
    position: absolute
}

.x-nbr .x-segmented-button-item-horizontal.x-btn-default-toolbar-medium:after {
    top: 1px;
    right: 0;
    bottom: 1px;
    left: 0
}

.x-nbr .x-segmented-button-item-horizontal.x-btn-default-toolbar-medium.x-segmented-button-first:after {
    left: 1px
}

.x-nbr .x-segmented-button-item-horizontal.x-btn-default-toolbar-medium.x-segmented-button-last:after {
    right: 1px
}

.x-nbr .x-segmented-button-item-vertical.x-btn-default-toolbar-medium:after {
    top: 0;
    right: 1px;
    bottom: 0;
    left: 1px
}

.x-nbr .x-segmented-button-item-vertical.x-btn-default-toolbar-medium.x-segmented-button-first:after {
    top: 1px
}

.x-nbr .x-segmented-button-item-vertical.x-btn-default-toolbar-medium.x-segmented-button-last:after {
    bottom: 1px
}

.x-cmd-slicer.x-btn-focus.x-btn-default-toolbar-medium:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url(images/btn/btn-default-toolbar-medium-focus-corners.gif), sides:url(images/btn/btn-default-toolbar-medium-focus-sides.gif), frame-bg:url(images/btn/btn-default-toolbar-medium-focus-fbg.gif)" !important
}

.x-cmd-slicer.x-btn-over.x-btn-default-toolbar-medium:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url("data:image/gif;R0lGODlhAwASAPMAAIGk0Iys1I2s1JOy25y63rjR8brN5r3V9NHn+9Ln+9nt/9rt/////wAAAIGk0IGk0CH5BAEAAAwALAAAAAADABIAQwg0AAEIDIBAQYEBBg4oDFDggIKHDAwESEDAQEQBCzIqPCAQgAECCQJYVIBAgIEBDQsIMMkgIAA7"), sides:url("data:image/gif;R0lGODlhBgAgA/QAAIGk0LvS8LvS8bvT8bzT8bzT8rzU8rzU873U873V873V9M7l/dDn/9Hn/9Lo/9Pp/9Tp/9Xq/9bq/9br/9fr/9js/9ns/////4Gk0IGk0IGk0IGk0IGk0IGk0IGk0IGk0CH5BAEAABcALAAAAAAGACADRAj/AAFYGGgBAAAHCB0YFMBQgMEEEBMYVEBRwcSKFylmtAigIkePG0N2xDhSY8mPJEGeFKmyZcqXJl3GhIlyps2aOFnS1HmTZ86VQGX+FOqzaNCdR3smHYqU6FKjTqM2napUalWqTK9qzcoVKkkJYCUYXEB2gcECaAt43bq269O3Vt3GbUsXLta6c+2y1Sv3Ll+8fvMKDkx472DDhfsiXuyWgmMKBiFIhmCwgeUGBgNoDmCQgGcCBg+IPgCYcWnFqE+r/sv6cOrWiVe7lh0btmnbr2fjpn1bt+/av3sDHy68eG7ix43zTs58ufPd0IM3j45cZIXrFQxO2D7BYITvEQw+eBj/wGBChQAYqGfQ+XPmzQYHyB9wNq1BA/gNGETAH8Fz6f9VR51yA04HYIEBEnjgggIyqGCDED4ooYERUjhhghZmiOGGCHbooIYeVsjhhyOKGOKFJ4JIYoolorjiiybC6GKMNM5oo4o14nhjizr2yOOPLAYpY2oBAQA7"), frame-bg:url("data:image/gif;R0lGODlhAQAgA/QAALvS8LvS8bvT8bzT8bzT8rzU8rzU873U873V873V9M7l/dDn/9Hn/9Lo/9Pp/9Tp/9Xq/9bq/9br/9fr/9js/9ns/////7vS8LvS8LvS8LvS8LvS8LvS8LvS8LvS8LvS8CH5BAEAABYALAAAAAABACADRAhNACs0CIAggcGDCBMqXMiwocOHECMmjKCAgMSLGDNqzDjhAQMAAwxsHEmypMmTKFNKpCABgoMGCwYAEECgwAGVOHPq3Mmzp8+fQIMCDQgAOw==")" !important
}

.x-cmd-slicer.x-btn-focus.x-btn-over.x-btn-default-toolbar-medium:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url("data:image/gif;R0lGODlhAwASAPMAAIGk0Iys1I2s1JOy25y63rjR8brN5r3V9NHn+9Ln+9nt/9rt/////wAAAIGk0IGk0CH5BAEAAAwALAAAAAADABIAQwg0AAEIDIBAQYEBBg4oDFDggIKHDAwESEDAQEQBCzIqPCAQgAECCQJYVIBAgIEBDQsIMMkgIAA7"), sides:url("data:image/gif;R0lGODlhBgAgA/QAAIGk0LvS8LvS8bvT8bzT8bzT8rzU8rzU873U873V873V9M7l/dDn/9Hn/9Lo/9Pp/9Tp/9Xq/9bq/9br/9fr/9js/9ns/////4Gk0IGk0IGk0IGk0IGk0IGk0IGk0IGk0CH5BAEAABcALAAAAAAGACADRAj/AAFYGGgBAAAHCB0YFMBQgMEEEBMYVEBRwcSKFylmtAigIkePG0N2xDhSY8mPJEGeFKmyZcqXJl3GhIlyps2aOFnS1HmTZ86VQGX+FOqzaNCdR3smHYqU6FKjTqM2napUalWqTK9qzcoVKkkJYCUYXEB2gcECaAt43bq269O3Vt3GbUsXLta6c+2y1Sv3Ll+8fvMKDkx472DDhfsiXuyWgmMKBiFIhmCwgeUGBgNoDmCQgGcCBg+IPgCYcWnFqE+r/sv6cOrWiVe7lh0btmnbr2fjpn1bt+/av3sDHy68eG7ix43zTs58ufPd0IM3j45cZIXrFQxO2D7BYITvEQw+eBj/wGBChQAYqGfQ+XPmzQYHyB9wNq1BA/gNGETAH8Fz6f9VR51yA04HYIEBEnjgggIyqGCDED4ooYERUjhhghZmiOGGCHbooIYeVsjhhyOKGOKFJ4JIYoolorjiiybC6GKMNM5oo4o14nhjizr2yOOPLAYpY2oBAQA7"), frame-bg:url("data:image/gif;R0lGODlhAQAgA/QAALvS8LvS8bvT8bzT8bzT8rzU8rzU873U873V873V9M7l/dDn/9Hn/9Lo/9Pp/9Tp/9Xq/9bq/9br/9fr/9js/9ns/////7vS8LvS8LvS8LvS8LvS8LvS8LvS8LvS8LvS8CH5BAEAABYALAAAAAABACADRAhNACs0CIAggcGDCBMqXMiwocOHECMmjKCAgMSLGDNqzDjhAQMAAwxsHEmypMmTKFNKpCABgoMGCwYAEECgwAGVOHPq3Mmzp8+fQIMCDQgAOw==")" !important
}

.x-cmd-slicer.x-btn-pressed.x-btn-default-toolbar-medium:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url("data:image/gif;R0lGODlhAwASAPMAAHqaxIWo04ejyYekyY6qzprE8JvE8J3I9J7I9LbK4rfH37zP5f///wAAAHqaxHqaxCH5BAEAAAwALAAAAAADABIAQwg0AAEIHJBggYEAChAoHFDgwIKHDBQQJKAgooCHCw5oFAhAAYEEAyouSCBAQQADBwoIKMkgIAA7"), sides:url("data:image/gif;R0lGODlhBgAgA/QAAHqaxJXE9JbE9JfF9JjF85jF9JnG9JrG9JvH9JzH9J3I9L3Q5b7Q5b7R5b/R5cDS5cDS5sHT5sHU58LU5sPU5sPV5sTV5v///3qaxHqaxHqaxHqaxHqaxHqaxHqaxHqaxCH5BAEAABcALAAAAAAGACADRAj/AAEsGLgAAIAJCCcYHMBwgMEEEBMYVEBRwcSKFylmtAigIkePG0N2xDhSY8mPJEGeFKmyZcqXJl3GhIlyps2aOFnS1HmTZ86VQGX+FOqzaNCdR3smHYqU6FKjTqM2napUalWqTK9qzcoVKskHYB8YlEBWgkEDaA143bq269O3Vt3GbUsXLta6c+2y1Sv3Ll+8fvMKDkx472DDhfsiXuy2geMGBiNIjmCwguUKBgNoDmCwgOcCBhGIRgCYcWnFqE+r/sv6cOrWiVe7lh0btmnbr2fjpn1bt+/av3sDHy68eG7ix43zTs58ufPd0IM3j45cJIPrDAw62O7AIITvECJPdjZIoTwFgxbSWzBIoD0BgwLiC1jY8GxagwfyHwg9+rl0/9VRp5yA0/1HIIADGqhggAsmyOCDDkZYIIQTSohghRheqOGBHDaYYYcUbuihiCGCaKGJH46IIoknquhiiS+2COOMMtaYIo032shijjzu6OOKQMaYWkAAOw=="), frame-bg:url("data:image/gif;R0lGODlhAQAgA/QAAJXE9JbE9JfF9JjF85jF9JnG9JrG9JvH9JzH9J3I9L3Q5b7Q5b7R5b/R5cDS5cDS5sHT5sHU58LU5sPU5sPV5sTV5v///5XE9JXE9JXE9JXE9JXE9JXE9JXE9JXE9JXE9CH5BAEAABYALAAAAAABACADRAhNABVIEIAggcGDCBMqXMiwocOHECMmdBChgMSLGDNqzMgAAgUABA5sHEmypMmTKFNKXNDgAYQJFQYEEFDAgEiVOHPq3Mmzp8+fQIP+DAgAOw==")" !important
}

.x-cmd-slicer.x-btn-focus.x-btn-pressed.x-btn-default-toolbar-medium:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url("data:image/gif;R0lGODlhAwASAPMAAHqaxIWo04ejyYekyY6qzprE8JvE8J3I9J7I9LbK4rfH37zP5f///wAAAHqaxHqaxCH5BAEAAAwALAAAAAADABIAQwg0AAEIHJBggYEAChAoHFDgwIKHDBQQJKAgooCHCw5oFAhAAYEEAyouSCBAQQADBwoIKMkgIAA7"), sides:url("data:image/gif;R0lGODlhBgAgA/QAAHqaxJXE9JbE9JfF9JjF85jF9JnG9JrG9JvH9JzH9J3I9L3Q5b7Q5b7R5b/R5cDS5cDS5sHT5sHU58LU5sPU5sPV5sTV5v///3qaxHqaxHqaxHqaxHqaxHqaxHqaxHqaxCH5BAEAABcALAAAAAAGACADRAj/AAEsGLgAAIAJCCcYHMBwgMEEEBMYVEBRwcSKFylmtAigIkePG0N2xDhSY8mPJEGeFKmyZcqXJl3GhIlyps2aOFnS1HmTZ86VQGX+FOqzaNCdR3smHYqU6FKjTqM2napUalWqTK9qzcoVKskHYB8YlEBWgkEDaA143bq269O3Vt3GbUsXLta6c+2y1Sv3Ll+8fvMKDkx472DDhfsiXuy2geMGBiNIjmCwguUKBgNoDmCwgOcCBhGIRgCYcWnFqE+r/sv6cOrWiVe7lh0btmnbr2fjpn1bt+/av3sDHy68eG7ix43zTs58ufPd0IM3j45cJIPrDAw62O7AIITvECJPdjZIoTwFgxbSWzBIoD0BgwLiC1jY8GxagwfyHwg9+rl0/9VRp5yA0/1HIIADGqhggAsmyOCDDkZYIIQTSohghRheqOGBHDaYYYcUbuihiCGCaKGJH46IIoknquhiiS+2COOMMtaYIo032shijjzu6OOKQMaYWkAAOw=="), frame-bg:url("data:image/gif;R0lGODlhAQAgA/QAAJXE9JbE9JfF9JjF85jF9JnG9JrG9JvH9JzH9J3I9L3Q5b7Q5b7R5b/R5cDS5cDS5sHT5sHU58LU5sPU5sPV5sTV5v///5XE9JXE9JXE9JXE9JXE9JXE9JXE9JXE9JXE9CH5BAEAABYALAAAAAABACADRAhNABVIEIAggcGDCBMqXMiwocOHECMmdBChgMSLGDNqzMgAAgUABA5sHEmypMmTKFNKXNDgAYQJFQYEEFDAgEiVOHPq3Mmzp8+fQIP+DAgAOw==")" !important
}

.x-cmd-slicer.x-btn-disabled.x-btn-default-toolbar-medium:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url("data:image/gif;R0lGODlhAwASAPIAAPDw8PHx8fT09Pb29v///wAAAPDw8PDw8CH5BAEAAAQALAAAAAADABIAQggnAAEIDECgoIABBQkQTFhwAMGDBBwyLCgQwAABChEWDHAxYQCOBAICADs="), sides:url("data:image/gif;R0lGODlhBgAgA/EAAPDw8P///wAAAPDw8CH5BAEAAAEALAAAAAAGACADQQj/AAEEGBgAgECCBgkWPDgwIUKGCxU6bAhxYsSHEitqzMgRo0eKHUF+vCiyJMmTFlNuHKkyJMqVJluyhPnSpcyYNG/WnGkzp8+eQHkKxRmU6NCdRpMiXaqz6c+jTosyfao0KlSqU6VarYp1a9arWruKDUsWrFmuZdGe/aq2Ldu3XuOOXSs3Ldy5buvSxXvXrt68fP/23es3sOHCiAkrBpyY8eLBjiNDniy48uHHlhtTviw5M2bOmzV77gx6dOjPokurTs0atWvSrWG/Pi27Nu3bpnOvnq07Nu7dtnvzBv7bt/DgxI8XH248ufPm0JlLRx6d+vTl1rNj3668+/Pr3qtzDP+uPTx48uPFm28YEAA7"), frame-bg:url("data:image/gif;R0lGODlhAQAgA/AAAP///wAAACH5BAEAAAAALAAAAAABACADQAgwAAEIHEiwoMGDCBMqXMiwocOHECNKnEixosWLGDNq3Mixo8ePIEOKHEmypMmTFAMCADs=")" !important
}

.x-button-default-toolbar-medium-cell > .x-grid-cell-inner {
    padding-top: 0;
    padding-bottom: 0
}

.x-button-default-toolbar-medium-cell > .x-grid-cell-inner > .x-btn-default-toolbar-medium {
    vertical-align: top
}

.x-btn-default-toolbar-large {
    -webkit-border-radius: 3px;
    -moz-border-radius: 3px;
    -ms-border-radius: 3px;
    -o-border-radius: 3px;
    border-radius: 3px;
    padding: 3px 3px 3px 3px;
    border-width: 1px;
    border-style: solid;
    background-color: transparent
}

.x-btn-default-toolbar-large-mc {
    background-color: transparent
}

.x-nbr .x-btn-default-toolbar-large {
    padding: 0 !important;
    border-width: 0 !important;
    -webkit-border-radius: 0px;
    -moz-border-radius: 0px;
    -ms-border-radius: 0px;
    -o-border-radius: 0px;
    border-radius: 0px;
    background-color: transparent !important;
    box-shadow: none !important
}

.x-btn-default-toolbar-large-frameInfo {
    font-family: th-3-3-3-3-1-1-1-1-3-3-3-3
}

.x-btn-default-toolbar-large-tl {
    background-position: 0 -6px
}

.x-btn-default-toolbar-large-tr {
    background-position: right -9px
}

.x-btn-default-toolbar-large-bl {
    background-position: 0 -12px
}

.x-btn-default-toolbar-large-br {
    background-position: right -15px
}

.x-btn-default-toolbar-large-ml {
    background-position: 0 top
}

.x-btn-default-toolbar-large-mr {
    background-position: right top
}

.x-btn-default-toolbar-large-tc {
    background-position: 0 0
}

.x-btn-default-toolbar-large-bc {
    background-position: 0 -3px
}

.x-btn-default-toolbar-large-tr, .x-btn-default-toolbar-large-br, .x-btn-default-toolbar-large-mr {
    padding-right: 3px
}

.x-btn-default-toolbar-large-tl, .x-btn-default-toolbar-large-bl, .x-btn-default-toolbar-large-ml {
    padding-left: 3px
}

.x-btn-default-toolbar-large-tc {
    height: 3px
}

.x-btn-default-toolbar-large-bc {
    height: 3px
}

.x-btn-default-toolbar-large-mc {
    padding: 1px 1px 1px 1px
}

.x-cmd-slicer.x-btn-default-toolbar-large:before {
    display: none;
    content: "x-slicer:, frame:3px 3px 3px 3px" !important
}

.x-btn-default-toolbar-large {
    border-color: transparent
}

.x-btn-button-default-toolbar-large {
    min-height: 32px
}

.x-ie9m .x-btn-button-default-toolbar-large {
    min-height: auto;
    height: 32px
}

.x-btn-inner-default-toolbar-large {
    font: normal 11px/16px tahoma, arial, verdana, sans-serif;
    color: #333;
    padding: 0 4px;
    max-width: 100%
}

.x-btn-icon-right > .x-btn-inner-default-toolbar-large, .x-btn-icon-left > .x-btn-inner-default-toolbar-large {
    max-width: calc(100% - 32px)
}

.x-ie10p .x-btn-inner-default-toolbar-large {
    max-width: none
}

.x-btn-icon-el-default-toolbar-large {
    font-size: 32px;
    height: 32px;
    color: #333;
    line-height: 32px
}

.x-btn-icon-left > .x-btn-icon-el-default-toolbar-large, .x-btn-icon-right > .x-btn-icon-el-default-toolbar-large {
    width: 32px
}

.x-btn-icon-top > .x-btn-icon-el-default-toolbar-large, .x-btn-icon-bottom > .x-btn-icon-el-default-toolbar-large {
    min-width: 32px
}

.x-btn-icon-el-default-toolbar-large.x-btn-glyph {
    opacity: 0.5
}

.x-ie8 .x-btn-icon-el-default-toolbar-large.x-btn-glyph {
    color: #999
}

.x-btn-text.x-btn-icon-left > .x-btn-icon-el-default-toolbar-large {
    margin-right: 0px
}

.x-btn-text.x-btn-icon-right > .x-btn-icon-el-default-toolbar-large {
    margin-left: 0px
}

.x-btn-text.x-btn-icon-top > .x-btn-icon-el-default-toolbar-large {
    margin-bottom: 4px
}

.x-btn-text.x-btn-icon-bottom > .x-btn-icon-el-default-toolbar-large {
    margin-top: 4px
}

.x-btn-arrow-right > .x-btn-icon.x-btn-no-text.x-btn-button-default-toolbar-large {
    padding-right: 4px
}

.x-btn-arrow-right > .x-btn-text.x-btn-icon-right > .x-btn-icon-el-default-toolbar-large {
    margin-right: 4px
}

.x-btn-arrow-bottom > .x-btn-button-default-toolbar-large, .x-btn-split-bottom > .x-btn-button-default-toolbar-large {
    padding-bottom: 3px
}

.x-btn-wrap-default-toolbar-large.x-btn-arrow-right:after {
    width: 8px;
    background-image: url("data:image/gif;R0lGODlhCgAKAIcAAAAAAP///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAAEALAAAAAAKAAoAAAgZAAMIHEiwoMGDCA0CWLhQYcODABJKnFgwIAA7");
    padding-right: 8px
}

.x-btn-wrap-default-toolbar-large.x-btn-arrow-bottom:after {
    height: 8px;
    background-image: url("data:image/gif;R0lGODlhCgAKAIcAAAAAAP///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAAEALAAAAAAKAAoAAAgZAAMIHEiwoMGDCA0CWLhQYcODABJKnFgwIAA7")
}

.x-btn-wrap-default-toolbar-large.x-btn-split-right:after {
    width: 14px;
    background-image: url("data:image/gif;R0lGODlhDgBIAIcAAAAAAMnJycLa9vX19QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAMAAAIALAAAAAAOAEgAAAg8AAUIHEiwoMGDCBMqXMiwocOHECNKnEixosWLGDNq3Mixo8ePAEKGVCiSIYCPKFOqXMmypcuXMGPKnBkQADs=");
    padding-right: 14px
}

.x-btn-wrap-default-toolbar-large.x-btn-split-bottom:after {
    height: 14px;
    background-image: url("data:image/gif;R0lGODlhyAAOAIcAAAAAAMTExMLa9v///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAMAAAIALAAAAADIAA4AAAhfAAUIHEiwoMGDCBMqXMiwocOHECNKnEixosWLGDNq3Mixo8ePIEOKHEmypMmTKFOqXMmypcuXMGPKnEmzpk2GAHLmvMmzJ0edPoMKrQhgqNGjSJMqXcq0qdOnUKN2DAgAOw==")
}

.x-btn-over > .x-btn-wrap-default-toolbar-large.x-btn-split-right:after {
    background-image: url("data:image/gif;R0lGODlhDgBIAMIEAAAAAKrI8cLa9tru/////////////////yH5BAEKAAIALAAAAAAOAEgAAANcGCPczupJEaerFq6sefdYFlrjVErnk14btzbv57YiTdomjuoqz3oUH0woqwFjwSMxCVoinzSAVDp8TH/WnnLb5M68xq74Ow6Tz+b0Dbwut9FvdY49d9fhd/kOmAAAOw==")
}

.x-btn-over > .x-btn-wrap-default-toolbar-large.x-btn-split-bottom:after {
    background-image: url("data:image/gif;R0lGODlhyAAOAKEDAAAAAKrI8e/4/////yH5BAEKAAMALAAAAADIAA4AAAJbjI+py+0Po5y02uuE3rz7D4biSJbmiabqKg7uC8fyTNf2jef6zvf+DwwKh8Si8YhMKpfMpvMJjUqn1Kr1is1qeYBudwsOi13esflsBaDX7Lb7DY/L5/S6/X4uAAA7")
}

.x-btn-split-right > .x-btn-icon.x-btn-no-text.x-btn-button-default-toolbar-large {
    padding-right: 4px
}

.x-btn-split-right > .x-btn-text.x-btn-icon-right > .x-btn-icon-el-default-toolbar-large {
    margin-right: 4px
}

.x-btn-focus.x-btn-default-toolbar-large {
    background-image: none;
    background-color: transparent
}

.x-btn-focus.x-btn-default-toolbar-large .x-btn-wrap {
    outline: 1px dotted #333
}

.x-btn-default-toolbar-large .x-btn-arrow-el {
    position: absolute;
    top: 0;
    right: 0;
    height: 100%;
    width: 17px;
    pointer-events: none
}

.x-btn-over.x-btn-default-toolbar-large {
    border-color: #81a4d0;
    background-image: none;
    background-color: #dbeeff;
    background-image: -webkit-gradient(linear, top, bottom, color-stop(0%, #dbeeff), color-stop(48%, #d0e7ff), color-stop(52%, #bbd2f0), color-stop(0%, #bed6f5));
    background-image: -webkit-linear-gradient(top, #dbeeff, #d0e7ff 48%, #bbd2f0 52%, #bed6f5);
    background-image: -moz-linear-gradient(top, #dbeeff, #d0e7ff 48%, #bbd2f0 52%, #bed6f5);
    background-image: -o-linear-gradient(top, #dbeeff, #d0e7ff 48%, #bbd2f0 52%, #bed6f5);
    background-image: -ms-linear-gradient(top, #dbeeff, #d0e7ff 48%, #bbd2f0 52%, #bed6f5);
    background-image: linear-gradient(top, #dbeeff, #d0e7ff 48%, #bbd2f0 52%, #bed6f5)
}

.x-btn.x-btn-menu-active.x-btn-default-toolbar-large, .x-btn.x-btn-pressed.x-btn-default-toolbar-large {
    border-color: #7a9ac4;
    background-image: none;
    background-color: #bccfe5;
    background-image: -webkit-gradient(linear, top, bottom, color-stop(0%, #bccfe5), color-stop(48%, #c5d6e7), color-stop(52%, #95c4f4), color-stop(0%, #9fc9f5));
    background-image: -webkit-linear-gradient(top, #bccfe5, #c5d6e7 48%, #95c4f4 52%, #9fc9f5);
    background-image: -moz-linear-gradient(top, #bccfe5, #c5d6e7 48%, #95c4f4 52%, #9fc9f5);
    background-image: -o-linear-gradient(top, #bccfe5, #c5d6e7 48%, #95c4f4 52%, #9fc9f5);
    background-image: -ms-linear-gradient(top, #bccfe5, #c5d6e7 48%, #95c4f4 52%, #9fc9f5);
    background-image: linear-gradient(top, #bccfe5, #c5d6e7 48%, #95c4f4 52%, #9fc9f5)
}

.x-btn.x-btn-disabled.x-btn-default-toolbar-large {
    border-color: #e1e1e1;
    background-image: none;
    background-color: transparent
}

.x-btn.x-btn-disabled.x-btn-default-toolbar-large .x-btn-inner {
    color: #8c8c8c
}

.x-btn-focus .x-btn-default-toolbar-large-tl, .x-btn-focus .x-btn-default-toolbar-large-bl, .x-btn-focus .x-btn-default-toolbar-large-tr, .x-btn-focus .x-btn-default-toolbar-large-br, .x-btn-focus .x-btn-default-toolbar-large-tc, .x-btn-focus .x-btn-default-toolbar-large-bc {
    background-image: url(images/btn/btn-default-toolbar-large-focus-corners.gif)
}

.x-btn-focus .x-btn-default-toolbar-large-ml, .x-btn-focus .x-btn-default-toolbar-large-mr {
    background-image: url(images/btn/btn-default-toolbar-large-focus-sides.gif)
}

.x-btn-focus .x-btn-default-toolbar-large-mc {
    background-color: transparent;
    background-image: url(images/btn/btn-default-toolbar-large-focus-fbg.gif)
}

.x-btn-over .x-btn-default-toolbar-large-tl, .x-btn-over .x-btn-default-toolbar-large-bl, .x-btn-over .x-btn-default-toolbar-large-tr, .x-btn-over .x-btn-default-toolbar-large-br, .x-btn-over .x-btn-default-toolbar-large-tc, .x-btn-over .x-btn-default-toolbar-large-bc {
    background-image: url("data:image/gif;R0lGODlhAwASAPMAAIGk0Iys1I2s1JOy25y63rjR8brN5r3V9NLn+9rt/////wAAAIGk0IGk0IGk0IGk0CH5BAEAAAoALAAAAAADABIAQwgzAAEIDIAgQYEBBg4oDFDgQIKHCgwQJGAgooCHCRQeEAjAAAEEASomQCDAwICGBQSUVBAQADs=")
}

.x-btn-over .x-btn-default-toolbar-large-ml, .x-btn-over .x-btn-default-toolbar-large-mr {
    background-image: url("data:image/gif;R0lGODlhBgAgA/QAAIGk0LvS8LvS8bvT8bzT8bzT8rzU8rzU873U873V873V9L7V8szj/NDn/9Hn/9Ho/9Lo/9Pp/9Tp/9Xq/9br/9fr/9js/9nt/////4Gk0IGk0IGk0IGk0IGk0IGk0IGk0CH5BAEAABgALAAAAAAGACADRAj/AAFcGHgBAAAJCCUYZMCQgUECEAkYVEBRwcSKFylmtAigIkePG0N2xDhSY8mPJEGeFKmyZcqXJl3GhIlyps2aOFnS1HmTZ86VQGX+FOqzaNCdR3smHYqU6FKjTqM2napUalWqTK9qzcoVKskKYCsYhEAWgsEAaAMYNMDWgNetb7s+nWtVbt24eOlizXtXL1y/dvcC5iu4r+HCiP8eVpw4MOPHPy1ItmBwguUJBiNojmDQgWcHZ9MaHEB6gMECqAsYRMAaAWHIrx3Ljk17sO3Fs283ro2b927dsIHn7i3cd3DiyH8nP668OfPnw51Hh258uvXq2ItrX359++/JlAGEjhULgIJ5CpUvG0yoEEBZswAeyH9gsIH9BgYX6F8QGq1BAQAKMFppp6W2VlsGHaDgAQYl4GAC2XEXoXQTUuedhRJe2F2GHFKoYYUbetghhiKWSOKJIaII4ooftjhiijCy+KKMJsboYo00qnijjjPuaGOPQOLoY44/Chkkj0YmieSSRTJJ5JNDRnlkk1SGFBAAOw==")
}

.x-btn-over .x-btn-default-toolbar-large-mc {
    background-color: #dbeeff;
    background-image: url("data:image/gif;R0lGODlhAQAgA/QAALvS8LvS8bvT8bzT8bzT8rzU8rzU873U873V873V9L7V8szj/NDn/9Hn/9Ho/9Lo/9Pp/9Tp/9Xq/9br/9fr/9js/9nt/////7vS8LvS8LvS8LvS8LvS8LvS8LvS8LvS8CH5BAEAABcALAAAAAABACADRAhUAC1EWDAggcGDCBMqXMiwocOHECMmpPAAQAGJGDNq3JixggQIDQAIIHCAo8mTKFOqXMkSYgUKEyREeOCAgQIAAUYWMICgpc+fQIMKHUq0qNGjQgMCADs=")
}

.x-btn-focus.x-btn-over .x-btn-default-toolbar-large-tl, .x-btn-focus.x-btn-over .x-btn-default-toolbar-large-bl, .x-btn-focus.x-btn-over .x-btn-default-toolbar-large-tr, .x-btn-focus.x-btn-over .x-btn-default-toolbar-large-br, .x-btn-focus.x-btn-over .x-btn-default-toolbar-large-tc, .x-btn-focus.x-btn-over .x-btn-default-toolbar-large-bc {
    background-image: url("data:image/gif;R0lGODlhAwASAPMAAIGk0Iys1I2s1JOy25y63rjR8brN5r3V9NLn+9rt/////wAAAIGk0IGk0IGk0IGk0CH5BAEAAAoALAAAAAADABIAQwgzAAEIDIAgQYEBBg4oDFDgQIKHCgwQJGAgooCHCRQeEAjAAAEEASomQCDAwICGBQSUVBAQADs=")
}

.x-btn-focus.x-btn-over .x-btn-default-toolbar-large-ml, .x-btn-focus.x-btn-over .x-btn-default-toolbar-large-mr {
    background-image: url("data:image/gif;R0lGODlhBgAgA/QAAIGk0LvS8LvS8bvT8bzT8bzT8rzU8rzU873U873V873V9L7V8szj/NDn/9Hn/9Ho/9Lo/9Pp/9Tp/9Xq/9br/9fr/9js/9nt/////4Gk0IGk0IGk0IGk0IGk0IGk0IGk0CH5BAEAABgALAAAAAAGACADRAj/AAFcGHgBAAAJCCUYZMCQgUECEAkYVEBRwcSKFylmtAigIkePG0N2xDhSY8mPJEGeFKmyZcqXJl3GhIlyps2aOFnS1HmTZ86VQGX+FOqzaNCdR3smHYqU6FKjTqM2napUalWqTK9qzcoVKskKYCsYhEAWgsEAaAMYNMDWgNetb7s+nWtVbt24eOlizXtXL1y/dvcC5iu4r+HCiP8eVpw4MOPHPy1ItmBwguUJBiNojmDQgWcHZ9MaHEB6gMECqAsYRMAaAWHIrx3Ljk17sO3Fs283ro2b927dsIHn7i3cd3DiyH8nP668OfPnw51Hh258uvXq2ItrX359++/JlAGEjhULgIJ5CpUvG0yoEEBZswAeyH9gsIH9BgYX6F8QGq1BAQAKMFppp6W2VlsGHaDgAQYl4GAC2XEXoXQTUuedhRJe2F2GHFKoYYUbetghhiKWSOKJIaII4ooftjhiijCy+KKMJsboYo00qnijjjPuaGOPQOLoY44/Chkkj0YmieSSRTJJ5JNDRnlkk1SGFBAAOw==")
}

.x-btn-focus.x-btn-over .x-btn-default-toolbar-large-mc {
    background-color: #dbeeff;
    background-image: url("data:image/gif;R0lGODlhAQAgA/QAALvS8LvS8bvT8bzT8bzT8rzU8rzU873U873V873V9L7V8szj/NDn/9Hn/9Ho/9Lo/9Pp/9Tp/9Xq/9br/9fr/9js/9nt/////7vS8LvS8LvS8LvS8LvS8LvS8LvS8LvS8CH5BAEAABcALAAAAAABACADRAhUAC1EWDAggcGDCBMqXMiwocOHECMmpPAAQAGJGDNq3JixggQIDQAIIHCAo8mTKFOqXMkSYgUKEyREeOCAgQIAAUYWMICgpc+fQIMKHUq0qNGjQgMCADs=")
}

.x-btn.x-btn-menu-active .x-btn-default-toolbar-large-tl, .x-btn.x-btn-menu-active .x-btn-default-toolbar-large-bl, .x-btn.x-btn-menu-active .x-btn-default-toolbar-large-tr, .x-btn.x-btn-menu-active .x-btn-default-toolbar-large-br, .x-btn.x-btn-menu-active .x-btn-default-toolbar-large-tc, .x-btn.x-btn-menu-active .x-btn-default-toolbar-large-bc, .x-btn.x-btn-pressed .x-btn-default-toolbar-large-tl, .x-btn.x-btn-pressed .x-btn-default-toolbar-large-bl, .x-btn.x-btn-pressed .x-btn-default-toolbar-large-tr, .x-btn.x-btn-pressed .x-btn-default-toolbar-large-br, .x-btn.x-btn-pressed .x-btn-default-toolbar-large-tc, .x-btn.x-btn-pressed .x-btn-default-toolbar-large-bc {
    background-image: url("data:image/gif;R0lGODlhAwASAPMAAHqaxIWo04ejyYekyY6qzpvE8J7I9LbK4rfH37zP5f///wAAAHqaxHqaxHqaxHqaxCH5BAEAAAoALAAAAAADABIAQwgzAAEIHHAgQYEACAwoHFDAQIKHChAQJIAgooCHCRQaEAgAAYEDAyomOCAAQYCGBQSUVBAQADs=")
}

.x-btn.x-btn-menu-active .x-btn-default-toolbar-large-ml, .x-btn.x-btn-menu-active .x-btn-default-toolbar-large-mr, .x-btn.x-btn-pressed .x-btn-default-toolbar-large-ml, .x-btn.x-btn-pressed .x-btn-default-toolbar-large-mr {
    background-image: url("data:image/gif;R0lGODlhBgAgA/QAAHqaxJXE9JbE9JfF9JjF9JnG9JrG9JvH9JzH9J3H8Z3I9LzS6b3P5b3Q5b7Q5b7R5b/R5cDS5cDS5sHT5sLT5sLU5sPU5sTV5v///3qaxHqaxHqaxHqaxHqaxHqaxHqaxCH5BAEAABgALAAAAAAGACADRAj/AAEwGMgAAIAJCCcYXMBwgUECEAkYVEBRwcSKFylmtAigIkePG0N2xDhSY8mPJEGeFKmyZcqXJl3GhIlyps2aOFnS1HmTZ86VQGX+FOqzaNCdR3smHYqU6FKjTqM2napUalWqTK9qzcoVKkkIYCEYtEDWgkEBaAUYNMDWgNetb7s+nWtVbt24eOlizXtXL1y/dvcC5iu4r+HCiP8eVpw4MOPHPx1IdmAwguUIBilopmDwgucLBgOIDmBwgOkBBguoLmDwgOsDhCHHdkx7tu3BuBfXzt34tm7fvXnLFr77N3Hgw40rD748OfPnzqMXhz5dOvLq2K9rP869efbuwRuIjG9g8IH5BwbDigUgob0EgwkVAqhAv8LYsp0/G0zAP0Ho0aWd9lBEqa22VlutvWYQAgwisJ13D1IXoXXgUQhhhd9dqKGEGE6YIYcbWgjiiCKW+KGJHqbY4Yohnuiiii3CSOKLLM4oI4o14hhjjjTu6KONPN7YI5A/6kjkkUYmOaSSQjYZ5JNFLillSAEBADs=")
}

.x-btn.x-btn-menu-active .x-btn-default-toolbar-large-mc, .x-btn.x-btn-pressed .x-btn-default-toolbar-large-mc {
    background-color: #bccfe5;
    background-image: url("data:image/gif;R0lGODlhAQAgA/QAAJXE9JbE9JfF9JjF9JnG9JrG9JvH9JzH9J3H8Z3I9LzS6b3P5b3Q5b7Q5b7R5b/R5cDS5cDS5sHT5sLT5sLU5sPU5sTV5v///5XE9JXE9JXE9JXE9JXE9JXE9JXE9JXE9CH5BAEAABcALAAAAAABACADRAhUABdIUDAggcGDCBMqXMiwocOHECMmfFAhQAGJGDNq3JixAYQJFgAIIGCAo8mTKFOqXMkSIgMHDyJIoFDBAgKRAwgUMHCgpc+fQIMKHUq0qNGjQgMCADs=")
}

.x-btn-focus.x-btn-menu-active .x-btn-default-toolbar-large-tl, .x-btn-focus.x-btn-menu-active .x-btn-default-toolbar-large-bl, .x-btn-focus.x-btn-menu-active .x-btn-default-toolbar-large-tr, .x-btn-focus.x-btn-menu-active .x-btn-default-toolbar-large-br, .x-btn-focus.x-btn-menu-active .x-btn-default-toolbar-large-tc, .x-btn-focus.x-btn-menu-active .x-btn-default-toolbar-large-bc, .x-btn-focus.x-btn-pressed .x-btn-default-toolbar-large-tl, .x-btn-focus.x-btn-pressed .x-btn-default-toolbar-large-bl, .x-btn-focus.x-btn-pressed .x-btn-default-toolbar-large-tr, .x-btn-focus.x-btn-pressed .x-btn-default-toolbar-large-br, .x-btn-focus.x-btn-pressed .x-btn-default-toolbar-large-tc, .x-btn-focus.x-btn-pressed .x-btn-default-toolbar-large-bc {
    background-image: url("data:image/gif;R0lGODlhAwASAPMAAHqaxIWo04ejyYekyY6qzpvE8J7I9LbK4rfH37zP5f///wAAAHqaxHqaxHqaxHqaxCH5BAEAAAoALAAAAAADABIAQwgzAAEIHHAgQYEACAwoHFDAQIKHChAQJIAgooCHCRQaEAgAAYEDAyomOCAAQYCGBQSUVBAQADs=")
}

.x-btn-focus.x-btn-menu-active .x-btn-default-toolbar-large-ml, .x-btn-focus.x-btn-menu-active .x-btn-default-toolbar-large-mr, .x-btn-focus.x-btn-pressed .x-btn-default-toolbar-large-ml, .x-btn-focus.x-btn-pressed .x-btn-default-toolbar-large-mr {
    background-image: url("data:image/gif;R0lGODlhBgAgA/QAAHqaxJXE9JbE9JfF9JjF9JnG9JrG9JvH9JzH9J3H8Z3I9LzS6b3P5b3Q5b7Q5b7R5b/R5cDS5cDS5sHT5sLT5sLU5sPU5sTV5v///3qaxHqaxHqaxHqaxHqaxHqaxHqaxCH5BAEAABgALAAAAAAGACADRAj/AAEwGMgAAIAJCCcYXMBwgUECEAkYVEBRwcSKFylmtAigIkePG0N2xDhSY8mPJEGeFKmyZcqXJl3GhIlyps2aOFnS1HmTZ86VQGX+FOqzaNCdR3smHYqU6FKjTqM2napUalWqTK9qzcoVKkkIYCEYtEDWgkEBaAUYNMDWgNetb7s+nWtVbt24eOlizXtXL1y/dvcC5iu4r+HCiP8eVpw4MOPHPx1IdmAwguUIBilopmDwgucLBgOIDmBwgOkBBguoLmDwgOsDhCHHdkx7tu3BuBfXzt34tm7fvXnLFr77N3Hgw40rD748OfPnzqMXhz5dOvLq2K9rP869efbuwRuIjG9g8IH5BwbDigUgob0EgwkVAqhAv8LYsp0/G0zAP0Ho0aWd9lBEqa22VlutvWYQAgwisJ13D1IXoXXgUQhhhd9dqKGEGE6YIYcbWgjiiCKW+KGJHqbY4Yohnuiiii3CSOKLLM4oI4o14hhjjjTu6KONPN7YI5A/6kjkkUYmOaSSQjYZ5JNFLillSAEBADs=")
}

.x-btn-focus.x-btn-menu-active .x-btn-default-toolbar-large-mc, .x-btn-focus.x-btn-pressed .x-btn-default-toolbar-large-mc {
    background-color: #bccfe5;
    background-image: url("data:image/gif;R0lGODlhAQAgA/QAAJXE9JbE9JfF9JjF9JnG9JrG9JvH9JzH9J3H8Z3I9LzS6b3P5b3Q5b7Q5b7R5b/R5cDS5cDS5sHT5sLT5sLU5sPU5sTV5v///5XE9JXE9JXE9JXE9JXE9JXE9JXE9JXE9CH5BAEAABcALAAAAAABACADRAhUABdIUDAggcGDCBMqXMiwocOHECMmfFAhQAGJGDNq3JixAYQJFgAIIGCAo8mTKFOqXMkSIgMHDyJIoFDBAgKRAwgUMHCgpc+fQIMKHUq0qNGjQgMCADs=")
}

.x-btn.x-btn-disabled .x-btn-default-toolbar-large-tl, .x-btn.x-btn-disabled .x-btn-default-toolbar-large-bl, .x-btn.x-btn-disabled .x-btn-default-toolbar-large-tr, .x-btn.x-btn-disabled .x-btn-default-toolbar-large-br, .x-btn.x-btn-disabled .x-btn-default-toolbar-large-tc, .x-btn.x-btn-disabled .x-btn-default-toolbar-large-bc {
    background-image: url("data:image/gif;R0lGODlhAwASAPIAAPDw8PHx8fT09Pb29v///wAAAPDw8PDw8CH5BAEAAAQALAAAAAADABIAQggnAAEIDECgoIABBQkQTFhwAMGDBBwyLCgQwAABChEWDHAxYQCOBAICADs=")
}

.x-btn.x-btn-disabled .x-btn-default-toolbar-large-ml, .x-btn.x-btn-disabled .x-btn-default-toolbar-large-mr {
    background-image: url("data:image/gif;R0lGODlhBgAgA/EAAPDw8P///wAAAPDw8CH5BAEAAAEALAAAAAAGACADQQj/AAEEGBgAgECCBgkWPDgwIUKGCxU6bAhxYsSHEitqzMgRo0eKHUF+vCiyJMmTFlNuHKkyJMqVJluyhPnSpcyYNG/WnGkzp8+eQHkKxRmU6NCdRpMiXaqz6c+jTosyfao0KlSqU6VarYp1a9arWruKDUsWrFmuZdGe/aq2Ldu3XuOOXSs3Ldy5buvSxXvXrt68fP/23es3sOHCiAkrBpyY8eLBjiNDniy48uHHlhtTviw5M2bOmzV77gx6dOjPokurTs0atWvSrWG/Pi27Nu3bpnOvnq07Nu7dtnvzBv7bt/DgxI8XH248ufPm0JlLRx6d+vTl1rNj3668+/Pr3qtzDP+uPTx48uPFm28YEAA7")
}

.x-btn.x-btn-disabled .x-btn-default-toolbar-large-mc {
    background-color: transparent;
    background-image: url("data:image/gif;R0lGODlhAQAgA/AAAP///wAAACH5BAEAAAAALAAAAAABACADQAgwAAEIHEiwoMGDCBMqXMiwocOHECNKnEixosWLGDNq3Mixo8ePIEOKHEmypMmTFAMCADs=")
}

.x-nbr .x-btn-default-toolbar-large {
    background-image: none
}

.x-btn-disabled.x-btn-default-toolbar-large {
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=50)";
    opacity: 0.5
}

.x-nbr .x-segmented-button-item-horizontal.x-btn-default-toolbar-large.x-segmented-button-first {
    border-right-width: 1px !important
}

.x-nbr .x-segmented-button-item-horizontal.x-btn-default-toolbar-large.x-segmented-button-first .x-btn-default-toolbar-large-mc {
    padding-right: 3px !important
}

.x-nbr .x-segmented-button-item-horizontal.x-btn-default-toolbar-large.x-segmented-button-middle {
    border-right-width: 1px !important
}

.x-nbr .x-segmented-button-item-horizontal.x-btn-default-toolbar-large.x-segmented-button-middle .x-btn-default-toolbar-large-mc {
    padding-right: 3px !important;
    padding-left: 3px !important
}

.x-nbr .x-segmented-button-item-horizontal.x-btn-default-toolbar-large.x-segmented-button-last .x-btn-default-toolbar-large-mc {
    padding-left: 3px !important
}

.x-nbr .x-segmented-button-item-vertical.x-btn-default-toolbar-large.x-segmented-button-first {
    border-bottom-width: 1px !important
}

.x-nbr .x-segmented-button-item-vertical.x-btn-default-toolbar-large.x-segmented-button-first .x-btn-default-toolbar-large-mc {
    padding-bottom: 3px !important
}

.x-nbr .x-segmented-button-item-vertical.x-btn-default-toolbar-large.x-segmented-button-middle {
    border-bottom-width: 1px !important
}

.x-nbr .x-segmented-button-item-vertical.x-btn-default-toolbar-large.x-segmented-button-middle .x-btn-default-toolbar-large-mc {
    padding-top: 3px !important;
    padding-bottom: 3px !important
}

.x-nbr .x-segmented-button-item-vertical.x-btn-default-toolbar-large.x-segmented-button-last .x-btn-default-toolbar-large-mc {
    padding-top: 3px !important
}

.x-nbr .x-segmented-button-item.x-btn-default-toolbar-large:after {
    content: ' ';
    border-style: solid;
    border-width: 0;
    position: absolute
}

.x-nbr .x-segmented-button-item-horizontal.x-btn-default-toolbar-large:after {
    top: 1px;
    right: 0;
    bottom: 1px;
    left: 0
}

.x-nbr .x-segmented-button-item-horizontal.x-btn-default-toolbar-large.x-segmented-button-first:after {
    left: 1px
}

.x-nbr .x-segmented-button-item-horizontal.x-btn-default-toolbar-large.x-segmented-button-last:after {
    right: 1px
}

.x-nbr .x-segmented-button-item-vertical.x-btn-default-toolbar-large:after {
    top: 0;
    right: 1px;
    bottom: 0;
    left: 1px
}

.x-nbr .x-segmented-button-item-vertical.x-btn-default-toolbar-large.x-segmented-button-first:after {
    top: 1px
}

.x-nbr .x-segmented-button-item-vertical.x-btn-default-toolbar-large.x-segmented-button-last:after {
    bottom: 1px
}

.x-cmd-slicer.x-btn-focus.x-btn-default-toolbar-large:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url(images/btn/btn-default-toolbar-large-focus-corners.gif), sides:url(images/btn/btn-default-toolbar-large-focus-sides.gif), frame-bg:url(images/btn/btn-default-toolbar-large-focus-fbg.gif)" !important
}

.x-cmd-slicer.x-btn-over.x-btn-default-toolbar-large:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url("data:image/gif;R0lGODlhAwASAPMAAIGk0Iys1I2s1JOy25y63rjR8brN5r3V9NLn+9rt/////wAAAIGk0IGk0IGk0IGk0CH5BAEAAAoALAAAAAADABIAQwgzAAEIDIAgQYEBBg4oDFDgQIKHCgwQJGAgooCHCRQeEAjAAAEEASomQCDAwICGBQSUVBAQADs="), sides:url("data:image/gif;R0lGODlhBgAgA/QAAIGk0LvS8LvS8bvT8bzT8bzT8rzU8rzU873U873V873V9L7V8szj/NDn/9Hn/9Ho/9Lo/9Pp/9Tp/9Xq/9br/9fr/9js/9nt/////4Gk0IGk0IGk0IGk0IGk0IGk0IGk0CH5BAEAABgALAAAAAAGACADRAj/AAFcGHgBAAAJCCUYZMCQgUECEAkYVEBRwcSKFylmtAigIkePG0N2xDhSY8mPJEGeFKmyZcqXJl3GhIlyps2aOFnS1HmTZ86VQGX+FOqzaNCdR3smHYqU6FKjTqM2napUalWqTK9qzcoVKskKYCsYhEAWgsEAaAMYNMDWgNetb7s+nWtVbt24eOlizXtXL1y/dvcC5iu4r+HCiP8eVpw4MOPHPy1ItmBwguUJBiNojmDQgWcHZ9MaHEB6gMECqAsYRMAaAWHIrx3Ljk17sO3Fs283ro2b927dsIHn7i3cd3DiyH8nP668OfPnw51Hh258uvXq2ItrX359++/JlAGEjhULgIJ5CpUvG0yoEEBZswAeyH9gsIH9BgYX6F8QGq1BAQAKMFppp6W2VlsGHaDgAQYl4GAC2XEXoXQTUuedhRJe2F2GHFKoYYUbetghhiKWSOKJIaII4ooftjhiijCy+KKMJsboYo00qnijjjPuaGOPQOLoY44/Chkkj0YmieSSRTJJ5JNDRnlkk1SGFBAAOw=="), frame-bg:url("data:image/gif;R0lGODlhAQAgA/QAALvS8LvS8bvT8bzT8bzT8rzU8rzU873U873V873V9L7V8szj/NDn/9Hn/9Ho/9Lo/9Pp/9Tp/9Xq/9br/9fr/9js/9nt/////7vS8LvS8LvS8LvS8LvS8LvS8LvS8LvS8CH5BAEAABcALAAAAAABACADRAhUAC1EWDAggcGDCBMqXMiwocOHECMmpPAAQAGJGDNq3JixggQIDQAIIHCAo8mTKFOqXMkSYgUKEyREeOCAgQIAAUYWMICgpc+fQIMKHUq0qNGjQgMCADs=")" !important
}

.x-cmd-slicer.x-btn-focus.x-btn-over.x-btn-default-toolbar-large:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url("data:image/gif;R0lGODlhAwASAPMAAIGk0Iys1I2s1JOy25y63rjR8brN5r3V9NLn+9rt/////wAAAIGk0IGk0IGk0IGk0CH5BAEAAAoALAAAAAADABIAQwgzAAEIDIAgQYEBBg4oDFDgQIKHCgwQJGAgooCHCRQeEAjAAAEEASomQCDAwICGBQSUVBAQADs="), sides:url("data:image/gif;R0lGODlhBgAgA/QAAIGk0LvS8LvS8bvT8bzT8bzT8rzU8rzU873U873V873V9L7V8szj/NDn/9Hn/9Ho/9Lo/9Pp/9Tp/9Xq/9br/9fr/9js/9nt/////4Gk0IGk0IGk0IGk0IGk0IGk0IGk0CH5BAEAABgALAAAAAAGACADRAj/AAFcGHgBAAAJCCUYZMCQgUECEAkYVEBRwcSKFylmtAigIkePG0N2xDhSY8mPJEGeFKmyZcqXJl3GhIlyps2aOFnS1HmTZ86VQGX+FOqzaNCdR3smHYqU6FKjTqM2napUalWqTK9qzcoVKskKYCsYhEAWgsEAaAMYNMDWgNetb7s+nWtVbt24eOlizXtXL1y/dvcC5iu4r+HCiP8eVpw4MOPHPy1ItmBwguUJBiNojmDQgWcHZ9MaHEB6gMECqAsYRMAaAWHIrx3Ljk17sO3Fs283ro2b927dsIHn7i3cd3DiyH8nP668OfPnw51Hh258uvXq2ItrX359++/JlAGEjhULgIJ5CpUvG0yoEEBZswAeyH9gsIH9BgYX6F8QGq1BAQAKMFppp6W2VlsGHaDgAQYl4GAC2XEXoXQTUuedhRJe2F2GHFKoYYUbetghhiKWSOKJIaII4ooftjhiijCy+KKMJsboYo00qnijjjPuaGOPQOLoY44/Chkkj0YmieSSRTJJ5JNDRnlkk1SGFBAAOw=="), frame-bg:url("data:image/gif;R0lGODlhAQAgA/QAALvS8LvS8bvT8bzT8bzT8rzU8rzU873U873V873V9L7V8szj/NDn/9Hn/9Ho/9Lo/9Pp/9Tp/9Xq/9br/9fr/9js/9nt/////7vS8LvS8LvS8LvS8LvS8LvS8LvS8LvS8CH5BAEAABcALAAAAAABACADRAhUAC1EWDAggcGDCBMqXMiwocOHECMmpPAAQAGJGDNq3JixggQIDQAIIHCAo8mTKFOqXMkSYgUKEyREeOCAgQIAAUYWMICgpc+fQIMKHUq0qNGjQgMCADs=")" !important
}

.x-cmd-slicer.x-btn-pressed.x-btn-default-toolbar-large:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url("data:image/gif;R0lGODlhAwASAPMAAHqaxIWo04ejyYekyY6qzpvE8J7I9LbK4rfH37zP5f///wAAAHqaxHqaxHqaxHqaxCH5BAEAAAoALAAAAAADABIAQwgzAAEIHHAgQYEACAwoHFDAQIKHChAQJIAgooCHCRQaEAgAAYEDAyomOCAAQYCGBQSUVBAQADs="), sides:url("data:image/gif;R0lGODlhBgAgA/QAAHqaxJXE9JbE9JfF9JjF9JnG9JrG9JvH9JzH9J3H8Z3I9LzS6b3P5b3Q5b7Q5b7R5b/R5cDS5cDS5sHT5sLT5sLU5sPU5sTV5v///3qaxHqaxHqaxHqaxHqaxHqaxHqaxCH5BAEAABgALAAAAAAGACADRAj/AAEwGMgAAIAJCCcYXMBwgUECEAkYVEBRwcSKFylmtAigIkePG0N2xDhSY8mPJEGeFKmyZcqXJl3GhIlyps2aOFnS1HmTZ86VQGX+FOqzaNCdR3smHYqU6FKjTqM2napUalWqTK9qzcoVKkkIYCEYtEDWgkEBaAUYNMDWgNetb7s+nWtVbt24eOlizXtXL1y/dvcC5iu4r+HCiP8eVpw4MOPHPx1IdmAwguUIBilopmDwgucLBgOIDmBwgOkBBguoLmDwgOsDhCHHdkx7tu3BuBfXzt34tm7fvXnLFr77N3Hgw40rD748OfPnzqMXhz5dOvLq2K9rP869efbuwRuIjG9g8IH5BwbDigUgob0EgwkVAqhAv8LYsp0/G0zAP0Ho0aWd9lBEqa22VlutvWYQAgwisJ13D1IXoXXgUQhhhd9dqKGEGE6YIYcbWgjiiCKW+KGJHqbY4Yohnuiiii3CSOKLLM4oI4o14hhjjjTu6KONPN7YI5A/6kjkkUYmOaSSQjYZ5JNFLillSAEBADs="), frame-bg:url("data:image/gif;R0lGODlhAQAgA/QAAJXE9JbE9JfF9JjF9JnG9JrG9JvH9JzH9J3H8Z3I9LzS6b3P5b3Q5b7Q5b7R5b/R5cDS5cDS5sHT5sLT5sLU5sPU5sTV5v///5XE9JXE9JXE9JXE9JXE9JXE9JXE9JXE9CH5BAEAABcALAAAAAABACADRAhUABdIUDAggcGDCBMqXMiwocOHECMmfFAhQAGJGDNq3JixAYQJFgAIIGCAo8mTKFOqXMkSIgMHDyJIoFDBAgKRAwgUMHCgpc+fQIMKHUq0qNGjQgMCADs=")" !important
}

.x-cmd-slicer.x-btn-focus.x-btn-pressed.x-btn-default-toolbar-large:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url("data:image/gif;R0lGODlhAwASAPMAAHqaxIWo04ejyYekyY6qzpvE8J7I9LbK4rfH37zP5f///wAAAHqaxHqaxHqaxHqaxCH5BAEAAAoALAAAAAADABIAQwgzAAEIHHAgQYEACAwoHFDAQIKHChAQJIAgooCHCRQaEAgAAYEDAyomOCAAQYCGBQSUVBAQADs="), sides:url("data:image/gif;R0lGODlhBgAgA/QAAHqaxJXE9JbE9JfF9JjF9JnG9JrG9JvH9JzH9J3H8Z3I9LzS6b3P5b3Q5b7Q5b7R5b/R5cDS5cDS5sHT5sLT5sLU5sPU5sTV5v///3qaxHqaxHqaxHqaxHqaxHqaxHqaxCH5BAEAABgALAAAAAAGACADRAj/AAEwGMgAAIAJCCcYXMBwgUECEAkYVEBRwcSKFylmtAigIkePG0N2xDhSY8mPJEGeFKmyZcqXJl3GhIlyps2aOFnS1HmTZ86VQGX+FOqzaNCdR3smHYqU6FKjTqM2napUalWqTK9qzcoVKkkIYCEYtEDWgkEBaAUYNMDWgNetb7s+nWtVbt24eOlizXtXL1y/dvcC5iu4r+HCiP8eVpw4MOPHPx1IdmAwguUIBilopmDwgucLBgOIDmBwgOkBBguoLmDwgOsDhCHHdkx7tu3BuBfXzt34tm7fvXnLFr77N3Hgw40rD748OfPnzqMXhz5dOvLq2K9rP869efbuwRuIjG9g8IH5BwbDigUgob0EgwkVAqhAv8LYsp0/G0zAP0Ho0aWd9lBEqa22VlutvWYQAgwisJ13D1IXoXXgUQhhhd9dqKGEGE6YIYcbWgjiiCKW+KGJHqbY4Yohnuiiii3CSOKLLM4oI4o14hhjjjTu6KONPN7YI5A/6kjkkUYmOaSSQjYZ5JNFLillSAEBADs="), frame-bg:url("data:image/gif;R0lGODlhAQAgA/QAAJXE9JbE9JfF9JjF9JnG9JrG9JvH9JzH9J3H8Z3I9LzS6b3P5b3Q5b7Q5b7R5b/R5cDS5cDS5sHT5sLT5sLU5sPU5sTV5v///5XE9JXE9JXE9JXE9JXE9JXE9JXE9JXE9CH5BAEAABcALAAAAAABACADRAhUABdIUDAggcGDCBMqXMiwocOHECMmfFAhQAGJGDNq3JixAYQJFgAIIGCAo8mTKFOqXMkSIgMHDyJIoFDBAgKRAwgUMHCgpc+fQIMKHUq0qNGjQgMCADs=")" !important
}

.x-cmd-slicer.x-btn-disabled.x-btn-default-toolbar-large:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url("data:image/gif;R0lGODlhAwASAPIAAPDw8PHx8fT09Pb29v///wAAAPDw8PDw8CH5BAEAAAQALAAAAAADABIAQggnAAEIDECgoIABBQkQTFhwAMGDBBwyLCgQwAABChEWDHAxYQCOBAICADs="), sides:url("data:image/gif;R0lGODlhBgAgA/EAAPDw8P///wAAAPDw8CH5BAEAAAEALAAAAAAGACADQQj/AAEEGBgAgECCBgkWPDgwIUKGCxU6bAhxYsSHEitqzMgRo0eKHUF+vCiyJMmTFlNuHKkyJMqVJluyhPnSpcyYNG/WnGkzp8+eQHkKxRmU6NCdRpMiXaqz6c+jTosyfao0KlSqU6VarYp1a9arWruKDUsWrFmuZdGe/aq2Ldu3XuOOXSs3Ldy5buvSxXvXrt68fP/23es3sOHCiAkrBpyY8eLBjiNDniy48uHHlhtTviw5M2bOmzV77gx6dOjPokurTs0atWvSrWG/Pi27Nu3bpnOvnq07Nu7dtnvzBv7bt/DgxI8XH248ufPm0JlLRx6d+vTl1rNj3668+/Pr3qtzDP+uPTx48uPFm28YEAA7"), frame-bg:url("data:image/gif;R0lGODlhAQAgA/AAAP///wAAACH5BAEAAAAALAAAAAABACADQAgwAAEIHEiwoMGDCBMqXMiwocOHECNKnEixosWLGDNq3Mixo8ePIEOKHEmypMmTFAMCADs=")" !important
}

.x-button-default-toolbar-large-cell > .x-grid-cell-inner {
    padding-top: 0;
    padding-bottom: 0
}

.x-button-default-toolbar-large-cell > .x-grid-cell-inner > .x-btn-default-toolbar-large {
    vertical-align: top
}

.x-tool {
    cursor: pointer
}

.x-tool-tool-el {
    overflow: hidden;
    width: 15px;
    height: 15px;
    margin: 0;
    color: #558fd9;
    text-align: center
}

.x-tool-focus {
    outline: 1px dotted #c0d4ed;
    outline-offset: 0
}

.x-ie8 .x-tool-focus {
    outline: none
}

.x-ie8 .x-tool-focus:after {
    position: absolute;
    content: ' ';
    top: -1px;
    right: -1px;
    bottom: -1px;
    left: -1px;
    border: 1px dotted #c0d4ed;
    pointer-events: none
}

.x-tool-img {
    background-image: url("data:image/gif;R0lGODlhHgBoAff+AP///8/k+3Gg3Zm76Nns/+/9/+b2/yZDkNTo/ur5/9bq/+Hz/9Hm/DJVslCAsJ+y41F/w87i+MPX8rPN7bTS/05pqUFNZn2j3nOKvIKTyi5LlYOPt5jJb2yN3HqJu5nJcejz6pu5+4S/VIS/UZyw4lSBxFd+u1WDxkRwsDppqnmf22yLzXCP4YSpz0FcoHee2W6K13Oa1G2L2miL00Rtq3uh3D5qq4Gn4XWDsIGn4m55p1Fhh7za/3CGtjQ6TZGgyf39/oym4W6X1IOUy2WNylZmiml8p0FOb5Wo3GJtonJ9rF5mcWGLyX2Mv6S55F2Ev6S54XF/vXie2F9rovH4/63D6W+Lyaa56tf2ovv8/pCs6nyj23GY0MHe/6K2405cfqC054yvzomZxIaUufr8/Zqt30ZZgYKk1qG15Jm2+V9xmd3s9Wd8qO3183mg2ebx709YkZSl0XGFtEVNhHWa0Ke86Ja2/56x4ldifv//3YCd24Cm3S5fpnCDsT9IYF2IyE9ce3OZ0VN/wZ+z42t1nYWi3Wd6pKvA63qKtzlBVLbN8p7A/9f0ooOUyP//4Mfuh09fgWd4omZukZmo0kJJXNzy/+bw7+rz83WDv2mQzWZ6pWFnkI6g02t9qGKLyFuGx+n05EJPabbU/36l3VFYiouk4HJ/oGF0nvr7/W59ovf7/3mc1eHy+FZqlUZVdy81RMrl/6S251xtlXuc3Yyv5GiOzam+6qKx0HqQyIih2HJ/saO457vS91likoWo3U9adHqIteXx7a/F7nGGtlVliWl9qhwfKXif2Flwnm6TzGCJyYud0nOCuPz9/mGKx+bx7ZGj2pao0XWLvXqg2Y2f1GSQuomZzISVvLXM8fv8/ThDXMfujK/E7VaFtMbd9sLX8jJOl8vi+Ymtz1mHtT9anm6Ywsjd9oCmyrPO5GR9tb/U8W+IvGuFvMrg+C9MlWiAtVeGtNnr+t/x/ldxrHKJuoSpyt/y/neexMTb9brT6KS52dvu/K7B3srf9////wAAACH/C1hNUCBEYXRhWE1QPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4gPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iQWRvYmUgWE1QIENvcmUgNS4wLWMwNjAgNjEuMTM0Nzc3LCAyMDEwLzAyLzEyLTE3OjMyOjAwICAgICAgICAiPiA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPiA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIiB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHhtbG5zOnhtcE1NPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvbW0vIiB4bWxuczpzdFJlZj0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL3NUeXBlL1Jlc291cmNlUmVmIyIgeG1wOkNyZWF0b3JUb29sPSJBZG9iZSBQaG90b3Nob3AgQ1M1IE1hY2ludG9zaCIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDo1QkI4Rjg1QkU1MUYxMURGQTg1Q0IzNzFDQzg3NDJFNyIgeG1wTU06RG9jdW1lbnRJRD0ieG1wLmRpZDo1QkI4Rjg1Q0U1MUYxMURGQTg1Q0IzNzFDQzg3NDJFNyI+IDx4bXBNTTpEZXJpdmVkRnJvbSBzdFJlZjppbnN0YW5jZUlEPSJ4bXAuaWlkOjVCQjhGODU5RTUxRjExREZBODVDQjM3MUNDODc0MkU3IiBzdFJlZjpkb2N1bWVudElEPSJ4bXAuZGlkOjVCQjhGODVBRTUxRjExREZBODVDQjM3MUNDODc0MkU3Ii8+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kPSJyIj8+Af/+/fz7+vn49/b19PPy8fDv7u3s6+rp6Ofm5eTj4uHg397d3Nva2djX1tXU09LR0M/OzczLysnIx8bFxMPCwcC/vr28u7q5uLe2tbSzsrGwr66trKuqqainpqWko6KhoJ+enZybmpmYl5aVlJOSkZCPjo2Mi4qJiIeGhYSDgoGAf359fHt6eXh3dnV0c3JxcG9ubWxramloZ2ZlZGNiYWBfXl1cW1pZWFdWVVRTUlFQT05NTEtKSUhHRkVEQ0JBQD8+PTw7Ojk4NzY1NDMyMTAvLi0sKyopKCcmJSQjIiEg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")
}

.x-tool-placeholder {
    visibility: hidden
}

.x-tool-close {
    background-position: 0 0
}

.x-tool-minimize {
    background-position: 0 -15px
}

.x-tool-maximize {
    background-position: 0 -30px
}

.x-tool-restore {
    background-position: 0 -45px
}

.x-tool-toggle {
    background-position: 0 -60px
}

.x-panel-collapsed .x-tool-toggle {
    background-position: 0 -75px
}

.x-tool-gear {
    background-position: 0 -90px
}

.x-tool-prev {
    background-position: 0 -105px
}

.x-tool-next {
    background-position: 0 -120px
}

.x-tool-pin {
    background-position: 0 -135px
}

.x-tool-unpin {
    background-position: 0 -150px
}

.x-tool-right {
    background-position: 0 -165px
}

.x-tool-left {
    background-position: 0 -180px
}

.x-tool-down {
    background-position: 0 -195px
}

.x-tool-up {
    background-position: 0 -210px
}

.x-tool-refresh {
    background-position: 0 -225px
}

.x-tool-plus {
    background-position: 0 -240px
}

.x-tool-minus {
    background-position: 0 -255px
}

.x-tool-search {
    background-position: 0 -270px
}

.x-tool-save {
    background-position: 0 -285px
}

.x-tool-help {
    background-position: 0 -300px
}

.x-tool-print {
    background-position: 0 -315px
}

.x-tool-expand {
    background-position: 0 -330px
}

.x-tool-collapse {
    background-position: 0 -345px
}

.x-tool-resize {
    background-position: 0 -360px
}

.x-tool-move {
    background-position: 0 -375px
}

.x-tool-expand-bottom {
    background-position: 0 -195px
}

.x-tool-collapse-bottom {
    background-position: 0 -195px
}

.x-tool-expand-top {
    background-position: 0 -210px
}

.x-tool-collapse-top {
    background-position: 0 -210px
}

.x-tool-expand-left {
    background-position: 0 -180px
}

.x-tool-collapse-left {
    background-position: 0 -180px
}

.x-tool-expand-right {
    background-position: 0 -165px
}

.x-tool-collapse-right {
    background-position: 0 -165px
}

.x-tool-over .x-tool-close {
    background-position: -15px 0
}

.x-tool-over .x-tool-minimize {
    background-position: -15px -15px
}

.x-tool-over .x-tool-maximize {
    background-position: -15px -30px
}

.x-tool-over .x-tool-restore {
    background-position: -15px -45px
}

.x-tool-over .x-tool-toggle {
    background-position: -15px -60px
}

.x-panel-collapsed .x-tool-over .x-tool-toggle {
    background-position: -15px -75px
}

.x-tool-over .x-tool-gear {
    background-position: -15px -90px
}

.x-tool-over .x-tool-prev {
    background-position: -15px -105px
}

.x-tool-over .x-tool-next {
    background-position: -15px -120px
}

.x-tool-over .x-tool-pin {
    background-position: -15px -135px
}

.x-tool-over .x-tool-unpin {
    background-position: -15px -150px
}

.x-tool-over .x-tool-right {
    background-position: -15px -165px
}

.x-tool-over .x-tool-left {
    background-position: -15px -180px
}

.x-tool-over .x-tool-down {
    background-position: -15px -195px
}

.x-tool-over .x-tool-up {
    background-position: -15px -210px
}

.x-tool-over .x-tool-refresh {
    background-position: -15px -225px
}

.x-tool-over .x-tool-plus {
    background-position: -15px -240px
}

.x-tool-over .x-tool-minus {
    background-position: -15px -255px
}

.x-tool-over .x-tool-search {
    background-position: -15px -270px
}

.x-tool-over .x-tool-save {
    background-position: -15px -285px
}

.x-tool-over .x-tool-help {
    background-position: -15px -300px
}

.x-tool-over .x-tool-print {
    background-position: -15px -315px
}

.x-tool-over .x-tool-expand {
    background-position: -15px -330px
}

.x-tool-over .x-tool-collapse {
    background-position: -15px -345px
}

.x-tool-over .x-tool-resize {
    background-position: -15px -360px
}

.x-tool-over .x-tool-move {
    background-position: -15px -375px
}

.x-tool-over .x-tool-expand-bottom {
    background-position: -15px -195px
}

.x-tool-over .x-tool-collapse-bottom {
    background-position: -15px -195px
}

.x-tool-over .x-tool-expand-top {
    background-position: -15px -210px
}

.x-tool-over .x-tool-collapse-top {
    background-position: -15px -210px
}

.x-tool-over .x-tool-expand-left {
    background-position: -15px -180px
}

.x-tool-over .x-tool-collapse-left {
    background-position: -15px -180px
}

.x-tool-over .x-tool-expand-right {
    background-position: -15px -165px
}

.x-tool-over .x-tool-collapse-right {
    background-position: -15px -165px
}

.x-header-draggable, .x-header-ghost {
    cursor: move
}

.x-header-text {
    white-space: nowrap
}

.x-collapse-el {
    cursor: pointer
}

.x-layout-split-left {
    background-image: url("data:image/gif;R0lGODlhBQAjAIcAAENDRUD/QNHR0ezs7AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAMAAAEALAAAAAAFACMAAAhEAAMIDCBgoICCBAcUFDBAIcOGBxs6lBgR4sOJFilerIixY0UAEQGAFCBy5ACRHzmq3MhSo8uMMD1uTKhQIEOEBHESDAgAOw==")
}

.x-layout-split-right {
    background-image: url("data:image/gif;R0lGODlhBQAjAIcAAENDRUD/QNHR0ezs7AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAMAAAEALAAAAAAFACMAAAhFAAUEGBhAgMCBAgYcTKiw4ICHBh8qZDhRYkSIFC9WxGgxo0cAGAGANCgSAMmRAkBuXKmxpceOMDnKZMlQYMKFBwsSDBAQADs=")
}

.x-layout-split-top {
    background-image: url("data:image/gif;R0lGODlhIwAFAIcAAENDRUD/QNHR0ezs7AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAMAAAEALAAAAAAjAAUAAAg1AAMIDCCgoMGDCBMmHMhQwICHECNCBCCx4kMBDAlarAig40aJGAU6/Dixo0eSFwkqXMmyZUAAOw==")
}

.x-layout-split-bottom {
    background-image: url("data:image/gif;R0lGODlhIwAFAIcAAENDRUD/QNHR0ezs7AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAMAAAEALAAAAAAjAAUAAAg1AAUIHEiwoMGDBwMIGMCwocOGACJGfEiRoYAAGBdWfChx48OLGDN6dAhgZEOQITMiXLkyZUAAOw==")
}

.x-splitter-collapsed .x-layout-split-left {
    background-image: url("data:image/gif;R0lGODlhBQAjAIcAAENDRUD/QNHR0ezs7AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAMAAAEALAAAAAAFACMAAAhFAAUEGBhAgMCBAgYcTKiw4ICHBh8qZDhRYkSIFC9WxGgxo0cAGAGANCgSAMmRAkBuXKmxpceOMDnKZMlQYMKFBwsSDBAQADs=")
}

.x-splitter-collapsed .x-layout-split-right {
    background-image: url("data:image/gif;R0lGODlhBQAjAIcAAENDRUD/QNHR0ezs7AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAMAAAEALAAAAAAFACMAAAhEAAMIDCBgoICCBAcUFDBAIcOGBxs6lBgR4sOJFilerIixY0UAEQGAFCBy5ACRHzmq3MhSo8uMMD1uTKhQIEOEBHESDAgAOw==")
}

.x-splitter-collapsed .x-layout-split-top {
    background-image: url("data:image/gif;R0lGODlhIwAFAIcAAENDRUD/QNHR0ezs7AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAMAAAEALAAAAAAjAAUAAAg1AAUIHEiwoMGDBwMIGMCwocOGACJGfEiRoYAAGBdWfChx48OLGDN6dAhgZEOQITMiXLkyZUAAOw==")
}

.x-splitter-collapsed .x-layout-split-bottom {
    background-image: url("data:image/gif;R0lGODlhIwAFAIcAAENDRUD/QNHR0ezs7AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAMAAAEALAAAAAAjAAUAAAg1AAMIDCCgoMGDCBMmHMhQwICHECNCBCCx4kMBDAlarAig40aJGAU6/Dixo0eSFwkqXMmyZUAAOw==")
}

.x-splitter-active {
    background-color: #b4b4b4;
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=80)";
    opacity: 0.8
}

.x-splitter-active .x-collapse-el {
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=30)";
    opacity: 0.3
}

.x-layout-split-left, .x-layout-split-right {
    top: 50%;
    margin-top: -17px;
    width: 100%;
    height: 35px
}

.x-layout-split-top, .x-layout-split-bottom {
    left: 50%;
    width: 35px;
    height: 100%;
    margin-left: -17px
}

.x-splitter-focus:after {
    position: absolute;
    content: ' ';
    top: 0px;
    right: 0px;
    bottom: 0px;
    left: 0px;
    border: 1px dotted #464646;
    pointer-events: none
}

.x-toolbar-default {
    padding: 2px 0 2px 2px;
    border-style: solid;
    border-color: #99bce8;
    border-width: 1px;
    background-image: none;
    background-color: #d3e1f1;
    background-image: -webkit-gradient(linear, top, bottom, color-stop(0%, #dfe9f5), color-stop(0%, #d3e1f1));
    background-image: -webkit-linear-gradient(top, #dfe9f5, #d3e1f1);
    background-image: -moz-linear-gradient(top, #dfe9f5, #d3e1f1);
    background-image: -o-linear-gradient(top, #dfe9f5, #d3e1f1);
    background-image: -ms-linear-gradient(top, #dfe9f5, #d3e1f1);
    background-image: linear-gradient(top, #dfe9f5, #d3e1f1)
}

.x-toolbar-default .x-toolbar-item {
    margin: 0 2px 0 0
}

.x-toolbar-default .x-toolbar-separator-horizontal {
    margin: 0 2px 0 0;
    height: 14px;
    border-style: solid;
    border-width: 0 1px;
    border-left-color: #98c8ff;
    border-right-color: #fff
}

.x-toolbar-default .x-box-menu-after {
    margin: 0 2px
}

.x-toolbar-default-vertical {
    padding: 2px 2px 0
}

.x-toolbar-default-vertical .x-toolbar-item {
    margin: 0 0 2px 0
}

.x-toolbar-default-vertical .x-toolbar-separator-vertical {
    margin: 0 5px 2px;
    border-style: solid none;
    border-width: 1px 0;
    border-top-color: #98c8ff;
    border-bottom-color: #fff
}

.x-toolbar-default-vertical .x-box-menu-after {
    margin: 2px 0
}

.x-nlg .x-toolbar-default {
    background-image: url("data:image/gif;R0lGODlhAQAgA/QAANPh8dTh8dTi8dXi8tbj8tfk8tjk89jl89nl89rl89rm89vm9Nzn9N3o9N7o9d7p9d/p9f///9Ph8dPh8dPh8dPh8dPh8dPh8dPh8dPh8dPh8dPh8dPh8dPh8dPh8dPh8SH5BAEAABEALAAAAAABACADRAhMACEsKBAAgMGDCBMqXMiwocOHECMmbICAgMSLGDNqzOiAgYIDBAZsHEmypMmTKFNKfNCAAYMFCRAYKBBSgMqbOHPq3Mmzp8+fQH8GBAA7") !important;
    background-repeat: repeat-x
}

.x-toolbar-text-default {
    padding: 0 4px;
    color: #4d4d4d;
    font: normal 11px/16px tahoma, arial, verdana, sans-serif
}

.x-toolbar-spacer-default {
    width: 2px
}

.x-toolbar-default-scroller .x-box-scroller-body-horizontal {
    margin-left: 12px
}

.x-toolbar-default-vertical-scroller .x-box-scroller-body-vertical {
    margin-top: 13px
}

.x-box-scroller-toolbar-default {
    cursor: pointer;
    color: #eee
}

.x-box-scroller-toolbar-default.x-box-scroller-disabled {
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=50)";
    opacity: 0.5;
    cursor: default
}

.x-box-scroller-toolbar-default.x-box-scroller-left, .x-box-scroller-toolbar-default.x-box-scroller-right {
    width: 14px;
    height: 22px;
    border-style: solid;
    border-color: #8db2e3;
    border-width: 0 0 1px;
    top: 50%;
    margin-top: -11px
}

.x-box-scroller-toolbar-default.x-box-scroller-left {
    margin-left: 0;
    margin-right: 0;
    margin-bottom: 0;
    background-image: url("data:image/gif;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");
    background-position: -14px 0
}

.x-box-scroller-toolbar-default.x-box-scroller-left.x-box-scroller-hover {
    background-position: 0 0
}

.x-box-scroller-toolbar-default.x-box-scroller-right {
    margin-left: 0;
    margin-right: 0;
    margin-bottom: 0;
    background-image: url("data:image/gif;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");
    background-position: 0 0
}

.x-box-scroller-toolbar-default.x-box-scroller-right.x-box-scroller-hover {
    background-position: -14px 0
}

.x-box-scroller-toolbar-default.x-box-scroller-top, .x-box-scroller-toolbar-default.x-box-scroller-bottom {
    height: 5px;
    width: 35px;
    left: 50%;
    margin-left: -17px
}

.x-box-scroller-toolbar-default.x-box-scroller-top {
    margin-top: 5px;
    margin-right: 0;
    margin-bottom: 5px;
    background-image: url("data:image/gif;R0lGODlhIwAKAMIEADxdk5m86Mna7uDq9f///////////////yH5BAEKAAQALAAAAAAjAAoAAAM9SErR/jDGRcO4OGOg+w0U43VAOWqgYp1babIfI810XdU4FKpC7/8+AHDYSy0CxKErCTQimUGXEFqU5a6zBAA7");
    background-position: 0 -5px
}

.x-box-scroller-toolbar-default.x-box-scroller-top.x-box-scroller-hover {
    background-position: 0 0
}

.x-box-scroller-toolbar-default.x-box-scroller-bottom {
    margin-top: 5px;
    margin-right: 0;
    margin-bottom: 5px;
    background-image: url("data:image/gif;R0lGODlhIwAKAMIEADxdk5m86Mna7uDq9f///////////////yH5BAEKAAQALAAAAAAjAAoAAAM8GLrc/o8EQautIOfLaSDg1F3aeH1gaFrAWqFpCM1zTN+4Ig187/eazG/IgwWIQw3yBwstfYBnr5nKWWMJADs=");
    background-position: 0 0
}

.x-box-scroller-toolbar-default.x-box-scroller-bottom.x-box-scroller-hover {
    background-position: 0 -5px
}

.x-ie8 .x-box-scroller-toolbar-default {
    background-color: #d3e1f1
}

.x-toolbar-more-icon {
    background-image: url("data:image/gif;R0lGODlhDAAQAIcAABVCi0D/QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAMAAAEALAAAAAAMABAAAAgqAAMIHEiwoMGDCBMqXIgQAACBDg9GDDCx4MSKEB9S1DjwIkeGIEOKPBgQADs=")
}

.x-cmd-slicer.x-toolbar-default:before {
    display: none;
    content: "x-slicer:, bg:url("data:image/gif;R0lGODlhAQAgA/QAANPh8dTh8dTi8dXi8tbj8tfk8tjk89jl89nl89rl89rm89vm9Nzn9N3o9N7o9d7p9d/p9f///9Ph8dPh8dPh8dPh8dPh8dPh8dPh8dPh8dPh8dPh8dPh8dPh8dPh8dPh8SH5BAEAABEALAAAAAABACADRAhMACEsKBAAgMGDCBMqXMiwocOHECMmbICAgMSLGDNqzOiAgYIDBAZsHEmypMmTKFNKfNCAAYMFCRAYKBBSgMqbOHPq3Mmzp8+fQH8GBAA7"), stretch:bottom" !important
}

.x-toolbar-footer {
    padding: 4px 0 4px 6px;
    border-style: solid;
    border-color: #99bce8;
    border-width: 0;
    background-image: none;
    background-color: transparent
}

.x-toolbar-footer .x-toolbar-item {
    margin: 0 6px 0 0
}

.x-toolbar-footer .x-toolbar-separator-horizontal {
    margin: 0 2px 0 0;
    height: 14px;
    border-style: solid;
    border-width: 0 1px;
    border-left-color: #98c8ff;
    border-right-color: #fff
}

.x-toolbar-footer .x-box-menu-after {
    margin: 0 6px
}

.x-toolbar-footer-vertical {
    padding: 4px 6px 0
}

.x-toolbar-footer-vertical .x-toolbar-item {
    margin: 0 0 4px 0
}

.x-toolbar-footer-vertical .x-toolbar-separator-vertical {
    margin: 0 5px 2px;
    border-style: solid none;
    border-width: 1px 0;
    border-top-color: #98c8ff;
    border-bottom-color: #fff
}

.x-toolbar-footer-vertical .x-box-menu-after {
    margin: 4px 0
}

.x-nlg .x-toolbar-footer {
    background-image: url(images/toolbar/toolbar-footer-bg.gif) !important;
    background-repeat: repeat-x
}

.x-toolbar-text-footer {
    padding: 0 4px;
    color: #4d4d4d;
    font: normal 11px/16px tahoma, arial, verdana, sans-serif
}

.x-toolbar-spacer-footer {
    width: 2px
}

.x-toolbar-footer-scroller .x-box-scroller-body-horizontal {
    margin-left: 8px
}

.x-toolbar-footer-vertical-scroller .x-box-scroller-body-vertical {
    margin-top: 11px
}

.x-box-scroller-toolbar-footer {
    cursor: pointer;
    color: #eee
}

.x-box-scroller-toolbar-footer.x-box-scroller-disabled {
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=50)";
    opacity: 0.5;
    cursor: default
}

.x-box-scroller-toolbar-footer.x-box-scroller-left, .x-box-scroller-toolbar-footer.x-box-scroller-right {
    width: 14px;
    height: 22px;
    border-style: solid;
    border-color: #8db2e3;
    border-width: 0 0 1px;
    top: 50%;
    margin-top: -11px
}

.x-box-scroller-toolbar-footer.x-box-scroller-left {
    margin-left: 0;
    margin-right: 0;
    margin-bottom: 0;
    background-image: url("data:image/gif;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");
    background-position: -14px 0
}

.x-box-scroller-toolbar-footer.x-box-scroller-left.x-box-scroller-hover {
    background-position: 0 0
}

.x-box-scroller-toolbar-footer.x-box-scroller-right {
    margin-left: 0;
    margin-right: 0;
    margin-bottom: 0;
    background-image: url("data:image/gif;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");
    background-position: 0 0
}

.x-box-scroller-toolbar-footer.x-box-scroller-right.x-box-scroller-hover {
    background-position: -14px 0
}

.x-ie8 .x-box-scroller-toolbar-footer {
    background-color: transparent
}

.x-toolbar-more-icon {
    background-image: url("data:image/gif;R0lGODlhDAAQAIcAABVCi0D/QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAMAAAEALAAAAAAMABAAAAgqAAMIHEiwoMGDCBMqXIgQAACBDg9GDDCx4MSKEB9S1DjwIkeGIEOKPBgQADs=")
}

.x-cmd-slicer.x-toolbar-footer:before {
    display: none;
    content: "x-slicer:, bg:url(images/toolbar/toolbar-footer-bg.gif), stretch:bottom" !important
}

.x-dd-drag-proxy {
    color: #000;
    font: normal 11px/normal tahoma, arial, verdana, sans-serif;
    border-width: 1px;
    border-style: solid;
    border-color: #ddd #bbb #bbb #ddd;
    background-color: #fff
}

.x-dd-drag-ghost, .x-dd-drop-icon {
    padding: 5px
}

.x-dd-drag-ghost {
    padding-left: 0
}

.x-dd-drop-ok .x-dd-drop-icon {
    background-image: url("data:image/gif;R0lGODlhEAAQAIcAACdyJCZ/Iyl3JSl6JTR8MDV/MSaEIyqPJTWPMT+FOz+LOz+NOz+ZPDuhJ0yXPUKhM0ShM0mwJ1G3LlWzNV21P1q+N06bQVKgQl6pSGSwTGy2Vm23V261WG+1WG+1WWq5UHS3W3S3XHC/V3C4WXG5W3K5W3O6XHG+X3e8YH23Zny6ZH28Zn2+Z3+4aVzAO1zDPWbFSWrDSWzFS2nISnTCWXLLVW/CYW/DYW7EYW7EYm7FY2/GZHDBY3HEY3DHZXPHZnTDZHLIaHTIaHXIaHbJaXbKannBZH7BaX7Hb3nJa3rMbX/KcIO+bYfCcoXFdYDKc4DMcoPOd4fJeYnEdovIeJDOf5G5j5C8jpbHg5HAj5bLhpfMhZTIj5bNiJrHh5jLhprKh5jMh5nNip3Oi5nRi5nQjJrUjZvXkZ/SkJ/SkZ3YkqHWlaHXlaPXlqvSm6vTm6rcl63fm67Xoa/XoK7cpa/cprPZpbHdp7TZpbTaprLbqLXbqLTdqrTfrLXfrLbQtbbRtbfZtbrbtb7ftbDjn7Xhrrfhr7fhsL7jtr/juMHjtsDkucvsv8DAwMvtwNbu0tns1Ob04+336/H58PT68vz9+/3+/f///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAMAAI0ALAAAAAAQABAAAAjVABsJHEiwoEFCNVxUiAHHoEBHM2i0oUNnzYcJigoyelHFkJooUdQUotJgEEEYVQopKRJEyJAkfaY8GBhHhCElQXzoyNEDERI/GLgIlMHmDJEdOG7YWHQpEpkxDARKuAPlx6FHPBJdqlTmiBwDAiPUWfJk0iVJW7uQYDEngEAKacwAkULpkiUtG0ps8aJAIJoMfIyccAJJjAYOIfJYuDIQQhM9KEyM8NABhJ0WBQgKOsBkT5gVKr7gSQEAUMFACC6AeeMGiwMCfxw2yrJggIAEVmTrJhgQADs=")
}

.x-dd-drop-ok-add .x-dd-drop-icon {
    background-image: url("data:image/gif;R0lGODlhEAAQAIcAAD2GNUKNNkOPOESMO0WNPEmPP0iNQUmPQlOVTFWWTVCZQVeeRV6cVmGeWGSgVWSgV2aiWGejW2WrVWirU2uqWGqsW2yqWm61WG+1WG+1WXS3W3S3XHC4WXK5W3O6XHG+X3asZ3iuaHe8YHi0ZH+yany6ZH28Zn2+Z3m9bn25an25a3+5bXDBY3nBZHrGa3zDa37BaX7Hb4K1boO1boa3cYi4d4y7doq5eYm+eI2+e5O/f4HMdYbJeobJfIXNeYrCeY/CfYnIf4rPfZW/gozLgY7MhI7Sg5LFgJXAgpfHhZfMhZPNiJjLhpjMh5jMipvBl5vBmJTTipbTiZXUipbUi5fVi5nRi53YkqTOlKbPlqbQlqDZlaDZlqXbm6rUnavUnKbIoKfJoa/fpa/fprPZpbTZpbTaprLbqLPdqbXbqLfaqrTdqrXfrLbdrLjVr7jdr7vcr7rWsbzVubfgr77itr3ktsTcuMXducnexMrexcXowMvmw8zgxs3gx87pydTrz9fu0tnp0dzx2ODy3OPt4ePu4ufw5ejx5uvz6e/27P///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAMAAIsALAAAAAAQABAAAAjGABcJHEiwoME7SGjIuBHHoMBAOrDs+ePnzYoQfQoGsgFnUJ0uXMTo+QEhD0EdagRdWVKEyhQjc1REGGgnCaAtUYIoUuTjRQw2C8IIHNJmDJEeKHZWEOHBypEGAmfQqcJjp1VFHGB4KSCQBBohO67u5HDiywCBNZxIccFCwlgOHZTkSCDQzYQ1LT6IGHthgxkBTwaCSHGGKYcMGDSQsXCAIB8HI9I0MVGCSRkKAOQUxPNAARAtWXAEMKDZIRgGBQgggOKwtcGAADs=")
}

.x-dd-drop-nodrop div.x-dd-drop-icon {
    background-image: url("data:image/gif;R0lGODlhEAAQAIcAAMAAAMEEBMQQEMUUFMccHMkkJM00NM88PNRQUNVUVNlkZNpoaNxwcN10dOSQkOecnOmkpOuwsO24uO68vO/AwPDExPHIyPLMzPXY2Pfg4Pjk5Pno6Pvw8Pz09P34+P///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAMAAB8ALAAAAAAQABAAAAiSAD8IHNiBAoUOAxMOjGAAgMMAByoo/LABAQACDSA8YCAAgAKEAy0u4JBQg0MGCwE0mOgQQIALAg0UADmwpYYBCT50AOBAYUuBDAZ8oABgQsKfAh8AyCChaE2HCZVi4MBTINKBQWPOvCrwZs4PEVoCmJjgZUiHJAdqSAAA5cCKFzNu7PhxIsOWECVOJCjBgoeJAQEAOw==")
}

.x-panel-ghost {
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=65)";
    opacity: 0.65
}

.x-panel-default {
    border-color: #99bce8;
    padding: 0
}

.x-panel-header-default {
    font-size: 11px;
    border: 1px solid #99bce8
}

.x-panel-header-default-horizontal {
    padding: 5px
}

.x-panel-header-default-horizontal .x-panel-header-default-tab-bar {
    margin-top: -5px;
    margin-bottom: -5px
}

.x-panel-header-default-horizontal.x-header-noborder {
    padding: 6px 6px 5px 6px
}

.x-panel-header-default-horizontal.x-header-noborder .x-panel-header-default-tab-bar {
    margin-top: -6px;
    margin-bottom: -5px
}

.x-panel-header-default-vertical {
    padding: 5px 5px 5px 5px
}

.x-panel-header-default-vertical .x-panel-header-default-tab-bar {
    margin-right: -5px;
    margin-left: -5px
}

.x-panel-header-default-vertical.x-header-noborder {
    padding: 6px 6px 6px 5px
}

.x-panel-header-default-vertical.x-header-noborder .x-panel-header-default-tab-bar {
    margin-right: -6px;
    margin-left: -5px
}

.x-panel-header-title-default {
    color: #04408c;
    font-size: 11px;
    font-weight: bold;
    font-family: tahoma, arial, verdana, sans-serif;
    line-height: 15px
}

.x-panel-header-title-default > .x-title-text-default {
    text-transform: none;
    padding: 0 2px 1px
}

.x-panel-header-title-default > .x-title-icon-wrap-default.x-title-icon-top {
    height: 18px;
    padding-bottom: 2px
}

.x-panel-header-title-default > .x-title-icon-wrap-default.x-title-icon-right {
    width: 18px;
    padding-left: 2px
}

.x-panel-header-title-default > .x-title-icon-wrap-default.x-title-icon-bottom {
    height: 18px;
    padding-top: 2px
}

.x-panel-header-title-default > .x-title-icon-wrap-default.x-title-icon-left {
    width: 18px;
    padding-right: 2px
}

.x-panel-header-title-default > .x-title-icon-wrap-default > .x-title-icon-default {
    width: 16px;
    height: 16px;
    font-size: 16px;
    color: #04408c;
    background-position: center center
}

.x-panel-header-title-default > .x-title-icon-wrap-default > .x-title-icon-default.x-title-glyph {
    opacity: 0.5
}

.x-ie8 .x-panel-header-title-default > .x-title-icon-wrap-default > .x-title-icon-default.x-title-glyph {
    color: #678fc0
}

.x-panel-body-default {
    background: #fff;
    border-color: #99bce8;
    color: #000;
    font-size: 12px;
    font-weight: normal;
    font-family: tahoma, arial, verdana, sans-serif;
    border-width: 1px;
    border-style: solid
}

.x-panel-header-default {
    background-image: none;
    background-color: #cbddf3;
    background-image: -webkit-gradient(linear, top, bottom, color-stop(0%, #dae7f6), color-stop(45%, #cddef3), color-stop(46%, #abc7ec), color-stop(50%, #abc7ec), color-stop(51%, #b8cfee), color-stop(0%, #cbddf3));
    background-image: -webkit-linear-gradient(top, #dae7f6, #cddef3 45%, #abc7ec 46%, #abc7ec 50%, #b8cfee 51%, #cbddf3);
    background-image: -moz-linear-gradient(top, #dae7f6, #cddef3 45%, #abc7ec 46%, #abc7ec 50%, #b8cfee 51%, #cbddf3);
    background-image: -o-linear-gradient(top, #dae7f6, #cddef3 45%, #abc7ec 46%, #abc7ec 50%, #b8cfee 51%, #cbddf3);
    background-image: -ms-linear-gradient(top, #dae7f6, #cddef3 45%, #abc7ec 46%, #abc7ec 50%, #b8cfee 51%, #cbddf3);
    background-image: linear-gradient(top, #dae7f6, #cddef3 45%, #abc7ec 46%, #abc7ec 50%, #b8cfee 51%, #cbddf3)
}

.x-panel-header-default-vertical {
    background-image: none;
    background-color: #cbddf3;
    background-image: -webkit-gradient(linear, top, bottom, color-stop(0%, #dae7f6), color-stop(45%, #cddef3), color-stop(46%, #abc7ec), color-stop(50%, #abc7ec), color-stop(51%, #b8cfee), color-stop(0%, #cbddf3));
    background-image: -webkit-linear-gradient(right, #dae7f6, #cddef3 45%, #abc7ec 46%, #abc7ec 50%, #b8cfee 51%, #cbddf3);
    background-image: -moz-linear-gradient(right, #dae7f6, #cddef3 45%, #abc7ec 46%, #abc7ec 50%, #b8cfee 51%, #cbddf3);
    background-image: -o-linear-gradient(right, #dae7f6, #cddef3 45%, #abc7ec 46%, #abc7ec 50%, #b8cfee 51%, #cbddf3);
    background-image: -ms-linear-gradient(right, #dae7f6, #cddef3 45%, #abc7ec 46%, #abc7ec 50%, #b8cfee 51%, #cbddf3);
    background-image: linear-gradient(right, #dae7f6, #cddef3 45%, #abc7ec 46%, #abc7ec 50%, #b8cfee 51%, #cbddf3)
}

.x-nlg .x-panel-header-default-top {
    background: url("data:image/gif;R0lGODlhAQAgA/QAAKvH7LjP7rnQ7rvR7rzS777T77/U8MHV8MLW8MTY8cXZ8cfa8sjb8src8s3e887e88/f89Dg89Hh9NLi9NPi9NTj9Nbk9dfl9djl9fP3+////6vH7KvH7KvH7KvH7KvH7CH5BAEAABoALAAAAAABACADRAhNADNEIMCggcGDCBMqXMiwocOHECMmrAAAgcSLGDNqzHhhwgMBBhRsHEmypMmTKFNKxGCBggQIDgIMKHAgwQKVOHPq3Mmzp8+fQIMCDQgAOw==")
}

.x-nlg .x-panel-header-default-bottom {
    background: url("data:image/gif;R0lGODlhAQAgA/QAAKvH7LjP7rnQ7rvR7rzS777T77/U8MHV8MLW8MTY8cXZ8cfa8sjb8s3e887e88/f89Dg89Hh9NLi9NPi9NTj9Nbk9dfl9djl9dnm9fP3+////6vH7KvH7KvH7KvH7KvH7CH5BAEAABoALAAAAAABACADRAhNADEIHEiwoMGDCBMqXMiwoUELDgw4nEixosWKEgQouMixo8ePIEOKdEgBAgACCBiMXMmypcuXMGPKnElT5oUKEyI8aBBgQIEDCRZkCAgAOw==") bottom left
}

.x-nlg .x-panel-header-default-left {
    background: url("data:image/gif;R0lGODlhIAMBAPQAAKvH7LjP7rnQ7rvR7rzS777T77/U8MHV8MLW8MTY8cXZ8cfa8sjb8s3e887e88/f89Dg89Hh9NLi9NPi9NTj9Nbk9dfl9djl9dnm9fP3+////6vH7KvH7KvH7KvH7KvH7CH5BAEAABoALAAAAAAgAwEARAhLADMwWKAgAYIDBgoQGCAgAIAGDh5AiCBhAoUKFi5g2Mixo8ePIEOKHEmypMmTKFOqXMmypcuXMGPKnEmzps2bOHPq3Mmzp8+fOwMCADs=") top left
}

.x-nlg .x-panel-header-default-right {
    background: url("data:image/gif;R0lGODlhIAMBAPQAAKvH7LjP7rnQ7rvR7rzS777T77/U8MHV8MLW8MTY8cXZ8cfa8sjb8src8s3e887e88/f89Dg89Hh9NLi9NPi9NTj9Nbk9dfl9djl9fP3+////6vH7KvH7KvH7KvH7KvH7CH5BAEAABoALAAAAAAgAwEARAhLABsIHEiwoMGDCBMqXMiwocOHECNKnEixosWLGDNq3Mixo8ePIEOKHEmypEmRDBYoSIDggIECBAYICADAwQMIESRMoFDBwgUMGQICADs=") top right
}

.x-panel .x-panel-header-default-collapsed-border-top {
    border-bottom-width: 1px !important
}

.x-panel .x-panel-header-default-collapsed-border-right {
    border-left-width: 1px !important
}

.x-panel .x-panel-header-default-collapsed-border-bottom {
    border-top-width: 1px !important
}

.x-panel .x-panel-header-default-collapsed-border-left {
    border-right-width: 1px !important
}

.x-cmd-slicer.x-panel-header-default-top:before {
    display: none;
    content: "x-slicer:, bg:url("data:image/gif;R0lGODlhAQAgA/QAAKvH7LjP7rnQ7rvR7rzS777T77/U8MHV8MLW8MTY8cXZ8cfa8sjb8src8s3e887e88/f89Dg89Hh9NLi9NPi9NTj9Nbk9dfl9djl9fP3+////6vH7KvH7KvH7KvH7KvH7CH5BAEAABoALAAAAAABACADRAhNADNEIMCggcGDCBMqXMiwocOHECMmrAAAgcSLGDNqzHhhwgMBBhRsHEmypMmTKFNKxGCBggQIDgIMKHAgwQKVOHPq3Mmzp8+fQIMCDQgAOw=="), stretch:bottom" !important
}

.x-cmd-slicer.x-panel-header-default-bottom:before {
    display: none;
    content: "x-slicer:, bg:url("data:image/gif;R0lGODlhAQAgA/QAAKvH7LjP7rnQ7rvR7rzS777T77/U8MHV8MLW8MTY8cXZ8cfa8sjb8s3e887e88/f89Dg89Hh9NLi9NPi9NTj9Nbk9dfl9djl9dnm9fP3+////6vH7KvH7KvH7KvH7KvH7CH5BAEAABoALAAAAAABACADRAhNADEIHEiwoMGDCBMqXMiwoUELDgw4nEixosWKEgQouMixo8ePIEOKdEgBAgACCBiMXMmypcuXMGPKnElT5oUKEyI8aBBgQIEDCRZkCAgAOw=="), stretch:top" !important
}

.x-cmd-slicer.x-panel-header-default-left:before {
    display: none;
    content: "x-slicer:, bg:url("data:image/gif;R0lGODlhIAMBAPQAAKvH7LjP7rnQ7rvR7rzS777T77/U8MHV8MLW8MTY8cXZ8cfa8sjb8s3e887e88/f89Dg89Hh9NLi9NPi9NTj9Nbk9dfl9djl9dnm9fP3+////6vH7KvH7KvH7KvH7KvH7CH5BAEAABoALAAAAAAgAwEARAhLADMwWKAgAYIDBgoQGCAgAIAGDh5AiCBhAoUKFi5g2Mixo8ePIEOKHEmypMmTKFOqXMmypcuXMGPKnEmzps2bOHPq3Mmzp8+fOwMCADs="), stretch:right" !important
}

.x-cmd-slicer.x-panel-header-default-right:before {
    display: none;
    content: "x-slicer:, bg:url("data:image/gif;R0lGODlhIAMBAPQAAKvH7LjP7rnQ7rvR7rzS777T77/U8MHV8MLW8MTY8cXZ8cfa8sjb8src8s3e887e88/f89Dg89Hh9NLi9NPi9NTj9Nbk9dfl9djl9fP3+////6vH7KvH7KvH7KvH7KvH7CH5BAEAABoALAAAAAAgAwEARAhLABsIHEiwoMGDCBMqXMiwocOHECNKnEixosWLGDNq3Mixo8ePIEOKHEmypEmRDBYoSIDggIECBAYICADAwQMIESRMoFDBwgUMGQICADs="), stretch:left" !important
}

.x-panel-header-default-top {
    -webkit-box-shadow: #f3f7fb 0 1px 0px 0 inset;
    -moz-box-shadow: #f3f7fb 0 1px 0px 0 inset;
    box-shadow: #f3f7fb 0 1px 0px 0 inset
}

.x-panel-header-default-right {
    -webkit-box-shadow: #f3f7fb -1px 0 0px 0 inset;
    -moz-box-shadow: #f3f7fb -1px 0 0px 0 inset;
    box-shadow: #f3f7fb -1px 0 0px 0 inset
}

.x-panel-header-default-bottom {
    -webkit-box-shadow: #f3f7fb 0 -1px 0px 0 inset;
    -moz-box-shadow: #f3f7fb 0 -1px 0px 0 inset;
    box-shadow: #f3f7fb 0 -1px 0px 0 inset
}

.x-panel-header-default-left {
    -webkit-box-shadow: #f3f7fb 1px 0 0px 0 inset;
    -moz-box-shadow: #f3f7fb 1px 0 0px 0 inset;
    box-shadow: #f3f7fb 1px 0 0px 0 inset
}

.x-panel-header-default-horizontal .x-tool-after-title {
    margin: 0 0 0 2px
}

.x-panel-header-default-horizontal .x-tool-before-title {
    margin: 0 2px 0 0
}

.x-panel-header-default-vertical .x-tool-after-title {
    margin: 2px 0 0 0
}

.x-panel-header-default-vertical .x-tool-before-title {
    margin: 0 0 2px 0
}

.x-panel-header-default .x-tool-focus {
    outline: 1px dotted #464646;
    outline-offset: 0
}

.x-ie8 .x-panel-header-default .x-tool-focus {
    outline: none
}

.x-ie8 .x-panel-header-default .x-tool-focus:after {
    position: absolute;
    content: ' ';
    top: -1px;
    right: -1px;
    bottom: -1px;
    left: -1px;
    border: 1px dotted #464646;
    pointer-events: none
}

.x-panel-default-resizable .x-panel-handle {
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=0)";
    opacity: 0
}

.x-panel-default-framed {
    border-color: #99bce8;
    padding: 4px
}

.x-panel-header-default-framed {
    font-size: 11px;
    border: 1px solid #99bce8
}

.x-panel-header-default-framed-horizontal {
    padding: 5px
}

.x-panel-header-default-framed-horizontal .x-panel-header-default-framed-tab-bar {
    margin-top: -5px;
    margin-bottom: -5px
}

.x-panel-header-default-framed-horizontal.x-header-noborder {
    padding: 6px 6px 5px 6px
}

.x-panel-header-default-framed-horizontal.x-header-noborder .x-panel-header-default-framed-tab-bar {
    margin-top: -6px;
    margin-bottom: -5px
}

.x-panel-header-default-framed-vertical {
    padding: 5px 5px 5px 5px
}

.x-panel-header-default-framed-vertical .x-panel-header-default-framed-tab-bar {
    margin-right: -5px;
    margin-left: -5px
}

.x-panel-header-default-framed-vertical.x-header-noborder {
    padding: 6px 6px 6px 5px
}

.x-panel-header-default-framed-vertical.x-header-noborder .x-panel-header-default-framed-tab-bar {
    margin-right: -6px;
    margin-left: -5px
}

.x-panel-header-title-default-framed {
    color: #04408c;
    font-size: 11px;
    font-weight: bold;
    font-family: tahoma, arial, verdana, sans-serif;
    line-height: 15px
}

.x-panel-header-title-default-framed > .x-title-text-default-framed {
    text-transform: none;
    padding: 0 2px 1px
}

.x-panel-header-title-default-framed > .x-title-icon-wrap-default-framed.x-title-icon-top {
    height: 18px;
    padding-bottom: 2px
}

.x-panel-header-title-default-framed > .x-title-icon-wrap-default-framed.x-title-icon-right {
    width: 18px;
    padding-left: 2px
}

.x-panel-header-title-default-framed > .x-title-icon-wrap-default-framed.x-title-icon-bottom {
    height: 18px;
    padding-top: 2px
}

.x-panel-header-title-default-framed > .x-title-icon-wrap-default-framed.x-title-icon-left {
    width: 18px;
    padding-right: 2px
}

.x-panel-header-title-default-framed > .x-title-icon-wrap-default-framed > .x-title-icon-default-framed {
    width: 16px;
    height: 16px;
    font-size: 16px;
    color: #04408c;
    background-position: center center
}

.x-panel-header-title-default-framed > .x-title-icon-wrap-default-framed > .x-title-icon-default-framed.x-title-glyph {
    opacity: 0.5
}

.x-ie8 .x-panel-header-title-default-framed > .x-title-icon-wrap-default-framed > .x-title-icon-default-framed.x-title-glyph {
    color: #678fc0
}

.x-panel-body-default-framed {
    background: #dfe9f6;
    border-color: #99bce8;
    color: #000;
    font-size: 12px;
    font-weight: normal;
    font-family: tahoma, arial, verdana, sans-serif;
    border-width: 0;
    border-style: solid
}

.x-panel-default-framed {
    -webkit-border-radius: 4px;
    -moz-border-radius: 4px;
    -ms-border-radius: 4px;
    -o-border-radius: 4px;
    border-radius: 4px;
    padding: 4px 4px 4px 4px;
    border-width: 1px;
    border-style: solid;
    background-color: #dfe9f6
}

.x-panel-default-framed-mc {
    background-color: #dfe9f6
}

.x-nbr .x-panel-default-framed {
    padding: 0 !important;
    border-width: 0 !important;
    -webkit-border-radius: 0px;
    -moz-border-radius: 0px;
    -ms-border-radius: 0px;
    -o-border-radius: 0px;
    border-radius: 0px;
    background-color: transparent !important;
    box-shadow: none !important
}

.x-panel-default-framed-frameInfo {
    font-family: dh-4-4-4-4-1-1-1-1-4-4-4-4
}

.x-panel-default-framed-tl {
    background-position: 0 -8px
}

.x-panel-default-framed-tr {
    background-position: right -12px
}

.x-panel-default-framed-bl {
    background-position: 0 -16px
}

.x-panel-default-framed-br {
    background-position: right -20px
}

.x-panel-default-framed-ml {
    background-position: 0 top
}

.x-panel-default-framed-mr {
    background-position: right top
}

.x-panel-default-framed-tc {
    background-position: 0 0
}

.x-panel-default-framed-bc {
    background-position: 0 -4px
}

.x-panel-default-framed-tr, .x-panel-default-framed-br, .x-panel-default-framed-mr {
    padding-right: 4px
}

.x-panel-default-framed-tl, .x-panel-default-framed-bl, .x-panel-default-framed-ml {
    padding-left: 4px
}

.x-panel-default-framed-tc {
    height: 4px
}

.x-panel-default-framed-bc {
    height: 4px
}

.x-panel-default-framed-tl, .x-panel-default-framed-bl, .x-panel-default-framed-tr, .x-panel-default-framed-br, .x-panel-default-framed-tc, .x-panel-default-framed-bc, .x-panel-default-framed-ml, .x-panel-default-framed-mr {
    background-image: url("data:image/gif;R0lGODlhBAAYAPMAAJm86KHB66LC6qPC6rvS77/U79jk9djl9d/p9vL3/PP3/P///wAAAJm86Jm86Jm86CH5BAEAAAsALAAAAAAEABgAQwhGAAEIBLBAAQEBAg4gWMhQAIEECxYaGMCwIgICBSoWeBiggAEDBQIksEgSwUAACToeSLjwQMiRCCZiXLggAQGKCDYOeLggIAA7")
}

.x-panel-default-framed-ml, .x-panel-default-framed-mr {
    background-image: url("data:image/gif;R0lGODlhCADAAPEAAJm86N/p9v///5m86CH5BAEAAAIALAAAAAAIAMAAQQilAAEEGEgQgECCAw0iTHgQocKFDx02LDiR4cIAESlezGgRYkWMHzmC3BiyJMmTHlFKVKkxpcuVL1vCnCmzZkeaN22OjJmz506cP3WKHGqSZ1CfRFkiLQo0qVGnTZkKlbpU6dGrUKdazVr1KVWsX7mC3Rq2LNmzXtFGVas1rdu1b9vCnSu3ble6d+2OjZu37168f/WKHWyWb2C/hNkiLgw4sWHHDgMCADs=");
    background-repeat: repeat-y
}

.x-panel-default-framed-mc {
    padding: 1px 1px 1px 1px
}

.x-cmd-slicer.x-panel-default-framed:before {
    display: none;
    content: "x-slicer:, frame:4px 4px 4px 4px, corners:url("data:image/gif;R0lGODlhBAAYAPMAAJm86KHB66LC6qPC6rvS77/U79jk9djl9d/p9vL3/PP3/P///wAAAJm86Jm86Jm86CH5BAEAAAsALAAAAAAEABgAQwhGAAEIBLBAAQEBAg4gWMhQAIEECxYaGMCwIgICBSoWeBiggAEDBQIksEgSwUAACToeSLjwQMiRCCZiXLggAQGKCDYOeLggIAA7"), sides:url("data:image/gif;R0lGODlhCADAAPEAAJm86N/p9v///5m86CH5BAEAAAIALAAAAAAIAMAAQQilAAEEGEgQgECCAw0iTHgQocKFDx02LDiR4cIAESlezGgRYkWMHzmC3BiyJMmTHlFKVKkxpcuVL1vCnCmzZkeaN22OjJmz506cP3WKHGqSZ1CfRFkiLQo0qVGnTZkKlbpU6dGrUKdazVr1KVWsX7mC3Rq2LNmzXtFGVas1rdu1b9vCnSu3ble6d+2OjZu37168f/WKHWyWb2C/hNkiLgw4sWHHDgMCADs=")" !important
}

.x-panel-header-default-framed-top {
    -moz-border-radius-topleft: 4px;
    -webkit-border-top-left-radius: 4px;
    border-top-left-radius: 4px;
    -moz-border-radius-topright: 4px;
    -webkit-border-top-right-radius: 4px;
    border-top-right-radius: 4px;
    -moz-border-radius-bottomright: 0;
    -webkit-border-bottom-right-radius: 0;
    border-bottom-right-radius: 0;
    -moz-border-radius-bottomleft: 0;
    -webkit-border-bottom-left-radius: 0;
    border-bottom-left-radius: 0;
    padding: 5px 5px 5px 5px;
    border-width: 1px 1px 0 1px;
    border-style: solid;
    background-image: none;
    background-color: #cbddf3;
    background-image: -webkit-gradient(linear, top, bottom, color-stop(0%, #dae7f6), color-stop(45%, #cddef3), color-stop(46%, #abc7ec), color-stop(50%, #abc7ec), color-stop(51%, #b8cfee), color-stop(0%, #cbddf3));
    background-image: -webkit-linear-gradient(top, #dae7f6, #cddef3 45%, #abc7ec 46%, #abc7ec 50%, #b8cfee 51%, #cbddf3);
    background-image: -moz-linear-gradient(top, #dae7f6, #cddef3 45%, #abc7ec 46%, #abc7ec 50%, #b8cfee 51%, #cbddf3);
    background-image: -o-linear-gradient(top, #dae7f6, #cddef3 45%, #abc7ec 46%, #abc7ec 50%, #b8cfee 51%, #cbddf3);
    background-image: -ms-linear-gradient(top, #dae7f6, #cddef3 45%, #abc7ec 46%, #abc7ec 50%, #b8cfee 51%, #cbddf3);
    background-image: linear-gradient(top, #dae7f6, #cddef3 45%, #abc7ec 46%, #abc7ec 50%, #b8cfee 51%, #cbddf3)
}

.x-panel-header-default-framed-top-mc {
    background-image: url("data:image/gif;R0lGODlhAQAgA/QAAKvH7LjP7rnQ7rvR7rzS777T77/U8MHV8MLW8MTY8cXZ8c3e887e88/f89Dg89Hh9NLi9NPi9NTj9Nbk9f///6vH7KvH7KvH7KvH7KvH7KvH7KvH7KvH7KvH7KvH7KvH7CH5BAEAABQALAAAAAABACADRAhHACcsOKCgoMGDCBMqXMiwocOHEBM+GBCxosWLGDFGaBCgQIKMIEOKHEmypMmKEiA4YABAAAEDCE7KnEmzps2bOHPq3MlTQUAAOw==");
    background-position: 0 top;
    background-color: #cbddf3
}

.x-nbr .x-panel-header-default-framed-top {
    padding: 0 !important;
    border-width: 0 !important;
    -webkit-border-radius: 0px;
    -moz-border-radius: 0px;
    -ms-border-radius: 0px;
    -o-border-radius: 0px;
    border-radius: 0px;
    background-color: transparent !important;
    background-image: none;
    box-shadow: none !important
}

.x-panel-header-default-framed-top-frameInfo {
    font-family: dh-4-4-0-4-1-1-0-1-5-5-5-5
}

.x-panel-header-default-framed-top-tl {
    background-position: 0 -8px
}

.x-panel-header-default-framed-top-tr {
    background-position: right -12px
}

.x-panel-header-default-framed-top-bl {
    background-position: 0 -16px
}

.x-panel-header-default-framed-top-br {
    background-position: right -20px
}

.x-panel-header-default-framed-top-ml {
    background-position: 0 top
}

.x-panel-header-default-framed-top-mr {
    background-position: right top
}

.x-panel-header-default-framed-top-tc {
    background-position: 0 0
}

.x-panel-header-default-framed-top-bc {
    background-position: 0 -4px
}

.x-panel-header-default-framed-top-tr, .x-panel-header-default-framed-top-br, .x-panel-header-default-framed-top-mr {
    padding-right: 4px
}

.x-panel-header-default-framed-top-tl, .x-panel-header-default-framed-top-bl, .x-panel-header-default-framed-top-ml {
    padding-left: 4px
}

.x-panel-header-default-framed-top-tc {
    height: 4px
}

.x-panel-header-default-framed-top-bc {
    height: 0
}

.x-panel-header-default-framed-top-tl, .x-panel-header-default-framed-top-bl, .x-panel-header-default-framed-top-tr, .x-panel-header-default-framed-top-br, .x-panel-header-default-framed-top-tc, .x-panel-header-default-framed-top-bc, .x-panel-header-default-framed-top-ml, .x-panel-header-default-framed-top-mr {
    background-image: url("data:image/gif;R0lGODlhBAAYAPQAAJm86KHB66LC6qPC6rvS78fa8sjb8src8tbj9dbk9tfl9djl9drn9tvn9urx+e70+u71+u/0+vL3/PP3+/P3/P///wAAAJm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86CH5BAEAABUALAAAAAAEABgARAhRAAEIBFCBAgEBACYUWMhQAAEJFRZOALCg4oIDGA8QQOCgQQMHCAgkzHhg4oSTExSoVGCgpYGBACQESBBBwAMGCiIkCCBBAQMIAxK2hNlyIsyAADs=")
}

.x-panel-header-default-framed-top-ml, .x-panel-header-default-framed-top-mr {
    background-image: url("data:image/gif;R0lGODlhCAAgA/QAAJm86KvH7LjP7rnQ7rvR7rzS777T77/U8MHV8MLW8MTY8cXZ8c3e887e88/f89Dg89Hh9NLi9NPi9NTj9Nbk9fP3+////5m86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86CH5BAEAABYALAAAAAAIACADRAj/AAFUoECQQgUAAhkoZHBQIIKHCBpWWEBxgcSKFhFOrHiRo0aMHSmGzCgQ5EePJVFuFHmSZUqXK0nGHEmzpUyTL2+qxDnTZs2cP3sC9Ul0qFGhSHkq3ckU5lKnTXVCnSq1atCnVosmjXqVq1asXamGzXoU7FevZdFuFXuWbVq3a8nGHUtXK4S7ECQS2Eug7lu5Zv/6ndsWsNrAhAUXHoy48eHHcB1Hhmx4suXKmBlT1nyZc+bFoBWLTkxa8ufRpj2r1iihtQSJDmI7kCigtgCJBnIbkKigt4LVqDeHLi08eOfhqZEXJ37c+Gnmz5M7Bw6duvTqyptjn549+vLr4L+Lxdcenvx47+bTo19v/Xx79e/Zd49Pf7597vi36y8vPz//+qNNIOAEEkVgYAQSPaDgAxI14GADEgUgYQASDWDhABIVoGEBEh3g4QESJSBiAgDu5959JsKH4n8rnuifiyn2F2OJLL6ooo0y1jhjizfuiCONMOooZJBE9jikkUXmmCSQSDappJNMPilllFTyOKWVVf6I5ZZadunjl0de6WWYWYK5JJdmQokmmWueOaabaYoZZ5lsvqmmnXLWOWebd+6JJ51wmhUQADs=")
}

.x-panel-header-default-framed-top-mc {
    padding: 2px 2px 5px 2px
}

.x-cmd-slicer.x-panel-header-default-framed-top:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:4px 4px 0 4px, frame-bg:url("data:image/gif;R0lGODlhAQAgA/QAAKvH7LjP7rnQ7rvR7rzS777T77/U8MHV8MLW8MTY8cXZ8c3e887e88/f89Dg89Hh9NLi9NPi9NTj9Nbk9f///6vH7KvH7KvH7KvH7KvH7KvH7KvH7KvH7KvH7KvH7KvH7CH5BAEAABQALAAAAAABACADRAhHACcsOKCgoMGDCBMqXMiwocOHEBM+GBCxosWLGDFGaBCgQIKMIEOKHEmypMmKEiA4YABAAAEDCE7KnEmzps2bOHPq3MlTQUAAOw=="), corners:url("data:image/gif;R0lGODlhBAAYAPQAAJm86KHB66LC6qPC6rvS78fa8sjb8src8tbj9dbk9tfl9djl9drn9tvn9urx+e70+u71+u/0+vL3/PP3+/P3/P///wAAAJm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86CH5BAEAABUALAAAAAAEABgARAhRAAEIBFCBAgEBACYUWMhQAAEJFRZOALCg4oIDGA8QQOCgQQMHCAgkzHhg4oSTExSoVGCgpYGBACQESBBBwAMGCiIkCCBBAQMIAxK2hNlyIsyAADs="), sides:url("data:image/gif;R0lGODlhCAAgA/QAAJm86KvH7LjP7rnQ7rvR7rzS777T77/U8MHV8MLW8MTY8cXZ8c3e887e88/f89Dg89Hh9NLi9NPi9NTj9Nbk9fP3+////5m86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86CH5BAEAABYALAAAAAAIACADRAj/AAFUoECQQgUAAhkoZHBQIIKHCBpWWEBxgcSKFhFOrHiRo0aMHSmGzCgQ5EePJVFuFHmSZUqXK0nGHEmzpUyTL2+qxDnTZs2cP3sC9Ul0qFGhSHkq3ckU5lKnTXVCnSq1atCnVosmjXqVq1asXamGzXoU7FevZdFuFXuWbVq3a8nGHUtXK4S7ECQS2Eug7lu5Zv/6ndsWsNrAhAUXHoy48eHHcB1Hhmx4suXKmBlT1nyZc+bFoBWLTkxa8ufRpj2r1iihtQSJDmI7kCigtgCJBnIbkKigt4LVqDeHLi08eOfhqZEXJ37c+Gnmz5M7Bw6duvTqyptjn549+vLr4L+Lxdcenvx47+bTo19v/Xx79e/Zd49Pf7597vi36y8vPz//+qNNIOAEEkVgYAQSPaDgAxI14GADEgUgYQASDWDhABIVoGEBEh3g4QESJSBiAgDu5959JsKH4n8rnuifiyn2F2OJLL6ooo0y1jhjizfuiCONMOooZJBE9jikkUXmmCSQSDappJNMPilllFTyOKWVVf6I5ZZadunjl0de6WWYWYK5JJdmQokmmWueOaabaYoZZ5lsvqmmnXLWOWebd+6JJ51wmhUQADs=")" !important
}

.x-panel-header-default-framed-right {
    -moz-border-radius-topleft: 0;
    -webkit-border-top-left-radius: 0;
    border-top-left-radius: 0;
    -moz-border-radius-topright: 4px;
    -webkit-border-top-right-radius: 4px;
    border-top-right-radius: 4px;
    -moz-border-radius-bottomright: 4px;
    -webkit-border-bottom-right-radius: 4px;
    border-bottom-right-radius: 4px;
    -moz-border-radius-bottomleft: 0;
    -webkit-border-bottom-left-radius: 0;
    border-bottom-left-radius: 0;
    padding: 5px 5px 5px 5px;
    border-width: 1px 1px 1px 0;
    border-style: solid;
    background-image: none;
    background-color: #cbddf3;
    background-image: -webkit-gradient(linear, top, bottom, color-stop(0%, #dae7f6), color-stop(45%, #cddef3), color-stop(46%, #abc7ec), color-stop(50%, #abc7ec), color-stop(51%, #b8cfee), color-stop(0%, #cbddf3));
    background-image: -webkit-linear-gradient(right, #dae7f6, #cddef3 45%, #abc7ec 46%, #abc7ec 50%, #b8cfee 51%, #cbddf3);
    background-image: -moz-linear-gradient(right, #dae7f6, #cddef3 45%, #abc7ec 46%, #abc7ec 50%, #b8cfee 51%, #cbddf3);
    background-image: -o-linear-gradient(right, #dae7f6, #cddef3 45%, #abc7ec 46%, #abc7ec 50%, #b8cfee 51%, #cbddf3);
    background-image: -ms-linear-gradient(right, #dae7f6, #cddef3 45%, #abc7ec 46%, #abc7ec 50%, #b8cfee 51%, #cbddf3);
    background-image: linear-gradient(right, #dae7f6, #cddef3 45%, #abc7ec 46%, #abc7ec 50%, #b8cfee 51%, #cbddf3)
}

.x-panel-header-default-framed-right-mc {
    background-image: url("data:image/gif;R0lGODlhIAMBAPQAAKvH7LjP7rnQ7rvR7rzS777T77/U8MHV8MLW8MTY8cXZ8c3e887e88/f89Dg89Hh9NLi9NPi9NTj9Nbk9f///6vH7KvH7KvH7KvH7KvH7KvH7KvH7KvH7KvH7KvH7KvH7CH5BAEAABQALAAAAAAgAwEARAhFABUIHEiwoMGDCBMqXMiwocOHECNKnEixosWLGDNq3Mixo8ePIEOKHEmypMmTChIgOGCgAIEBAgIAWMCggYMHECJImBAQADs=");
    background-position: right 0;
    background-repeat: repeat-y;
    background-color: #cbddf3
}

.x-nbr .x-panel-header-default-framed-right {
    padding: 0 !important;
    border-width: 0 !important;
    -webkit-border-radius: 0px;
    -moz-border-radius: 0px;
    -ms-border-radius: 0px;
    -o-border-radius: 0px;
    border-radius: 0px;
    background-color: transparent !important;
    background-image: none;
    box-shadow: none !important
}

.x-panel-header-default-framed-right-frameInfo {
    font-family: dv-4-4-4-0-1-1-1-0-5-5-5-5
}

.x-panel-header-default-framed-right-tl {
    background-position: 0 0
}

.x-panel-header-default-framed-right-tr {
    background-position: 0 -4px
}

.x-panel-header-default-framed-right-bl {
    background-position: 0 -8px
}

.x-panel-header-default-framed-right-br {
    background-position: 0 -12px
}

.x-panel-header-default-framed-right-ml {
    background-position: -4px 0
}

.x-panel-header-default-framed-right-mr {
    background-position: right 0
}

.x-panel-header-default-framed-right-tc {
    background-position: right 0
}

.x-panel-header-default-framed-right-bc {
    background-position: right -4px
}

.x-panel-header-default-framed-right-tr, .x-panel-header-default-framed-right-br, .x-panel-header-default-framed-right-mr {
    padding-right: 4px
}

.x-panel-header-default-framed-right-tl, .x-panel-header-default-framed-right-bl, .x-panel-header-default-framed-right-ml {
    padding-left: 0
}

.x-panel-header-default-framed-right-tc {
    height: 4px
}

.x-panel-header-default-framed-right-bc {
    height: 4px
}

.x-panel-header-default-framed-right-tl, .x-panel-header-default-framed-right-bl, .x-panel-header-default-framed-right-tr, .x-panel-header-default-framed-right-br, .x-panel-header-default-framed-right-tc, .x-panel-header-default-framed-right-bc, .x-panel-header-default-framed-right-ml, .x-panel-header-default-framed-right-mr {
    background-image: url("data:image/gif;R0lGODlhDAAQAPQAAJm86KHB66LC6qPC6rvS78fa8sjb8src8tbk9tfl9djl9drn9tvn9urx+e70+u71+u/0+vL3/PP3+////wAAAJm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86CH5BAEAABMALAAAAAAMABAARAheAAEIFHjAQIEECiQQNAig4MGEAAQQiDChoUGEChMweDDA4kOFHj1iBLCggQICIiECkMAypUIHCAJEcCmQpUKHI0PihAgh5sydGTd2BLqwAM2BRUeWTICS6ICJFYkGBAA7")
}

.x-panel-header-default-framed-right-tc, .x-panel-header-default-framed-right-bc {
    background-image: url("data:image/gif;R0lGODlhIAMIAPQAAJm86KvH7LjP7rnQ7rvR7rzS777T77/U8MHV8MLW8MTY8c3e887e88/f89Dg89Hh9NLi9NPi9NTj9Nbk9fP3+////5m86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86CH5BAEAABUALAAAAAAgAwgARAj/AAEIHEiwoMGDCBMqXMiwocOHECNKnEixosWLGDNq3Mixo8ePIEOKHEmypMmTFBWoXMmypcuXMGPKnEmzps2bOHPq3Mmzp8+fQIMKHUq0qNGjSJMqXcq0qdOnKhMgOGCgAIEBAgIsYNDAwQMIESRMgEq2rNmzaNOqXcu2rdu3cOPK9SmVqlWsWrl6BSuWgt+/gAMLHky4sOHDiBMrXsy4sePHkCNLnky5suXLmDNr3sy5s+fPoEOLHk26tOnTqFOrXs26tevXsGPLnk0b8NzbuHPr3s27t+/fwIOfrVv1atatXb+GHSu8ufPn0KNLn069+lzid4/rVS4Wpffv4MOLDh9Pvrz58+jTq1/PHmVAADs=");
    background-repeat: repeat-x
}

.x-panel-header-default-framed-right-mc {
    padding: 2px 2px 2px 5px
}

.x-cmd-slicer.x-panel-header-default-framed-right:before {
    display: none;
    content: "x-slicer:, stretch:left, frame:4px 4px 4px 0, frame-bg:url("data:image/gif;R0lGODlhIAMBAPQAAKvH7LjP7rnQ7rvR7rzS777T77/U8MHV8MLW8MTY8cXZ8c3e887e88/f89Dg89Hh9NLi9NPi9NTj9Nbk9f///6vH7KvH7KvH7KvH7KvH7KvH7KvH7KvH7KvH7KvH7KvH7CH5BAEAABQALAAAAAAgAwEARAhFABUIHEiwoMGDCBMqXMiwocOHECNKnEixosWLGDNq3Mixo8ePIEOKHEmypMmTChIgOGCgAIEBAgIAWMCggYMHECJImBAQADs="), corners:url("data:image/gif;R0lGODlhDAAQAPQAAJm86KHB66LC6qPC6rvS78fa8sjb8src8tbk9tfl9djl9drn9tvn9urx+e70+u71+u/0+vL3/PP3+////wAAAJm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86CH5BAEAABMALAAAAAAMABAARAheAAEIFHjAQIEECiQQNAig4MGEAAQQiDChoUGEChMweDDA4kOFHj1iBLCggQICIiECkMAypUIHCAJEcCmQpUKHI0PihAgh5sydGTd2BLqwAM2BRUeWTICS6ICJFYkGBAA7"), sides:url("data:image/gif;R0lGODlhIAMIAPQAAJm86KvH7LjP7rnQ7rvR7rzS777T77/U8MHV8MLW8MTY8c3e887e88/f89Dg89Hh9NLi9NPi9NTj9Nbk9fP3+////5m86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86CH5BAEAABUALAAAAAAgAwgARAj/AAEIHEiwoMGDCBMqXMiwocOHECNKnEixosWLGDNq3Mixo8ePIEOKHEmypMmTFBWoXMmypcuXMGPKnEmzps2bOHPq3Mmzp8+fQIMKHUq0qNGjSJMqXcq0qdOnKhMgOGCgAIEBAgIsYNDAwQMIESRMgEq2rNmzaNOqXcu2rdu3cOPK9SmVqlWsWrl6BSuWgt+/gAMLHky4sOHDiBMrXsy4sePHkCNLnky5suXLmDNr3sy5s+fPoEOLHk26tOnTqFOrXs26tevXsGPLnk0b8NzbuHPr3s27t+/fwIOfrVv1atatXb+GHSu8ufPn0KNLn069+lzid4/rVS4Wpffv4MOLDh9Pvrz58+jTq1/PHmVAADs=")" !important
}

.x-panel-header-default-framed-bottom {
    -moz-border-radius-topleft: 0;
    -webkit-border-top-left-radius: 0;
    border-top-left-radius: 0;
    -moz-border-radius-topright: 0;
    -webkit-border-top-right-radius: 0;
    border-top-right-radius: 0;
    -moz-border-radius-bottomright: 4px;
    -webkit-border-bottom-right-radius: 4px;
    border-bottom-right-radius: 4px;
    -moz-border-radius-bottomleft: 4px;
    -webkit-border-bottom-left-radius: 4px;
    border-bottom-left-radius: 4px;
    padding: 5px 5px 5px 5px;
    border-width: 0 1px 1px 1px;
    border-style: solid;
    background-image: none;
    background-color: #cbddf3;
    background-image: -webkit-gradient(linear, top, bottom, color-stop(0%, #dae7f6), color-stop(45%, #cddef3), color-stop(46%, #abc7ec), color-stop(50%, #abc7ec), color-stop(51%, #b8cfee), color-stop(0%, #cbddf3));
    background-image: -webkit-linear-gradient(top, #dae7f6, #cddef3 45%, #abc7ec 46%, #abc7ec 50%, #b8cfee 51%, #cbddf3);
    background-image: -moz-linear-gradient(top, #dae7f6, #cddef3 45%, #abc7ec 46%, #abc7ec 50%, #b8cfee 51%, #cbddf3);
    background-image: -o-linear-gradient(top, #dae7f6, #cddef3 45%, #abc7ec 46%, #abc7ec 50%, #b8cfee 51%, #cbddf3);
    background-image: -ms-linear-gradient(top, #dae7f6, #cddef3 45%, #abc7ec 46%, #abc7ec 50%, #b8cfee 51%, #cbddf3);
    background-image: linear-gradient(top, #dae7f6, #cddef3 45%, #abc7ec 46%, #abc7ec 50%, #b8cfee 51%, #cbddf3)
}

.x-panel-header-default-framed-bottom-mc {
    background-image: url("data:image/gif;R0lGODlhAQAgA/QAAKvH7LjP7rnQ7rvR7rzS777T77/U8MHV8MLW8MTY8cXZ8c3e887e88/f89Dg89Hh9NLi9NPi9NTj9Nbk9f///6vH7KvH7KvH7KvH7KvH7KvH7KvH7KvH7KvH7KvH7KvH7CH5BAEAABQALAAAAAABACADRAhGACcIHEiwoMGDCBMqXMiw4cEHAxxKnEixYsUFByxq3Mixo8ePICVGaBCgQIKQKFOqXMmypcuXMGPKlADBAQMAAggYQKAgIAA7");
    background-position: 0 bottom;
    background-color: #cbddf3
}

.x-nbr .x-panel-header-default-framed-bottom {
    padding: 0 !important;
    border-width: 0 !important;
    -webkit-border-radius: 0px;
    -moz-border-radius: 0px;
    -ms-border-radius: 0px;
    -o-border-radius: 0px;
    border-radius: 0px;
    background-color: transparent !important;
    background-image: none;
    box-shadow: none !important
}

.x-panel-header-default-framed-bottom-frameInfo {
    font-family: dh-0-4-4-4-0-1-1-1-5-5-5-5
}

.x-panel-header-default-framed-bottom-tl {
    background-position: 0 -8px
}

.x-panel-header-default-framed-bottom-tr {
    background-position: right -12px
}

.x-panel-header-default-framed-bottom-bl {
    background-position: 0 -16px
}

.x-panel-header-default-framed-bottom-br {
    background-position: right -20px
}

.x-panel-header-default-framed-bottom-ml {
    background-position: 0 bottom
}

.x-panel-header-default-framed-bottom-mr {
    background-position: right bottom
}

.x-panel-header-default-framed-bottom-tc {
    background-position: 0 0
}

.x-panel-header-default-framed-bottom-bc {
    background-position: 0 -4px
}

.x-panel-header-default-framed-bottom-tr, .x-panel-header-default-framed-bottom-br, .x-panel-header-default-framed-bottom-mr {
    padding-right: 4px
}

.x-panel-header-default-framed-bottom-tl, .x-panel-header-default-framed-bottom-bl, .x-panel-header-default-framed-bottom-ml {
    padding-left: 4px
}

.x-panel-header-default-framed-bottom-tc {
    height: 0
}

.x-panel-header-default-framed-bottom-bc {
    height: 4px
}

.x-panel-header-default-framed-bottom-tl, .x-panel-header-default-framed-bottom-bl, .x-panel-header-default-framed-bottom-tr, .x-panel-header-default-framed-bottom-br, .x-panel-header-default-framed-bottom-tc, .x-panel-header-default-framed-bottom-bc, .x-panel-header-default-framed-bottom-ml, .x-panel-header-default-framed-bottom-mr {
    background-image: url("data:image/gif;R0lGODlhBAAYAPQAAJm86KHB66LC6qPC6rvS78fa8sjb8svd88zd883e89Pi9dTj9dTk9tfl9djl9dnm9ebv+Ozz+e3z+e30+vL3/PP3+////wAAAJm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86CH5BAEAABYALAAAAAAEABgARAhOAAEIHChQgIQDBRImJFgAQYQBDiI6qECxAoAKEicCoBBgwYQJDAJQeEDyQYOTDQyoNEDwIsmLJ0laPGmRgAIICSxQIDAgAQQFPAlQsBAQADs=")
}

.x-panel-header-default-framed-bottom-ml, .x-panel-header-default-framed-bottom-mr {
    background-image: url("data:image/gif;R0lGODlhCAAgA/QAAJm86KvH7LjP7rnQ7rvR7rzS777T77/U8MHV8MLW8MTY8cXZ8c3e887e88/f89Dg89Hh9NLi9NPi9NTj9PP3+////5m86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86CH5BAEAABUALAAAAAAIACADRAj/AAFQmEBwAgUAAgsaRDiw4MGEDhkqfNiQIMWJEiNCtJiR48aFHy9qrAiSpEiPJjuWxBhS5cmVI1mmbElzpk2ZOGPqRJmT506YPoMCHfqyqMujNXsSRXrzp9GkTpkqfdpUKNWpUqNCtZqV69alX69qrQqWrFivZruWhMAWAkUCcAmcLYs1rNq5eO/qtcs3bd+6fgMDHjyWMFrDdAsrPrw4MePHjiPn/dt4suDKey9DtoyYM2bKKBmIZkARgWkEnjdn7rz6s2bJrVWDhj07Ne3XtnPHvs269m7dvoPj/k1ceO/hxl0fX668uWzk0Jk/l87befXp1oFHz158O/bv18NrwKc+nnty8OXRSlgvgaKD9w4oCpgvgKKB+wYoKtivIL347uQBaJ53/51XIIH+JSggegseGKCBCkLYYIQITmihhBhWmOGDGnbI4YcDgsjghiGWOKKHJjqYIoUiqnhiiyyueCGKL8pIYo04uqhjjDnyuOOMMAJpI40/3lgkkT4mKWSPSx4ZpJFKQtlklEhOaaWUWEIXwZYRUPTAlw9Q1MCYDVAUwJkBUDTAmgNQVMCbBVB0wJwHUJTAnQlQtMCeCxwUEAA7")
}

.x-panel-header-default-framed-bottom-mc {
    padding: 5px 2px 2px 2px
}

.x-cmd-slicer.x-panel-header-default-framed-bottom:before {
    display: none;
    content: "x-slicer:, stretch:top, frame:0 4px 4px 4px, frame-bg:url("data:image/gif;R0lGODlhAQAgA/QAAKvH7LjP7rnQ7rvR7rzS777T77/U8MHV8MLW8MTY8cXZ8c3e887e88/f89Dg89Hh9NLi9NPi9NTj9Nbk9f///6vH7KvH7KvH7KvH7KvH7KvH7KvH7KvH7KvH7KvH7KvH7CH5BAEAABQALAAAAAABACADRAhGACcIHEiwoMGDCBMqXMiw4cEHAxxKnEixYsUFByxq3Mixo8ePICVGaBCgQIKQKFOqXMmypcuXMGPKlADBAQMAAggYQKAgIAA7"), corners:url("data:image/gif;R0lGODlhBAAYAPQAAJm86KHB66LC6qPC6rvS78fa8sjb8svd88zd883e89Pi9dTj9dTk9tfl9djl9dnm9ebv+Ozz+e3z+e30+vL3/PP3+////wAAAJm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86CH5BAEAABYALAAAAAAEABgARAhOAAEIHChQgIQDBRImJFgAQYQBDiI6qECxAoAKEicCoBBgwYQJDAJQeEDyQYOTDQyoNEDwIsmLJ0laPGmRgAIICSxQIDAgAQQFPAlQsBAQADs="), sides:url("data:image/gif;R0lGODlhCAAgA/QAAJm86KvH7LjP7rnQ7rvR7rzS777T77/U8MHV8MLW8MTY8cXZ8c3e887e88/f89Dg89Hh9NLi9NPi9NTj9PP3+////5m86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86CH5BAEAABUALAAAAAAIACADRAj/AAFQmEBwAgUAAgsaRDiw4MGEDhkqfNiQIMWJEiNCtJiR48aFHy9qrAiSpEiPJjuWxBhS5cmVI1mmbElzpk2ZOGPqRJmT506YPoMCHfqyqMujNXsSRXrzp9GkTpkqfdpUKNWpUqNCtZqV69alX69qrQqWrFivZruWhMAWAkUCcAmcLYs1rNq5eO/qtcs3bd+6fgMDHjyWMFrDdAsrPrw4MePHjiPn/dt4suDKey9DtoyYM2bKKBmIZkARgWkEnjdn7rz6s2bJrVWDhj07Ne3XtnPHvs269m7dvoPj/k1ceO/hxl0fX668uWzk0Jk/l87befXp1oFHz158O/bv18NrwKc+nnty8OXRSlgvgaKD9w4oCpgvgKKB+wYoKtivIL347uQBaJ53/51XIIH+JSggegseGKCBCkLYYIQITmihhBhWmOGDGnbI4YcDgsjghiGWOKKHJjqYIoUiqnhiiyyueCGKL8pIYo04uqhjjDnyuOOMMAJpI40/3lgkkT4mKWSPSx4ZpJFKQtlklEhOaaWUWEIXwZYRUPTAlw9Q1MCYDVAUwJkBUDTAmgNQVMCbBVB0wJwHUJTAnQlQtMCeCxwUEAA7")" !important
}

.x-panel-header-default-framed-left {
    -moz-border-radius-topleft: 4px;
    -webkit-border-top-left-radius: 4px;
    border-top-left-radius: 4px;
    -moz-border-radius-topright: 0;
    -webkit-border-top-right-radius: 0;
    border-top-right-radius: 0;
    -moz-border-radius-bottomright: 0;
    -webkit-border-bottom-right-radius: 0;
    border-bottom-right-radius: 0;
    -moz-border-radius-bottomleft: 4px;
    -webkit-border-bottom-left-radius: 4px;
    border-bottom-left-radius: 4px;
    padding: 5px 5px 5px 5px;
    border-width: 1px 0 1px 1px;
    border-style: solid;
    background-image: none;
    background-color: #cbddf3;
    background-image: -webkit-gradient(linear, top, bottom, color-stop(0%, #dae7f6), color-stop(45%, #cddef3), color-stop(46%, #abc7ec), color-stop(50%, #abc7ec), color-stop(51%, #b8cfee), color-stop(0%, #cbddf3));
    background-image: -webkit-linear-gradient(right, #dae7f6, #cddef3 45%, #abc7ec 46%, #abc7ec 50%, #b8cfee 51%, #cbddf3);
    background-image: -moz-linear-gradient(right, #dae7f6, #cddef3 45%, #abc7ec 46%, #abc7ec 50%, #b8cfee 51%, #cbddf3);
    background-image: -o-linear-gradient(right, #dae7f6, #cddef3 45%, #abc7ec 46%, #abc7ec 50%, #b8cfee 51%, #cbddf3);
    background-image: -ms-linear-gradient(right, #dae7f6, #cddef3 45%, #abc7ec 46%, #abc7ec 50%, #b8cfee 51%, #cbddf3);
    background-image: linear-gradient(right, #dae7f6, #cddef3 45%, #abc7ec 46%, #abc7ec 50%, #b8cfee 51%, #cbddf3)
}

.x-panel-header-default-framed-left-mc {
    background-image: url("data:image/gif;R0lGODlhIAMBAPQAAKvH7LjP7rnQ7rvR7rzS777T77/U8MHV8MLW8MTY8cXZ8c3e887e88/f89Dg89Hh9NLi9NPi9NTj9Nbk9f///6vH7KvH7KvH7KvH7KvH7KvH7KvH7KvH7KvH7KvH7KvH7CH5BAEAABQALAAAAAAgAwEARAhFABUkQHDAQAECAwQEALCAQQMHDyBEkDChosWLGDNq3Mixo8ePIEOKHEmypMmTKFOqXMmypcuXMGPKnEmzps2bOHPqnBAQADs=");
    background-position: left 0;
    background-repeat: repeat-y;
    background-color: #cbddf3
}

.x-nbr .x-panel-header-default-framed-left {
    padding: 0 !important;
    border-width: 0 !important;
    -webkit-border-radius: 0px;
    -moz-border-radius: 0px;
    -ms-border-radius: 0px;
    -o-border-radius: 0px;
    border-radius: 0px;
    background-color: transparent !important;
    background-image: none;
    box-shadow: none !important
}

.x-panel-header-default-framed-left-frameInfo {
    font-family: dv-4-0-4-4-1-0-1-1-5-5-5-5
}

.x-panel-header-default-framed-left-tl {
    background-position: 0 0
}

.x-panel-header-default-framed-left-tr {
    background-position: 0 -4px
}

.x-panel-header-default-framed-left-bl {
    background-position: 0 -8px
}

.x-panel-header-default-framed-left-br {
    background-position: 0 -12px
}

.x-panel-header-default-framed-left-ml {
    background-position: -4px 0
}

.x-panel-header-default-framed-left-mr {
    background-position: right 0
}

.x-panel-header-default-framed-left-tc {
    background-position: left 0
}

.x-panel-header-default-framed-left-bc {
    background-position: left -4px
}

.x-panel-header-default-framed-left-tr, .x-panel-header-default-framed-left-br, .x-panel-header-default-framed-left-mr {
    padding-right: 0
}

.x-panel-header-default-framed-left-tl, .x-panel-header-default-framed-left-bl, .x-panel-header-default-framed-left-ml {
    padding-left: 4px
}

.x-panel-header-default-framed-left-tc {
    height: 4px
}

.x-panel-header-default-framed-left-bc {
    height: 4px
}

.x-panel-header-default-framed-left-tl, .x-panel-header-default-framed-left-bl, .x-panel-header-default-framed-left-tr, .x-panel-header-default-framed-left-br, .x-panel-header-default-framed-left-tc, .x-panel-header-default-framed-left-bc, .x-panel-header-default-framed-left-ml, .x-panel-header-default-framed-left-mr {
    background-image: url("data:image/gif;R0lGODlhDAAQAPQAAJm86KHB66LC6qPC6rvS78fa8sjb8svd88zd88ze89Pi9dTk9dXj9dfl9djl9dnm9ebv+O3z+e3z+u30+vL3/PP3+/P3/P///wAAAJm86Jm86Jm86Jm86Jm86Jm86Jm86CH5BAEAABcALAAAAAAMABAARAheAC9YICAAQAUDBRo4eABAQIQEBQwiVMgQgEWLBxMuBEAR48SNBBhAOCBRI8OOJTtSCKBgQsqNFWJ6NAlgpQIJLxk6hJjToMyeKDN2JLAAAoKeFygQGAB0Y8+LMzsGBAA7")
}

.x-panel-header-default-framed-left-tc, .x-panel-header-default-framed-left-bc {
    background-image: url("data:image/gif;R0lGODlhIAMIAPQAAJm86KvH7LjP7rnQ7rvR7rzS777T77/U8MHV8MLW8MTY8cXZ8c3e887e88/f89Dg89Hh9NLi9NPi9NTj9Nbk9fP3+////5m86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86CH5BAEAABYALAAAAAAgAwgARAj/AAEIHEiwoMGDCBMqXMiwocOHECNKnEixosWLGDNq3Mixo8ePIEOKHEmypMmTFBcoSIDggIECBAYICMCggYMHECJImEChp8+fQIMKHUq0qNGjSJMqXcq0qdOnUKNKnUq1qtWrWLNq3cq1q9evYMOKpaCSpUuYMmnaxKmT59i3cOPKnUu3rt27ePPq3cu379MKgAMLHky4sOHDiBMrXsy4sePHkCNLnky5suXLmDNr3sy5s+fPoEOLHk26tOnTqFOrXs26tevXsGPLnk27tm3BZVu+jDmz5s2cO/0KH068uPHjyJMrX848bu6zvNX+btu8uvXr2LNr3869u1+U4MOLER9Pvrz58+jTq1/Pvr17lAEBADs=");
    background-repeat: repeat-x
}

.x-panel-header-default-framed-left-mc {
    padding: 2px 5px 2px 2px
}

.x-cmd-slicer.x-panel-header-default-framed-left:before {
    display: none;
    content: "x-slicer:, stretch:right, frame:4px 0 4px 4px, frame-bg:url("data:image/gif;R0lGODlhIAMBAPQAAKvH7LjP7rnQ7rvR7rzS777T77/U8MHV8MLW8MTY8cXZ8c3e887e88/f89Dg89Hh9NLi9NPi9NTj9Nbk9f///6vH7KvH7KvH7KvH7KvH7KvH7KvH7KvH7KvH7KvH7KvH7CH5BAEAABQALAAAAAAgAwEARAhFABUkQHDAQAECAwQEALCAQQMHDyBEkDChosWLGDNq3Mixo8ePIEOKHEmypMmTKFOqXMmypcuXMGPKnEmzps2bOHPqnBAQADs="), corners:url("data:image/gif;R0lGODlhDAAQAPQAAJm86KHB66LC6qPC6rvS78fa8sjb8svd88zd88ze89Pi9dTk9dXj9dfl9djl9dnm9ebv+O3z+e3z+u30+vL3/PP3+/P3/P///wAAAJm86Jm86Jm86Jm86Jm86Jm86Jm86CH5BAEAABcALAAAAAAMABAARAheAC9YICAAQAUDBRo4eABAQIQEBQwiVMgQgEWLBxMuBEAR48SNBBhAOCBRI8OOJTtSCKBgQsqNFWJ6NAlgpQIJLxk6hJjToMyeKDN2JLAAAoKeFygQGAB0Y8+LMzsGBAA7"), sides:url("data:image/gif;R0lGODlhIAMIAPQAAJm86KvH7LjP7rnQ7rvR7rzS777T77/U8MHV8MLW8MTY8cXZ8c3e887e88/f89Dg89Hh9NLi9NPi9NTj9Nbk9fP3+////5m86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86CH5BAEAABYALAAAAAAgAwgARAj/AAEIHEiwoMGDCBMqXMiwocOHECNKnEixosWLGDNq3Mixo8ePIEOKHEmypMmTFBcoSIDggIECBAYICMCggYMHECJImEChp8+fQIMKHUq0qNGjSJMqXcq0qdOnUKNKnUq1qtWrWLNq3cq1q9evYMOKpaCSpUuYMmnaxKmT59i3cOPKnUu3rt27ePPq3cu379MKgAMLHky4sOHDiBMrXsy4sePHkCNLnky5suXLmDNr3sy5s+fPoEOLHk26tOnTqFOrXs26tevXsGPLnk27tm3BZVu+jDmz5s2cO/0KH068uPHjyJMrX848bu6zvNX+btu8uvXr2LNr3869u1+U4MOLER9Pvrz58+jTq1/Pvr17lAEBADs=")" !important
}

.x-panel-header-default-framed-collapsed-top {
    -moz-border-radius-topleft: 4px;
    -webkit-border-top-left-radius: 4px;
    border-top-left-radius: 4px;
    -moz-border-radius-topright: 4px;
    -webkit-border-top-right-radius: 4px;
    border-top-right-radius: 4px;
    -moz-border-radius-bottomright: 4px;
    -webkit-border-bottom-right-radius: 4px;
    border-bottom-right-radius: 4px;
    -moz-border-radius-bottomleft: 4px;
    -webkit-border-bottom-left-radius: 4px;
    border-bottom-left-radius: 4px;
    padding: 5px 5px 5px 5px;
    border-width: 1px;
    border-style: solid;
    background-image: none;
    background-color: #cbddf3;
    background-image: -webkit-gradient(linear, top, bottom, color-stop(0%, #dae7f6), color-stop(45%, #cddef3), color-stop(46%, #abc7ec), color-stop(50%, #abc7ec), color-stop(51%, #b8cfee), color-stop(0%, #cbddf3));
    background-image: -webkit-linear-gradient(top, #dae7f6, #cddef3 45%, #abc7ec 46%, #abc7ec 50%, #b8cfee 51%, #cbddf3);
    background-image: -moz-linear-gradient(top, #dae7f6, #cddef3 45%, #abc7ec 46%, #abc7ec 50%, #b8cfee 51%, #cbddf3);
    background-image: -o-linear-gradient(top, #dae7f6, #cddef3 45%, #abc7ec 46%, #abc7ec 50%, #b8cfee 51%, #cbddf3);
    background-image: -ms-linear-gradient(top, #dae7f6, #cddef3 45%, #abc7ec 46%, #abc7ec 50%, #b8cfee 51%, #cbddf3);
    background-image: linear-gradient(top, #dae7f6, #cddef3 45%, #abc7ec 46%, #abc7ec 50%, #b8cfee 51%, #cbddf3)
}

.x-panel-header-default-framed-collapsed-top-mc {
    background-image: url("data:image/gif;R0lGODlhAQAgA/QAAKvH7LjP7rnQ7rvR7rzS777T77/U78HV8MLW8MPX8cXY8c3e887f88/f89Dg89Hh9NLi9NTi9NXj9Nbk9f///6vH7KvH7KvH7KvH7KvH7KvH7KvH7KvH7KvH7KvH7KvH7CH5BAEAABQALAAAAAABACADRAhHACcsOKCgoMGDCBMqXMiwocOHEBM+GBCxosWLGDFGaBCgQIKMIEOKHEmypMmKEiA4YABAAAEDCE7KnEmzps2bOHPq3MlTQUAAOw==");
    background-position: 0 top;
    background-color: #cbddf3
}

.x-nbr .x-panel-header-default-framed-collapsed-top {
    padding: 0 !important;
    border-width: 0 !important;
    -webkit-border-radius: 0px;
    -moz-border-radius: 0px;
    -ms-border-radius: 0px;
    -o-border-radius: 0px;
    border-radius: 0px;
    background-color: transparent !important;
    background-image: none;
    box-shadow: none !important
}

.x-panel-header-default-framed-collapsed-top-frameInfo {
    font-family: dh-4-4-4-4-1-1-1-1-5-5-5-5
}

.x-panel-header-default-framed-collapsed-top-tl {
    background-position: 0 -8px
}

.x-panel-header-default-framed-collapsed-top-tr {
    background-position: right -12px
}

.x-panel-header-default-framed-collapsed-top-bl {
    background-position: 0 -16px
}

.x-panel-header-default-framed-collapsed-top-br {
    background-position: right -20px
}

.x-panel-header-default-framed-collapsed-top-ml {
    background-position: 0 top
}

.x-panel-header-default-framed-collapsed-top-mr {
    background-position: right top
}

.x-panel-header-default-framed-collapsed-top-tc {
    background-position: 0 0
}

.x-panel-header-default-framed-collapsed-top-bc {
    background-position: 0 -4px
}

.x-panel-header-default-framed-collapsed-top-tr, .x-panel-header-default-framed-collapsed-top-br, .x-panel-header-default-framed-collapsed-top-mr {
    padding-right: 4px
}

.x-panel-header-default-framed-collapsed-top-tl, .x-panel-header-default-framed-collapsed-top-bl, .x-panel-header-default-framed-collapsed-top-ml {
    padding-left: 4px
}

.x-panel-header-default-framed-collapsed-top-tc {
    height: 4px
}

.x-panel-header-default-framed-collapsed-top-bc {
    height: 4px
}

.x-panel-header-default-framed-collapsed-top-tl, .x-panel-header-default-framed-collapsed-top-bl, .x-panel-header-default-framed-collapsed-top-tr, .x-panel-header-default-framed-collapsed-top-br, .x-panel-header-default-framed-collapsed-top-tc, .x-panel-header-default-framed-collapsed-top-bc, .x-panel-header-default-framed-collapsed-top-ml, .x-panel-header-default-framed-collapsed-top-mr {
    background-image: url("data:image/gif;R0lGODlhBAAYAPQAAJm86KHB66LC6qPC6rvS78ba8cja8sjb8sjb88nc8svd8s7f89Pj9Nbj9dbk9tfl9djl9drn9tvn9tvo9unx+erx+e70+u71+u/0+vL3/PP3+/P3/P///wAAAJm86Jm86CH5BAEAABwALAAAAAAEABgARAhfAAEIBMBhAwEBAigoKMCQoQACGTgUUEBhAISLEBYk2EigQQUJEio0gBjAAAMGCAJk0MBSw4OXDw7IPDAQQIYADjAIsBDhAQYHKh9EuDCAgIEJBzhkIDDgwAQDTCFyCAgAOw==")
}

.x-panel-header-default-framed-collapsed-top-ml, .x-panel-header-default-framed-collapsed-top-mr {
    background-image: url("data:image/gif;R0lGODlhCAAgA/QAAJm86KvH7LjP7rnQ7rvR7rzS777T77/U78HV8MLW8MPX8cXY8c3e887f88/f89Dg89Hh9NLi9NTi9NXj9Nbk9fP3+////5m86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86CH5BAEAABYALAAAAAAIACADRAj/AAFUoECQQgUAAhkoZHBQIIKHCBpWWEBxgcSKFhFOrHiRo0aMHSmGzCgQ5EePJVFuFHmSZUqXK0nGHEmzpUyTL2+qxDnTZs2cP3sC9Ul0qFGhSHkq3ckU5lKnTXVCnSq1atCnVosmjXqVq1asXamGzXoU7FevZdFuFXuWbVq3a8nGHUtXK4S7ECQS2Eug7lu5Zv/6ndsWsNrAhAUXHoy48eHHcB1Hhmx4suXKmBlT1nyZc+bFoBWLTkxa8ufRpj2r1iihtQSJDmI7kCigtgCJBnIbkKigt4LVqDeHLi08eOfhqZEXJ37c+Gnmz5M7Bw6duvTqyptjn549+vLr4L+Lxdcenvx47+bTo19v/Xx79e/Zd49Pf7597vi36y8vPz//+qNNIOAEEkVgYAQSPaDgAxI14GADEgUgYQASDWDhABIVoGEBEh3g4QESJSBiAgDu5959JsKH4n8rnuifiyn2F2OJLL6ooo0y1jhjizfuiCONMOooZJBE9jikkUXmmCSQSDappJNMPilllFTyOKWVVf6I5ZZadunjl0de6WWYWYK5JJdmQokmmWueOaabaYoZZ5lsvqmmnXLWOWebd+6JJ51wmhUQADs=")
}

.x-panel-header-default-framed-collapsed-top-mc {
    padding: 2px 2px 2px 2px
}

.x-cmd-slicer.x-panel-header-default-framed-collapsed-top:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:4px 4px 4px 4px, frame-bg:url("data:image/gif;R0lGODlhAQAgA/QAAKvH7LjP7rnQ7rvR7rzS777T77/U78HV8MLW8MPX8cXY8c3e887f88/f89Dg89Hh9NLi9NTi9NXj9Nbk9f///6vH7KvH7KvH7KvH7KvH7KvH7KvH7KvH7KvH7KvH7KvH7CH5BAEAABQALAAAAAABACADRAhHACcsOKCgoMGDCBMqXMiwocOHEBM+GBCxosWLGDFGaBCgQIKMIEOKHEmypMmKEiA4YABAAAEDCE7KnEmzps2bOHPq3MlTQUAAOw=="), corners:url("data:image/gif;R0lGODlhBAAYAPQAAJm86KHB66LC6qPC6rvS78ba8cja8sjb8sjb88nc8svd8s7f89Pj9Nbj9dbk9tfl9djl9drn9tvn9tvo9unx+erx+e70+u71+u/0+vL3/PP3+/P3/P///wAAAJm86Jm86CH5BAEAABwALAAAAAAEABgARAhfAAEIBMBhAwEBAigoKMCQoQACGTgUUEBhAISLEBYk2EigQQUJEio0gBjAAAMGCAJk0MBSw4OXDw7IPDAQQIYADjAIsBDhAQYHKh9EuDCAgIEJBzhkIDDgwAQDTCFyCAgAOw=="), sides:url("data:image/gif;R0lGODlhCAAgA/QAAJm86KvH7LjP7rnQ7rvR7rzS777T77/U78HV8MLW8MPX8cXY8c3e887f88/f89Dg89Hh9NLi9NTi9NXj9Nbk9fP3+////5m86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86CH5BAEAABYALAAAAAAIACADRAj/AAFUoECQQgUAAhkoZHBQIIKHCBpWWEBxgcSKFhFOrHiRo0aMHSmGzCgQ5EePJVFuFHmSZUqXK0nGHEmzpUyTL2+qxDnTZs2cP3sC9Ul0qFGhSHkq3ckU5lKnTXVCnSq1atCnVosmjXqVq1asXamGzXoU7FevZdFuFXuWbVq3a8nGHUtXK4S7ECQS2Eug7lu5Zv/6ndsWsNrAhAUXHoy48eHHcB1Hhmx4suXKmBlT1nyZc+bFoBWLTkxa8ufRpj2r1iihtQSJDmI7kCigtgCJBnIbkKigt4LVqDeHLi08eOfhqZEXJ37c+Gnmz5M7Bw6duvTqyptjn549+vLr4L+Lxdcenvx47+bTo19v/Xx79e/Zd49Pf7597vi36y8vPz//+qNNIOAEEkVgYAQSPaDgAxI14GADEgUgYQASDWDhABIVoGEBEh3g4QESJSBiAgDu5959JsKH4n8rnuifiyn2F2OJLL6ooo0y1jhjizfuiCONMOooZJBE9jikkUXmmCSQSDappJNMPilllFTyOKWVVf6I5ZZadunjl0de6WWYWYK5JJdmQokmmWueOaabaYoZZ5lsvqmmnXLWOWebd+6JJ51wmhUQADs=")" !important
}

.x-panel-header-default-framed-collapsed-right {
    -moz-border-radius-topleft: 4px;
    -webkit-border-top-left-radius: 4px;
    border-top-left-radius: 4px;
    -moz-border-radius-topright: 4px;
    -webkit-border-top-right-radius: 4px;
    border-top-right-radius: 4px;
    -moz-border-radius-bottomright: 4px;
    -webkit-border-bottom-right-radius: 4px;
    border-bottom-right-radius: 4px;
    -moz-border-radius-bottomleft: 4px;
    -webkit-border-bottom-left-radius: 4px;
    border-bottom-left-radius: 4px;
    padding: 5px 5px 5px 5px;
    border-width: 1px;
    border-style: solid;
    background-image: none;
    background-color: #cbddf3;
    background-image: -webkit-gradient(linear, top, bottom, color-stop(0%, #dae7f6), color-stop(45%, #cddef3), color-stop(46%, #abc7ec), color-stop(50%, #abc7ec), color-stop(51%, #b8cfee), color-stop(0%, #cbddf3));
    background-image: -webkit-linear-gradient(right, #dae7f6, #cddef3 45%, #abc7ec 46%, #abc7ec 50%, #b8cfee 51%, #cbddf3);
    background-image: -moz-linear-gradient(right, #dae7f6, #cddef3 45%, #abc7ec 46%, #abc7ec 50%, #b8cfee 51%, #cbddf3);
    background-image: -o-linear-gradient(right, #dae7f6, #cddef3 45%, #abc7ec 46%, #abc7ec 50%, #b8cfee 51%, #cbddf3);
    background-image: -ms-linear-gradient(right, #dae7f6, #cddef3 45%, #abc7ec 46%, #abc7ec 50%, #b8cfee 51%, #cbddf3);
    background-image: linear-gradient(right, #dae7f6, #cddef3 45%, #abc7ec 46%, #abc7ec 50%, #b8cfee 51%, #cbddf3)
}

.x-panel-header-default-framed-collapsed-right-mc {
    background-image: url("data:image/gif;R0lGODlhIAMBAPQAAKvH7LjP7rnQ7rvR7rzS777T77/U8MHV8MLW8MTY8cXZ8c3e887e88/f89Dg89Hh9NLi9NPi9NTj9Nbk9f///6vH7KvH7KvH7KvH7KvH7KvH7KvH7KvH7KvH7KvH7KvH7CH5BAEAABQALAAAAAAgAwEARAhFABUIHEiwoMGDCBMqXMiwocOHECNKnEixosWLGDNq3Mixo8ePIEOKHEmypMmTChIgOGCgAIEBAgIAWMCggYMHECJImBAQADs=");
    background-position: right 0;
    background-repeat: repeat-y;
    background-color: #cbddf3
}

.x-nbr .x-panel-header-default-framed-collapsed-right {
    padding: 0 !important;
    border-width: 0 !important;
    -webkit-border-radius: 0px;
    -moz-border-radius: 0px;
    -ms-border-radius: 0px;
    -o-border-radius: 0px;
    border-radius: 0px;
    background-color: transparent !important;
    background-image: none;
    box-shadow: none !important
}

.x-panel-header-default-framed-collapsed-right-frameInfo {
    font-family: dv-4-4-4-4-1-1-1-1-5-5-5-5
}

.x-panel-header-default-framed-collapsed-right-tl {
    background-position: 0 0
}

.x-panel-header-default-framed-collapsed-right-tr {
    background-position: 0 -4px
}

.x-panel-header-default-framed-collapsed-right-bl {
    background-position: 0 -8px
}

.x-panel-header-default-framed-collapsed-right-br {
    background-position: 0 -12px
}

.x-panel-header-default-framed-collapsed-right-ml {
    background-position: -4px 0
}

.x-panel-header-default-framed-collapsed-right-mr {
    background-position: right 0
}

.x-panel-header-default-framed-collapsed-right-tc {
    background-position: right 0
}

.x-panel-header-default-framed-collapsed-right-bc {
    background-position: right -4px
}

.x-panel-header-default-framed-collapsed-right-tr, .x-panel-header-default-framed-collapsed-right-br, .x-panel-header-default-framed-collapsed-right-mr {
    padding-right: 4px
}

.x-panel-header-default-framed-collapsed-right-tl, .x-panel-header-default-framed-collapsed-right-bl, .x-panel-header-default-framed-collapsed-right-ml {
    padding-left: 4px
}

.x-panel-header-default-framed-collapsed-right-tc {
    height: 4px
}

.x-panel-header-default-framed-collapsed-right-bc {
    height: 4px
}

.x-panel-header-default-framed-collapsed-right-tl, .x-panel-header-default-framed-collapsed-right-bl, .x-panel-header-default-framed-collapsed-right-tr, .x-panel-header-default-framed-collapsed-right-br, .x-panel-header-default-framed-collapsed-right-tc, .x-panel-header-default-framed-collapsed-right-bc, .x-panel-header-default-framed-collapsed-right-ml, .x-panel-header-default-framed-collapsed-right-mr {
    background-image: url("data:image/gif;R0lGODlhDAAQAPQAAJm86KHB66LC6qPC6rvS78fa8sfb88ja8sjb8src8svd88zd887e89Tj9NXk9tfl9djl9drn9tvn9tvo9unx+erw+erx+e70+u71+u/0+vL3/PP3+/P3/P///wAAAJm86CH5BAEAAB0ALAAAAAAMABAARAh1ADtwICAAAAMEBR5A2ABAQAOEBhEqZCiAgIYOERMuBPBAAoYBGScCIHBgggIACSRujGABAgGUKhlqCGCAAkyNDC84CKDhpsiZBSr43OgQYkqcADLs7HlUZMePQxmSnLAgKoAOGgiAbLrSwoOXXBkOsIgxLICAADs=")
}

.x-panel-header-default-framed-collapsed-right-tc, .x-panel-header-default-framed-collapsed-right-bc {
    background-image: url("data:image/gif;R0lGODlhIAMIAPQAAJm86KvH7LjP7rnQ7rvR7rzS777T77/U8MHV8MLW8MTY8c3e887e88/f89Dg89Hh9NLi9NPi9NTj9Nbk9fP3+////5m86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86CH5BAEAABUALAAAAAAgAwgARAj/AAEIHEiwoMGDCBMqXMiwocOHECNKnEixosWLGDNq3Mixo8ePIEOKHEmypMmTFBWoXMmypcuXMGPKnEmzps2bOHPq3Mmzp8+fQIMKHUq0qNGjSJMqXcq0qdOnKhMgOGCgAIEBAgIsYNDAwQMIESRMgEq2rNmzaNOqXcu2rdu3cOPK9SmVqlWsWrl6BSuWgt+/gAMLHky4sOHDiBMrXsy4sePHkCNLnky5suXLmDNr3sy5s+fPoEOLHk26tOnTqFOrXs26tevXsGPLnk0b8NzbuHPr3s27t+/fwIOfrVv1atatXb+GHSu8ufPn0KNLn069+lzid4/rVS4Wpffv4MOLDh9Pvrz58+jTq1/PHmVAADs=");
    background-repeat: repeat-x
}

.x-panel-header-default-framed-collapsed-right-mc {
    padding: 2px 2px 2px 2px
}

.x-cmd-slicer.x-panel-header-default-framed-collapsed-right:before {
    display: none;
    content: "x-slicer:, stretch:left, frame:4px 4px 4px 4px, frame-bg:url("data:image/gif;R0lGODlhIAMBAPQAAKvH7LjP7rnQ7rvR7rzS777T77/U8MHV8MLW8MTY8cXZ8c3e887e88/f89Dg89Hh9NLi9NPi9NTj9Nbk9f///6vH7KvH7KvH7KvH7KvH7KvH7KvH7KvH7KvH7KvH7KvH7CH5BAEAABQALAAAAAAgAwEARAhFABUIHEiwoMGDCBMqXMiwocOHECNKnEixosWLGDNq3Mixo8ePIEOKHEmypMmTChIgOGCgAIEBAgIAWMCggYMHECJImBAQADs="), corners:url("data:image/gif;R0lGODlhDAAQAPQAAJm86KHB66LC6qPC6rvS78fa8sfb88ja8sjb8src8svd88zd887e89Tj9NXk9tfl9djl9drn9tvn9tvo9unx+erw+erx+e70+u71+u/0+vL3/PP3+/P3/P///wAAAJm86CH5BAEAAB0ALAAAAAAMABAARAh1ADtwICAAAAMEBR5A2ABAQAOEBhEqZCiAgIYOERMuBPBAAoYBGScCIHBgggIACSRujGABAgGUKhlqCGCAAkyNDC84CKDhpsiZBSr43OgQYkqcADLs7HlUZMePQxmSnLAgKoAOGgiAbLrSwoOXXBkOsIgxLICAADs="), sides:url("data:image/gif;R0lGODlhIAMIAPQAAJm86KvH7LjP7rnQ7rvR7rzS777T77/U8MHV8MLW8MTY8c3e887e88/f89Dg89Hh9NLi9NPi9NTj9Nbk9fP3+////5m86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86CH5BAEAABUALAAAAAAgAwgARAj/AAEIHEiwoMGDCBMqXMiwocOHECNKnEixosWLGDNq3Mixo8ePIEOKHEmypMmTFBWoXMmypcuXMGPKnEmzps2bOHPq3Mmzp8+fQIMKHUq0qNGjSJMqXcq0qdOnKhMgOGCgAIEBAgIsYNDAwQMIESRMgEq2rNmzaNOqXcu2rdu3cOPK9SmVqlWsWrl6BSuWgt+/gAMLHky4sOHDiBMrXsy4sePHkCNLnky5suXLmDNr3sy5s+fPoEOLHk26tOnTqFOrXs26tevXsGPLnk0b8NzbuHPr3s27t+/fwIOfrVv1atatXb+GHSu8ufPn0KNLn069+lzid4/rVS4Wpffv4MOLDh9Pvrz58+jTq1/PHmVAADs=")" !important
}

.x-panel-header-default-framed-collapsed-bottom {
    -moz-border-radius-topleft: 4px;
    -webkit-border-top-left-radius: 4px;
    border-top-left-radius: 4px;
    -moz-border-radius-topright: 4px;
    -webkit-border-top-right-radius: 4px;
    border-top-right-radius: 4px;
    -moz-border-radius-bottomright: 4px;
    -webkit-border-bottom-right-radius: 4px;
    border-bottom-right-radius: 4px;
    -moz-border-radius-bottomleft: 4px;
    -webkit-border-bottom-left-radius: 4px;
    border-bottom-left-radius: 4px;
    padding: 5px 5px 5px 5px;
    border-width: 1px;
    border-style: solid;
    background-image: none;
    background-color: #cbddf3;
    background-image: -webkit-gradient(linear, top, bottom, color-stop(0%, #dae7f6), color-stop(45%, #cddef3), color-stop(46%, #abc7ec), color-stop(50%, #abc7ec), color-stop(51%, #b8cfee), color-stop(0%, #cbddf3));
    background-image: -webkit-linear-gradient(top, #dae7f6, #cddef3 45%, #abc7ec 46%, #abc7ec 50%, #b8cfee 51%, #cbddf3);
    background-image: -moz-linear-gradient(top, #dae7f6, #cddef3 45%, #abc7ec 46%, #abc7ec 50%, #b8cfee 51%, #cbddf3);
    background-image: -o-linear-gradient(top, #dae7f6, #cddef3 45%, #abc7ec 46%, #abc7ec 50%, #b8cfee 51%, #cbddf3);
    background-image: -ms-linear-gradient(top, #dae7f6, #cddef3 45%, #abc7ec 46%, #abc7ec 50%, #b8cfee 51%, #cbddf3);
    background-image: linear-gradient(top, #dae7f6, #cddef3 45%, #abc7ec 46%, #abc7ec 50%, #b8cfee 51%, #cbddf3)
}

.x-panel-header-default-framed-collapsed-bottom-mc {
    background-image: url("data:image/gif;R0lGODlhAQAgA/QAAKvH7LjP7rnQ7rvR7rzS777T77/U78HV8MLW8MPX8cXY8c3e887f88/f89Dg89Hh9NLi9NTi9NXj9Nbk9f///6vH7KvH7KvH7KvH7KvH7KvH7KvH7KvH7KvH7KvH7KvH7CH5BAEAABQALAAAAAABACADRAhGACcIHEiwoMGDCBMqXMiw4cEHAxxKnEixYsUFByxq3Mixo8ePICVGaBCgQIKQKFOqXMmypcuXMGPKlADBAQMAAggYQKAgIAA7");
    background-position: 0 bottom;
    background-color: #cbddf3
}

.x-nbr .x-panel-header-default-framed-collapsed-bottom {
    padding: 0 !important;
    border-width: 0 !important;
    -webkit-border-radius: 0px;
    -moz-border-radius: 0px;
    -ms-border-radius: 0px;
    -o-border-radius: 0px;
    border-radius: 0px;
    background-color: transparent !important;
    background-image: none;
    box-shadow: none !important
}

.x-panel-header-default-framed-collapsed-bottom-frameInfo {
    font-family: dh-4-4-4-4-1-1-1-1-5-5-5-5
}

.x-panel-header-default-framed-collapsed-bottom-tl {
    background-position: 0 -8px
}

.x-panel-header-default-framed-collapsed-bottom-tr {
    background-position: right -12px
}

.x-panel-header-default-framed-collapsed-bottom-bl {
    background-position: 0 -16px
}

.x-panel-header-default-framed-collapsed-bottom-br {
    background-position: right -20px
}

.x-panel-header-default-framed-collapsed-bottom-ml {
    background-position: 0 bottom
}

.x-panel-header-default-framed-collapsed-bottom-mr {
    background-position: right bottom
}

.x-panel-header-default-framed-collapsed-bottom-tc {
    background-position: 0 0
}

.x-panel-header-default-framed-collapsed-bottom-bc {
    background-position: 0 -4px
}

.x-panel-header-default-framed-collapsed-bottom-tr, .x-panel-header-default-framed-collapsed-bottom-br, .x-panel-header-default-framed-collapsed-bottom-mr {
    padding-right: 4px
}

.x-panel-header-default-framed-collapsed-bottom-tl, .x-panel-header-default-framed-collapsed-bottom-bl, .x-panel-header-default-framed-collapsed-bottom-ml {
    padding-left: 4px
}

.x-panel-header-default-framed-collapsed-bottom-tc {
    height: 4px
}

.x-panel-header-default-framed-collapsed-bottom-bc {
    height: 4px
}

.x-panel-header-default-framed-collapsed-bottom-tl, .x-panel-header-default-framed-collapsed-bottom-bl, .x-panel-header-default-framed-collapsed-bottom-tr, .x-panel-header-default-framed-collapsed-bottom-br, .x-panel-header-default-framed-collapsed-bottom-tc, .x-panel-header-default-framed-collapsed-bottom-bc, .x-panel-header-default-framed-collapsed-bottom-ml, .x-panel-header-default-framed-collapsed-bottom-mr {
    background-image: url("data:image/gif;R0lGODlhBAAYAPQAAJm86KHB66LC6qPC6rvS78ba8cjb8svc88vd8szc883e89Pi9dTj9dTk9tfl9djl9dnm9drn9tzn9tzp9uTt+Obv+Ozy+uzz+ezz+u30+vL3/PP3+/P3/P///wAAAJm86CH5BAEAAB0ALAAAAAAEABgARAheAAEIBNCBAwEBAi4gKMCQoQACGjoUQHBhwIOLDzZo3EDgAIWLFBJADMAgQ4YGATRIgMDSgUsHBmIaGAhAQ4ADEwRYiOBgwoGUDiJgGEBgQQUFHTQQGKCgwoKlEDsEBAA7")
}

.x-panel-header-default-framed-collapsed-bottom-ml, .x-panel-header-default-framed-collapsed-bottom-mr {
    background-image: url("data:image/gif;R0lGODlhCAAgA/QAAJm86KvH7LjP7rnQ7rvR7rzS777T77/U78HV8MLW8MPX8cXY8c3e887f88/f89Dg89Hh9NLi9NTi9NXj9PP3+////5m86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86CH5BAEAABUALAAAAAAIACADRAj/AAFQmEBwAgUAAgsaRDiw4MGEDhkqfNiQIMWJEiNCtJiR48aFHy9qrAiSpEiPJjuWxBhS5cmVI1mmbElzpk2ZOGPqRJmT506YPoMCHfqyqMujNXsSRXrzp9GkTpkqfdpUKNWpUqNCtZqV69alX69qrQqWrFivZruWhMAWAkUCcAmcLYs1rNq5eO/qtcs3bd+6fgMDHjyWMFrDdAsrPrw4MePHjiPn/dt4suDKey9DtoyYM2bKKBmIZkARgWkEnjdn7rz6s2bJrVWDhj07Ne3XtnPHvs269m7dvoPj/k1ceO/hxl0fX668uWzk0Jk/l87befXp1oFHz158O/bv18NrwKc+nnty8OXRSlgvgaKD9w4oCpgvgKKB+wYoKtivIL347uQBaJ53/51XIIH+JSggegseGKCBCkLYYIQITmihhBhWmOGDGnbI4YcDgsjghiGWOKKHJjqYIoUiqnhiiyyueCGKL8pIYo04uqhjjDnyuOOMMAJpI40/3lgkkT4mKWSPSx4ZpJFKQtlklEhOaaWUWEIXwZYRUPTAlw9Q1MCYDVAUwJkBUDTAmgNQVMCbBVB0wJwHUJTAnQlQtMCeCxwUEAA7")
}

.x-panel-header-default-framed-collapsed-bottom-mc {
    padding: 2px 2px 2px 2px
}

.x-cmd-slicer.x-panel-header-default-framed-collapsed-bottom:before {
    display: none;
    content: "x-slicer:, stretch:top, frame:4px 4px 4px 4px, frame-bg:url("data:image/gif;R0lGODlhAQAgA/QAAKvH7LjP7rnQ7rvR7rzS777T77/U78HV8MLW8MPX8cXY8c3e887f88/f89Dg89Hh9NLi9NTi9NXj9Nbk9f///6vH7KvH7KvH7KvH7KvH7KvH7KvH7KvH7KvH7KvH7KvH7CH5BAEAABQALAAAAAABACADRAhGACcIHEiwoMGDCBMqXMiw4cEHAxxKnEixYsUFByxq3Mixo8ePICVGaBCgQIKQKFOqXMmypcuXMGPKlADBAQMAAggYQKAgIAA7"), corners:url("data:image/gif;R0lGODlhBAAYAPQAAJm86KHB66LC6qPC6rvS78ba8cjb8svc88vd8szc883e89Pi9dTj9dTk9tfl9djl9dnm9drn9tzn9tzp9uTt+Obv+Ozy+uzz+ezz+u30+vL3/PP3+/P3/P///wAAAJm86CH5BAEAAB0ALAAAAAAEABgARAheAAEIBNCBAwEBAi4gKMCQoQACGjoUQHBhwIOLDzZo3EDgAIWLFBJADMAgQ4YGATRIgMDSgUsHBmIaGAhAQ4ADEwRYiOBgwoGUDiJgGEBgQQUFHTQQGKCgwoKlEDsEBAA7"), sides:url("data:image/gif;R0lGODlhCAAgA/QAAJm86KvH7LjP7rnQ7rvR7rzS777T77/U78HV8MLW8MPX8cXY8c3e887f88/f89Dg89Hh9NLi9NTi9NXj9PP3+////5m86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86CH5BAEAABUALAAAAAAIACADRAj/AAFQmEBwAgUAAgsaRDiw4MGEDhkqfNiQIMWJEiNCtJiR48aFHy9qrAiSpEiPJjuWxBhS5cmVI1mmbElzpk2ZOGPqRJmT506YPoMCHfqyqMujNXsSRXrzp9GkTpkqfdpUKNWpUqNCtZqV69alX69qrQqWrFivZruWhMAWAkUCcAmcLYs1rNq5eO/qtcs3bd+6fgMDHjyWMFrDdAsrPrw4MePHjiPn/dt4suDKey9DtoyYM2bKKBmIZkARgWkEnjdn7rz6s2bJrVWDhj07Ne3XtnPHvs269m7dvoPj/k1ceO/hxl0fX668uWzk0Jk/l87befXp1oFHz158O/bv18NrwKc+nnty8OXRSlgvgaKD9w4oCpgvgKKB+wYoKtivIL347uQBaJ53/51XIIH+JSggegseGKCBCkLYYIQITmihhBhWmOGDGnbI4YcDgsjghiGWOKKHJjqYIoUiqnhiiyyueCGKL8pIYo04uqhjjDnyuOOMMAJpI40/3lgkkT4mKWSPSx4ZpJFKQtlklEhOaaWUWEIXwZYRUPTAlw9Q1MCYDVAUwJkBUDTAmgNQVMCbBVB0wJwHUJTAnQlQtMCeCxwUEAA7")" !important
}

.x-panel-header-default-framed-collapsed-left {
    -moz-border-radius-topleft: 4px;
    -webkit-border-top-left-radius: 4px;
    border-top-left-radius: 4px;
    -moz-border-radius-topright: 4px;
    -webkit-border-top-right-radius: 4px;
    border-top-right-radius: 4px;
    -moz-border-radius-bottomright: 4px;
    -webkit-border-bottom-right-radius: 4px;
    border-bottom-right-radius: 4px;
    -moz-border-radius-bottomleft: 4px;
    -webkit-border-bottom-left-radius: 4px;
    border-bottom-left-radius: 4px;
    padding: 5px 5px 5px 5px;
    border-width: 1px;
    border-style: solid;
    background-image: none;
    background-color: #cbddf3;
    background-image: -webkit-gradient(linear, top, bottom, color-stop(0%, #dae7f6), color-stop(45%, #cddef3), color-stop(46%, #abc7ec), color-stop(50%, #abc7ec), color-stop(51%, #b8cfee), color-stop(0%, #cbddf3));
    background-image: -webkit-linear-gradient(right, #dae7f6, #cddef3 45%, #abc7ec 46%, #abc7ec 50%, #b8cfee 51%, #cbddf3);
    background-image: -moz-linear-gradient(right, #dae7f6, #cddef3 45%, #abc7ec 46%, #abc7ec 50%, #b8cfee 51%, #cbddf3);
    background-image: -o-linear-gradient(right, #dae7f6, #cddef3 45%, #abc7ec 46%, #abc7ec 50%, #b8cfee 51%, #cbddf3);
    background-image: -ms-linear-gradient(right, #dae7f6, #cddef3 45%, #abc7ec 46%, #abc7ec 50%, #b8cfee 51%, #cbddf3);
    background-image: linear-gradient(right, #dae7f6, #cddef3 45%, #abc7ec 46%, #abc7ec 50%, #b8cfee 51%, #cbddf3)
}

.x-panel-header-default-framed-collapsed-left-mc {
    background-image: url("data:image/gif;R0lGODlhIAMBAPQAAKvH7LjP7rnQ7rvR7rzS777T77/U8MHV8MLW8MTY8cXZ8c3e887e88/f89Dg89Hh9NLi9NPi9NTj9Nbk9f///6vH7KvH7KvH7KvH7KvH7KvH7KvH7KvH7KvH7KvH7KvH7CH5BAEAABQALAAAAAAgAwEARAhFABUkQHDAQAECAwQEALCAQQMHDyBEkDChosWLGDNq3Mixo8ePIEOKHEmypMmTKFOqXMmypcuXMGPKnEmzps2bOHPqnBAQADs=");
    background-position: left 0;
    background-repeat: repeat-y;
    background-color: #cbddf3
}

.x-nbr .x-panel-header-default-framed-collapsed-left {
    padding: 0 !important;
    border-width: 0 !important;
    -webkit-border-radius: 0px;
    -moz-border-radius: 0px;
    -ms-border-radius: 0px;
    -o-border-radius: 0px;
    border-radius: 0px;
    background-color: transparent !important;
    background-image: none;
    box-shadow: none !important
}

.x-panel-header-default-framed-collapsed-left-frameInfo {
    font-family: dv-4-4-4-4-1-1-1-1-5-5-5-5
}

.x-panel-header-default-framed-collapsed-left-tl {
    background-position: 0 0
}

.x-panel-header-default-framed-collapsed-left-tr {
    background-position: 0 -4px
}

.x-panel-header-default-framed-collapsed-left-bl {
    background-position: 0 -8px
}

.x-panel-header-default-framed-collapsed-left-br {
    background-position: 0 -12px
}

.x-panel-header-default-framed-collapsed-left-ml {
    background-position: -4px 0
}

.x-panel-header-default-framed-collapsed-left-mr {
    background-position: right 0
}

.x-panel-header-default-framed-collapsed-left-tc {
    background-position: left 0
}

.x-panel-header-default-framed-collapsed-left-bc {
    background-position: left -4px
}

.x-panel-header-default-framed-collapsed-left-tr, .x-panel-header-default-framed-collapsed-left-br, .x-panel-header-default-framed-collapsed-left-mr {
    padding-right: 4px
}

.x-panel-header-default-framed-collapsed-left-tl, .x-panel-header-default-framed-collapsed-left-bl, .x-panel-header-default-framed-collapsed-left-ml {
    padding-left: 4px
}

.x-panel-header-default-framed-collapsed-left-tc {
    height: 4px
}

.x-panel-header-default-framed-collapsed-left-bc {
    height: 4px
}

.x-panel-header-default-framed-collapsed-left-tl, .x-panel-header-default-framed-collapsed-left-bl, .x-panel-header-default-framed-collapsed-left-tr, .x-panel-header-default-framed-collapsed-left-br, .x-panel-header-default-framed-collapsed-left-tc, .x-panel-header-default-framed-collapsed-left-bc, .x-panel-header-default-framed-collapsed-left-ml, .x-panel-header-default-framed-collapsed-left-mr {
    background-image: url("data:image/gif;R0lGODlhDAAQAPUAAJm86KHB66LC6qPC6rvS78fa8sjb8srd88vc88vd88zc88zd88ze89Pi9dTk9dXj9dfl9djl9dnm9drn9tvo9tzo9uTt+Obv+Ovz+uzy+u3z+e3z+u30+vL3/PP3+/P3/P///wAAAJm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86CH5BAEAACAALAAAAAAMABAARQhyAEF8ICAAgAcDBSBEqABAgAYGBQwiVMhQAIEOICQmXAhAIYUBGikCIPDgQoKQESQAmGABAQGUKjsEaMABJgAMBwJ0sCmzwQabDiHazJBz58GNKj2CPKpQJQEHFxbYBNGBwNKJKVdaUPCSadYBFzN6VRkQADs=")
}

.x-panel-header-default-framed-collapsed-left-tc, .x-panel-header-default-framed-collapsed-left-bc {
    background-image: url("data:image/gif;R0lGODlhIAMIAPQAAJm86KvH7LjP7rnQ7rvR7rzS777T77/U8MHV8MLW8MTY8cXZ8c3e887e88/f89Dg89Hh9NLi9NPi9NTj9Nbk9fP3+////5m86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86CH5BAEAABYALAAAAAAgAwgARAj/AAEIHEiwoMGDCBMqXMiwocOHECNKnEixosWLGDNq3Mixo8ePIEOKHEmypMmTFBcoSIDggIECBAYICMCggYMHECJImEChp8+fQIMKHUq0qNGjSJMqXcq0qdOnUKNKnUq1qtWrWLNq3cq1q9evYMOKpaCSpUuYMmnaxKmT59i3cOPKnUu3rt27ePPq3cu379MKgAMLHky4sOHDiBMrXsy4sePHkCNLnky5suXLmDNr3sy5s+fPoEOLHk26tOnTqFOrXs26tevXsGPLnk27tm3BZVu+jDmz5s2cO/0KH068uPHjyJMrX848bu6zvNX+btu8uvXr2LNr3869u1+U4MOLER9Pvrz58+jTq1/Pvr17lAEBADs=");
    background-repeat: repeat-x
}

.x-panel-header-default-framed-collapsed-left-mc {
    padding: 2px 2px 2px 2px
}

.x-cmd-slicer.x-panel-header-default-framed-collapsed-left:before {
    display: none;
    content: "x-slicer:, stretch:right, frame:4px 4px 4px 4px, frame-bg:url("data:image/gif;R0lGODlhIAMBAPQAAKvH7LjP7rnQ7rvR7rzS777T77/U8MHV8MLW8MTY8cXZ8c3e887e88/f89Dg89Hh9NLi9NPi9NTj9Nbk9f///6vH7KvH7KvH7KvH7KvH7KvH7KvH7KvH7KvH7KvH7KvH7CH5BAEAABQALAAAAAAgAwEARAhFABUkQHDAQAECAwQEALCAQQMHDyBEkDChosWLGDNq3Mixo8ePIEOKHEmypMmTKFOqXMmypcuXMGPKnEmzps2bOHPqnBAQADs="), corners:url("data:image/gif;R0lGODlhDAAQAPUAAJm86KHB66LC6qPC6rvS78fa8sjb8srd88vc88vd88zc88zd88ze89Pi9dTk9dXj9dfl9djl9dnm9drn9tvo9tzo9uTt+Obv+Ovz+uzy+u3z+e3z+u30+vL3/PP3+/P3/P///wAAAJm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86CH5BAEAACAALAAAAAAMABAARQhyAEF8ICAAgAcDBSBEqABAgAYGBQwiVMhQAIEOICQmXAhAIYUBGikCIPDgQoKQESQAmGABAQGUKjsEaMABJgAMBwJ0sCmzwQabDiHazJBz58GNKj2CPKpQJQEHFxbYBNGBwNKJKVdaUPCSadYBFzN6VRkQADs="), sides:url("data:image/gif;R0lGODlhIAMIAPQAAJm86KvH7LjP7rnQ7rvR7rzS777T77/U8MHV8MLW8MTY8cXZ8c3e887e88/f89Dg89Hh9NLi9NPi9NTj9Nbk9fP3+////5m86Jm86Jm86Jm86Jm86Jm86Jm86Jm86Jm86CH5BAEAABYALAAAAAAgAwgARAj/AAEIHEiwoMGDCBMqXMiwocOHECNKnEixosWLGDNq3Mixo8ePIEOKHEmypMmTFBcoSIDggIECBAYICMCggYMHECJImEChp8+fQIMKHUq0qNGjSJMqXcq0qdOnUKNKnUq1qtWrWLNq3cq1q9evYMOKpaCSpUuYMmnaxKmT59i3cOPKnUu3rt27ePPq3cu379MKgAMLHky4sOHDiBMrXsy4sePHkCNLnky5suXLmDNr3sy5s+fPoEOLHk26tOnTqFOrXs26tevXsGPLnk27tm3BZVu+jDmz5s2cO/0KH068uPHjyJMrX848bu6zvNX+btu8uvXr2LNr3869u1+U4MOLER9Pvrz58+jTq1/Pvr17lAEBADs=")" !important
}

.x-panel .x-panel-header-default-framed-top {
    border-bottom-width: 1px !important
}

.x-panel .x-panel-header-default-framed-right {
    border-left-width: 1px !important
}

.x-panel .x-panel-header-default-framed-bottom {
    border-top-width: 1px !important
}

.x-panel .x-panel-header-default-framed-left {
    border-right-width: 1px !important
}

.x-nbr .x-panel-header-default-framed-collapsed-top {
    border-bottom-width: 0 !important
}

.x-nbr .x-panel-header-default-framed-collapsed-right {
    border-left-width: 0 !important
}

.x-nbr .x-panel-header-default-framed-collapsed-bottom {
    border-top-width: 0 !important
}

.x-nbr .x-panel-header-default-framed-collapsed-left {
    border-right-width: 0 !important
}

.x-panel-header-default-framed-top {
    -webkit-box-shadow: #f3f7fb 0 1px 0px 0 inset, #f3f7fb -1px 0 0px 0 inset, #f3f7fb 1px 0 0px 0 inset;
    -moz-box-shadow: #f3f7fb 0 1px 0px 0 inset, #f3f7fb -1px 0 0px 0 inset, #f3f7fb 1px 0 0px 0 inset;
    box-shadow: #f3f7fb 0 1px 0px 0 inset, #f3f7fb -1px 0 0px 0 inset, #f3f7fb 1px 0 0px 0 inset
}

.x-panel-header-default-framed-right {
    -webkit-box-shadow: #f3f7fb 0 1px 0px 0 inset, #f3f7fb 0 -1px 0px 0 inset, #f3f7fb -1px 0 0px 0 inset;
    -moz-box-shadow: #f3f7fb 0 1px 0px 0 inset, #f3f7fb 0 -1px 0px 0 inset, #f3f7fb -1px 0 0px 0 inset;
    box-shadow: #f3f7fb 0 1px 0px 0 inset, #f3f7fb 0 -1px 0px 0 inset, #f3f7fb -1px 0 0px 0 inset
}

.x-panel-header-default-framed-bottom {
    -webkit-box-shadow: #f3f7fb 0 -1px 0px 0 inset, #f3f7fb -1px 0 0px 0 inset, #f3f7fb 1px 0 0px 0 inset;
    -moz-box-shadow: #f3f7fb 0 -1px 0px 0 inset, #f3f7fb -1px 0 0px 0 inset, #f3f7fb 1px 0 0px 0 inset;
    box-shadow: #f3f7fb 0 -1px 0px 0 inset, #f3f7fb -1px 0 0px 0 inset, #f3f7fb 1px 0 0px 0 inset
}

.x-panel-header-default-framed-left {
    -webkit-box-shadow: #f3f7fb 0 1px 0px 0 inset, #f3f7fb 0 -1px 0px 0 inset, #f3f7fb 1px 0 0px 0 inset;
    -moz-box-shadow: #f3f7fb 0 1px 0px 0 inset, #f3f7fb 0 -1px 0px 0 inset, #f3f7fb 1px 0 0px 0 inset;
    box-shadow: #f3f7fb 0 1px 0px 0 inset, #f3f7fb 0 -1px 0px 0 inset, #f3f7fb 1px 0 0px 0 inset
}

.x-panel-header-default-framed-horizontal .x-tool-after-title {
    margin: 0 0 0 2px
}

.x-panel-header-default-framed-horizontal .x-tool-before-title {
    margin: 0 2px 0 0
}

.x-panel-header-default-framed-vertical .x-tool-after-title {
    margin: 2px 0 0 0
}

.x-panel-header-default-framed-vertical .x-tool-before-title {
    margin: 0 0 2px 0
}

.x-panel-header-default-framed .x-tool-focus {
    outline: 1px dotted #464646;
    outline-offset: 0
}

.x-ie8 .x-panel-header-default-framed .x-tool-focus {
    outline: none
}

.x-ie8 .x-panel-header-default-framed .x-tool-focus:after {
    position: absolute;
    content: ' ';
    top: -1px;
    right: -1px;
    bottom: -1px;
    left: -1px;
    border: 1px dotted #464646;
    pointer-events: none
}

.x-panel-default-framed-resizable .x-panel-handle {
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=0)";
    opacity: 0
}

.x-btn-group-default {
    border-color: #b7c8d7;
    -webkit-box-shadow: #e3ebf5 0 1px 0px 0 inset, #e3ebf5 0 -1px 0px 0 inset, #e3ebf5 -1px 0 0px 0 inset, #e3ebf5 1px 0 0px 0 inset;
    -moz-box-shadow: #e3ebf5 0 1px 0px 0 inset, #e3ebf5 0 -1px 0px 0 inset, #e3ebf5 -1px 0 0px 0 inset, #e3ebf5 1px 0 0px 0 inset;
    box-shadow: #e3ebf5 0 1px 0px 0 inset, #e3ebf5 0 -1px 0px 0 inset, #e3ebf5 -1px 0 0px 0 inset, #e3ebf5 1px 0 0px 0 inset
}

.x-btn-group-header-default {
    margin: 2px 2px 0 2px;
    padding: 1px 0;
    line-height: 15px;
    background: #c2d8f0;
    -moz-border-radius-topleft: 0px;
    -webkit-border-top-left-radius: 0px;
    border-top-left-radius: 0px;
    -moz-border-radius-topright: 0px;
    -webkit-border-top-right-radius: 0px;
    border-top-right-radius: 0px
}

.x-btn-group-header-default .x-tool-img {
    background-color: #c2d8f0
}

.x-btn-group-header-title-default {
    font: normal 11px tahoma, arial, verdana, sans-serif;
    line-height: 15px;
    color: #3e6aaa
}

.x-btn-group-body-default {
    padding: 0 1px
}

.x-btn-group-body-default .x-table-layout {
    border-spacing: 0
}

.x-btn-group-default-framed {
    -webkit-border-radius: 2px;
    -moz-border-radius: 2px;
    -ms-border-radius: 2px;
    -o-border-radius: 2px;
    border-radius: 2px;
    padding: 1px 1px 1px 1px;
    border-width: 1px;
    border-style: solid;
    background-color: #d0def0
}

.x-btn-group-default-framed-mc {
    background-color: #d0def0
}

.x-nbr .x-btn-group-default-framed {
    padding: 0 !important;
    border-width: 0 !important;
    -webkit-border-radius: 0px;
    -moz-border-radius: 0px;
    -ms-border-radius: 0px;
    -o-border-radius: 0px;
    border-radius: 0px;
    background-color: transparent !important;
    box-shadow: none !important
}

.x-btn-group-default-framed-frameInfo {
    font-family: dh-2-2-2-2-1-1-1-1-1-1-1-1
}

.x-btn-group-default-framed-tl {
    background-position: 0 -4px
}

.x-btn-group-default-framed-tr {
    background-position: right -6px
}

.x-btn-group-default-framed-bl {
    background-position: 0 -8px
}

.x-btn-group-default-framed-br {
    background-position: right -10px
}

.x-btn-group-default-framed-ml {
    background-position: 0 top
}

.x-btn-group-default-framed-mr {
    background-position: right top
}

.x-btn-group-default-framed-tc {
    background-position: 0 0
}

.x-btn-group-default-framed-bc {
    background-position: 0 -2px
}

.x-btn-group-default-framed-tr, .x-btn-group-default-framed-br, .x-btn-group-default-framed-mr {
    padding-right: 2px
}

.x-btn-group-default-framed-tl, .x-btn-group-default-framed-bl, .x-btn-group-default-framed-ml {
    padding-left: 2px
}

.x-btn-group-default-framed-tc {
    height: 2px
}

.x-btn-group-default-framed-bc {
    height: 2px
}

.x-btn-group-default-framed-tl, .x-btn-group-default-framed-bl, .x-btn-group-default-framed-tr, .x-btn-group-default-framed-br, .x-btn-group-default-framed-tc, .x-btn-group-default-framed-bc, .x-btn-group-default-framed-ml, .x-btn-group-default-framed-mr {
    background-image: url("data:image/gif;R0lGODlhAgAMAPIAALfI17zM2uHq9ePr9eru8////7fI17fI1yH5BAEAAAUALAAAAAACAAwAQggXAAEACCCAQIABAwIQEHBwgECCDA0qDAgAOw==")
}

.x-btn-group-default-framed-ml, .x-btn-group-default-framed-mr {
    background-image: url("data:image/gif;R0lGODlhBABUAPEAALfI1+Pr9f///7fI1yH5BAEAAAIALAAAAAAEAFQAQQg7AAEECABAIEGDBQcmPKgQocOGEBlKXEjx4USLFSNmvKgRo8eOIDmK3Ejy40iTJUOmPKkSpcuWMFmODAgAOw==");
    background-repeat: repeat-y
}

.x-btn-group-default-framed-mc {
    padding: 0px 0px 0px 0px
}

.x-cmd-slicer.x-btn-group-default-framed:before {
    display: none;
    content: "x-slicer:, frame:2px 2px 2px 2px, corners:url("data:image/gif;R0lGODlhAgAMAPIAALfI17zM2uHq9ePr9eru8////7fI17fI1yH5BAEAAAUALAAAAAACAAwAQggXAAEACCCAQIABAwIQEHBwgECCDA0qDAgAOw=="), sides:url("data:image/gif;R0lGODlhBABUAPEAALfI1+Pr9f///7fI1yH5BAEAAAIALAAAAAAEAFQAQQg7AAEECABAIEGDBQcmPKgQocOGEBlKXEjx4USLFSNmvKgRo8eOIDmK3Ejy40iTJUOmPKkSpcuWMFmODAgAOw==")" !important
}

.x-btn-group-default-framed-notitle {
    -webkit-border-radius: 2px;
    -moz-border-radius: 2px;
    -ms-border-radius: 2px;
    -o-border-radius: 2px;
    border-radius: 2px;
    padding: 1px 1px 1px 1px;
    border-width: 1px;
    border-style: solid;
    background-color: #d0def0
}

.x-btn-group-default-framed-notitle-mc {
    background-color: #d0def0
}

.x-nbr .x-btn-group-default-framed-notitle {
    padding: 0 !important;
    border-width: 0 !important;
    -webkit-border-radius: 0px;
    -moz-border-radius: 0px;
    -ms-border-radius: 0px;
    -o-border-radius: 0px;
    border-radius: 0px;
    background-color: transparent !important;
    box-shadow: none !important
}

.x-btn-group-default-framed-notitle-frameInfo {
    font-family: dh-2-2-2-2-1-1-1-1-1-1-1-1
}

.x-btn-group-default-framed-notitle-tl {
    background-position: 0 -4px
}

.x-btn-group-default-framed-notitle-tr {
    background-position: right -6px
}

.x-btn-group-default-framed-notitle-bl {
    background-position: 0 -8px
}

.x-btn-group-default-framed-notitle-br {
    background-position: right -10px
}

.x-btn-group-default-framed-notitle-ml {
    background-position: 0 top
}

.x-btn-group-default-framed-notitle-mr {
    background-position: right top
}

.x-btn-group-default-framed-notitle-tc {
    background-position: 0 0
}

.x-btn-group-default-framed-notitle-bc {
    background-position: 0 -2px
}

.x-btn-group-default-framed-notitle-tr, .x-btn-group-default-framed-notitle-br, .x-btn-group-default-framed-notitle-mr {
    padding-right: 2px
}

.x-btn-group-default-framed-notitle-tl, .x-btn-group-default-framed-notitle-bl, .x-btn-group-default-framed-notitle-ml {
    padding-left: 2px
}

.x-btn-group-default-framed-notitle-tc {
    height: 2px
}

.x-btn-group-default-framed-notitle-bc {
    height: 2px
}

.x-btn-group-default-framed-notitle-tl, .x-btn-group-default-framed-notitle-bl, .x-btn-group-default-framed-notitle-tr, .x-btn-group-default-framed-notitle-br, .x-btn-group-default-framed-notitle-tc, .x-btn-group-default-framed-notitle-bc, .x-btn-group-default-framed-notitle-ml, .x-btn-group-default-framed-notitle-mr {
    background-image: url("data:image/gif;R0lGODlhAgAMAPIAALfI17zM2uHq9ePr9eru8////7fI17fI1yH5BAEAAAUALAAAAAACAAwAQggXAAEACCCAQIABAwIQEHBwgECCDA0qDAgAOw==")
}

.x-btn-group-default-framed-notitle-ml, .x-btn-group-default-framed-notitle-mr {
    background-image: url("data:image/gif;R0lGODlhBABCAPEAALfI1+Pr9f///7fI1yH5BAEAAAIALAAAAAAEAEIAQQg0AAEECABAIEGDBQcmPKgQocOGEBlKXEjx4USLFSNmvKgRo8eOIDmK3Ejy40iTJUOmPKkyIAA7");
    background-repeat: repeat-y
}

.x-btn-group-default-framed-notitle-mc {
    padding: 0px 0px 0px 0px
}

.x-cmd-slicer.x-btn-group-default-framed-notitle:before {
    display: none;
    content: "x-slicer:, frame:2px 2px 2px 2px, corners:url("data:image/gif;R0lGODlhAgAMAPIAALfI17zM2uHq9ePr9eru8////7fI17fI1yH5BAEAAAUALAAAAAACAAwAQggXAAEACCCAQIABAwIQEHBwgECCDA0qDAgAOw=="), sides:url("data:image/gif;R0lGODlhBABCAPEAALfI1+Pr9f///7fI1yH5BAEAAAIALAAAAAAEAEIAQQg0AAEECABAIEGDBQcmPKgQocOGEBlKXEjx4USLFSNmvKgRo8eOIDmK3Ejy40iTJUOmPKkyIAA7")" !important
}

.x-btn-group-default-framed {
    border-color: #b7c8d7;
    -webkit-box-shadow: #e3ebf5 0 1px 0px 0 inset, #e3ebf5 0 -1px 0px 0 inset, #e3ebf5 -1px 0 0px 0 inset, #e3ebf5 1px 0 0px 0 inset;
    -moz-box-shadow: #e3ebf5 0 1px 0px 0 inset, #e3ebf5 0 -1px 0px 0 inset, #e3ebf5 -1px 0 0px 0 inset, #e3ebf5 1px 0 0px 0 inset;
    box-shadow: #e3ebf5 0 1px 0px 0 inset, #e3ebf5 0 -1px 0px 0 inset, #e3ebf5 -1px 0 0px 0 inset, #e3ebf5 1px 0 0px 0 inset
}

.x-btn-group-header-default-framed {
    margin: 2px 2px 0 2px;
    padding: 1px 0;
    line-height: 15px;
    background: #c2d8f0;
    -moz-border-radius-topleft: 2px;
    -webkit-border-top-left-radius: 2px;
    border-top-left-radius: 2px;
    -moz-border-radius-topright: 2px;
    -webkit-border-top-right-radius: 2px;
    border-top-right-radius: 2px
}

.x-btn-group-header-default-framed .x-tool-img {
    background-color: #c2d8f0
}

.x-btn-group-header-title-default-framed {
    font: normal 11px tahoma, arial, verdana, sans-serif;
    line-height: 15px;
    color: #3e6aaa
}

.x-btn-group-body-default-framed {
    padding: 0 1px
}

.x-btn-group-body-default-framed .x-table-layout {
    border-spacing: 0
}

.x-dashboard-column {
    padding: 0 0 7px 0
}

.x-dashboard-panel {
    margin-top: 7px
}

.x-dashboard-column-first {
    padding-left: 7px;
    clear: left
}

.x-dashboard-column-last {
    padding-right: 7px
}

.x-dashboard .x-panel-dd-spacer {
    border: 2px dashed #99bbe8;
    background: #f6f6f6;
    border-radius: 4px;
    -moz-border-radius: 4px;
    margin-top: 7px
}

.x-dashboard-dd-over {
    overflow: hidden !important
}

.x-window-ghost {
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=65)";
    opacity: 0.65
}

.x-window-default {
    border-color: #a2b1c5;
    -webkit-border-radius: 5px;
    -moz-border-radius: 5px;
    -ms-border-radius: 5px;
    -o-border-radius: 5px;
    border-radius: 5px;
    -webkit-box-shadow: #ecf2fb 0 1px 0px 0 inset, #ecf2fb 0 -1px 0px 0 inset, #ecf2fb -1px 0 0px 0 inset, #ecf2fb 1px 0 0px 0 inset;
    -moz-box-shadow: #ecf2fb 0 1px 0px 0 inset, #ecf2fb 0 -1px 0px 0 inset, #ecf2fb -1px 0 0px 0 inset, #ecf2fb 1px 0 0px 0 inset;
    box-shadow: #ecf2fb 0 1px 0px 0 inset, #ecf2fb 0 -1px 0px 0 inset, #ecf2fb -1px 0 0px 0 inset, #ecf2fb 1px 0 0px 0 inset
}

.x-window-default {
    -webkit-border-radius: 5px;
    -moz-border-radius: 5px;
    -ms-border-radius: 5px;
    -o-border-radius: 5px;
    border-radius: 5px;
    padding: 4px 4px 4px 4px;
    border-width: 1px;
    border-style: solid;
    background-color: #ced9e7
}

.x-window-default-mc {
    background-color: #ced9e7
}

.x-nbr .x-window-default {
    padding: 0 !important;
    border-width: 0 !important;
    -webkit-border-radius: 0px;
    -moz-border-radius: 0px;
    -ms-border-radius: 0px;
    -o-border-radius: 0px;
    border-radius: 0px;
    background-color: transparent !important;
    box-shadow: none !important
}

.x-window-default-frameInfo {
    font-family: dh-5-5-5-5-1-1-1-1-4-4-4-4
}

.x-window-default-tl {
    background-position: 0 -10px
}

.x-window-default-tr {
    background-position: right -15px
}

.x-window-default-bl {
    background-position: 0 -20px
}

.x-window-default-br {
    background-position: right -25px
}

.x-window-default-ml {
    background-position: 0 top
}

.x-window-default-mr {
    background-position: right top
}

.x-window-default-tc {
    background-position: 0 0
}

.x-window-default-bc {
    background-position: 0 -5px
}

.x-window-default-tr, .x-window-default-br, .x-window-default-mr {
    padding-right: 5px
}

.x-window-default-tl, .x-window-default-bl, .x-window-default-ml {
    padding-left: 5px
}

.x-window-default-tc {
    height: 5px
}

.x-window-default-bc {
    height: 5px
}

.x-window-default-tl, .x-window-default-bl, .x-window-default-tr, .x-window-default-br, .x-window-default-tc, .x-window-default-bc, .x-window-default-ml, .x-window-default-mr {
    background-image: url("data:image/gif;R0lGODlhBQAeAPUAAKKxxai1yKm3yKq5y6u4yrfD0bjC0LnC0bnF1rnG1rnG17vF08XN1cbN187S187Z59DT2NDX39Hc6dnj8Nrj79vb2+Dk6ePn7OXs9+bm5ubs9+fs9+fs+Orw+evx++zy+////wAAAKKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxSH5BAEAACAALAAAAAAFAB4ARQh4AAEIFPihYMEOGhJEAJGhAoQDAx5IlGghgYcJEgh0kCARIYIGFSaKnAgCxIUFBAJsFElBgwEICi5yfECBwwGDBUfqFDlQIIgICDB0KKCBgkQCCy6UlDDBQwILEiV0EGBgg9EHFRgg0NAhaocBTD0ocDDgAIQKGQICADs=")
}

.x-window-default-ml, .x-window-default-mr {
    background-image: url("data:image/gif;R0lGODlhCgC+APEAAKKxxc7Z5+zy+////yH5BAEAAAMALAAAAAAKAL4AQQjNAAEICECwoAAAAgsaRDhQYYCDCR1CbKhwosOHDC9alJiRY8SKHUF+XDiS4EaRFEmmNBlSpcaWLEtilHnSpceVM3HWjKkTZs6XNH3u/HkTaM+gSI8qNcq0qFOUTaE+tSm1KtWrPKNiJWo161SvXbluHUpWqNmkWsGOPbv0q1i1cN/KLYvWLd22Ye+mnct2r167fQHXzRuY8OC1h+P+NYwXcWPFhR37jQw5MV/LiyULfnyZc+bKnil3noxZ9OfRm0mHLs16tWvVsFPLZjw5IAA7");
    background-repeat: repeat-y
}

.x-window-default-mc {
    padding: 0px 0px 0px 0px
}

.x-cmd-slicer.x-window-default:before {
    display: none;
    content: "x-slicer:, frame:5px 5px 5px 5px, corners:url("data:image/gif;R0lGODlhBQAeAPUAAKKxxai1yKm3yKq5y6u4yrfD0bjC0LnC0bnF1rnG1rnG17vF08XN1cbN187S187Z59DT2NDX39Hc6dnj8Nrj79vb2+Dk6ePn7OXs9+bm5ubs9+fs9+fs+Orw+evx++zy+////wAAAKKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxSH5BAEAACAALAAAAAAFAB4ARQh4AAEIFPihYMEOGhJEAJGhAoQDAx5IlGghgYcJEgh0kCARIYIGFSaKnAgCxIUFBAJsFElBgwEICi5yfECBwwGDBUfqFDlQIIgICDB0KKCBgkQCCy6UlDDBQwILEiV0EGBgg9EHFRgg0NAhaocBTD0ocDDgAIQKGQICADs="), sides:url("data:image/gif;R0lGODlhCgC+APEAAKKxxc7Z5+zy+////yH5BAEAAAMALAAAAAAKAL4AQQjNAAEICECwoAAAAgsaRDhQYYCDCR1CbKhwosOHDC9alJiRY8SKHUF+XDiS4EaRFEmmNBlSpcaWLEtilHnSpceVM3HWjKkTZs6XNH3u/HkTaM+gSI8qNcq0qFOUTaE+tSm1KtWrPKNiJWo161SvXbluHUpWqNmkWsGOPbv0q1i1cN/KLYvWLd22Ye+mnct2r167fQHXzRuY8OC1h+P+NYwXcWPFhR37jQw5MV/LiyULfnyZc+bKnil3noxZ9OfRm0mHLs16tWvVsFPLZjw5IAA7")" !important
}

.x-window-body-default {
    border-color: #99bbe8;
    border-width: 1px;
    border-style: solid;
    background: #dfe8f6;
    color: #000;
    font-size: 12px;
    font-weight: normal;
    font-family: tahoma, arial, verdana, sans-serif
}

.x-window-header-default {
    font-size: 11px;
    border-color: #a2b1c5;
    background-color: #ced9e7
}

.x-window-header-default .x-tool-img {
    background-color: #ced9e7
}

.x-window-header-default-horizontal .x-window-header-default-tab-bar {
    margin-top: -5px;
    margin-bottom: -5px
}

.x-window-header-default-vertical .x-window-header-default-tab-bar {
    margin-right: -5px;
    margin-left: -5px
}

.x-window-header-title-default {
    color: #04468c;
    font-size: 11px;
    font-weight: bold;
    font-family: tahoma, arial, verdana, sans-serif;
    line-height: 15px
}

.x-window-header-title-default > .x-title-text-default {
    padding: 0 2px 1px;
    text-transform: none
}

.x-window-header-title-default > .x-title-icon-wrap-default.x-title-icon-top {
    height: 18px;
    padding-bottom: 2px
}

.x-window-header-title-default > .x-title-icon-wrap-default.x-title-icon-right {
    width: 18px;
    padding-left: 2px
}

.x-window-header-title-default > .x-title-icon-wrap-default.x-title-icon-bottom {
    height: 18px;
    padding-top: 2px
}

.x-window-header-title-default > .x-title-icon-wrap-default.x-title-icon-left {
    width: 18px;
    padding-right: 2px
}

.x-window-header-title-default > .x-title-icon-wrap-default > .x-title-icon-default {
    width: 16px;
    height: 16px;
    font-size: 16px;
    color: #04468c;
    background-position: center center
}

.x-window-header-title-default > .x-title-icon-wrap-default > .x-title-icon-default.x-title-glyph {
    opacity: 0.5
}

.x-ie8 .x-window-header-title-default > .x-title-icon-wrap-default > .x-title-icon-default.x-title-glyph {
    color: #6990ba
}

.x-window-header-default-top {
    -moz-border-radius-topleft: 5px;
    -webkit-border-top-left-radius: 5px;
    border-top-left-radius: 5px;
    -moz-border-radius-topright: 5px;
    -webkit-border-top-right-radius: 5px;
    border-top-right-radius: 5px;
    -moz-border-radius-bottomright: 0;
    -webkit-border-bottom-right-radius: 0;
    border-bottom-right-radius: 0;
    -moz-border-radius-bottomleft: 0;
    -webkit-border-bottom-left-radius: 0;
    border-bottom-left-radius: 0;
    padding: 5px 5px 1px 5px;
    border-width: 1px 1px 0 1px;
    border-style: solid;
    background-color: #ced9e7
}

.x-window-header-default-top-mc {
    background-color: #ced9e7
}

.x-nbr .x-window-header-default-top {
    padding: 0 !important;
    border-width: 0 !important;
    -webkit-border-radius: 0px;
    -moz-border-radius: 0px;
    -ms-border-radius: 0px;
    -o-border-radius: 0px;
    border-radius: 0px;
    background-color: transparent !important;
    box-shadow: none !important
}

.x-window-header-default-top-frameInfo {
    font-family: dh-5-5-0-5-1-1-0-1-5-5-1-5
}

.x-window-header-default-top-tl {
    background-position: 0 -10px
}

.x-window-header-default-top-tr {
    background-position: right -15px
}

.x-window-header-default-top-bl {
    background-position: 0 -20px
}

.x-window-header-default-top-br {
    background-position: right -25px
}

.x-window-header-default-top-ml {
    background-position: 0 top
}

.x-window-header-default-top-mr {
    background-position: right top
}

.x-window-header-default-top-tc {
    background-position: 0 0
}

.x-window-header-default-top-bc {
    background-position: 0 -5px
}

.x-window-header-default-top-tr, .x-window-header-default-top-br, .x-window-header-default-top-mr {
    padding-right: 5px
}

.x-window-header-default-top-tl, .x-window-header-default-top-bl, .x-window-header-default-top-ml {
    padding-left: 5px
}

.x-window-header-default-top-tc {
    height: 5px
}

.x-window-header-default-top-bc {
    height: 0
}

.x-window-header-default-top-tl, .x-window-header-default-top-bl, .x-window-header-default-top-tr, .x-window-header-default-top-br, .x-window-header-default-top-tc, .x-window-header-default-top-bc, .x-window-header-default-top-ml, .x-window-header-default-top-mr {
    background-image: url("data:image/gif;R0lGODlhBQAeAPQAAKKxxai1yKm3yKu4yrfD0bjC0LjF17jH1rvF087Z59DX39Hc6dnj8Nrj797l8N7m8d/m8eDk6ePn7Oft+Ofu+Orw+urx+uzy+////wAAAKKxxaKxxaKxxaKxxaKxxaKxxSH5BAEAABgALAAAAAAFAB4ARAhdAAEIFJigYEEKEA4owADggsGHCSIcqMBgQUOICS4AwPgQAwYJCAYEmLDgYQMHBS5C1HihZUuOMCFiUGDgAQUCDhoUHIBAgscFDCwciFBwwQQBKhMkNaiR6caCGgMCADs=")
}

.x-window-header-default-top-ml, .x-window-header-default-top-mr {
    background-image: url("data:image/gif;R0lGODlhCgANAPEAAKKxxc7Z5+zy+////yH5BAEAAAMALAAAAAAKAA0AQQgtAAEICECwoAAAAgsaRDhQYYCDCR1CbKhwosOHDC9alJiRY8SKHUF+XDiS4MGAADs=");
    background-repeat: repeat-y
}

.x-window-header-default-top-mc {
    padding: 1px 1px 1px 1px
}

.x-cmd-slicer.x-window-header-default-top:before {
    display: none;
    content: "x-slicer:, frame:5px 5px 0 5px, corners:url("data:image/gif;R0lGODlhBQAeAPQAAKKxxai1yKm3yKu4yrfD0bjC0LjF17jH1rvF087Z59DX39Hc6dnj8Nrj797l8N7m8d/m8eDk6ePn7Oft+Ofu+Orw+urx+uzy+////wAAAKKxxaKxxaKxxaKxxaKxxaKxxSH5BAEAABgALAAAAAAFAB4ARAhdAAEIFJigYEEKEA4owADggsGHCSIcqMBgQUOICS4AwPgQAwYJCAYEmLDgYQMHBS5C1HihZUuOMCFiUGDgAQUCDhoUHIBAgscFDCwciFBwwQQBKhMkNaiR6caCGgMCADs="), sides:url("data:image/gif;R0lGODlhCgANAPEAAKKxxc7Z5+zy+////yH5BAEAAAMALAAAAAAKAA0AQQgtAAEICECwoAAAAgsaRDhQYYCDCR1CbKhwosOHDC9alJiRY8SKHUF+XDiS4MGAADs=")" !important
}

.x-window-header-default-right {
    -moz-border-radius-topleft: 0;
    -webkit-border-top-left-radius: 0;
    border-top-left-radius: 0;
    -moz-border-radius-topright: 5px;
    -webkit-border-top-right-radius: 5px;
    border-top-right-radius: 5px;
    -moz-border-radius-bottomright: 5px;
    -webkit-border-bottom-right-radius: 5px;
    border-bottom-right-radius: 5px;
    -moz-border-radius-bottomleft: 0;
    -webkit-border-bottom-left-radius: 0;
    border-bottom-left-radius: 0;
    padding: 5px 5px 5px 1px;
    border-width: 1px 1px 1px 0;
    border-style: solid;
    background-color: #ced9e7
}

.x-window-header-default-right-mc {
    background-color: #ced9e7
}

.x-nbr .x-window-header-default-right {
    padding: 0 !important;
    border-width: 0 !important;
    -webkit-border-radius: 0px;
    -moz-border-radius: 0px;
    -ms-border-radius: 0px;
    -o-border-radius: 0px;
    border-radius: 0px;
    background-color: transparent !important;
    box-shadow: none !important
}

.x-window-header-default-right-frameInfo {
    font-family: dh-5-5-5-0-1-1-1-0-5-5-5-1
}

.x-window-header-default-right-tl {
    background-position: 0 -10px
}

.x-window-header-default-right-tr {
    background-position: right -15px
}

.x-window-header-default-right-bl {
    background-position: 0 -20px
}

.x-window-header-default-right-br {
    background-position: right -25px
}

.x-window-header-default-right-ml {
    background-position: 0 top
}

.x-window-header-default-right-mr {
    background-position: right top
}

.x-window-header-default-right-tc {
    background-position: 0 0
}

.x-window-header-default-right-bc {
    background-position: 0 -5px
}

.x-window-header-default-right-tr, .x-window-header-default-right-br, .x-window-header-default-right-mr {
    padding-right: 5px
}

.x-window-header-default-right-tl, .x-window-header-default-right-bl, .x-window-header-default-right-ml {
    padding-left: 0
}

.x-window-header-default-right-tc {
    height: 5px
}

.x-window-header-default-right-bc {
    height: 5px
}

.x-window-header-default-right-tl, .x-window-header-default-right-bl, .x-window-header-default-right-tr, .x-window-header-default-right-br, .x-window-header-default-right-tc, .x-window-header-default-right-bc, .x-window-header-default-right-ml, .x-window-header-default-right-mr {
    background-image: url("data:image/gif;R0lGODlhBQAeAPQAAKKxxam3yKq5y6u4yrjC0LjG1rjH1rnC0bvF08bN187S187Z59DT2NDX39Hc6dnj8Nrj79vb297l8d/l8eDk6ePn7Obm5uft+Ofu+Ojt+Orx+uzy+////wAAAKKxxaKxxSH5BAEAABwALAAAAAAFAB4ARAhTAAEIFLihYEEMEgw04DBQ4IKHECNKzCChQIIIEiU2BJBxAYQJBDpCkHDAYMGOKDea3CBxAIIKHDg4eKDBAIWHDi4EkLgS5wUBM2sqEHCAQQQLAQEAOw==")
}

.x-window-header-default-right-ml, .x-window-header-default-right-mr {
    background-image: url("data:image/gif;R0lGODlhCgC+APQAAARGjC9moDtupVB+r4qoyZSvzZ620aKxxaO61Ke81avA17TG27fI3bfJ3bjJ3r/P4cfT5MjV5c3Y587Z5+zy+////wRGjARGjARGjARGjARGjARGjARGjARGjARGjARGjCH5BAEAABUALAAAAAAKAL4ARAjnACcIHCiQwgGCBA0KRAAgwUCFCAseHBjh4cSIEDFeRJiR48aEHy1GlDhyQkeQJU+KHKmSJMuQLjWmhGmSZsuaMwdKKLBS5sucPwcu6DnBAVGUQX0q9Qh0KVKnR6PGZJqUKtSpT6kyACBAKs6qELzeHGuzbFOraCWINVs1q9u1Z99ihduW7tWvd8nGtYtWLt6+fP3qrTu38F+kDwIQWGkAgIKeAwAEnmy4YwPKhzEPzsuW896pYaeqrdx5wmXRmksLVp36c2bSrjcDhk34tW3Zq2Ozpu25Nu7WvnffFv6b9+zhupMH1x0QADs=");
    background-repeat: repeat-y
}

.x-window-header-default-right-mc {
    padding: 1px 1px 1px 1px
}

.x-cmd-slicer.x-window-header-default-right:before {
    display: none;
    content: "x-slicer:, frame:5px 5px 5px 0, corners:url("data:image/gif;R0lGODlhBQAeAPQAAKKxxam3yKq5y6u4yrjC0LjG1rjH1rnC0bvF08bN187S187Z59DT2NDX39Hc6dnj8Nrj79vb297l8d/l8eDk6ePn7Obm5uft+Ofu+Ojt+Orx+uzy+////wAAAKKxxaKxxSH5BAEAABwALAAAAAAFAB4ARAhTAAEIFLihYEEMEgw04DBQ4IKHECNKzCChQIIIEiU2BJBxAYQJBDpCkHDAYMGOKDea3CBxAIIKHDg4eKDBAIWHDi4EkLgS5wUBM2sqEHCAQQQLAQEAOw=="), sides:url("data:image/gif;R0lGODlhCgC+APQAAARGjC9moDtupVB+r4qoyZSvzZ620aKxxaO61Ke81avA17TG27fI3bfJ3bjJ3r/P4cfT5MjV5c3Y587Z5+zy+////wRGjARGjARGjARGjARGjARGjARGjARGjARGjARGjCH5BAEAABUALAAAAAAKAL4ARAjnACcIHCiQwgGCBA0KRAAgwUCFCAseHBjh4cSIEDFeRJiR48aEHy1GlDhyQkeQJU+KHKmSJMuQLjWmhGmSZsuaMwdKKLBS5sucPwcu6DnBAVGUQX0q9Qh0KVKnR6PGZJqUKtSpT6kyACBAKs6qELzeHGuzbFOraCWINVs1q9u1Z99ihduW7tWvd8nGtYtWLt6+fP3qrTu38F+kDwIQWGkAgIKeAwAEnmy4YwPKhzEPzsuW896pYaeqrdx5wmXRmksLVp36c2bSrjcDhk34tW3Zq2Ozpu25Nu7WvnffFv6b9+zhupMH1x0QADs=")" !important
}

.x-window-header-default-bottom {
    -moz-border-radius-topleft: 0;
    -webkit-border-top-left-radius: 0;
    border-top-left-radius: 0;
    -moz-border-radius-topright: 0;
    -webkit-border-top-right-radius: 0;
    border-top-right-radius: 0;
    -moz-border-radius-bottomright: 5px;
    -webkit-border-bottom-right-radius: 5px;
    border-bottom-right-radius: 5px;
    -moz-border-radius-bottomleft: 5px;
    -webkit-border-bottom-left-radius: 5px;
    border-bottom-left-radius: 5px;
    padding: 1px 5px 5px 5px;
    border-width: 0 1px 1px 1px;
    border-style: solid;
    background-color: #ced9e7
}

.x-window-header-default-bottom-mc {
    background-color: #ced9e7
}

.x-nbr .x-window-header-default-bottom {
    padding: 0 !important;
    border-width: 0 !important;
    -webkit-border-radius: 0px;
    -moz-border-radius: 0px;
    -ms-border-radius: 0px;
    -o-border-radius: 0px;
    border-radius: 0px;
    background-color: transparent !important;
    box-shadow: none !important
}

.x-window-header-default-bottom-frameInfo {
    font-family: dh-0-5-5-5-0-1-1-1-1-5-5-5
}

.x-window-header-default-bottom-tl {
    background-position: 0 -10px
}

.x-window-header-default-bottom-tr {
    background-position: right -15px
}

.x-window-header-default-bottom-bl {
    background-position: 0 -20px
}

.x-window-header-default-bottom-br {
    background-position: right -25px
}

.x-window-header-default-bottom-ml {
    background-position: 0 top
}

.x-window-header-default-bottom-mr {
    background-position: right top
}

.x-window-header-default-bottom-tc {
    background-position: 0 0
}

.x-window-header-default-bottom-bc {
    background-position: 0 -5px
}

.x-window-header-default-bottom-tr, .x-window-header-default-bottom-br, .x-window-header-default-bottom-mr {
    padding-right: 5px
}

.x-window-header-default-bottom-tl, .x-window-header-default-bottom-bl, .x-window-header-default-bottom-ml {
    padding-left: 5px
}

.x-window-header-default-bottom-tc {
    height: 0
}

.x-window-header-default-bottom-bc {
    height: 5px
}

.x-window-header-default-bottom-tl, .x-window-header-default-bottom-bl, .x-window-header-default-bottom-tr, .x-window-header-default-bottom-br, .x-window-header-default-bottom-tc, .x-window-header-default-bottom-bc, .x-window-header-default-bottom-ml, .x-window-header-default-bottom-mr {
    background-image: url("data:image/gif;R0lGODlhBQAeAPQAAKKxxaq5y6u4yrjC0LjG1rjH1rnC0cXN1cbN187S187Z59DT2NHc6dnj8Nrj79vb297l8N/m8ebm5uft+Ojt+Orx+uzy+////6KxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxSH5BAEAABcALAAAAAAFAB4ARAhfABUIFGihYMGBFgBIeLDAQICBAgFYGChgAgOBFCIQQPAAokcFEgeG9JhwQYEKDS4qcADBwMeXLwHInDkxYk2ICREC0DkAggOBDw4QiEBBIIMJARg0qFAgQQADCx5ICAgAOw==")
}

.x-window-header-default-bottom-ml, .x-window-header-default-bottom-mr {
    background-image: url("data:image/gif;R0lGODlhCgANAPEAAKKxxc7Z5+zy+////yH5BAEAAAMALAAAAAAKAA0AQQgtAAEICECwoAAAAgsaRDhQYYCDCR1CbKhwosOHDC9alJiRY8SKHUF+XDiS4MGAADs=");
    background-repeat: repeat-y
}

.x-window-header-default-bottom-mc {
    padding: 1px 1px 1px 1px
}

.x-cmd-slicer.x-window-header-default-bottom:before {
    display: none;
    content: "x-slicer:, frame:0 5px 5px 5px, corners:url("data:image/gif;R0lGODlhBQAeAPQAAKKxxaq5y6u4yrjC0LjG1rjH1rnC0cXN1cbN187S187Z59DT2NHc6dnj8Nrj79vb297l8N/m8ebm5uft+Ojt+Orx+uzy+////6KxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxSH5BAEAABcALAAAAAAFAB4ARAhfABUIFGihYMGBFgBIeLDAQICBAgFYGChgAgOBFCIQQPAAokcFEgeG9JhwQYEKDS4qcADBwMeXLwHInDkxYk2ICREC0DkAggOBDw4QiEBBIIMJARg0qFAgQQADCx5ICAgAOw=="), sides:url("data:image/gif;R0lGODlhCgANAPEAAKKxxc7Z5+zy+////yH5BAEAAAMALAAAAAAKAA0AQQgtAAEICECwoAAAAgsaRDhQYYCDCR1CbKhwosOHDC9alJiRY8SKHUF+XDiS4MGAADs=")" !important
}

.x-window-header-default-left {
    -moz-border-radius-topleft: 5px;
    -webkit-border-top-left-radius: 5px;
    border-top-left-radius: 5px;
    -moz-border-radius-topright: 0;
    -webkit-border-top-right-radius: 0;
    border-top-right-radius: 0;
    -moz-border-radius-bottomright: 0;
    -webkit-border-bottom-right-radius: 0;
    border-bottom-right-radius: 0;
    -moz-border-radius-bottomleft: 5px;
    -webkit-border-bottom-left-radius: 5px;
    border-bottom-left-radius: 5px;
    padding: 5px 1px 5px 5px;
    border-width: 1px 0 1px 1px;
    border-style: solid;
    background-color: #ced9e7
}

.x-window-header-default-left-mc {
    background-color: #ced9e7
}

.x-nbr .x-window-header-default-left {
    padding: 0 !important;
    border-width: 0 !important;
    -webkit-border-radius: 0px;
    -moz-border-radius: 0px;
    -ms-border-radius: 0px;
    -o-border-radius: 0px;
    border-radius: 0px;
    background-color: transparent !important;
    box-shadow: none !important
}

.x-window-header-default-left-frameInfo {
    font-family: dh-5-0-5-5-1-0-1-1-5-1-5-5
}

.x-window-header-default-left-tl {
    background-position: 0 -10px
}

.x-window-header-default-left-tr {
    background-position: right -15px
}

.x-window-header-default-left-bl {
    background-position: 0 -20px
}

.x-window-header-default-left-br {
    background-position: right -25px
}

.x-window-header-default-left-ml {
    background-position: 0 top
}

.x-window-header-default-left-mr {
    background-position: right top
}

.x-window-header-default-left-tc {
    background-position: 0 0
}

.x-window-header-default-left-bc {
    background-position: 0 -5px
}

.x-window-header-default-left-tr, .x-window-header-default-left-br, .x-window-header-default-left-mr {
    padding-right: 0
}

.x-window-header-default-left-tl, .x-window-header-default-left-bl, .x-window-header-default-left-ml {
    padding-left: 5px
}

.x-window-header-default-left-tc {
    height: 5px
}

.x-window-header-default-left-bc {
    height: 5px
}

.x-window-header-default-left-tl, .x-window-header-default-left-bl, .x-window-header-default-left-tr, .x-window-header-default-left-br, .x-window-header-default-left-tc, .x-window-header-default-left-bc, .x-window-header-default-left-ml, .x-window-header-default-left-mr {
    background-image: url("data:image/gif;R0lGODlhBQAeAPQAAKKxxai1yKq5y6u4yrfD0bjC0LjF17jG1rjH1rnC0bvF08XN1c7Z59DT2NDX39Hc6dnj8Nrj79vb297l8d/l8eDk6ePn7Obm5uft+Ofu+Ojt+Orw+urx+uzy+////wAAACH5BAEAAB4ALAAAAAAFAB4ARAhWAAEIFNihoMGDFyQ0SCCAgUOHFRBsgPBgAIYHDg92eMjxoQcPFhQMCHCxo8MGCDhQ7KjRpEuHAwV6cGBgQgYCFCLAjPnSYYEJOhlIWHBggoaeDGICCAgAOw==")
}

.x-window-header-default-left-ml, .x-window-header-default-left-mr {
    background-image: url("data:image/gif;R0lGODlhCgC+APMAAH6fw4Wkx4qoyJexzp+30qKxxbTF27zM37/P4c7Z5+zy+////36fw36fw36fw36fwyH5BAEAAAsALAAAAAAKAL4AQwjTAAsoSECwIEGBBg0iTHhwIMMECxlGDKDQoUSLCSNmxFjxIUSOBTV2fCgyJMiGHkuiJHnyY8qWKl2yfEmToIGRF2vmnMlzp8+NOoH2FPoTJ9GjRpOaDKp0ZdGlPQU0lfnUKVKoVakSpYj1qtWpMcPCHMu0K1iyQ8+W/Wq2Ldu3WtWmdRuXrti1deHenasXrU8EOAHIzbqXsF+vVA/gHDAYcWGiirESaEzZ7uHKffE+xpy382bLmi+D5utZdGbSn08bDs0atenSrVe7ju34dWrYs0kHBAA7");
    background-repeat: repeat-y
}

.x-window-header-default-left-mc {
    padding: 1px 1px 1px 1px
}

.x-cmd-slicer.x-window-header-default-left:before {
    display: none;
    content: "x-slicer:, frame:5px 0 5px 5px, corners:url("data:image/gif;R0lGODlhBQAeAPQAAKKxxai1yKq5y6u4yrfD0bjC0LjF17jG1rjH1rnC0bvF08XN1c7Z59DT2NDX39Hc6dnj8Nrj79vb297l8d/l8eDk6ePn7Obm5uft+Ofu+Ojt+Orw+urx+uzy+////wAAACH5BAEAAB4ALAAAAAAFAB4ARAhWAAEIFNihoMGDFyQ0SCCAgUOHFRBsgPBgAIYHDg92eMjxoQcPFhQMCHCxo8MGCDhQ7KjRpEuHAwV6cGBgQgYCFCLAjPnSYYEJOhlIWHBggoaeDGICCAgAOw=="), sides:url("data:image/gif;R0lGODlhCgC+APMAAH6fw4Wkx4qoyJexzp+30qKxxbTF27zM37/P4c7Z5+zy+////36fw36fw36fw36fwyH5BAEAAAsALAAAAAAKAL4AQwjTAAsoSECwIEGBBg0iTHhwIMMECxlGDKDQoUSLCSNmxFjxIUSOBTV2fCgyJMiGHkuiJHnyY8qWKl2yfEmToIGRF2vmnMlzp8+NOoH2FPoTJ9GjRpOaDKp0ZdGlPQU0lfnUKVKoVakSpYj1qtWpMcPCHMu0K1iyQ8+W/Wq2Ldu3WtWmdRuXrti1deHenasXrU8EOAHIzbqXsF+vVA/gHDAYcWGiirESaEzZ7uHKffE+xpy382bLmi+D5utZdGbSn08bDs0atenSrVe7ju34dWrYs0kHBAA7")" !important
}

.x-window-header-default-collapsed-top {
    -webkit-border-radius: 5px;
    -moz-border-radius: 5px;
    -ms-border-radius: 5px;
    -o-border-radius: 5px;
    border-radius: 5px;
    padding: 5px 5px 5px 5px;
    border-width: 1px;
    border-style: solid;
    background-color: #ced9e7
}

.x-window-header-default-collapsed-top-mc {
    background-color: #ced9e7
}

.x-nbr .x-window-header-default-collapsed-top {
    padding: 0 !important;
    border-width: 0 !important;
    -webkit-border-radius: 0px;
    -moz-border-radius: 0px;
    -ms-border-radius: 0px;
    -o-border-radius: 0px;
    border-radius: 0px;
    background-color: transparent !important;
    box-shadow: none !important
}

.x-window-header-default-collapsed-top-frameInfo {
    font-family: dh-5-5-5-5-1-1-1-1-5-5-5-5
}

.x-window-header-default-collapsed-top-tl {
    background-position: 0 -10px
}

.x-window-header-default-collapsed-top-tr {
    background-position: right -15px
}

.x-window-header-default-collapsed-top-bl {
    background-position: 0 -20px
}

.x-window-header-default-collapsed-top-br {
    background-position: right -25px
}

.x-window-header-default-collapsed-top-ml {
    background-position: 0 top
}

.x-window-header-default-collapsed-top-mr {
    background-position: right top
}

.x-window-header-default-collapsed-top-tc {
    background-position: 0 0
}

.x-window-header-default-collapsed-top-bc {
    background-position: 0 -5px
}

.x-window-header-default-collapsed-top-tr, .x-window-header-default-collapsed-top-br, .x-window-header-default-collapsed-top-mr {
    padding-right: 5px
}

.x-window-header-default-collapsed-top-tl, .x-window-header-default-collapsed-top-bl, .x-window-header-default-collapsed-top-ml {
    padding-left: 5px
}

.x-window-header-default-collapsed-top-tc {
    height: 5px
}

.x-window-header-default-collapsed-top-bc {
    height: 5px
}

.x-window-header-default-collapsed-top-tl, .x-window-header-default-collapsed-top-bl, .x-window-header-default-collapsed-top-tr, .x-window-header-default-collapsed-top-br, .x-window-header-default-collapsed-top-tc, .x-window-header-default-collapsed-top-bc, .x-window-header-default-collapsed-top-ml, .x-window-header-default-collapsed-top-mr {
    background-image: url("data:image/gif;R0lGODlhBQAeAPUAAKKxxai1yKm3yKq5y6u4yrfD0bfF1rfG1rjC0LjF17jH1rnC0bvF08XN1cbN187S187Z59DT2NDX39Db6dHc6dLb6dTd6dTd6tbd69ji7tnj8Nrj79vb297l8N7m8d/m8eDk6ePn7OTr9uXs9+bm5uft+Ofu+Orw+urx+uzy+////wAAAKKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxSH5BAEAACoALAAAAAAFAB4ARQh7AAEIFEgBgkEIJj4okKCCBIcICwYcNAhCwQkNFAiMKAihggUDDjhMHAlBhYoQDAgEKMHR4IYOCCIcEDHhYAYMC1Lo1Emyp8GBAlVISODBRIEOGwwSYBDCJAUNKBSAMEihhAAEGDIY5NDAwIUKVEdInCDiwIMBCyJwIBEQADs=")
}

.x-window-header-default-collapsed-top-ml, .x-window-header-default-collapsed-top-mr {
    background-image: url("data:image/gif;R0lGODlhCgASAPEAAKKxxc7Z5+zy+////yH5BAEAAAMALAAAAAAKABIAQQg4AAEICECwoAAAAgsaRDhQYYCDCR1CbKhwosOHDC9alJiRY8SKHUF+XDiS4EaRFEmmNBlSpUYAAQEAOw==");
    background-repeat: repeat-y
}

.x-window-header-default-collapsed-top-mc {
    padding: 1px 1px 1px 1px
}

.x-cmd-slicer.x-window-header-default-collapsed-top:before {
    display: none;
    content: "x-slicer:, frame:5px 5px 5px 5px, corners:url("data:image/gif;R0lGODlhBQAeAPUAAKKxxai1yKm3yKq5y6u4yrfD0bfF1rfG1rjC0LjF17jH1rnC0bvF08XN1cbN187S187Z59DT2NDX39Db6dHc6dLb6dTd6dTd6tbd69ji7tnj8Nrj79vb297l8N7m8d/m8eDk6ePn7OTr9uXs9+bm5uft+Ofu+Orw+urx+uzy+////wAAAKKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxSH5BAEAACoALAAAAAAFAB4ARQh7AAEIFEgBgkEIJj4okKCCBIcICwYcNAhCwQkNFAiMKAihggUDDjhMHAlBhYoQDAgEKMHR4IYOCCIcEDHhYAYMC1Lo1Emyp8GBAlVISODBRIEOGwwSYBDCJAUNKBSAMEihhAAEGDIY5NDAwIUKVEdInCDiwIMBCyJwIBEQADs="), sides:url("data:image/gif;R0lGODlhCgASAPEAAKKxxc7Z5+zy+////yH5BAEAAAMALAAAAAAKABIAQQg4AAEICECwoAAAAgsaRDhQYYCDCR1CbKhwosOHDC9alJiRY8SKHUF+XDiS4EaRFEmmNBlSpUYAAQEAOw==")" !important
}

.x-window-header-default-collapsed-right {
    -webkit-border-radius: 5px;
    -moz-border-radius: 5px;
    -ms-border-radius: 5px;
    -o-border-radius: 5px;
    border-radius: 5px;
    padding: 5px 5px 5px 5px;
    border-width: 1px;
    border-style: solid;
    background-color: #ced9e7
}

.x-window-header-default-collapsed-right-mc {
    background-color: #ced9e7
}

.x-nbr .x-window-header-default-collapsed-right {
    padding: 0 !important;
    border-width: 0 !important;
    -webkit-border-radius: 0px;
    -moz-border-radius: 0px;
    -ms-border-radius: 0px;
    -o-border-radius: 0px;
    border-radius: 0px;
    background-color: transparent !important;
    box-shadow: none !important
}

.x-window-header-default-collapsed-right-frameInfo {
    font-family: dh-5-5-5-5-1-1-1-1-5-5-5-5
}

.x-window-header-default-collapsed-right-tl {
    background-position: 0 -10px
}

.x-window-header-default-collapsed-right-tr {
    background-position: right -15px
}

.x-window-header-default-collapsed-right-bl {
    background-position: 0 -20px
}

.x-window-header-default-collapsed-right-br {
    background-position: right -25px
}

.x-window-header-default-collapsed-right-ml {
    background-position: 0 top
}

.x-window-header-default-collapsed-right-mr {
    background-position: right top
}

.x-window-header-default-collapsed-right-tc {
    background-position: 0 0
}

.x-window-header-default-collapsed-right-bc {
    background-position: 0 -5px
}

.x-window-header-default-collapsed-right-tr, .x-window-header-default-collapsed-right-br, .x-window-header-default-collapsed-right-mr {
    padding-right: 5px
}

.x-window-header-default-collapsed-right-tl, .x-window-header-default-collapsed-right-bl, .x-window-header-default-collapsed-right-ml {
    padding-left: 5px
}

.x-window-header-default-collapsed-right-tc {
    height: 5px
}

.x-window-header-default-collapsed-right-bc {
    height: 5px
}

.x-window-header-default-collapsed-right-tl, .x-window-header-default-collapsed-right-bl, .x-window-header-default-collapsed-right-tr, .x-window-header-default-collapsed-right-br, .x-window-header-default-collapsed-right-tc, .x-window-header-default-collapsed-right-bc, .x-window-header-default-collapsed-right-ml, .x-window-header-default-collapsed-right-mr {
    background-image: url("data:image/gif;R0lGODlhBQAeAPUAAKKxxai1yKm3yKq5y6u4yrfD0bfE1rfF1rfG1rjC0LjG1rjH1rnC0bvF08XN1cbN187S187Z59DT2NDX39Db6dHc6dLb6NTd6dTd6tbe69ji7tnj8Nrj79vb297l8d/l8eDk6ePn7OTr9uXs9+bm5uft+Ofu+Ojt+Orx+uzy+////wAAAKKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxSH5BAEAACoALAAAAAAFAB4ARQh0AAEIFJiiYEETHhZMUEGigwQGAyJIlAgCgQgNFQhYmHjCg4IHHSaKnKhCRYgGBAJsFMnhQwIJFjFK5OCBgcGCI3OKHChQxQQDGUYUuEBBIoEGIUpW2IBiAQiJFUoISIChaIQODg4EhVpiwNKmEAYwkNCBREAAOw==")
}

.x-window-header-default-collapsed-right-ml, .x-window-header-default-collapsed-right-mr {
    background-image: url("data:image/gif;R0lGODlhCgC+APIAAKKxxc7Z59Hc6ezy+////6KxxaKxxaKxxSH5BAEAAAQALAAAAAAKAL4AQgjMAAEICECw4AAAAAoqPJhQIUGGDh8ijBgAYkSLDjEunHiRY0aPGxt+FBmSokaDIFGSVGkypcSVL1vCrOiS5syTMTverInTpsyfOoGOFFoyqNGhR4siXaq0KcukT5lGdZpTalWqPqFencp1q9esVsFi7UmWp9mdaIl2Fbu2bFqtbL+6VSv3LN24eOfC1RuW71i7ewH3Ffz37WDDhe/6bUuYMWLHihvXfTw5MuW8kjFfXlw58ObMnDVbHu2Z9GHTiUurPr06NevXrkMO/BgQADs=");
    background-repeat: repeat-y
}

.x-window-header-default-collapsed-right-mc {
    padding: 1px 1px 1px 1px
}

.x-cmd-slicer.x-window-header-default-collapsed-right:before {
    display: none;
    content: "x-slicer:, frame:5px 5px 5px 5px, corners:url("data:image/gif;R0lGODlhBQAeAPUAAKKxxai1yKm3yKq5y6u4yrfD0bfE1rfF1rfG1rjC0LjG1rjH1rnC0bvF08XN1cbN187S187Z59DT2NDX39Db6dHc6dLb6NTd6dTd6tbe69ji7tnj8Nrj79vb297l8d/l8eDk6ePn7OTr9uXs9+bm5uft+Ofu+Ojt+Orx+uzy+////wAAAKKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxSH5BAEAACoALAAAAAAFAB4ARQh0AAEIFJiiYEETHhZMUEGigwQGAyJIlAgCgQgNFQhYmHjCg4IHHSaKnKhCRYgGBAJsFMnhQwIJFjFK5OCBgcGCI3OKHChQxQQDGUYUuEBBIoEGIUpW2IBiAQiJFUoISIChaIQODg4EhVpiwNKmEAYwkNCBREAAOw=="), sides:url("data:image/gif;R0lGODlhCgC+APIAAKKxxc7Z59Hc6ezy+////6KxxaKxxaKxxSH5BAEAAAQALAAAAAAKAL4AQgjMAAEICECw4AAAAAoqPJhQIUGGDh8ijBgAYkSLDjEunHiRY0aPGxt+FBmSokaDIFGSVGkypcSVL1vCrOiS5syTMTverInTpsyfOoGOFFoyqNGhR4siXaq0KcukT5lGdZpTalWqPqFencp1q9esVsFi7UmWp9mdaIl2Fbu2bFqtbL+6VSv3LN24eOfC1RuW71i7ewH3Ffz37WDDhe/6bUuYMWLHihvXfTw5MuW8kjFfXlw58ObMnDVbHu2Z9GHTiUurPr06NevXrkMO/BgQADs=")" !important
}

.x-window-header-default-collapsed-bottom {
    -webkit-border-radius: 5px;
    -moz-border-radius: 5px;
    -ms-border-radius: 5px;
    -o-border-radius: 5px;
    border-radius: 5px;
    padding: 5px 5px 5px 5px;
    border-width: 1px;
    border-style: solid;
    background-color: #ced9e7
}

.x-window-header-default-collapsed-bottom-mc {
    background-color: #ced9e7
}

.x-nbr .x-window-header-default-collapsed-bottom {
    padding: 0 !important;
    border-width: 0 !important;
    -webkit-border-radius: 0px;
    -moz-border-radius: 0px;
    -ms-border-radius: 0px;
    -o-border-radius: 0px;
    border-radius: 0px;
    background-color: transparent !important;
    box-shadow: none !important
}

.x-window-header-default-collapsed-bottom-frameInfo {
    font-family: dh-5-5-5-5-1-1-1-1-5-5-5-5
}

.x-window-header-default-collapsed-bottom-tl {
    background-position: 0 -10px
}

.x-window-header-default-collapsed-bottom-tr {
    background-position: right -15px
}

.x-window-header-default-collapsed-bottom-bl {
    background-position: 0 -20px
}

.x-window-header-default-collapsed-bottom-br {
    background-position: right -25px
}

.x-window-header-default-collapsed-bottom-ml {
    background-position: 0 top
}

.x-window-header-default-collapsed-bottom-mr {
    background-position: right top
}

.x-window-header-default-collapsed-bottom-tc {
    background-position: 0 0
}

.x-window-header-default-collapsed-bottom-bc {
    background-position: 0 -5px
}

.x-window-header-default-collapsed-bottom-tr, .x-window-header-default-collapsed-bottom-br, .x-window-header-default-collapsed-bottom-mr {
    padding-right: 5px
}

.x-window-header-default-collapsed-bottom-tl, .x-window-header-default-collapsed-bottom-bl, .x-window-header-default-collapsed-bottom-ml {
    padding-left: 5px
}

.x-window-header-default-collapsed-bottom-tc {
    height: 5px
}

.x-window-header-default-collapsed-bottom-bc {
    height: 5px
}

.x-window-header-default-collapsed-bottom-tl, .x-window-header-default-collapsed-bottom-bl, .x-window-header-default-collapsed-bottom-tr, .x-window-header-default-collapsed-bottom-br, .x-window-header-default-collapsed-bottom-tc, .x-window-header-default-collapsed-bottom-bc, .x-window-header-default-collapsed-bottom-ml, .x-window-header-default-collapsed-bottom-mr {
    background-image: url("data:image/gif;R0lGODlhBQAeAPUAAKKxxai1yKm3yKq5y6u4yrfD0bfE1rfG1rjC0LjG1rjH1rnC0bvF08XN1cbN187S187Z59DT2NDX39Db6dHc6dLb6NPd6tTd6dbd69ji7tnj8Nrj79vb297l8N/m8eDk6ePn7OTr9uXs9+bm5uft+Ojt+Orx+uzy+////wAAAKKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxSH5BAEAACgALAAAAAAFAB4ARQh6AAEIFHiiYMEKFw5IQDGCQ4QFAyBIlPjhQIgJEAiQoCCxhIcEDjhMHDkRBQoQDAgEEMFxYgYMCCIoMKGh5YYOC1qS3LlzoEAUEgxYqFAAQwaJBBiAMAlhQogDHyRSECEAQYcNEjk0SOChhFQSAyhoMKHgwYAFETiMCAgAOw==")
}

.x-window-header-default-collapsed-bottom-ml, .x-window-header-default-collapsed-bottom-mr {
    background-image: url("data:image/gif;R0lGODlhCgASAPEAAKKxxc7Z5+zy+////yH5BAEAAAMALAAAAAAKABIAQQg4AAEICECwoAAAAgsaRDhQYYCDCR1CbKhwosOHDC9alJiRY8SKHUF+XDiS4EaRFEmmNBlSpUYAAQEAOw==");
    background-repeat: repeat-y
}

.x-window-header-default-collapsed-bottom-mc {
    padding: 1px 1px 1px 1px
}

.x-cmd-slicer.x-window-header-default-collapsed-bottom:before {
    display: none;
    content: "x-slicer:, frame:5px 5px 5px 5px, corners:url("data:image/gif;R0lGODlhBQAeAPUAAKKxxai1yKm3yKq5y6u4yrfD0bfE1rfG1rjC0LjG1rjH1rnC0bvF08XN1cbN187S187Z59DT2NDX39Db6dHc6dLb6NPd6tTd6dbd69ji7tnj8Nrj79vb297l8N/m8eDk6ePn7OTr9uXs9+bm5uft+Ojt+Orx+uzy+////wAAAKKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxSH5BAEAACgALAAAAAAFAB4ARQh6AAEIFHiiYMEKFw5IQDGCQ4QFAyBIlPjhQIgJEAiQoCCxhIcEDjhMHDkRBQoQDAgEEMFxYgYMCCIoMKGh5YYOC1qS3LlzoEAUEgxYqFAAQwaJBBiAMAlhQogDHyRSECEAQYcNEjk0SOChhFQSAyhoMKHgwYAFETiMCAgAOw=="), sides:url("data:image/gif;R0lGODlhCgASAPEAAKKxxc7Z5+zy+////yH5BAEAAAMALAAAAAAKABIAQQg4AAEICECwoAAAAgsaRDhQYYCDCR1CbKhwosOHDC9alJiRY8SKHUF+XDiS4EaRFEmmNBlSpUYAAQEAOw==")" !important
}

.x-window-header-default-collapsed-left {
    -webkit-border-radius: 5px;
    -moz-border-radius: 5px;
    -ms-border-radius: 5px;
    -o-border-radius: 5px;
    border-radius: 5px;
    padding: 5px 5px 5px 5px;
    border-width: 1px;
    border-style: solid;
    background-color: #ced9e7
}

.x-window-header-default-collapsed-left-mc {
    background-color: #ced9e7
}

.x-nbr .x-window-header-default-collapsed-left {
    padding: 0 !important;
    border-width: 0 !important;
    -webkit-border-radius: 0px;
    -moz-border-radius: 0px;
    -ms-border-radius: 0px;
    -o-border-radius: 0px;
    border-radius: 0px;
    background-color: transparent !important;
    box-shadow: none !important
}

.x-window-header-default-collapsed-left-frameInfo {
    font-family: dh-5-5-5-5-1-1-1-1-5-5-5-5
}

.x-window-header-default-collapsed-left-tl {
    background-position: 0 -10px
}

.x-window-header-default-collapsed-left-tr {
    background-position: right -15px
}

.x-window-header-default-collapsed-left-bl {
    background-position: 0 -20px
}

.x-window-header-default-collapsed-left-br {
    background-position: right -25px
}

.x-window-header-default-collapsed-left-ml {
    background-position: 0 top
}

.x-window-header-default-collapsed-left-mr {
    background-position: right top
}

.x-window-header-default-collapsed-left-tc {
    background-position: 0 0
}

.x-window-header-default-collapsed-left-bc {
    background-position: 0 -5px
}

.x-window-header-default-collapsed-left-tr, .x-window-header-default-collapsed-left-br, .x-window-header-default-collapsed-left-mr {
    padding-right: 5px
}

.x-window-header-default-collapsed-left-tl, .x-window-header-default-collapsed-left-bl, .x-window-header-default-collapsed-left-ml {
    padding-left: 5px
}

.x-window-header-default-collapsed-left-tc {
    height: 5px
}

.x-window-header-default-collapsed-left-bc {
    height: 5px
}

.x-window-header-default-collapsed-left-tl, .x-window-header-default-collapsed-left-bl, .x-window-header-default-collapsed-left-tr, .x-window-header-default-collapsed-left-br, .x-window-header-default-collapsed-left-tc, .x-window-header-default-collapsed-left-bc, .x-window-header-default-collapsed-left-ml, .x-window-header-default-collapsed-left-mr {
    background-image: url("data:image/gif;R0lGODlhBQAeAPUAAKKxxai1yKm3yKq5y6u4yrfD0bfF1rfG1rjC0LjF17jG1rjH1rnC0bvF08XN1cbN187S187Z59DT2NDX39Db6dHc6dLb6dTd6dTd6tbe69ji7tnj8Nrj79vb297l8d/l8eDk6ePn7OTr9uXs9+bm5uft+Ofu+Ojt+Orw+urx+uzy+////wAAAKKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxSH5BAEAACsALAAAAAAFAB4ARQh0AAEIFKiiYMERGQ5MWEGigwQGAyJIlAhiAYoNFQiUqCARoYEHHSaKnLhiRYgGBAJsFEnhAgIJC1JglEgBAwODBUfqFDlQ4IoJCTyYKPCBg0QCDUKUrKBBxAEQEy0IQODBaIQODhR4OBF1AFOnEAYwkNCBREAAOw==")
}

.x-window-header-default-collapsed-left-ml, .x-window-header-default-collapsed-left-mr {
    background-image: url("data:image/gif;R0lGODlhCgC+APIAAKKxxc7Z59Hc6ezy+////6KxxaKxxaKxxSH5BAEAAAQALAAAAAAKAL4AQgjLAAEMCECwoAAAAgsqRDhQIUGGDh8mjAiR4kSHFTFeXLixYEaODTWGBBkxwEePHSWORLlSZcmTLi22NJmS5kyYNl/WxMlzp8+bP3UCHSq0qEyjIpGSPMo0adOlTqNCncpSadWnV6VmpRpTa1euObF+3Up2rNmwXtGC7UlUrNqyb8+ytSo3qNu5d+2mxbtX71q/cPn+bduX8GC6cRMLDgy4rmHGjx0jXiw5b2TFjTFfpqx5cmbOoD+L3jzaM+nTplNbVl2Y9eHVsBUeDAgAOw==");
    background-repeat: repeat-y
}

.x-window-header-default-collapsed-left-mc {
    padding: 1px 1px 1px 1px
}

.x-cmd-slicer.x-window-header-default-collapsed-left:before {
    display: none;
    content: "x-slicer:, frame:5px 5px 5px 5px, corners:url("data:image/gif;R0lGODlhBQAeAPUAAKKxxai1yKm3yKq5y6u4yrfD0bfF1rfG1rjC0LjF17jG1rjH1rnC0bvF08XN1cbN187S187Z59DT2NDX39Db6dHc6dLb6dTd6dTd6tbe69ji7tnj8Nrj79vb297l8d/l8eDk6ePn7OTr9uXs9+bm5uft+Ofu+Ojt+Orw+urx+uzy+////wAAAKKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxaKxxSH5BAEAACsALAAAAAAFAB4ARQh0AAEIFKiiYMERGQ5MWEGigwQGAyJIlAhiAYoNFQiUqCARoYEHHSaKnLhiRYgGBAJsFEnhAgIJC1JglEgBAwODBUfqFDlQ4IoJCTyYKPCBg0QCDUKUrKBBxAEQEy0IQODBaIQODhR4OBF1AFOnEAYwkNCBREAAOw=="), sides:url("data:image/gif;R0lGODlhCgC+APIAAKKxxc7Z59Hc6ezy+////6KxxaKxxaKxxSH5BAEAAAQALAAAAAAKAL4AQgjLAAEMCECwoAAAAgsqRDhQIUGGDh8mjAiR4kSHFTFeXLixYEaODTWGBBkxwEePHSWORLlSZcmTLi22NJmS5kyYNl/WxMlzp8+bP3UCHSq0qEyjIpGSPMo0adOlTqNCncpSadWnV6VmpRpTa1euObF+3Up2rNmwXtGC7UlUrNqyb8+ytSo3qNu5d+2mxbtX71q/cPn+bduX8GC6cRMLDgy4rmHGjx0jXiw5b2TFjTFfpqx5cmbOoD+L3jzaM+nTplNbVl2Y9eHVsBUeDAgAOw==")" !important
}

.x-window-header-default-top {
    -webkit-box-shadow: #ecf2fb 0 1px 0px 0 inset, #ecf2fb -1px 0 0px 0 inset, #ecf2fb 1px 0 0px 0 inset;
    -moz-box-shadow: #ecf2fb 0 1px 0px 0 inset, #ecf2fb -1px 0 0px 0 inset, #ecf2fb 1px 0 0px 0 inset;
    box-shadow: #ecf2fb 0 1px 0px 0 inset, #ecf2fb -1px 0 0px 0 inset, #ecf2fb 1px 0 0px 0 inset
}

.x-window-header-default-right {
    -webkit-box-shadow: #ecf2fb 0 1px 0px 0 inset, #ecf2fb 0 -1px 0px 0 inset, #ecf2fb -1px 0 0px 0 inset;
    -moz-box-shadow: #ecf2fb 0 1px 0px 0 inset, #ecf2fb 0 -1px 0px 0 inset, #ecf2fb -1px 0 0px 0 inset;
    box-shadow: #ecf2fb 0 1px 0px 0 inset, #ecf2fb 0 -1px 0px 0 inset, #ecf2fb -1px 0 0px 0 inset
}

.x-window-header-default-bottom {
    -webkit-box-shadow: #ecf2fb 0 -1px 0px 0 inset, #ecf2fb -1px 0 0px 0 inset, #ecf2fb 1px 0 0px 0 inset;
    -moz-box-shadow: #ecf2fb 0 -1px 0px 0 inset, #ecf2fb -1px 0 0px 0 inset, #ecf2fb 1px 0 0px 0 inset;
    box-shadow: #ecf2fb 0 -1px 0px 0 inset, #ecf2fb -1px 0 0px 0 inset, #ecf2fb 1px 0 0px 0 inset
}

.x-window-header-default-left {
    -webkit-box-shadow: #ecf2fb 0 1px 0px 0 inset, #ecf2fb 0 -1px 0px 0 inset, #ecf2fb 1px 0 0px 0 inset;
    -moz-box-shadow: #ecf2fb 0 1px 0px 0 inset, #ecf2fb 0 -1px 0px 0 inset, #ecf2fb 1px 0 0px 0 inset;
    box-shadow: #ecf2fb 0 1px 0px 0 inset, #ecf2fb 0 -1px 0px 0 inset, #ecf2fb 1px 0 0px 0 inset
}

.x-window-header-default .x-window-header-icon {
    width: 16px;
    height: 16px;
    color: #04468c;
    font-size: 16px;
    line-height: 16px;
    background-position: center center
}

.x-window-header-default .x-window-header-glyph {
    color: #04468c;
    font-size: 16px;
    line-height: 16px;
    opacity: 0.5
}

.x-ie8 .x-window-header-default .x-window-header-glyph {
    color: #6990ba
}

.x-window-header-default-horizontal .x-tool-after-title {
    margin: 0 0 0 2px
}

.x-window-header-default-horizontal .x-tool-before-title {
    margin: 0 2px 0 0
}

.x-window-header-default-vertical .x-tool-after-title {
    margin: 2px 0 0 0
}

.x-window-header-default-vertical .x-tool-before-title {
    margin: 0 0 2px 0
}

.x-window-header-default .x-tool-focus {
    outline: 1px dotted #464646;
    outline-offset: 0
}

.x-ie8 .x-window-header-default .x-tool-focus {
    outline: none
}

.x-ie8 .x-window-header-default .x-tool-focus:after {
    position: absolute;
    content: ' ';
    top: -1px;
    right: -1px;
    bottom: -1px;
    left: -1px;
    border: 1px dotted #464646;
    pointer-events: none
}

.x-window-default-collapsed .x-window-header {
    border-width: 1px !important
}

.x-nbr .x-window-default-collapsed .x-window-header {
    border-width: 0 !important
}

.x-window-body-plain {
    background-color: transparent
}

.x-form-item-label-default {
    color: #000;
    font: normal 12px/14px tahoma, arial, verdana, sans-serif;
    min-height: 22px;
    padding-top: 4px;
    padding-right: 5px
}

.x-ie8 .x-form-item-label-default {
    min-height: 18px
}

.x-form-item-label-default.x-form-item-label-top {
    height: 1px
}

.x-form-item-label-default.x-form-item-label-top > .x-form-item-label-inner {
    padding-top: 4px;
    padding-bottom: 5px
}

.x-form-item-label-default.x-form-item-label-top-side-error:after {
    width: 18px
}

.x-form-item-body-default {
    min-height: 22px
}

.x-form-invalid-icon-default {
    width: 16px;
    height: 16px;
    margin: 0 1px;
    background: url("data:image/gif;R0lGODlhEAAQAIcAAED/QMJLMsNNNMVPNsNUPcxVPMZXQcddRs5dTNBZQcxiTM5kTtVgR9FjTNFhUNRkUthwWd5wWd1wXd18b919b+FdUuJfU+NhVOViVeZlVudnV+NmW+RnXOdsXehpWOpsWetuWulvX+F0XOVyWep2XexwW+5zXO92XfB4X/F6X+BzYO57Yel9aPN8YPN+YemCau2BaeyBbO6DbuOEdeaIeOqHfeuJfeqNe+yLf+ySf/KAZfSAYvWBYvWCY/SEZ/WEaveGbPaJa/iGbfONdvWOd/eMdfqOd/qUfN6hleWOg+eQhOeRheySiO2SieyYie2flfGTgvCXg/GXhPSZhPCfjvGdkOGkl+Onmu6glfihiPiiifijivOmkfSmkvGlmfGom/Gon/Kpn+uvovOvpvSsofWwo/ezoPezpPC0qPi0oPi2ofi1pfm5pvq8qPu9qfi+sfq/sv3DtfrZ0////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAMAAAAALAAAAAAQABAAAAjBAAEIHEiwoME4R4D8IPLG4EAjMrqkScOFBQyHQqS42RIkiJY2OUYULBLFTY8ec+a4aMHmhoiBcGKY5LEjZQoUJ9ZIECNwCJcsO1amPGGiBBQnEASuUOOjxc2UJUB8CPElgUASZnTgNCFnzgcPGjp4KSDwBZUpRUFUGaMhAwYbSxYIRKPijFQPKTFcsBDGgZWBEWiUaduEiYUKYSgYKMhgBhkcHDbUADMhgMMGD5RgeZIEAQGHAq8oGCDgABLQqAkGBAA7") no-repeat
}

.x-form-invalid-under-default {
    padding: 2px 2px 2px 20px;
    color: #c0272b;
    font: normal 11px/16px tahoma, arial, verdana, sans-serif;
    background: no-repeat 0 2px;
    background-image: url("data:image/gif;R0lGODlhEAAQAIcAAED/QMJLMsNNNMVPNsNUPcxVPMZXQcddRs5dTNBZQcxiTM5kTtVgR9FjTNFhUNRkUthwWd5wWd1wXd18b919b+FdUuJfU+NhVOViVeZlVudnV+NmW+RnXOdsXehpWOpsWetuWulvX+F0XOVyWep2XexwW+5zXO92XfB4X/F6X+BzYO57Yel9aPN8YPN+YemCau2BaeyBbO6DbuOEdeaIeOqHfeuJfeqNe+yLf+ySf/KAZfSAYvWBYvWCY/SEZ/WEaveGbPaJa/iGbfONdvWOd/eMdfqOd/qUfN6hleWOg+eQhOeRheySiO2SieyYie2flfGTgvCXg/GXhPSZhPCfjvGdkOGkl+Onmu6glfihiPiiifijivOmkfSmkvGlmfGom/Gon/Kpn+uvovOvpvSsofWwo/ezoPezpPC0qPi0oPi2ofi1pfm5pvq8qPu9qfi+sfq/sv3DtfrZ0////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAMAAAAALAAAAAAQABAAAAjBAAEIHEiwoME4R4D8IPLG4EAjMrqkScOFBQyHQqS42RIkiJY2OUYULBLFTY8ec+a4aMHmhoiBcGKY5LEjZQoUJ9ZIECNwCJcsO1amPGGiBBQnEASuUOOjxc2UJUB8CPElgUASZnTgNCFnzgcPGjp4KSDwBZUpRUFUGaMhAwYbSxYIRKPijFQPKTFcsBDGgZWBEWiUaduEiYUKYSgYKMhgBhkcHDbUADMhgMMGD5RgeZIEAQGHAq8oGCDgABLQqAkGBAA7")
}

.x-form-error-wrap-default.x-form-error-wrap-side {
    width: 18px
}

.x-form-item-default.x-item-disabled {
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=30)";
    opacity: 0.3
}

.x-form-item-label-toolbar {
    color: #000;
    font: normal 11px/13px tahoma, arial, verdana, sans-serif;
    min-height: 20px;
    padding-top: 4px;
    padding-right: 5px
}

.x-ie8 .x-form-item-label-toolbar {
    min-height: 16px
}

.x-form-item-label-toolbar.x-form-item-label-top {
    height: 1px
}

.x-form-item-label-toolbar.x-form-item-label-top > .x-form-item-label-inner {
    padding-top: 4px;
    padding-bottom: 5px
}

.x-form-item-label-toolbar.x-form-item-label-top-side-error:after {
    width: 18px
}

.x-form-item-body-toolbar {
    min-height: 20px
}

.x-form-invalid-icon-toolbar {
    width: 16px;
    height: 16px;
    margin: 0 1px;
    background: url("data:image/gif;R0lGODlhEAAQAIcAAED/QMJLMsNNNMVPNsNUPcxVPMZXQcddRs5dTNBZQcxiTM5kTtVgR9FjTNFhUNRkUthwWd5wWd1wXd18b919b+FdUuJfU+NhVOViVeZlVudnV+NmW+RnXOdsXehpWOpsWetuWulvX+F0XOVyWep2XexwW+5zXO92XfB4X/F6X+BzYO57Yel9aPN8YPN+YemCau2BaeyBbO6DbuOEdeaIeOqHfeuJfeqNe+yLf+ySf/KAZfSAYvWBYvWCY/SEZ/WEaveGbPaJa/iGbfONdvWOd/eMdfqOd/qUfN6hleWOg+eQhOeRheySiO2SieyYie2flfGTgvCXg/GXhPSZhPCfjvGdkOGkl+Onmu6glfihiPiiifijivOmkfSmkvGlmfGom/Gon/Kpn+uvovOvpvSsofWwo/ezoPezpPC0qPi0oPi2ofi1pfm5pvq8qPu9qfi+sfq/sv3DtfrZ0////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAMAAAAALAAAAAAQABAAAAjBAAEIHEiwoME4R4D8IPLG4EAjMrqkScOFBQyHQqS42RIkiJY2OUYULBLFTY8ec+a4aMHmhoiBcGKY5LEjZQoUJ9ZIECNwCJcsO1amPGGiBBQnEASuUOOjxc2UJUB8CPElgUASZnTgNCFnzgcPGjp4KSDwBZUpRUFUGaMhAwYbSxYIRKPijFQPKTFcsBDGgZWBEWiUaduEiYUKYSgYKMhgBhkcHDbUADMhgMMGD5RgeZIEAQGHAq8oGCDgABLQqAkGBAA7") no-repeat
}

.x-form-invalid-under-toolbar {
    padding: 2px 2px 2px 20px;
    color: #c30;
    font: normal 12px/16px tahoma, arial, verdana, sans-serif;
    background: no-repeat 0 2px;
    background-image: url("data:image/gif;R0lGODlhEAAQAIcAAED/QMJLMsNNNMVPNsNUPcxVPMZXQcddRs5dTNBZQcxiTM5kTtVgR9FjTNFhUNRkUthwWd5wWd1wXd18b919b+FdUuJfU+NhVOViVeZlVudnV+NmW+RnXOdsXehpWOpsWetuWulvX+F0XOVyWep2XexwW+5zXO92XfB4X/F6X+BzYO57Yel9aPN8YPN+YemCau2BaeyBbO6DbuOEdeaIeOqHfeuJfeqNe+yLf+ySf/KAZfSAYvWBYvWCY/SEZ/WEaveGbPaJa/iGbfONdvWOd/eMdfqOd/qUfN6hleWOg+eQhOeRheySiO2SieyYie2flfGTgvCXg/GXhPSZhPCfjvGdkOGkl+Onmu6glfihiPiiifijivOmkfSmkvGlmfGom/Gon/Kpn+uvovOvpvSsofWwo/ezoPezpPC0qPi0oPi2ofi1pfm5pvq8qPu9qfi+sfq/sv3DtfrZ0////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAMAAAAALAAAAAAQABAAAAjBAAEIHEiwoME4R4D8IPLG4EAjMrqkScOFBQyHQqS42RIkiJY2OUYULBLFTY8ec+a4aMHmhoiBcGKY5LEjZQoUJ9ZIECNwCJcsO1amPGGiBBQnEASuUOOjxc2UJUB8CPElgUASZnTgNCFnzgcPGjp4KSDwBZUpRUFUGaMhAwYbSxYIRKPijFQPKTFcsBDGgZWBEWiUaduEiYUKYSgYKMhgBhkcHDbUADMhgMMGD5RgeZIEAQGHAq8oGCDgABLQqAkGBAA7")
}

.x-form-error-wrap-toolbar.x-form-error-wrap-side {
    width: 18px
}

.x-form-item-toolbar.x-item-disabled {
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=30)";
    opacity: 0.3
}

.x-autocontainer-form-item, .x-anchor-form-item, .x-vbox-form-item, .x-table-form-item {
    margin-bottom: 5px
}

.x-form-text-field-body-default {
    min-width: 150px;
    max-width: 150px
}

.x-form-text-wrap-default {
    border-width: 1px;
    border-style: solid;
    border-color: #b5b8c8
}

.x-form-text-wrap-default.x-form-text-wrap-focus {
    border-color: #7eadd9
}

.x-form-text-wrap-default.x-form-text-wrap-invalid {
    border-color: #c30
}

.x-form-text-default {
    color: #000;
    padding: 1px 3px 2px;
    background-color: #fff;
    background-image: url("data:image/gif;R0lGODlhAQASAIcAAN7j5vDz8/P19fX39/f5+fn7+/z8/f3+/v///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAAAAP8ALAAAAAABABIAAAgQAAEEEDCAQAEDBxAoXMgwIAA7");
    font: normal 12px/17px tahoma, arial, verdana, sans-serif;
    min-height: 20px
}

.x-ie8 .x-form-text-default {
    min-height: 17px
}

.x-form-text-default.x-form-textarea {
    line-height: 14px;
    min-height: 56px
}

.x-ie8 .x-form-text-default.x-form-textarea {
    min-height: 53px
}

.x-form-text-default.x-form-text-file {
    color: grey
}

.x-placeholder-label-default {
    padding: 1px 3px 2px
}

.x-form-empty-field-default + .x-placeholder-label-default {
    color: grey
}

.x-form-text-default:-ms-input-placeholder {
    color: grey
}

.x-form-invalid-field-default {
    background-color: #fff;
    background-image: url("data:image/gif;R0lGODlhBAADAIcAAAD/AP8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAAAALAAAAAAEAAMAAAgMAAMAGAhAoMCCAAICADs=");
    background-repeat: repeat-x;
    background-position: bottom
}

.x-form-trigger-default {
    width: 17px;
    background: 0 0 transparent url("data:image/gif;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") no-repeat;
    border-width: 0 0 1px;
    border-color: #b5b8c8;
    border-style: solid
}

.x-form-trigger-default.x-form-trigger-over {
    background-position: -17px 0;
    border-color: #7eadd9
}

.x-form-trigger-default.x-form-trigger-over.x-form-trigger-focus {
    background-position: -68px 0
}

.x-form-trigger-default.x-form-trigger-focus {
    background-position: -51px 0;
    border-color: #7eadd9
}

.x-form-trigger.x-form-trigger-default.x-form-trigger-click {
    background-position: -34px 0
}

.x-textfield-default-cell > .x-grid-cell-inner {
    padding-top: 0;
    padding-bottom: 0
}

.x-form-text-field-body-toolbar {
    min-width: 150px;
    max-width: 150px
}

.x-form-text-wrap-toolbar {
    border-width: 1px;
    border-style: solid;
    border-color: #b5b8c8
}

.x-form-text-wrap-toolbar.x-form-text-wrap-focus {
    border-color: #7eadd9
}

.x-form-text-wrap-toolbar.x-form-text-wrap-invalid {
    border-color: #c30
}

.x-form-text-toolbar {
    color: #000;
    padding: 1px 3px 2px;
    background-color: #fff;
    background-image: url("data:image/gif;R0lGODlhAQASAIcAAN7j5vDz8/P19fX39/f5+fn7+/z8/f3+/v///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAAAAP8ALAAAAAABABIAAAgQAAEEEDCAQAEDBxAoXMgwIAA7");
    font: normal 12px/15px tahoma, arial, verdana, sans-serif;
    min-height: 18px
}

.x-ie8 .x-form-text-toolbar {
    min-height: 15px
}

.x-form-text-toolbar.x-form-textarea {
    line-height: 14px;
    min-height: 56px
}

.x-ie8 .x-form-text-toolbar.x-form-textarea {
    min-height: 53px
}

.x-form-text-toolbar.x-form-text-file {
    color: grey
}

.x-placeholder-label-toolbar {
    padding: 1px 3px 2px
}

.x-form-empty-field-toolbar + .x-placeholder-label-toolbar {
    color: grey
}

.x-form-text-toolbar:-ms-input-placeholder {
    color: grey
}

.x-form-invalid-field-toolbar {
    background-color: #fff;
    background-image: url("data:image/gif;R0lGODlhBAADAIcAAAD/AP8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAAAALAAAAAAEAAMAAAgMAAMAGAhAoMCCAAICADs=");
    background-repeat: repeat-x;
    background-position: bottom
}

.x-form-trigger-toolbar {
    width: 17px;
    background: 0 0 #fff url("data:image/gif;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") no-repeat;
    border-width: 0 0 1px;
    border-color: #b5b8c8;
    border-style: solid
}

.x-form-trigger-toolbar.x-form-trigger-over {
    background-position: -17px 0
}

.x-form-trigger-toolbar.x-form-trigger-over.x-form-trigger-focus {
    background-position: -68px 0
}

.x-form-trigger-toolbar.x-form-trigger-focus {
    background-position: -51px 0
}

.x-form-trigger.x-form-trigger-toolbar.x-form-trigger-click {
    background-position: -34px 0
}

.x-textfield-toolbar-cell > .x-grid-cell-inner {
    padding-top: 0px;
    padding-bottom: 0px
}

.x-form-clear-trigger {
    background-image: url("data:image/gif;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")
}

.x-form-search-trigger {
    background-image: url("data:image/gif;R0lGODlhZgAYAIcAACxJcy5SiDVfnThnrjtorTxqsT1vsz9wsz5wtDx0tz52uD18ukVnlklolUhpmkJus0JvtEtxqURwtElztEp1tUx1tkx3uE54tk95uVB2tFF4tlF5uED/QDuEvjyEvzyMwkeDvUiDv0uFvlyCu12CvGyDn3GDnm6DoHCFonaMr3OLsHaUvXiVvUWKwkqGwEmMwkiNxEWRxUeUx0iTxUqUxkqVyFGLwVGMwVqXyFqYyWCUxmOdymSdynycyWyizXCkznat0niu1H6t2X6y1Hy016OuvrG1u4Cfy4qoz4Gv2o6314y514+825etwputxJOx1ZG525u515+415u+2p252qW0wKGzyqm0wa66yKC42KG/3aW92qS+3qi92bW4yJnA25jB35bD4JnU557V55zW6qrB3bTB17XD2bjL36jH4azD4q/L46HY66Ld7qTa6qfe7q7Q46/Q5Knb67TJ4bbL5LfM5LnK4LjL5LnN4rnO5r3O4bzP5bDQ5LXT5rXU5b7R4b3Q5rvQ6bnc6r7Z6L7f673f78TN3cjP18nQ2cjR3s/V3dLS0tfZ39nZ2d3d3cDP5sLQ4sHT5MPV5sXS5cfW58DS6cHU6sTT6MDZ6cLc6sTd68jV583X5srb5svc5srY68nZ7Mvc6cjf7Mza687e6M3c7sXd+crd9czf9Mjf+9DW4NHY49DZ5tfc49Dd6tDd7dXf7dne5Nze4dHf8MLi78jl787i7s7n78bo9M7g9Mrg+cvh/czi+83i/c3k/8vr9dLg7NTi69bh7dnj79nl7d3j6d7m7d/o79Lh8tDh9NXi8dXj9Nbk8tHm/tTk+Nfp/9jl8tnm9tzl8Njm+Nro9t7p8N3o9N/t9tjo+9nq/tvs/9zq+9zr/t3t/93z/9/0/+Hh4ePk5+Xl5eDk6eXn6ubo6+Xo7enp6e3t7eLp8eDq9eLs9uTq8+Xu9uHs+enu8+H1/+Xx+eX2/+vx9u7w8+/z9+rz+en5/+36//Hx8fX19fD7//H8//r6+vv8/v3+/iH5BAEAABwALAAAAABmABgAAAj/AL0IHEiwoBcOQhIqXMhQCMKGEBM+jNhwIsWFFi9K9Mexo8d/Hhl58UiyZB4hnVKqXMnyZMmXHF3CNImSpU2VJ/Pp3JlPn0+eHL0oGzqUGTRr6tRZgzbU37+aLD1J9cRSCNGiR5Mubfr0nlev+O7h24evrNd/T29OpbpSCM+e+mq5kXNL3059QokebVeIDBta65gqS7vSE6lgxIQFI8W2k1W91fj6BSy469ey/HC1efOLX9h7hFUaRqyYsUq3d48NmfHhA40vdvP184KsNrN1yoLEaC2DiTpoyEJ3OlxNkJgxhIiZdlwb2e3cuz/0/h1cyFex14jIaF0jzL6zUIcH/yt+PPlyIejS56P3owOPNWlwvJiiD91sZMmQUWPno8MO+Di0AIU6y4RGCjHAABFdDEsol5IQ+OnHn38ACkjgU/JkeI89P3jwXho5wABGWAYiqGBrDDroWHro5BPJAjrUE0ss89wggjGyeZFLLslQkweMMtJoQwjIQEOYJ8Ec099/8bWghINC7NjjjzHOOM+QRWIIjzz3WAKklTe4QA1oNSGpJIVNPknKiuptkUAZrRxyyDhPKKBHjqigkgs1VLwZ55xPJEAHNUcSgweQrQgJgivBeCJEnnv2CaecdApKqBDwZHqPFn4eggidCgBCZkqeGIqooow6ymI+XRiQRSyIqP9CDhIGQJLjKaegMg0VrsIqK610TFNoFJ0CmsAcxDiGSq679hrrrAYE+9Q31MrDhbO/IgCIPMMWWymyK57TIicFVJCOOeYII4EG5txqiq6XlHtuuhJYwIwzhUphgBS+QouGMI7ieso08ZqLrrr24iuENwzL84m8B0uAwTXclkmMvvw+S+u/jjriCDjnsPLAAA8c0cMDE5xxjiN4zTHHHq9sMnLJJ0uwxSh3xCMEHHDwockeENNLQSiD8CGEyzDLTLLJD9iMs86mmKLLNp9AsHTNamCji848+wy0wUITbXQjjoizigYEjEDA2hmYIY4jjeBVByClTHLBAGqvXUEXpQD/QgfXcPhhCyUzM22zKH7AIQQddNuN99oE7N3330Kkwks2o2wwAAlrF3BB1rykArjghF/d9BaIK162KhEIwAI6xRiSyDhvNxK3F5W8MknrK7ADix16wPJKJXnkwbUfokhyd94EUIB6HzwLkfvuAvT+e/DDF69zL9x80joL80DzyCXWcNPLLrtw3Ufyy0PuvCjQq65IAwGkQI444OQPju224wUKJAwIgAqkoYxXlKIUoLBEIBaoM+RFgnfpAAYa9GAL+PEMDkn4XwAHWMADJnCBgYhHEp7xCQcIcB3d6EY2tPGMZvjihTpb3wOrF8EJVjB+igNHEQBggvvxrxGLACIQ//FSCicA4ATSmIUCQchEEQ7iDxskhi00kYlMDCJxF0xCEY+YxCUykYFJyIYVAIACd3TDhS9MIwyT8MQoTrGKV7yg6mRhhHDsbxF4zGMe/eeKKwxDiV9sYhIy0QQAlIAYiOODIvkgRwyCoo9/9GIgRfiMaGBBHWdUoyZFSEhDItIPi2SkHIVgO48BUY+oxEslQIFASU6SjaGoQjDgx4c42PKWtlTcKlsZyCYKoRnPyEYLNblJWMqSlrjEpeJQyUw95sMLvYxmDDGhCUz0IZTYZKQQotlLnRHzmzAUQh+oac1shnKZzWwmXrg5SSEo8prmPOc22elLcH5TZ++MpzzT2WPMZ9LTl/rMpuL+CUJv2nOT7gzoPvmZSmgSNIQJVagiB/rQ7R1UjfiU6ESFwFBU+rOiEZUoRQlq0IuGU6Mb7age1wlSlGrzoRDthUlPilJ0qnQRHyVpSBU60n+W1KQZ1ajiAgIAOw==")
}

.x-message-box .x-window-body {
    background-color: #ced9e7;
    border-width: 0
}

.x-message-box-info, .x-message-box-warning, .x-message-box-question, .x-message-box-error {
    background-position: left top;
    background-repeat: no-repeat
}

.x-message-box-icon {
    height: 32px;
    width: 32px;
    margin-right: 10px
}

.x-message-box-info {
    background-image: url("data:image/gif;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")
}

.x-message-box-warning {
    background-image: url("data:image/gif;R0lGODlhHwAgAPcAAAAAAAAABQAACAAAEgAAFQAAGQAAHRAKBgAAIgAALgAAMQoAMBUAPiQZEScXJCcZIAAAQgcASxkBRR4ISh0QQwAAagAAfAYPcQsPdwwScw4UchcFYx4LbxEXbxUZbhodahESexQYfx0gaTEaYT0nTzIwXzUyXSQnZSgpZCssYi4tYi8wYjchaDEvYDEwYDs4bE06GFA8K0QxTkE/WVpODFhEHlxNLm1VImRQMnldIUBAWElJVFhOTlBHUVFTT3dhVn1iXRIUgBsdhiUrhSUthy4yhy81iTtBiFBAklNUh2lbumNlnmhqp29xp3Z4rn+Cr4x7HYNpIYFrNoR0Nox2M5WJLZ6JKZCAMZ+UKaWOE6qRFr+fEqWbJrOXPaemEbSjAbSvHb+6GLKoILidT8arDMulAs2kAMmoBs6uBsO4AtaqANWtANC8ANqwAN6yAN60AOC0AOK4AOW6AOS+AMbFFcrKI+bAAOfFAOXLAOrAAOjHAOrHBe/AAOzGAOrLAOzKHuXUAObcAOrUAezTD+nbAOrYDOjSFOzQGvHBAPHFAPXHAPHJAPXIAPXOAPnKAPnMAPzLAP3OAPPSAPLVAPfQAvLaAPnWAf/SAPzRB/7VAP7VBfjbAPreAP/ZAP/ZBP/dAP/dBv7bCv/fCv7fDObFKeTCPeXhAOnjAOrpAPLjAPHqAPnhAPvlAPjlBP/hAP7hBv/lAP/mBf/jCf/hDP7lCfroA//oAP/qBf/tAP7qCf/jEP/oEf/pFP/tEf/sFP/uG/PzAPn2APn0BP7xAP71AP/1Df79AP/+C//0Ev/yGf/wHf/3Gf79E//9HOPiI///Iv/+JP//Kfb2Pv//MenOaOvRYOnefuzqWevmZOrjbuvoZergfv//aIaIr4uLq4KCsomNsI6OsZCPuZKSt5WVuJaYuZmZtZqauqantqWkvbu6zL6y/+jZi+nciundjuXbsOrpocPC0cfH1srJ1dPT2tjX3dnZ39/f39va4Nzc4ODf4+PkwuHg1uHg3+Df4wAAACH5BAEAAP4ALAAAAAAfACAAAAj+AP0JHEhwID94BRMqXChwHzNj0uoxnJiwH7BgxozVEUexo79rqIxFy+jjm0eG/FChWsbtmDE6IOKdVKjNlKpm055h3LFkZsJTp4QxOwaNmLEwGOb5HIjNVKpjLpsxM7qDyVJ/94AOm5rm2DOjYEIo9Zkt0FMvAAAIcMZsmDEdTZYSIrRVgIAFCmw0cysmCL2Z2QA9PQaAgAQIMZgxwzVshpOZhQi1enjAAAMIN4xBw0WMi5C/HbcBqlTMJY0EEyRkMdZsGathK554FARoMi5jXxKwIIGHWLFntoZh+UzRGh5BuYrZMsYGARIZxnDZaobM1aoS3SgawlMJ2S1Yw2z+OVCCg5gtWMWaccJVZYjEhe7w+KFVbBWs5TUsaDHmylWsZrls4soJ4TA0CB6T9HJLf7AYA0UFaBADS3/LLGOJLe3lo1B8fryCzCef9DcMGRH4gYsrIMYCzSufTJLCOAodoockvdACIoiwWELBJ7bc+EmFlsByhREaEtSOHn6M0ssnnXQCoiuwbDEhk0y+Eo0smXyCAjkF7XEHJb7I0mSTn+DCmS09jtlJMtBc4ooVRBTpDztz9BHKLk1m0qQtZwwQwAOZuJJnJp5AI8oljagAzkB/2LGILqBkIqmetjQAQAEK5DDMpJLy8ssjrkxRBD7+vDNHHpjMksklq+r5SQCqA4zAARC4SHrJrZ4oo8kjiXhgjj/VxJGHJp5wSikMBGywzhiwdGLsLJow0gkPR/hDyhtyJKKIIowwwq0jl3QSxQ9dXOJIt9x2y0gifFxCxQXqULNGG2+4Ye+9bsAhhyOQIBIHvvfCEQcfkfTQgTf+lNJGGWY07PDDEEeshhtSZCDCr/6g80ILJXTs8ccgf+yCCSpo8EES9gwkTznlnOPyyzDHLLM56ZAaEAAAOw==")
}

.x-message-box-question {
    background-image: url("data:image/gif;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")
}

.x-message-box-error {
    background-image: url("data:image/gif;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")
}

.x-form-cb-wrap-default {
    height: 22px;
    min-width: 13px
}

.x-form-cb-default {
    margin-top: 5px
}

.x-form-checkbox-default, .x-form-radio-default {
    width: 13px;
    height: 13px
}

.x-form-radio-default {
    background: url("data:image/gif;R0lGODlhMwAaAOeuAA02WQ0+XRUyRxYySBc0ShgzRxgzSBg0ShE4WB0+Vx0+WBRAXB5AWg1DZxVGZCBAWCREXTBLXyVGYCZIYi5KYDZRZjVSaEZkekhjeAdUgwlWhA9ZhA9fjRZdhBRijRlljS5iijNjiEZshkptiFFxiTyEqQ+Dxw6ExheKxxiY0Q2g8xKi8h2q8x6+/yKPxiCd0Sii0Sqw8ijE/zLK/1iEnkCFrEeLrkqLsUyQt1aFoVeUt1KYvFqbvWWFmGqGl2mGmH2NmGuduWyauX6lvF2ixmOfx2ajzGyhwGmrznqlwXKx1nSz2HW12nq/5V3O3WnC1H/m7nT//4qLi4uMjIWTn4mXoo6apI+cppGaopejrJihppmjq6Kioqawuam0vK64v7S5vrm6uoCqw4yvxY6zyY+3yJGyxpG4yZi3ypy6zLu+wpzC0J7E3IPL+ZLM7ZjK5JDV5ZnT75TU+pXZ/JnW+pzZ+aDH3r3Bxb7DyanS6a/a7aTc+qzd/bfX6r3d5bHb8bbd87Hf/bve8b7g77Th/L7h87zl/L3o+7H2+sPDw8fHx8DFycXIzMjLzs3NzcnO087R1dDQ0NTU1NTW2dbZ3Nra2tzc3Nze4cfj7sHk9sHo/Mns/M/x+tHt/d/o9tP0+tbx/dj09tnx/dv2+N34+uHh4eXl5enp6evs7O/v8OP1/un3/vHx8fT09P///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////yH5BAEKAP8ALAAAAAAzABoAAAj+AP8J5DKl4BQuAhMK1OIjRw4fWhQmxEICBAgSWCQKlMRRUiRJEqWEqcSKVaUwUiT2KONn1Cg/ZXpIHCGETaFCbISMkBjJ1CmfqExFSiglESpGYMA0QpUopcAeaz7VadOmzqc1MgWKSCKVqtUkIhJG+mnKZ9lTQ7mEOQXmzqNHjO6gCoNQSxlObeTw4UOnDacyEbEI+ZN3b19AQjJKKuvzFKrHPyVJscQIzyNIlC5xtJTShx86dAIFImRozx4/Pv6RYANaNGnTbEj8G9v4cSpUjiNNYQUG0iRLjSOxmvIvx6g2ow1pWk5nVI5/IAohJ71cE51CIP5JOuXYdsnHknb+q6FU6lSq85ZSETfehtByUKJEBQpFA7p095rgyxcUQjt3VOeVxMpt4Vnim3mttIKbJcT94Ecde2wCiiqqiLKJHz+oZgeEElJooR2yRYJbKgK2wgqAkaiFiiOlpGIiKqzQ9Y8WZ3AihyGiVNjJKGcEJgQgN+YoSieZJDYbUAIOGBRIRbFSik8uNpUQVJ8cokknoJCCVUJbVXlllmCJ9d93uA0lkEiVJGgJSiqd4QcppPhxRlZc1pRJJjmFpVBPAJ4nlEQEFSQFQhox5BBEGv1DkUUYJeoRRx8lKumklFZqaaAFESqRoQ9FpNGiF2WkUSSNlNqImUSNVNJJTk3Jkkv+MNEpEE024aSTRIpUgkqCqFSiCFFGqUEFFXJJ+VRUbhRRhBtX0bkVIErccMMSgIQpkCKnsHJKKeVp+6tap1QhAQYVPGDFXHXdZcQEF1jAgBF/+fjHDRJcUIECOCCWUSQklfJRJCyaFMlkakBghiZPLJCAI5z945kbEKSxChQOKBAHaqqxocQDQ8xhAwIKNBHbP0uhZUoqpTjiyGON7AZEBHA4AQMKBlwxXHGj8BABIlHMwIIBRzhnXw0UEFHCBxsIoAN2JLdiyVilVFIJi620zAoVBbjwQgonGJCFejjzYEAMMrSwggFJ0De0AB14wIEGAwTBX9MpSy11wC1bskiwAgGYYEIAD1jC4D8OuqGAAyuo0IACg2CoIRMKAKBBBgAokAeI/yiSyikq371yKoqouEUCBxyQwBcx1lUjEgqUrkAaPPoIyA4JEEBAAmYUuW+/KqtsSiuVDNWkJF14cUkrxv5DpR5koIGJls4mUcgbYozRRybWZp5tUCe3csqvZ46kJpsK9eAmnHLK+o8IduIphJ4J5bqrgr4CatCgiXKK6KcVhZooqaZClaUGSEBLBQQAOw==") no-repeat
}

.x-form-cb-checked .x-form-radio-default {
    background-position: 0 -13px
}

.x-form-checkbox-default {
    background: url("data:image/gif;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") no-repeat
}

.x-form-cb-checked .x-form-checkbox-default {
    background-position: 0 -13px
}

.x-form-checkbox-focus.x-form-radio-default {
    background-position: -13px 0
}

.x-form-cb-checked .x-form-checkbox-focus.x-form-radio-default {
    background-position: -13px -13px
}

.x-form-checkbox-focus.x-form-checkbox-default {
    background-position: -13px 0
}

.x-form-cb-checked .x-form-checkbox-focus.x-form-checkbox-default {
    background-position: -13px -13px
}

.x-form-cb-label-default {
    margin-top: 4px;
    font: normal 12px/14px tahoma, arial, verdana, sans-serif;
    color: #000
}

.x-form-cb-label-default.x-form-cb-label-before {
    padding-right: 17px
}

.x-form-cb-label-default.x-form-cb-label-after {
    padding-left: 17px
}

.x-checkbox-default-cell > .x-grid-cell-inner {
    padding-top: 0;
    padding-bottom: 0
}

.x-form-cb-wrap-toolbar {
    height: 20px;
    min-width: 13px
}

.x-form-cb-toolbar {
    margin-top: 4px
}

.x-form-checkbox-toolbar, .x-form-radio-toolbar {
    width: 13px;
    height: 13px
}

.x-form-radio-toolbar {
    background: url("data:image/gif;R0lGODlhMwAaAOeuAA02WQ0+XRUyRxYySBc0ShgzRxgzSBg0ShE4WB0+Vx0+WBRAXB5AWg1DZxVGZCBAWCREXTBLXyVGYCZIYi5KYDZRZjVSaEZkekhjeAdUgwlWhA9ZhA9fjRZdhBRijRlljS5iijNjiEZshkptiFFxiTyEqQ+Dxw6ExheKxxiY0Q2g8xKi8h2q8x6+/yKPxiCd0Sii0Sqw8ijE/zLK/1iEnkCFrEeLrkqLsUyQt1aFoVeUt1KYvFqbvWWFmGqGl2mGmH2NmGuduWyauX6lvF2ixmOfx2ajzGyhwGmrznqlwXKx1nSz2HW12nq/5V3O3WnC1H/m7nT//4qLi4uMjIWTn4mXoo6apI+cppGaopejrJihppmjq6Kioqawuam0vK64v7S5vrm6uoCqw4yvxY6zyY+3yJGyxpG4yZi3ypy6zLu+wpzC0J7E3IPL+ZLM7ZjK5JDV5ZnT75TU+pXZ/JnW+pzZ+aDH3r3Bxb7DyanS6a/a7aTc+qzd/bfX6r3d5bHb8bbd87Hf/bve8b7g77Th/L7h87zl/L3o+7H2+sPDw8fHx8DFycXIzMjLzs3NzcnO087R1dDQ0NTU1NTW2dbZ3Nra2tzc3Nze4cfj7sHk9sHo/Mns/M/x+tHt/d/o9tP0+tbx/dj09tnx/dv2+N34+uHh4eXl5enp6evs7O/v8OP1/un3/vHx8fT09P///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////yH5BAEKAP8ALAAAAAAzABoAAAj+AP8J5DKl4BQuAhMK1OIjRw4fWhQmxEICBAgSWCQKlMRRUiRJEqWEqcSKVaUwUiT2KONn1Cg/ZXpIHCGETaFCbISMkBjJ1CmfqExFSiglESpGYMA0QpUopcAeaz7VadOmzqc1MgWKSCKVqtUkIhJG+mnKZ9lTQ7mEOQXmzqNHjO6gCoNQSxlObeTw4UOnDacyEbEI+ZN3b19AQjJKKuvzFKrHPyVJscQIzyNIlC5xtJTShx86dAIFImRozx4/Pv6RYANaNGnTbEj8G9v4cSpUjiNNYQUG0iRLjSOxmvIvx6g2ow1pWk5nVI5/IAohJ71cE51CIP5JOuXYdsnHknb+q6FU6lSq85ZSETfehtByUKJEBQpFA7p095rgyxcUQjt3VOeVxMpt4Vnim3mttIKbJcT94Ecde2wCiiqqiLKJHz+oZgeEElJooR2yRYJbKgK2wgqAkaiFiiOlpGIiKqzQ9Y8WZ3AihyGiVNjJKGcEJgQgN+YoSieZJDYbUAIOGBRIRbFSik8uNpUQVJ8cokknoJCCVUJbVXlllmCJ9d93uA0lkEiVJGgJSiqd4QcppPhxRlZc1pRJJjmFpVBPAJ4nlEQEFSQFQhox5BBEGv1DkUUYJeoRRx8lKumklFZqaaAFESqRoQ9FpNGiF2WkUSSNlNqImUSNVNJJTk3Jkkv+MNEpEE024aSTRIpUgkqCqFSiCFFGqUEFFXJJ+VRUbhRRhBtX0bkVIErccMMSgIQpkCKnsHJKKeVp+6tap1QhAQYVPGDFXHXdZcQEF1jAgBF/+fjHDRJcUIECOCCWUSQklfJRJCyaFMlkakBghiZPLJCAI5z945kbEKSxChQOKBAHaqqxocQDQ8xhAwIKNBHbP0uhZUoqpTjiyGON7AZEBHA4AQMKBlwxXHGj8BABIlHMwIIBRzhnXw0UEFHCBxsIoAN2JLdiyVilVFIJi620zAoVBbjwQgonGJCFejjzYEAMMrSwggFJ0De0AB14wIEGAwTBX9MpSy11wC1bskiwAgGYYEIAD1jC4D8OuqGAAyuo0IACg2CoIRMKAKBBBgAokAeI/yiSyikq371yKoqouEUCBxyQwBcx1lUjEgqUrkAaPPoIyA4JEEBAAmYUuW+/KqtsSiuVDNWkJF14cUkrxv5DpR5koIGJls4mUcgbYozRRybWZp5tUCe3csqvZ46kJpsK9eAmnHLK+o8IduIphJ4J5bqrgr4CatCgiXKK6KcVhZooqaZClaUGSEBLBQQAOw==") no-repeat
}

.x-form-cb-checked .x-form-radio-toolbar {
    background-position: 0 -13px
}

.x-form-checkbox-toolbar {
    background: url("data:image/gif;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") no-repeat
}

.x-form-cb-checked .x-form-checkbox-toolbar {
    background-position: 0 -13px
}

.x-form-checkbox-focus.x-form-radio-toolbar {
    background-position: -13px 0
}

.x-form-cb-checked .x-form-checkbox-focus.x-form-radio-toolbar {
    background-position: -13px -13px
}

.x-form-checkbox-focus.x-form-checkbox-toolbar {
    background-position: -13px 0
}

.x-form-cb-checked .x-form-checkbox-focus.x-form-checkbox-toolbar {
    background-position: -13px -13px
}

.x-form-cb-label-toolbar {
    margin-top: 4px;
    font: normal tahoma, arial, verdana, sans-serif/13px tahoma, arial, verdana, sans-serif;
    color: #000
}

.x-form-cb-label-toolbar.x-form-cb-label-before {
    padding-right: 17px
}

.x-form-cb-label-toolbar.x-form-cb-label-after {
    padding-left: 17px
}

.x-checkbox-toolbar-cell > .x-grid-cell-inner {
    padding-top: 0px;
    padding-bottom: 0px
}

.x-form-item-body-default.x-form-checkboxgroup-body {
    padding: 0 4px
}

.x-form-invalid .x-form-item-body-default.x-form-checkboxgroup-body {
    border-width: 1px;
    border-style: solid;
    border-color: #c30;
    background-image: url("data:image/gif;R0lGODlhBAADAIcAAAD/AP8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAAAALAAAAAAEAAMAAAgMAAMAGAhAoMCCAAICADs=");
    background-repeat: repeat-x;
    background-position: bottom
}

.x-fieldset-default {
    border: 1px solid #b5b8c8;
    padding: 0 10px;
    margin: 0 0 10px;
    -webkit-border-radius: 4px;
    -moz-border-radius: 4px;
    -ms-border-radius: 4px;
    -o-border-radius: 4px;
    border-radius: 4px
}

.x-ie8 .x-fieldset-default {
    padding-top: 0
}

.x-ie8 .x-fieldset-body-default {
    padding-top: 0
}

.x-fieldset-header-default {
    padding: 0 3px 1px;
    line-height: 14px
}

.x-fieldset-header-default > .x-fieldset-header-text {
    font: normal 11px/14px tahoma, arial, verdana, sans-serif;
    color: #15428b;
    padding: 1px 0
}

.x-fieldset-header-checkbox-default {
    margin: 2px 3px 1px 0;
    line-height: 14px
}

.x-fieldset-header-tool-default {
    margin: 1px 3px 0 0;
    padding: 0
}

.x-fieldset-header-tool-default > .x-tool-img {
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=100)";
    opacity: 1;
    height: 15px;
    width: 15px
}

.x-fieldset-header-tool-default > .x-tool-toggle {
    background-position: 0 -60px
}

.x-fieldset-header-tool-default.x-tool-over > .x-tool-toggle {
    background-position: -15px -60px
}

.x-fieldset-header-tool-default.x-focus {
    outline: 1px solid red
}

.x-fieldset-default.x-fieldset-collapsed {
    -webkit-border-radius: 0;
    -moz-border-radius: 0;
    -ms-border-radius: 0;
    -o-border-radius: 0;
    border-radius: 0;
    border-width: 1px 1px 0 1px;
    border-left-color: transparent;
    border-right-color: transparent
}

.x-fieldset-default.x-fieldset-collapsed .x-tool-toggle {
    background-position: 0 -75px
}

.x-fieldset-default.x-fieldset-collapsed .x-tool-over > .x-tool-toggle {
    background-position: -15px -75px
}

.x-form-trigger-spinner-default {
    width: 17px;
    border: 0
}

.x-form-spinner-default {
    background-image: url("data:image/gif;R0lGODlhZgAWAPcAADFQizJRjDNRjDRTjTVTjTVUjX2s2X6t2X+t2YCu2bS4x7W4yLnP57vQ573R6Mrb5crb5svb5tfZ38zc5s7d59nb4M7e6M/e6Mve9cve9tDe6Mze9M3f9M7f9NLg6c/g9NDg89Dg9NLh6tPh6tDh9NDh9dTh6tLh8NHh89Lh8tHh9dPh8NTi6tPi8tTi8dPj9tXj8dPj99fk7Nbk9dfl9djl9djm9dnm9Nrm8tnm9trm9Nvm89rn9Nrn9tzn8+3t7e7u7u/v7+/v8O/w8PDw8Ovx9d/0/+D0/+L0//Hx8eH1/+L1/+P1//Ly8uT1/+P2//Pz8+X2/+f2/+j2/+b3//D1+Of3//H1+Oj3//H1++n3//T19ef4//H2+/L2+ur4/+j5/+n5/un5/+r5//P3++v5/+z5/+r6/ur6/+v6//T4+uz6//X4+u36//X4/fX5/fb5/Pb5/ff5/Pr6+vb7//n7/Pn7/fn7/vr7/Pb8//v7+/r7/vj8//r8/vv8/fv8/vz8/Pj9//z8/vn9//r9//v9//z9/v39/f39/vv+//z+//3+//7+/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////yH5BAEAAP8ALAAAAABmABYAAAj/ABcIHEiw4IJ/CBIqXMjwwL8DECMeSCBRIkKGGBU6zMjRYUWICD5C/LeopElDJlMyqqAAkcuXgl7KZOTAwISbOD0UMYETZwMDMl3GDIqIpoGUJVEiXWS0500TV1g4nfCTiNWrTeY0uWrVj6EFK8KKxeEFh9iwdhodgMCWrQg2A9iIaMv2wYGzYcmaPZv2gJi/gM0EWhMGsJhFaulCeBt3Ll27XIk0AUQA0FauWxa42Lx5h5wBcnZwdnEicdsRbAIACCBX8YHRLjyDFs25tF/DZgoRKGTGMBjTbFGrZu247YEgyIMkASQAgABASZIH0bMghfUUN+AMh3PjegrgwgGI/2c9gu4B79m3d7+ulot7LmUINRdAaMx7LuBTi1/NprxxIAASoUdz4gmgBxEAAkEdCAzWoN1+AcBRA4MgmBZeAHgM159xFDqo2ngSUqhWFCRqId9+9GlBYhQW6oehhv5BcMAPPwg43yHzHUgjdR10MEMcw/UxXBwz9JgYBVUMwJ8M+g1QBQVsHdDjj0EOWWQHai2xhBSDzKfIfINIoeWRSS7Z5JNR/gDEHAQ4p0cSAwJAwBxA/EDdBiFkoWQAb+TwhmoDZBHCBhaqUYcac41gKKLG4annan3+CUCgg6p1BBJ0tCnAIFN0KScdSBxR6KGJLlrcjDXqcYgeQ6S6qhA0zv+xQAYZxODGHW7EUOutudKqVgTAXqDBBcBGcMGxxUZwAK224qprs71moJYRRjjBRyF8OFHttdlS+2uwwxZ7LLHFoqomgDSeW+eOC2zgbgkqlODuBiXUOy9wiuUb5bzwyvuuve5aesQRSzAR6sBLIHGwqGvp6/ABBkVMkEgUV2zxxRhnrLG5CabbMbv8xssvwIQ27HC+B4TsL70kC0ywwQMTrHDM+J5snMfo0vixne2+K/K/K9dss4wqjxz0ATEXvHDCCwttM6oCrtpq1HrAyjMGGLzghh1uvJD11l1jDZwFF1jQFtlmG4e11lx7zXbYGEy7LbbaWku3tyajfXbZ5gH/EQSbbjYR55xBKLgAByR0secbPUg6QBckcDAqo4qSahziikPaOKCQS36AEkzkoekgWHhKQB5MKDF5qZZHGWCcAuDoJoKGf/ABDUCuJuRqcdBgO5l7ssEkoGjKaDvuVfLu+wdqPfGEFZ4K8KVzg1jhPPBmEg+ljMktR6Bz0CVHHQrk2/AgiDaQj0KLw2XIX4wHqG/+h6vBkT75alGh/xcnFkjIF/qjAvtW4z7yGIcrk5mPZbhCnRY4sAU8kMNw5KCDB7YgP/QzoHEsGMEJVvCBagGDCMGQhhPRpwwj/I3JwjOeDRknCTCEIRQoAwgoxBCGmYGBDnXog8/IwQc71CG+lC7UGvMEEQY9BA0Qg6gWNDjRiW1IRAES0YYnOnGILiriC2+YBCjowYY3NMRXjohEMixxh4aoGWO0aBwy+sCMR0zjAawIxUG04QxWbIQa4cLGKInxj4b4AyABKYEF/OGQiNwDIhf5BwaYrC0iqEKM2uJIRv5BkZZs5AEsiUlLOjJfkZwkWxwpsVJurGIUOaUqV0mxgAAAOw==");
    background-color: #fff;
    width: 17px;
    height: 11px
}

.x-form-spinner-up-default {
    background-position: 0 0
}

.x-form-spinner-up-default.x-form-spinner-over {
    background-position: -17px 0
}

.x-form-spinner-up-default.x-form-spinner-over.x-form-spinner-focus {
    background-position: -68px 0
}

.x-form-spinner-up-default.x-form-spinner-focus {
    background-position: -51px 0
}

.x-form-spinner-up-default.x-form-spinner.x-form-spinner-click {
    background-position: -34px 0
}

.x-form-spinner-down-default {
    background-position: 0 -11px
}

.x-form-spinner-down-default.x-form-spinner-over {
    background-position: -17px -11px
}

.x-form-spinner-down-default.x-form-spinner-over.x-form-spinner-focus {
    background-position: -68px -11px
}

.x-form-spinner-down-default.x-form-spinner-focus {
    background-position: -51px -11px
}

.x-form-spinner-down-default.x-form-spinner.x-form-spinner-click {
    background-position: -34px -11px
}

.x-form-trigger-spinner-toolbar {
    width: 17px;
    border: 0
}

.x-form-spinner-toolbar {
    background-image: url("data:image/gif;R0lGODlhZgAUAMQAADFQi36s2YCu2bS4x7W4yLnP57vQ573R6Mrb5cve9M7e6M/g9NDe6NLh6dLh8tja39rm89/0/+L0/+f4/+n3/+n5/u3t7e3w8e/v8PDw8PH1+fX4+/v8/QAAAAAAAAAAACH5BAkAAB0ALAAAAABmABQAAAX/ICGOZEl0QaqubIC2Qpu+skzX7I2rHef/wOBjECwCDwGEctm4NJZLQ8BIRVKNSKiyoXlqpZmwOMMZh30Eh3oN0UDWal8S2tgANl5oAK5uv+FyFYKDFRyEgnJadXd5SwFmZABlkGlwEHYbf2scc1t2AIxae5aYmnEBh4WSqZx0n6F6FrIWkaBlsxYclX2vmYCdi6CgeHqkwr6bARPLE6q2FcwTrZ7Cw40Bs7XCt7K6bK/DmtPBksd5ow6X1XfiARLvFBzrHBTvEuOv8taOstr6khm6EUiQwEG+Yw4I4uNArA7DcwQNbkOo0N27fxjtLWy44SE/Wj8ugPSBQWDEjhsS/xpkmDDBNAQKYi6JqUDPSZYFUbbkFCHCPR8SfP4IGuGlAgY1ldCMhatpU10EC6qJuiaqUaQzZTqiOjViV5cW7Ykde6/T0aQwtSoJYKItiR1w48qdS3eH07smvbaUuvellr9rue6tWpGs4YudAP/FhtcpVL2CrZpVu3Qr5MtgDxs2SlktAsZkfIgMzaFkroE5ca5MWTEr2sqBU7NevTNAz58cguImevW1Z9AYtwU8vWCBRFsIi2984pDY2uLHyw1zoDxscFsa5zRnjvJctn+2hp/+tg6ZA3wT960lX808J3vOtlXITg25+s9mMObfla6XqZfk3PeZMeH8cghGBwIDDmQsa0EizyRm8NcfO3z4RY5zjvChjnmnsLJKgq6YIwokZDjojYZuVOgXAotgmCGKppzHSSqFsLJii42sdUURDxCwYxAFJLZFF38F+SMQRh7pQ5B/cZEjAkG6JWVdNcRA5ZVYshACADs=");
    background-color: #fff;
    width: 17px;
    height: 10px
}

.x-form-spinner-up-toolbar {
    background-position: 0 0
}

.x-form-spinner-up-toolbar.x-form-spinner-over {
    background-position: -17px 0
}

.x-form-spinner-up-toolbar.x-form-spinner-over.x-form-spinner-focus {
    background-position: -68px 0
}

.x-form-spinner-up-toolbar.x-form-spinner-focus {
    background-position: -51px 0
}

.x-form-spinner-up-toolbar.x-form-spinner.x-form-spinner-click {
    background-position: -34px 0
}

.x-form-spinner-down-toolbar {
    background-position: 0 -10px
}

.x-form-spinner-down-toolbar.x-form-spinner-over {
    background-position: -17px -10px
}

.x-form-spinner-down-toolbar.x-form-spinner-over.x-form-spinner-focus {
    background-position: -68px -10px
}

.x-form-spinner-down-toolbar.x-form-spinner-focus {
    background-position: -51px -10px
}

.x-form-spinner-down-toolbar.x-form-spinner.x-form-spinner-click {
    background-position: -34px -10px
}

.x-tbar-page-number {
    width: 30px
}

.x-btn-icon-el.x-tbar-page-first {
    background-image: url("data:image/gif;R0lGODlhEAAQAIcAACRIkChNli1TnjNZpjhgrz9otx1m9S9kzy9l0yxm2DBiyDFq2zhu3D5z2z913SRq8ixx7jRy6D5++URvwEJt1Ep1yE970Eh630574UD/QFOA1lOE3VWF3liH30+K9k+J/VGD4VeH4FaE6VmK4l+L4F+M4WCM5GWP62mR42iU5WuT62+W7G2Z5mec+2ma/2ic+XGa536f7oKg54Wu/42r8Iiu/5a076G+8KK9/6W//6rE7wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAMAABkALAAAAAAQABAAAAh6ADMIHEiwoMGDB2HIQGEwhEEWOhwSJKHBYIobFQeWyGHBoAkbHQV2yOGigsERNExm4JBjxocJBkHEgLkBR40XEgoYvLBCZ4YGLTxAIGDQgQqiAg9EeDDAIIMTTQcqMCDA4AIRVQkiCGAwAQauBQEYpABALMKzaNMODAgAOw==")
}

.x-btn-icon-el.x-tbar-page-prev {
    background-image: url("data:image/gif;R0lGODlhEAAQAIcAACRIkChNli1TnjNZpjhgrz9otx1m9S9kzy9l0yxm2DBiyDFq2zhu3D5z2z913SRq8ixx7jRy6D5++URvwEJt1Ep1yE970Eh630574UD/QFOA1lOE3VWF3liH30+K9k+J/VGD4VeH4FaE6VmK4l+L4F+M4WCM5GWP62mR42iU5WuT62+W7G2Z5mec+2ma/2ic+XGa536f7oKg54Wu/42r8Iiu/5a076G+8KK9/6W//6rE7wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAMAABkALAAAAAAQABAAAAhMADMIHEiwoMGDCAuGSFiQhAaGA0vksAAxQ4ccLipA5JBjxocJDDfgqPFCQgGIDVp4gECg4oEIDwZUzKDAgICZGRAEwJkBAM+fQA0GBAA7")
}

.x-btn-icon-el.x-tbar-page-next {
    background-image: url("data:image/gif;R0lGODlhEAAQAIcAACRIkChNli1TnjNZpjhgrz9otx1m9S9kzy9l0yxm2DBiyDFq2zhu3D5z2z913SRq8ixx7jRy6D5++URvwEJt1Ep1yE970Eh630574UD/QFOA1lOE3VWF3liH30+K9k+J/VGD4VeH4FaE6VmK4l+L4F+M4WCM5GWP62mR42iU5WuT62+W7G2Z5mec+2ma/2ic+XGa536f7oKg54Wu/42r8Iiu/5a076G+8KK9/6W//6rE7wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAMAABkALAAAAAAQABAAAAhIADMIHEiwoMGDCDPASGiQBQmGBFPgeAgxgwkcNShUHGHjRQuNDEHQaAEhwQCGF2CUBADRAYgELCEyoBAT4oKaEBNU3MmzJ8GAADs=")
}

.x-btn-icon-el.x-tbar-page-last {
    background-image: url("data:image/gif;R0lGODlhEAAQAIcAACRIkChNli1TnjNZpjhgrz9otx1m9S9kzy9l0yxm2DBiyDFq2zhu3D5z2z913SRq8ixx7jRy6D5++URvwEJt1Ep1yE970Eh630574UD/QFOA1lOE3VWF3liH30+K9k+J/VGD4VeH4FaE6VmK4l+L4F+M4WCM5GWP62mR42iU5WuT62+W7G2Z5mec+2ma/2ic+XGa536f7oKg54Wu/42r8Iiu/5a076G+8KK9/6W//6rE7wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAMAABkALAAAAAAQABAAAAh4ADMIHEiwoMGDB2EYhCEDhUEWJAqy0BHCYAocEQemuKHBoAkcNSgMNGHDgsERNl60EJlhBI0KBkHQaAEhwYAMIGJMMHgBRk0AAi+sKGDQAYgEQAU6UEHAIAMKSQUyOHGz4IKoAheIEGAwQVcMARAWhIpVrNmzGQICADs=")
}

.x-btn-icon-el.x-tbar-loading {
    background-image: url("data:image/gif;R0lGODlhEAAQAIcAABBYsRhcvRhuzhR0xiBxzyZ4zyd70yd71SR72Cp50Dd3yTp/zT16yEN5w0J8x1J+whqI3BqA7ByQ+CKA1iqA0iyE0SqC2jyK1iyL5SqV/CqX/zSL4jqh/z2n/0qHyEqMzkqH1UqG20+J1kKQ30qS1liOzVaR3VSb10Sa4Eyf6VKf40uh4Uii60On/0it/0+u/1Kj4Vqk6lew/1my/2Wb3Wuc1W+c2nCNx26n3G6q33Sj3GCm7G+q5Guz72O3/3ax53a3+HS+/3W+/3W//3nB/37D/4Wl1oOn25Sx3YWp4Iq1442y4Y+66JC+552+5ojC74XC/YjK/47J/5TM/5bM/5jP/5vM/p7P/5/P/6XA5qHK763C5KzE6arM7KDT/6LR/6HU/6TS/6DZ/7TM6rDU87Df/7fc/73W87Hg/7rk/73g/7zi/7zl/8Tb9MTd9s7d88Dk/8Xi/87k99bh9Nbm9tHp/9rm9uPr+eXz/+b0/+vy/O31/Pb7//j5/P3+//7+/////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAMAAIAALAAAAAAQABAAAAiuAAEJHEiwoMEmKCZQ+DDG4MAeEjJwaDHkgBOHWiA8IfMDgwwiCeaYCEGQR56BbjYIiQLAigKHA5cAmVKlTAOYgPQYWeDlC5oHArusgMEihQo5NcSwgbMmzQ2BOPDEMQOmSI43NESA8OBgi8ATdcJgqaDEYJ+BJNRcobKDCU5AF6AMkBLEQpuBd5IQHBGDTgEfMxDo4HIkQBaHZwy8cNFBQwQbOO2UICCAAZK3mAMCADs=")
}

.x-item-disabled .x-tbar-page-first {
    background-image: url("data:image/gif;R0lGODlhEAAQAIcAAGdnZ2xsbHJycnh4eH9/f0D/QIODg4WFhYaGhoeHh4uLi42NjY6Ojo+Pj5KSkpOTk5SUlJmZmZubm56enp+fn6GhoaOjo6SkpKenp6ioqKmpqaqqqq2tra+vr7GxsbS0tLW1tbe3t7i4uLm5ub29vb6+vsnJycvLy9HR0dra2tvb293d3eDg4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAMAAAUALAAAAAAQABAAAAh6AAsIHEiwoMGDB0OU6GDwgkEQLBwSzDDBoIcUFQdqWBHB4AYUHQVeWCHigUEMJkwWsLDihIYFBiuQgFlBxYkRFBAYjPBBZ4EHIzI4IGAQggeiAg88YDDAYAMOTQcaUCDAoAILVQkiCGAwgQSuBQEYZABALMKzaNMODAgAOw==")
}

.x-item-disabled .x-tbar-page-prev {
    background-image: url("data:image/gif;R0lGODlhEAAQAIcAAGdnZ2xsbHJycnh4eH9/f0D/QIODg4WFhYaGhouLi42NjY6OjpKSkpOTk5mZmZ6enp+fn6GhoaOjo6SkpKioqKmpqbi4uLm5ucvLy9vb293d3QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAMAAAUALAAAAAAQABAAAAhMAAsIHEiwoMGDCAtOSFiQwgOGAytocACxwAQNFhpAlKABQwUFDCNkwHABAgKIDS5QYECg4oEGCwZULGAggYCZBRAEwFkAAM+fQA0GBAA7")
}

.x-item-disabled .x-tbar-page-next {
    background-image: url("data:image/gif;R0lGODlhEAAQAIcAAGdnZ3h4eED/QIeHh4uLi46Ojo+Pj5KSkpSUlJmZmaGhoaenp6ioqKqqqrGxsbW1tbe3t7m5ucnJycvLy9HR0dvb2wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAAIALAAAAAAQABAAAAhIAAUIHEiwoMGDCAVASGjwAQOGBB1UeAhRQIMKEwpUXEAhQgSNDBVIiHBgQACGCSCUBAARgYIBLCEaKBATIoGaEAdU3MmzJ8GAADs=")
}

.x-item-disabled .x-tbar-page-last {
    background-image: url("data:image/gif;R0lGODlhEAAQAIcAAGdnZ2xsbHJycnh4eH9/f0D/QIaGhoeHh4uLi42NjY6Ojo+Pj5KSkpOTk5SUlJmZmZubm56enqGhoaOjo6SkpKenp6ioqKqqqq2tra+vr7GxsbS0tLW1tbe3t7m5ub29vb6+vsnJycvLy9HR0dra2tvb2+Dg4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAMAAAUALAAAAAAQABAAAAh4AAsIHEiwoMGDBzsY7AAig0EOFgpyMEHBoIYSEQdqIBHB4IUSIhQMvDDigcEKIzx4EFmgQogGBiWE8MDgwIACEj4kMPigQ00AAh9sMGDQgYQDQAU60EDA4AIFSQUuwHCzIIKoAhFMEGDwQFcIARAWhIpVrNmzBQICADs=")
}

.x-item-disabled .x-tbar-loading {
    background-image: url("data:image/gif;R0lGODlhEAAQAOZzAMXKzvDx8nh+htnd373Cx8LHzKmwt9fb3lhgaoOJkJGWnJedom50e7G3vMrO0cLGyaCmq2t0e7C2vKmtsautssTJzWhudmRtdp+or9LW2ZqgptDV2NDS1ZCVmo+WnUxTXIyUmtba3d3f4bG2ur/BxWVveYiQl6ass9rb3VliatXX2uLj5ZOcpLW5vWJqc1xkbm10fGpze3V8hK+zt3N8hH6FjL2/w9HW2be9w3mEjoGGjIeQlpecoePk5oSOl3R5f4uVnqqusmVtdsDFypCaop6hppmfpKyzumVsdUZNVmZvd2hxee/w8bi+w7/DxtbY27/EycbIy5miqYiLkenq62xyeXiCjHuBiImTnLG3vYGKkcjN0aGkqoeNk46Tmbq8wGtxeXqAh2RtdXd9g5+iqHuCipegqJ6lq4iRmPn5+Whye3F6g4mRl+Lk59/g4pOaoXB7hdrd36qxuAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAHMALAAAAAAQABAAAAeegHOCg4SFhiNaSkthUYaDZ3BWPkByQi2OTmoNDhBrZkdIbgkChBoBg080BjhJUBaOgxMnBEMbVbBzAUUwABU3P4IPOyBoJmwiHVsDAwcHU4ILTHEZABJGKF5XAmMMNoJdbQAFEUGGaYM1IQUEbzO4czJZKU0GMSqDVFyEZR4rLhhSLvAgQebDF0ccxLAggiVHCQW4euh4gQAMhXcYAwEAOw==")
}

.x-boundlist {
    border-width: 1px;
    border-style: solid;
    border-color: #98c0f4;
    background: #fff
}

.x-boundlist-item {
    padding: 0 3px;
    font: normal 12px tahoma, arial, verdana, sans-serif;
    line-height: 20px;
    cursor: pointer;
    cursor: hand;
    position: relative;
    border-width: 1px;
    border-style: dotted;
    border-color: #fff;
    color: #000
}

.x-boundlist-selected {
    background: #cbdaf0;
    border-color: #8eabe4
}

.x-boundlist-item-over {
    background: #dfe8f6;
    border-color: #a3bae9
}

.x-boundlist-floating {
    border-top-width: 0
}

.x-boundlist-above {
    border-top-width: 1px;
    border-bottom-width: 1px
}

.x-datepicker {
    border-width: 1px;
    border-style: solid;
    border-color: #1b376c;
    background-color: #fff;
    width: 177px
}

.x-datepicker-header {
    padding: 3px 6px;
    text-align: center;
    background-image: none;
    background-color: #23427c;
    background-image: -webkit-gradient(linear, top, bottom, color-stop(0%, #264888), color-stop(0%, #1f3a6c));
    background-image: -webkit-linear-gradient(top, #264888, #1f3a6c);
    background-image: -moz-linear-gradient(top, #264888, #1f3a6c);
    background-image: -o-linear-gradient(top, #264888, #1f3a6c);
    background-image: -ms-linear-gradient(top, #264888, #1f3a6c);
    background-image: linear-gradient(top, #264888, #1f3a6c)
}

.x-datepicker-arrow {
    width: 15px;
    height: 15px;
    top: 6px;
    cursor: pointer;
    -webkit-touch-callout: none;
    background-color: #23427c;
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=70)";
    opacity: 0.7
}

div.x-datepicker-arrow:hover {
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=100)";
    opacity: 1
}

.x-datepicker-next {
    right: 6px;
    background: url("data:image/gif;R0lGODlhDwAPAPcAABowbR04fSFChSdJki9klDx+pUCFpEGdqf///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACwAAAAADwAPAAAITAAFABhIsCBBAQEEDFjIsOEAhAEcSlwYIKGAixgzXqzIsSKCjiBBIvgYMuRIkiU5nkSZ8mTKjiNfwnxpsObAijZr4sxZMAAAmRwBBAQAOw==") no-repeat 0 0
}

.x-datepicker-prev {
    left: 6px;
    background: url("data:image/gif;R0lGODlhDwAPAPcAABowbR04fSFChSdJki9klDx+pUCFpEGdqf///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACwAAAAADwAPAAAISwAFABhIsCBBAQEEDFjIsOEAhAEcSlwYIKGAixgzXqzIsSOCjiA9fgwJEoFJkiJPouRocuTKiipfwiRpsObAijZr4sxZMAAAmTgDAgA7") no-repeat 0 0
}

.x-datepicker-month {
    background: transparent
}

.x-datepicker-month .x-btn, .x-datepicker-month .x-btn .x-btn-tc, .x-datepicker-month .x-btn .x-btn-tl, .x-datepicker-month .x-btn .x-btn-tr, .x-datepicker-month .x-btn .x-btn-mc, .x-datepicker-month .x-btn .x-btn-ml, .x-datepicker-month .x-btn .x-btn-mr, .x-datepicker-month .x-btn .x-btn-bc, .x-datepicker-month .x-btn .x-btn-bl, .x-datepicker-month .x-btn .x-btn-br {
    background: transparent;
    border-width: 0 !important
}

.x-datepicker-month .x-btn-inner {
    color: #fff
}

.x-datepicker-month .x-btn-split-right:after, .x-datepicker-month .x-btn-over .x-btn-split-right:after {
    background-image: url("data:image/gif;R0lGODlhDgBIAMIAAAAAAMnJycLa9vX19QAAAAAAAAAAAAAAACH+EUNyZWF0ZWQgd2l0aCBHSU1QACH5BAEAAAIALAAAAAAOAEgAAAMkKLrc/jDKSau9OOvNu/9gKI5kaZ5DmkoqNZxwLM90bd94ru8JADs=");
    padding: 0;
    text-align: right;
    width: 8px
}

.x-datepicker-month .x-btn {
    padding: 2px
}

.x-datepicker-month .x-btn-over {
    border-color: transparent;
    background: transparent
}

.x-datepicker-month .x-btn.x-btn-pressed {
    border-color: transparent;
    background: transparent
}

.x-datepicker-month .x-btn-inner {
    font-size: 11px
}

.x-datepicker-column-header {
    width: 25px;
    color: #233d6d;
    font: normal 10px tahoma, arial, verdana, sans-serif;
    text-align: right;
    border-width: 0 0 1px;
    border-style: solid;
    border-color: #b2d1f5;
    background-image: none;
    background-color: #dfecfb;
    background-image: -webkit-gradient(linear, top, bottom, color-stop(0%, #edf4fd), color-stop(0%, #cde1f9));
    background-image: -webkit-linear-gradient(top, #edf4fd, #cde1f9);
    background-image: -moz-linear-gradient(top, #edf4fd, #cde1f9);
    background-image: -o-linear-gradient(top, #edf4fd, #cde1f9);
    background-image: -ms-linear-gradient(top, #edf4fd, #cde1f9);
    background-image: linear-gradient(top, #edf4fd, #cde1f9)
}

.x-datepicker-column-header-inner {
    line-height: 19px;
    padding: 0 7px 0 0
}

.x-datepicker-cell {
    text-align: right;
    border: 1px solid #fff
}

.x-datepicker-date {
    padding: 0 4px 0 0;
    font: normal 11px tahoma, arial, verdana, sans-serif;
    color: #000;
    cursor: pointer;
    line-height: 18px
}

div.x-datepicker-date:hover {
    color: #000;
    background-color: #ddecfe
}

.x-datepicker-selected {
    border-style: solid;
    border-color: #8db2e3
}

.x-datepicker-selected div.x-datepicker-date {
    background-color: #dae5f3;
    color: #000;
    font-weight: bold
}

.x-datepicker-today {
    border-color: darkred;
    border-style: solid
}

.x-datepicker-prevday .x-datepicker-date, .x-datepicker-nextday .x-datepicker-date {
    color: #aaa
}

.x-datepicker-disabled .x-datepicker-date {
    background-color: #eee;
    cursor: default;
    color: #bbb
}

.x-datepicker-disabled div.x-datepicker-date:hover {
    background-color: #eee;
    color: #bbb
}

.x-datepicker-footer, .x-monthpicker-buttons {
    padding: 4px 0;
    border-width: 1px 0 0;
    border-style: solid;
    border-color: #b2d1f5;
    background-image: none;
    background-color: #dfecfb;
    background-image: -webkit-gradient(linear, top, bottom, color-stop(0%, #dee8f5), color-stop(49%, #d1dff0), color-stop(51%, #c7d8ed), color-stop(0%, #cbdaee));
    background-image: -webkit-linear-gradient(top, #dee8f5, #d1dff0 49%, #c7d8ed 51%, #cbdaee);
    background-image: -moz-linear-gradient(top, #dee8f5, #d1dff0 49%, #c7d8ed 51%, #cbdaee);
    background-image: -o-linear-gradient(top, #dee8f5, #d1dff0 49%, #c7d8ed 51%, #cbdaee);
    background-image: -ms-linear-gradient(top, #dee8f5, #d1dff0 49%, #c7d8ed 51%, #cbdaee);
    background-image: linear-gradient(top, #dee8f5, #d1dff0 49%, #c7d8ed 51%, #cbdaee);
    text-align: center
}

.x-datepicker-footer .x-btn, .x-monthpicker-buttons .x-btn {
    margin: 0 2px 0 2px
}

.x-monthpicker {
    width: 177px;
    border-width: 1px;
    border-style: solid;
    border-color: #1b376c;
    background-color: #fff
}

.x-monthpicker-months {
    border-width: 0 1px 0 0;
    border-color: #1b376c;
    border-style: solid;
    width: 87px
}

.x-monthpicker-months .x-monthpicker-item {
    width: 43px
}

.x-monthpicker-years {
    width: 88px
}

.x-monthpicker-years .x-monthpicker-item {
    width: 44px
}

.x-monthpicker-item {
    margin: 5px 0 4px;
    font: normal 11px tahoma, arial, verdana, sans-serif;
    text-align: center
}

.x-monthpicker-item-inner {
    margin: 0 5px 0 5px;
    color: #15428b;
    border: 1px solid #fff;
    line-height: 16px;
    cursor: pointer
}

a.x-monthpicker-item-inner:hover {
    color: #000;
    background-color: #ddecfe
}

.x-monthpicker-item a.x-monthpicker-selected {
    background-color: #dae5f3;
    color: #000;
    border-style: solid;
    border-color: #8db2e3
}

.x-monthpicker-yearnav {
    height: 27px
}

.x-monthpicker-yearnav-button-ct {
    width: 44px
}

.x-monthpicker-yearnav-button {
    height: 15px;
    width: 15px;
    cursor: pointer;
    margin-top: 6px;
    -webkit-touch-callout: none;
    background-color: #fff
}

.x-monthpicker-yearnav-next {
    background: url("data:image/gif;R0lGODlhHgBoAff+AP///8/k+3Gg3Zm76Nns/+/9/+b2/yZDkNTo/ur5/9bq/+Hz/9Hm/DJVslCAsJ+y41F/w87i+MPX8rPN7bTS/05pqUFNZn2j3nOKvIKTyi5LlYOPt5jJb2yN3HqJu5nJcejz6pu5+4S/VIS/UZyw4lSBxFd+u1WDxkRwsDppqnmf22yLzXCP4YSpz0FcoHee2W6K13Oa1G2L2miL00Rtq3uh3D5qq4Gn4XWDsIGn4m55p1Fhh7za/3CGtjQ6TZGgyf39/oym4W6X1IOUy2WNylZmiml8p0FOb5Wo3GJtonJ9rF5mcWGLyX2Mv6S55F2Ev6S54XF/vXie2F9rovH4/63D6W+Lyaa56tf2ovv8/pCs6nyj23GY0MHe/6K2405cfqC054yvzomZxIaUufr8/Zqt30ZZgYKk1qG15Jm2+V9xmd3s9Wd8qO3183mg2ebx709YkZSl0XGFtEVNhHWa0Ke86Ja2/56x4ldifv//3YCd24Cm3S5fpnCDsT9IYF2IyE9ce3OZ0VN/wZ+z42t1nYWi3Wd6pKvA63qKtzlBVLbN8p7A/9f0ooOUyP//4Mfuh09fgWd4omZukZmo0kJJXNzy/+bw7+rz83WDv2mQzWZ6pWFnkI6g02t9qGKLyFuGx+n05EJPabbU/36l3VFYiouk4HJ/oGF0nvr7/W59ovf7/3mc1eHy+FZqlUZVdy81RMrl/6S251xtlXuc3Yyv5GiOzam+6qKx0HqQyIih2HJ/saO457vS91likoWo3U9adHqIteXx7a/F7nGGtlVliWl9qhwfKXif2Flwnm6TzGCJyYud0nOCuPz9/mGKx+bx7ZGj2pao0XWLvXqg2Y2f1GSQuomZzISVvLXM8fv8/ThDXMfujK/E7VaFtMbd9sLX8jJOl8vi+Ymtz1mHtT9anm6Ywsjd9oCmyrPO5GR9tb/U8W+IvGuFvMrg+C9MlWiAtVeGtNnr+t/x/ldxrHKJuoSpyt/y/neexMTb9brT6KS52dvu/K7B3srf9////wAAACH/C1hNUCBEYXRhWE1QPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4gPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iQWRvYmUgWE1QIENvcmUgNS4wLWMwNjAgNjEuMTM0Nzc3LCAyMDEwLzAyLzEyLTE3OjMyOjAwICAgICAgICAiPiA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPiA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIiB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHhtbG5zOnhtcE1NPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvbW0vIiB4bWxuczpzdFJlZj0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL3NUeXBlL1Jlc291cmNlUmVmIyIgeG1wOkNyZWF0b3JUb29sPSJBZG9iZSBQaG90b3Nob3AgQ1M1IE1hY2ludG9zaCIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDo1QkI4Rjg1QkU1MUYxMURGQTg1Q0IzNzFDQzg3NDJFNyIgeG1wTU06RG9jdW1lbnRJRD0ieG1wLmRpZDo1QkI4Rjg1Q0U1MUYxMURGQTg1Q0IzNzFDQzg3NDJFNyI+IDx4bXBNTTpEZXJpdmVkRnJvbSBzdFJlZjppbnN0YW5jZUlEPSJ4bXAuaWlkOjVCQjhGODU5RTUxRjExREZBODVDQjM3MUNDODc0MkU3IiBzdFJlZjpkb2N1bWVudElEPSJ4bXAuZGlkOjVCQjhGODVBRTUxRjExREZBODVDQjM3MUNDODc0MkU3Ii8+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kPSJyIj8+Af/+/fz7+vn49/b19PPy8fDv7u3s6+rp6Ofm5eTj4uHg397d3Nva2djX1tXU09LR0M/OzczLysnIx8bFxMPCwcC/vr28u7q5uLe2tbSzsrGwr66trKuqqainpqWko6KhoJ+enZybmpmYl5aVlJOSkZCPjo2Mi4qJiIeGhYSDgoGAf359fHt6eXh3dnV0c3JxcG9ubWxramloZ2ZlZGNiYWBfXl1cW1pZWFdWVVRTUlFQT05NTEtKSUhHRkVEQ0JBQD8+PTw7Ojk4NzY1NDMyMTAvLi0sKyopKCcmJSQjIiEg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") no-repeat 0 -120px
}

.x-monthpicker-yearnav-next-over {
    background-position: -15px -120px
}

.x-monthpicker-yearnav-prev {
    background: url("data:image/gif;R0lGODlhHgBoAff+AP///8/k+3Gg3Zm76Nns/+/9/+b2/yZDkNTo/ur5/9bq/+Hz/9Hm/DJVslCAsJ+y41F/w87i+MPX8rPN7bTS/05pqUFNZn2j3nOKvIKTyi5LlYOPt5jJb2yN3HqJu5nJcejz6pu5+4S/VIS/UZyw4lSBxFd+u1WDxkRwsDppqnmf22yLzXCP4YSpz0FcoHee2W6K13Oa1G2L2miL00Rtq3uh3D5qq4Gn4XWDsIGn4m55p1Fhh7za/3CGtjQ6TZGgyf39/oym4W6X1IOUy2WNylZmiml8p0FOb5Wo3GJtonJ9rF5mcWGLyX2Mv6S55F2Ev6S54XF/vXie2F9rovH4/63D6W+Lyaa56tf2ovv8/pCs6nyj23GY0MHe/6K2405cfqC054yvzomZxIaUufr8/Zqt30ZZgYKk1qG15Jm2+V9xmd3s9Wd8qO3183mg2ebx709YkZSl0XGFtEVNhHWa0Ke86Ja2/56x4ldifv//3YCd24Cm3S5fpnCDsT9IYF2IyE9ce3OZ0VN/wZ+z42t1nYWi3Wd6pKvA63qKtzlBVLbN8p7A/9f0ooOUyP//4Mfuh09fgWd4omZukZmo0kJJXNzy/+bw7+rz83WDv2mQzWZ6pWFnkI6g02t9qGKLyFuGx+n05EJPabbU/36l3VFYiouk4HJ/oGF0nvr7/W59ovf7/3mc1eHy+FZqlUZVdy81RMrl/6S251xtlXuc3Yyv5GiOzam+6qKx0HqQyIih2HJ/saO457vS91likoWo3U9adHqIteXx7a/F7nGGtlVliWl9qhwfKXif2Flwnm6TzGCJyYud0nOCuPz9/mGKx+bx7ZGj2pao0XWLvXqg2Y2f1GSQuomZzISVvLXM8fv8/ThDXMfujK/E7VaFtMbd9sLX8jJOl8vi+Ymtz1mHtT9anm6Ywsjd9oCmyrPO5GR9tb/U8W+IvGuFvMrg+C9MlWiAtVeGtNnr+t/x/ldxrHKJuoSpyt/y/neexMTb9brT6KS52dvu/K7B3srf9////wAAACH/C1hNUCBEYXRhWE1QPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4gPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iQWRvYmUgWE1QIENvcmUgNS4wLWMwNjAgNjEuMTM0Nzc3LCAyMDEwLzAyLzEyLTE3OjMyOjAwICAgICAgICAiPiA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPiA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIiB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHhtbG5zOnhtcE1NPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvbW0vIiB4bWxuczpzdFJlZj0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL3NUeXBlL1Jlc291cmNlUmVmIyIgeG1wOkNyZWF0b3JUb29sPSJBZG9iZSBQaG90b3Nob3AgQ1M1IE1hY2ludG9zaCIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDo1QkI4Rjg1QkU1MUYxMURGQTg1Q0IzNzFDQzg3NDJFNyIgeG1wTU06RG9jdW1lbnRJRD0ieG1wLmRpZDo1QkI4Rjg1Q0U1MUYxMURGQTg1Q0IzNzFDQzg3NDJFNyI+IDx4bXBNTTpEZXJpdmVkRnJvbSBzdFJlZjppbnN0YW5jZUlEPSJ4bXAuaWlkOjVCQjhGODU5RTUxRjExREZBODVDQjM3MUNDODc0MkU3IiBzdFJlZjpkb2N1bWVudElEPSJ4bXAuZGlkOjVCQjhGODVBRTUxRjExREZBODVDQjM3MUNDODc0MkU3Ii8+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kPSJyIj8+Af/+/fz7+vn49/b19PPy8fDv7u3s6+rp6Ofm5eTj4uHg397d3Nva2djX1tXU09LR0M/OzczLysnIx8bFxMPCwcC/vr28u7q5uLe2tbSzsrGwr66trKuqqainpqWko6KhoJ+enZybmpmYl5aVlJOSkZCPjo2Mi4qJiIeGhYSDgoGAf359fHt6eXh3dnV0c3JxcG9ubWxramloZ2ZlZGNiYWBfXl1cW1pZWFdWVVRTUlFQT05NTEtKSUhHRkVEQ0JBQD8+PTw7Ojk4NzY1NDMyMTAvLi0sKyopKCcmJSQjIiEg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") no-repeat 0 -105px
}

.x-monthpicker-yearnav-prev-over {
    background-position: -15px -105px
}

.x-monthpicker-small .x-monthpicker-item {
    margin: 2px 0 2px
}

.x-monthpicker-small .x-monthpicker-item-inner {
    margin: 0 5px 0 5px
}

.x-monthpicker-small .x-monthpicker-yearnav {
    height: 22px
}

.x-monthpicker-small .x-monthpicker-yearnav-button {
    margin-top: 3px
}

.x-nlg .x-datepicker-header {
    background-image: url("data:image/gif;R0lGODlhAQAgA/QAAB86bR87biA7byA8cCA9cSE9ciE+cyE+dCE/dSI/diJAdyJAeSJBeiNBeyNCfCNCfSNDfiRDfyREgCRFgSVFgiVGgyVGhCVHhSZHhyZIiP///x86bR86bR86bR86bR86bSH5BAEAABoALAAAAAABACADRAhNADNESBAAgMGDCBMqXMiwocOHECMmrNCggMSLGDNqzHhhwoMFBwZsHEmypMmTKFNKxGCBggQIDhgoQGCAgACVOHPq3Mmzp8+fQIMCDQgAOw==");
    background-repeat: repeat-x;
    background-position: top left
}

.x-nlg .x-datepicker-footer, .x-nlg .x-monthpicker-buttons {
    background-image: url("data:image/gif;R0lGODlhAQAgA/QAAMfY7cjY7cnZ7crZ7dHf8NLf8NLg8NPg8dTh8dXi8dbi8tfj8tjj8tnk89rl89vm9Nzn9N3n9P///8fY7cfY7cfY7cfY7cfY7cfY7cfY7cfY7cfY7cfY7cfY7cfY7cfY7SH5BAEAABIALAAAAAABACADRAhNACMoACBggMGDCBMqXMiwocOHECMmdGAggMSLGDNqzPiAAQICACxuHEmypMmTKFNGhOCgwYIEBwoACBlAQEGVOHPq3Mmzp8+fQIP6DAgAOw==");
    background-repeat: repeat-x;
    background-position: top left
}

.x-cmd-slicer.x-datepicker-header:before {
    display: none;
    content: "x-slicer:, bg:url("data:image/gif;R0lGODlhAQAgA/QAAB86bR87biA7byA8cCA9cSE9ciE+cyE+dCE/dSI/diJAdyJAeSJBeiNBeyNCfCNCfSNDfiRDfyREgCRFgSVFgiVGgyVGhCVHhSZHhyZIiP///x86bR86bR86bR86bR86bSH5BAEAABoALAAAAAABACADRAhNADNESBAAgMGDCBMqXMiwocOHECMmrNCggMSLGDNqzHhhwoMFBwZsHEmypMmTKFNKxGCBggQIDhgoQGCAgACVOHPq3Mmzp8+fQIMCDQgAOw=="), stretch:bottom" !important
}

.x-cmd-slicer.x-datepicker-footer:before {
    display: none;
    content: "x-slicer:, bg:url("data:image/gif;R0lGODlhAQAgA/QAAMfY7cjY7cnZ7crZ7dHf8NLf8NLg8NPg8dTh8dXi8dbi8tfj8tjj8tnk89rl89vm9Nzn9N3n9P///8fY7cfY7cfY7cfY7cfY7cfY7cfY7cfY7cfY7cfY7cfY7cfY7cfY7SH5BAEAABIALAAAAAABACADRAhNACMoACBggMGDCBMqXMiwocOHECMmdGAggMSLGDNqzPiAAQICACxuHEmypMmTKFNGhOCgwYIEBwoACBlAQEGVOHPq3Mmzp8+fQIP6DAgAOw=="), stretch:bottom" !important
}

.x-form-field-date .x-form-date-trigger {
    background-image: url("data:image/gif;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")
}

.x-form-display-field-default {
    min-height: 22px;
    font: normal 12px/14px tahoma, arial, verdana, sans-serif;
    color: #000;
    margin-top: 4px
}

.x-form-display-field-default.x-field-form-focus {
    outline: 1px solid #7eadd9;
    outline-offset: -1px
}

.x-ie .x-form-display-field-default.x-field-form-focus, .x-ie10p .x-form-display-field-default.x-field-form-focus, .x-edge .x-form-display-field-default.x-field-form-focus {
    outline: none
}

.x-ie .x-form-display-field-default.x-field-form-focus:after, .x-ie10p .x-form-display-field-default.x-field-form-focus:after, .x-edge .x-form-display-field-default.x-field-form-focus:after {
    position: absolute;
    content: ' ';
    top: 0px;
    right: 0px;
    bottom: 0px;
    left: 0px;
    border: 1px solid #7eadd9;
    pointer-events: none
}

.x-ie8 .x-form-display-field-default.x-field-form-focus {
    position: relative
}

.x-form-display-field-toolbar {
    min-height: 22px;
    font: normal 11px/13px tahoma, arial, verdana, sans-serif;
    color: #000;
    margin-top: 5px
}

.x-form-display-field-toolbar.x-field-form-focus {
    outline: 1px solid #7eadd9;
    outline-offset: -1px
}

.x-ie .x-form-display-field-toolbar.x-field-form-focus, .x-ie10p .x-form-display-field-toolbar.x-field-form-focus, .x-edge .x-form-display-field-toolbar.x-field-form-focus {
    outline: none
}

.x-ie .x-form-display-field-toolbar.x-field-form-focus:after, .x-ie10p .x-form-display-field-toolbar.x-field-form-focus:after, .x-edge .x-form-display-field-toolbar.x-field-form-focus:after {
    position: absolute;
    content: ' ';
    top: 0px;
    right: 0px;
    bottom: 0px;
    left: 0px;
    border: 1px solid #7eadd9;
    pointer-events: none
}

.x-ie8 .x-form-display-field-toolbar.x-field-form-focus {
    position: relative
}

.x-tip-default {
    -webkit-border-radius: 3px;
    -moz-border-radius: 3px;
    -ms-border-radius: 3px;
    -o-border-radius: 3px;
    border-radius: 3px;
    padding: 2px 2px 2px 2px;
    border-width: 1px;
    border-style: solid;
    background-color: #e9f2ff
}

.x-tip-default-mc {
    background-color: #e9f2ff
}

.x-nbr .x-tip-default {
    padding: 0 !important;
    border-width: 0 !important;
    -webkit-border-radius: 0px;
    -moz-border-radius: 0px;
    -ms-border-radius: 0px;
    -o-border-radius: 0px;
    border-radius: 0px;
    background-color: transparent !important;
    box-shadow: none !important
}

.x-tip-default-frameInfo {
    font-family: th-3-3-3-3-1-1-1-1-2-2-2-2
}

.x-tip-default-tl {
    background-position: 0 -6px
}

.x-tip-default-tr {
    background-position: right -9px
}

.x-tip-default-bl {
    background-position: 0 -12px
}

.x-tip-default-br {
    background-position: right -15px
}

.x-tip-default-ml {
    background-position: 0 top
}

.x-tip-default-mr {
    background-position: right top
}

.x-tip-default-tc {
    background-position: 0 0
}

.x-tip-default-bc {
    background-position: 0 -3px
}

.x-tip-default-tr, .x-tip-default-br, .x-tip-default-mr {
    padding-right: 3px
}

.x-tip-default-tl, .x-tip-default-bl, .x-tip-default-ml {
    padding-left: 3px
}

.x-tip-default-tc {
    height: 3px
}

.x-tip-default-bc {
    height: 3px
}

.x-tip-default-tl, .x-tip-default-bl, .x-tip-default-tr, .x-tip-default-br, .x-tip-default-tc, .x-tip-default-bc, .x-tip-default-ml, .x-tip-default-mr {
    background-image: url("data:image/gif;R0lGODlhAwASAPMAAI6qzpWvz5au0Jex0piw0qm/3bLA07/O4cHQ4uHr++Pj5eny/////wAAAI6qzo6qziH5BAEAAAwALAAAAAADABIAQwgxAAEIHJBgQYICBhYoFFBQ4QIGCAgcPKDAQACHDgUCOFAgAQEEDAwSMNDRYIAABhQEBAA7")
}

.x-tip-default-ml, .x-tip-default-mr {
    background-image: url("data:image/gif;R0lGODlhBgAiAPEAAI6qzuny/////46qziH5BAEAAAIALAAAAAAGACIAQQg0AAEEGBgAgECCBgkWPDgwIUKGCxU6bAhxYsSHEitqzMgRo0eKHUF+vCiyJMmTFlNuHJkyIAA7");
    background-repeat: repeat-y
}

.x-tip-default-mc {
    padding: 0px 0px 0px 0px
}

.x-cmd-slicer.x-tip-default:before {
    display: none;
    content: "x-slicer:, frame:3px 3px 3px 3px, corners:url("data:image/gif;R0lGODlhAwASAPMAAI6qzpWvz5au0Jex0piw0qm/3bLA07/O4cHQ4uHr++Pj5eny/////wAAAI6qzo6qziH5BAEAAAwALAAAAAADABIAQwgxAAEIHJBgQYICBhYoFFBQ4QIGCAgcPKDAQACHDgUCOFAgAQEEDAwSMNDRYIAABhQEBAA7"), sides:url("data:image/gif;R0lGODlhBgAiAPEAAI6qzuny/////46qziH5BAEAAAIALAAAAAAGACIAQQg0AAEEGBgAgECCBgkWPDgwIUKGCxU6bAhxYsSHEitqzMgRo0eKHUF+vCiyJMmTFlNuHJkyIAA7")" !important
}

.x-tip-default {
    background-color: #e9f2ff;
    border-color: #8eaace
}

.x-tip-default .x-tool-img {
    background-color: #e9f2ff
}

.x-tip-header-default .x-tool-after-title {
    margin: 0 0 0 6px
}

.x-tip-header-default .x-tool-before-title {
    margin: 0 6px 0 0
}

.x-tip-header-default {
    padding: 3px 3px 0 3px
}

.x-tip-header-title-default {
    color: #444;
    font-size: 11px;
    font-weight: bold
}

.x-tip-body-default {
    padding: 3px;
    color: #444;
    font-size: 11px;
    font-weight: normal
}

.x-tip-body-default a {
    color: #2a2a2a
}

.x-tip-default .x-tip-anchor {
    border: 6px solid transparent;
    _border-color: pink;
    _filter: chroma(color=pink)
}

.x-tip-default .x-tip-anchor:after {
    position: absolute;
    border: 5px solid transparent;
    content: "";
    _border-color: pink;
    _filter: chroma(color=pink)
}

.x-tip-default .x-tip-anchor-top {
    border-top-width: 0;
    border-bottom: 6px solid #7c9dc6;
    top: -6px
}

.x-tip-default .x-tip-anchor-bottom {
    border-bottom-width: 0;
    border-top: 6px solid #7c9dc6;
    bottom: -6px
}

.x-tip-default .x-tip-anchor-left {
    border-left-width: 0;
    border-right: 6px solid #7c9dc6;
    left: -6px
}

.x-tip-default .x-tip-anchor-right {
    border-right-width: 0;
    border-left: 6px solid #7c9dc6;
    right: -6px
}

.x-tip-default .x-tip-anchor-top:after {
    border-top-width: 0;
    border-bottom-color: #e9f2ff;
    top: 1px;
    margin-left: -5px
}

.x-tip-default .x-tip-anchor-bottom:after {
    border-bottom-width: 0;
    border-top-color: #e9f2ff;
    bottom: 1px;
    margin-left: -5px
}

.x-tip-default .x-tip-anchor-left:after {
    border-left-width: 0;
    border-right-color: #e9f2ff;
    left: 1px;
    margin-top: -5px
}

.x-tip-default .x-tip-anchor-right:after {
    border-right-width: 0;
    border-left-color: #e9f2ff;
    right: 1px;
    margin-top: -5px
}

.x-tip-form-invalid {
    -webkit-border-radius: 5px;
    -moz-border-radius: 5px;
    -ms-border-radius: 5px;
    -o-border-radius: 5px;
    border-radius: 5px;
    padding: 4px 4px 4px 4px;
    border-width: 1px;
    border-style: solid;
    background-color: #fff
}

.x-tip-form-invalid-mc {
    background-color: #fff
}

.x-nbr .x-tip-form-invalid {
    padding: 0 !important;
    border-width: 0 !important;
    -webkit-border-radius: 0px;
    -moz-border-radius: 0px;
    -ms-border-radius: 0px;
    -o-border-radius: 0px;
    border-radius: 0px;
    background-color: transparent !important;
    box-shadow: none !important
}

.x-tip-form-invalid-frameInfo {
    font-family: th-5-5-5-5-1-1-1-1-4-4-4-4
}

.x-tip-form-invalid-tl {
    background-position: 0 -10px
}

.x-tip-form-invalid-tr {
    background-position: right -15px
}

.x-tip-form-invalid-bl {
    background-position: 0 -20px
}

.x-tip-form-invalid-br {
    background-position: right -25px
}

.x-tip-form-invalid-ml {
    background-position: 0 top
}

.x-tip-form-invalid-mr {
    background-position: right top
}

.x-tip-form-invalid-tc {
    background-position: 0 0
}

.x-tip-form-invalid-bc {
    background-position: 0 -5px
}

.x-tip-form-invalid-tr, .x-tip-form-invalid-br, .x-tip-form-invalid-mr {
    padding-right: 5px
}

.x-tip-form-invalid-tl, .x-tip-form-invalid-bl, .x-tip-form-invalid-ml {
    padding-left: 5px
}

.x-tip-form-invalid-tc {
    height: 5px
}

.x-tip-form-invalid-bc {
    height: 5px
}

.x-tip-form-invalid-tl, .x-tip-form-invalid-bl, .x-tip-form-invalid-tr, .x-tip-form-invalid-br, .x-tip-form-invalid-tc, .x-tip-form-invalid-bc, .x-tip-form-invalid-ml, .x-tip-form-invalid-mr {
    background-image: url("data:image/gif;R0lGODlhBQAeAPUAAKExH6hCMahDM6lFNKpDNLdSRLdpW7dpXLhSRLhSRbhSRrhpW7hpXblSRblSRrtrXsSPh8WPh86zr8+ZkNCzr9hxZth6cNl1atl5cNl6cNp4btp5btp5b9vb2+DEwOPHw+bm5vDHw/vx7/vx8P///////wAAAKExH6ExH6ExH6ExH6ExH6ExH6ExH6ExH6ExH6ExH6ExH6ExH6ExH6ExH6ExH6ExH6ExH6ExH6ExH6ExH6ExH6ExH6ExH6ExH6ExHyH5BAEAACUALAAAAAAFAB4ARQh5AAEIFFihYMENGRJMKAGiA4UDA0hIlOjBwYUQIwhoGCGRgwUEETpMHDmxRIkPDwgE2DgyhAUGFBpcFCExRIYDBguS3DlyoMASEwpk2GAgQwiJBB58MDkixAUFHiSK4CBgAYajJDpAaGCBg1QOA0Q4TSBhwAEKHUAEBAA7")
}

.x-tip-form-invalid-ml, .x-tip-form-invalid-mr {
    background-image: url("data:image/gif;R0lGODlhCgAeAPEAAKExH9hxZv///////yH5BAEAAAMALAAAAAAKAB4AQQhMAAEEEECwYAAAAgsaRDhQoYCDCR1CbKhwosOHDC9alJiRY8SKHUF+XDiS4EaRFEmmNBlSpcaWLEtilHnSpceVM3HWjKkTZs6XNAEEBAA7");
    background-repeat: repeat-y
}

.x-tip-form-invalid-mc {
    padding: 0px 0px 0px 0px
}

.x-cmd-slicer.x-tip-form-invalid:before {
    display: none;
    content: "x-slicer:, frame:5px 5px 5px 5px, corners:url("data:image/gif;R0lGODlhBQAeAPUAAKExH6hCMahDM6lFNKpDNLdSRLdpW7dpXLhSRLhSRbhSRrhpW7hpXblSRblSRrtrXsSPh8WPh86zr8+ZkNCzr9hxZth6cNl1atl5cNl6cNp4btp5btp5b9vb2+DEwOPHw+bm5vDHw/vx7/vx8P///////wAAAKExH6ExH6ExH6ExH6ExH6ExH6ExH6ExH6ExH6ExH6ExH6ExH6ExH6ExH6ExH6ExH6ExH6ExH6ExH6ExH6ExH6ExH6ExH6ExH6ExHyH5BAEAACUALAAAAAAFAB4ARQh5AAEIFFihYMENGRJMKAGiA4UDA0hIlOjBwYUQIwhoGCGRgwUEETpMHDmxRIkPDwgE2DgyhAUGFBpcFCExRIYDBguS3DlyoMASEwpk2GAgQwiJBB58MDkixAUFHiSK4CBgAYajJDpAaGCBg1QOA0Q4TSBhwAEKHUAEBAA7"), sides:url("data:image/gif;R0lGODlhCgAeAPEAAKExH9hxZv///////yH5BAEAAAMALAAAAAAKAB4AQQhMAAEEEECwYAAAAgsaRDhQoYCDCR1CbKhwosOHDC9alJiRY8SKHUF+XDiS4EaRFEmmNBlSpcaWLEtilHnSpceVM3HWjKkTZs6XNAEEBAA7")" !important
}

.x-tip-form-invalid {
    background-color: #fff;
    border-color: #a1311f;
    -webkit-box-shadow: #d87166 0 1px 0px 0 inset, #d87166 0 -1px 0px 0 inset, #d87166 -1px 0 0px 0 inset, #d87166 1px 0 0px 0 inset;
    -moz-box-shadow: #d87166 0 1px 0px 0 inset, #d87166 0 -1px 0px 0 inset, #d87166 -1px 0 0px 0 inset, #d87166 1px 0 0px 0 inset;
    box-shadow: #d87166 0 1px 0px 0 inset, #d87166 0 -1px 0px 0 inset, #d87166 -1px 0 0px 0 inset, #d87166 1px 0 0px 0 inset
}

.x-tip-form-invalid .x-tool-img {
    background-color: #fff
}

.x-tip-header-form-invalid .x-tool-after-title {
    margin: 0 0 0 6px
}

.x-tip-header-form-invalid .x-tool-before-title {
    margin: 0 6px 0 0
}

.x-tip-header-form-invalid {
    padding: 3px 3px 0 3px
}

.x-tip-header-title-form-invalid {
    color: #444;
    font-size: 11px;
    font-weight: bold
}

.x-tip-body-form-invalid {
    padding: 3px 3px 3px 22px;
    color: #444;
    font-size: 11px;
    font-weight: normal
}

.x-tip-body-form-invalid a {
    color: #2a2a2a
}

.x-tip-form-invalid .x-tip-anchor {
    border: 6px solid transparent;
    _border-color: pink;
    _filter: chroma(color=pink)
}

.x-tip-form-invalid .x-tip-anchor:after {
    position: absolute;
    border: 5px solid transparent;
    content: "";
    _border-color: pink;
    _filter: chroma(color=pink)
}

.x-tip-form-invalid .x-tip-anchor-top {
    border-top-width: 0;
    border-bottom: 6px solid #8c2a1b;
    top: -6px
}

.x-tip-form-invalid .x-tip-anchor-bottom {
    border-bottom-width: 0;
    border-top: 6px solid #8c2a1b;
    bottom: -6px
}

.x-tip-form-invalid .x-tip-anchor-left {
    border-left-width: 0;
    border-right: 6px solid #8c2a1b;
    left: -6px
}

.x-tip-form-invalid .x-tip-anchor-right {
    border-right-width: 0;
    border-left: 6px solid #8c2a1b;
    right: -6px
}

.x-tip-form-invalid .x-tip-anchor-top:after {
    border-top-width: 0;
    border-bottom-color: #fff;
    top: 1px;
    margin-left: -5px
}

.x-tip-form-invalid .x-tip-anchor-bottom:after {
    border-bottom-width: 0;
    border-top-color: #fff;
    bottom: 1px;
    margin-left: -5px
}

.x-tip-form-invalid .x-tip-anchor-left:after {
    border-left-width: 0;
    border-right-color: #fff;
    left: 1px;
    margin-top: -5px
}

.x-tip-form-invalid .x-tip-anchor-right:after {
    border-right-width: 0;
    border-left-color: #fff;
    right: 1px;
    margin-top: -5px
}

.x-tip-body-form-invalid {
    background: 1px 1px no-repeat;
    background-image: url("data:image/gif;R0lGODlhEAAQAIcAAED/QMJLMsNNNMVPNsNUPcxVPMZXQcddRs5dTNBZQcxiTM5kTtVgR9FjTNFhUNRkUthwWd5wWd1wXd18b919b+FdUuJfU+NhVOViVeZlVudnV+NmW+RnXOdsXehpWOpsWetuWulvX+F0XOVyWep2XexwW+5zXO92XfB4X/F6X+BzYO57Yel9aPN8YPN+YemCau2BaeyBbO6DbuOEdeaIeOqHfeuJfeqNe+yLf+ySf/KAZfSAYvWBYvWCY/SEZ/WEaveGbPaJa/iGbfONdvWOd/eMdfqOd/qUfN6hleWOg+eQhOeRheySiO2SieyYie2flfGTgvCXg/GXhPSZhPCfjvGdkOGkl+Onmu6glfihiPiiifijivOmkfSmkvGlmfGom/Gon/Kpn+uvovOvpvSsofWwo/ezoPezpPC0qPi0oPi2ofi1pfm5pvq8qPu9qfi+sfq/sv3DtfrZ0////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAMAAAAALAAAAAAQABAAAAjBAAEIHEiwoME4R4D8IPLG4EAjMrqkScOFBQyHQqS42RIkiJY2OUYULBLFTY8ec+a4aMHmhoiBcGKY5LEjZQoUJ9ZIECNwCJcsO1amPGGiBBQnEASuUOOjxc2UJUB8CPElgUASZnTgNCFnzgcPGjp4KSDwBZUpRUFUGaMhAwYbSxYIRKPijFQPKTFcsBDGgZWBEWiUaduEiYUKYSgYKMhgBhkcHDbUADMhgMMGD5RgeZIEAQGHAq8oGCDgABLQqAkGBAA7")
}

.x-tip-body-form-invalid li {
    margin-bottom: 4px
}

.x-tip-body-form-invalid li.last {
    margin-bottom: 0
}

.x-color-picker {
    width: 144px;
    height: 90px;
    background-color: #fff;
    border-color: #fff;
    border-width: 0;
    border-style: solid
}

.x-color-picker-item {
    width: 18px;
    height: 18px;
    border-width: 1px;
    border-color: #fff;
    border-style: solid;
    background-color: #fff;
    cursor: pointer;
    padding: 2px
}

a.x-color-picker-item:hover {
    border-color: #8bb8f3;
    background-color: #deecfd
}

.x-color-picker-selected {
    border-color: #8bb8f3;
    background-color: #deecfd
}

.x-color-picker-item-inner {
    line-height: 10px;
    border-color: #aca899;
    border-width: 1px;
    border-style: solid
}

.x-html-editor-tb .x-edit-bold, .x-menu-item div.x-edit-bold {
    background-position: 0 0;
    background-image: url("data:image/gif;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")
}

.x-html-editor-tb .x-edit-italic, .x-menu-item div.x-edit-italic {
    background-position: -16px 0;
    background-image: url("data:image/gif;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")
}

.x-html-editor-tb .x-edit-underline, .x-menu-item div.x-edit-underline {
    background-position: -32px 0;
    background-image: url("data:image/gif;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")
}

.x-html-editor-tb .x-edit-forecolor, .x-menu-item div.x-edit-forecolor {
    background-position: -160px 0;
    background-image: url("data:image/gif;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")
}

.x-html-editor-tb .x-edit-backcolor, .x-menu-item div.x-edit-backcolor {
    background-position: -176px 0;
    background-image: url("data:image/gif;R0lGODlh4AAQAIcAAAAAABAIEBATEBsjHSAYICAgEDA0ECEkIy80OjAoIDAqNDEyMzw6RyA4YCA0cDlBOylBaCJAcTBIYEA4MF1GGlBQMENDRElNU01WTElTWVBIQFBIUFFSU0JXclNcZE11S1FiUFdwV15ma1xtdWBYYGF+VHBoUGVmZW53aHZ+bnR0dCA4gCBAgCBIkDBIgDRQgzFTkTBYoEBYkEBYoEBggEVhl1JpmEdmo0BlsExwolh2rFBwsG13hGBwkHB3hmB4oGB4sEBowFBwwFB40GB4wDuCNz/Rd0CGPEWDQk+cSFGUTFC8WVepe2CRWGOLYWSJdmuZaGejWmCwVmysZWu/YHmlZneucny8ckrVZ13TbED/QGrbdnTGaH7Lc3fWdl+In0yArUeCsF+pr3eBhnqGlmaAr2eDt26Kv3WFpHaMuWe8vFOZxlCE4F2nyF6w02SFwnCIwH6XyHyX02mlwWu2yW/DgmzRkHPegnHWmm3EtGDYpn/FvXrRr3XJy5dtNZBxN7t3MYdqUv8AAJCAYIS9fqaKcKCYcLSXaqCoULCwUIbFdZHHesiRKceWW9GWTs+lU9imWe63ef//AMDAUMDAcOrCaPTYa/bhXuDmcPnjYfjldvDwcIOGhY6RjoSTnpaWloqYqIGTs5CYq5emiJqhqZelt6CggKytrai7p729vYCYwJWnxJer0pqy2Z246KOuwai2yaW41KK74IrDhIPYgZLMiZDThJvWkpzblYTLtYrbu43qnZzivaTIiKHXiaXWlbXemKzXpq/VvbDIsLTeoLDXvaLim6fvsazwtbvhpbTvtY7ByYvL15DN25jV2avA36jXy6bZ17HD2bTaxbXe1qnuybrmw7fo1Miqic+4ica1kdKuiNm0h9jAiNjGk9DYgMDIoMLbpdDIoM3nr83ns9bst9zwvu3NjezHmuLVm/bPpvTauPDggProov/wsMXGxc3S0tnay9fY2MDO7sHQ58DQ8Mrp0NPtztfu1Nryw+X0xvTgwv3s3PD4wOjo6PHx8SH5BAMAAFoALAAAAADgABAAAAj/ALUIHEiwoMGDCBMqXMiwocOHECM6fHbm4KaLFwtg3CQx4a0uXELe6kiyZEE4JlOqXMkQzg6LGzViFKgqVBqSv7gkI2dtmrBgVGqxHJrwDQwiDN+8AbIjxsAhDlvBiUW0qsIdO24YRFSgAKJNXb1yVIWG1SoaWuKoXctWrdaBtnzpw3ePGrVo0KDNumJ1JawTA43CaMGC4Q4YhQWyETIQgOPHjwXCYbNCIGTIjS9rdmx5s+bOnjEbjHNmBgxWBTFlBLuJK6ZV/+h16CEh7b/buHPPe6sFly9z+fDZixatGbNlwhYRIiigufMBnhguWKBg+kHnArRgT7jhwSuSiQfi/2jVUNYKVX3TD9SaA0aNgonCsgb77fa8ULVtz9td70a9/v7xxoU5yiBjzTXOOEMHHbngMk4SBMFywAbZlXLAAtEtZMEDCcGyAQewaAELBxuEiNADG64UhAwwVBUaAAi9GGNoBrGigxaywAADeQPJpJFGiFTQzz/zrJKffv79l6SSAt0CDDnHVGMPM8y4oQYed2zxSy9WMEdCdtpxcMBCr2zwHXcbDLRBmgjxwMN0ojR0pnp0rnSjQCzaQBAiBhhQwCRdVSAOkUYSFMc/N8zzn5L15LANN5Bo0UU5xuxyjT0L9rEFFlhkcUU4SnhZ4QALkLEQCSQsxAEHA62akAVaXP+wAKwLSQNAnAixMUQcDUnF40IvihZsZFoMyxlBz8xwQw03wOCCAwRttAkmlAwDzzylHCnQofwxGs856PCzTiMD0rIFL9C0oYYuehiBxRJTjHOElwsIMIAAHkijUCknlLIQBhgMBDBConigRSnT+asQDwBcoFArM4D2mRaTVVbsZnV2ZEYOsbDCSiwuRKCnQBthYog74HSA32hE7sbfO+m0A6463AzYhR28tOHGGnTwkYcYTEQxThEEBUBAAAcHIICpCRFAAENKDyQA0geRcCYCCxisEAIMm2iQKzigxlArK9zEkIwHoW2Q2ngWVIYDERx0sjvsmAJmQdwuWg88MWv/Ygkk3GhxxTi26LLHF5yQMgYYYYxBCiejIFH0AVQHMMCYBBPAtEIBUK1F5wdJs8AFpD+gwAD6IrSKB7EAwANCQszwQsa0G6TDCx0MpEoDEUQAgUGDDGKCBgkgdOgNyN9ASt+XVHKIQLX8QkwdT3TijzzvjDGGPNh3EsJApQQwAYylCKA5QrE47XVCDAjgb/kKHCSCB6+U8gosp2t9kAce8HDA07W72LAkhjZjwWggz4gFVQaiwFis7yHcUtQ7vNEOTTRvG7yRQjmaoAJ4jOACJ+iECk6wgRS8QwWZgUwANleQARDgfy5cSCwy8JgMLLAgHCKIDwhQPIQgQCBkAIDC9QoyhCHgoCGs+MEqAlgSQTjxiVCMoiAkQcUqWvGKkrAN8kiRjW5YsBKF2M1AZqEIFHACHnOwQCrgkYpTWKAK7+AEExEiDREgIIda8MQB9hg/g2TgAP7yAQAAeZAhiI1GWviBEKAlwMukEGNpQ+TaaCTFSj4Ri5isYloWdYh9OIIRj8DGfnijhSmUAAUetIAFVqVKEJywTpIUCCxmGaFZPjAicmgRQ1jhgFDMsSOWtGQmM5mW5P1BHZEARCCSR0otQAEDnTjFKT6hAhV8QpqfAMwvaxe7X23TKsGs5DAxWRAK+KER2lgIKjBwgnZ+wAkqQEE7tRAQADs=")
}

.x-html-editor-tb .x-edit-justifyleft, .x-menu-item div.x-edit-justifyleft {
    background-position: -112px 0;
    background-image: url("data:image/gif;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")
}

.x-html-editor-tb .x-edit-justifycenter, .x-menu-item div.x-edit-justifycenter {
    background-position: -128px 0;
    background-image: url("data:image/gif;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")
}

.x-html-editor-tb .x-edit-justifyright, .x-menu-item div.x-edit-justifyright {
    background-position: -144px 0;
    background-image: url("data:image/gif;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")
}

.x-html-editor-tb .x-edit-insertorderedlist, .x-menu-item div.x-edit-insertorderedlist {
    background-position: -80px 0;
    background-image: url("data:image/gif;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")
}

.x-html-editor-tb .x-edit-insertunorderedlist, .x-menu-item div.x-edit-insertunorderedlist {
    background-position: -96px 0;
    background-image: url("data:image/gif;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")
}

.x-html-editor-tb .x-edit-increasefontsize, .x-menu-item div.x-edit-increasefontsize {
    background-position: -48px 0;
    background-image: url("data:image/gif;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")
}

.x-html-editor-tb .x-edit-decreasefontsize, .x-menu-item div.x-edit-decreasefontsize {
    background-position: -64px 0;
    background-image: url("data:image/gif;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")
}

.x-html-editor-tb .x-edit-sourceedit, .x-menu-item div.x-edit-sourceedit {
    background-position: -192px 0;
    background-image: url("data:image/gif;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")
}

.x-html-editor-tb .x-edit-createlink, .x-menu-item div.x-edit-createlink {
    background-position: -208px 0;
    background-image: url("data:image/gif;R0lGODlh4AAQAIcAAAAAABAIEBATEBsjHSAYICAgEDA0ECEkIy80OjAoIDAqNDEyMzw6RyA4YCA0cDlBOylBaCJAcTBIYEA4MF1GGlBQMENDRElNU01WTElTWVBIQFBIUFFSU0JXclNcZE11S1FiUFdwV15ma1xtdWBYYGF+VHBoUGVmZW53aHZ+bnR0dCA4gCBAgCBIkDBIgDRQgzFTkTBYoEBYkEBYoEBggEVhl1JpmEdmo0BlsExwolh2rFBwsG13hGBwkHB3hmB4oGB4sEBowFBwwFB40GB4wDuCNz/Rd0CGPEWDQk+cSFGUTFC8WVepe2CRWGOLYWSJdmuZaGejWmCwVmysZWu/YHmlZneucny8ckrVZ13TbED/QGrbdnTGaH7Lc3fWdl+In0yArUeCsF+pr3eBhnqGlmaAr2eDt26Kv3WFpHaMuWe8vFOZxlCE4F2nyF6w02SFwnCIwH6XyHyX02mlwWu2yW/DgmzRkHPegnHWmm3EtGDYpn/FvXrRr3XJy5dtNZBxN7t3MYdqUv8AAJCAYIS9fqaKcKCYcLSXaqCoULCwUIbFdZHHesiRKceWW9GWTs+lU9imWe63ef//AMDAUMDAcOrCaPTYa/bhXuDmcPnjYfjldvDwcIOGhY6RjoSTnpaWloqYqIGTs5CYq5emiJqhqZelt6CggKytrai7p729vYCYwJWnxJer0pqy2Z246KOuwai2yaW41KK74IrDhIPYgZLMiZDThJvWkpzblYTLtYrbu43qnZzivaTIiKHXiaXWlbXemKzXpq/VvbDIsLTeoLDXvaLim6fvsazwtbvhpbTvtY7ByYvL15DN25jV2avA36jXy6bZ17HD2bTaxbXe1qnuybrmw7fo1Miqic+4ica1kdKuiNm0h9jAiNjGk9DYgMDIoMLbpdDIoM3nr83ns9bst9zwvu3NjezHmuLVm/bPpvTauPDggProov/wsMXGxc3S0tnay9fY2MDO7sHQ58DQ8Mrp0NPtztfu1Nryw+X0xvTgwv3s3PD4wOjo6PHx8SH5BAMAAFoALAAAAADgABAAAAj/ALUIHEiwoMGDCBMqXMiwocOHECM6fHbm4KaLFwtg3CQx4a0uXELe6kiyZEE4JlOqXMkQzg6LGzViFKgqVBqSv7gkI2dtmrBgVGqxHJrwDQwiDN+8AbIjxsAhDlvBiUW0qsIdO24YRFSgAKJNXb1yVIWG1SoaWuKoXctWrdaBtnzpw3ePGrVo0KDNumJ1JawTA43CaMGC4Q4YhQWyETIQgOPHjwXCYbNCIGTIjS9rdmx5s+bOnjEbjHNmBgxWBTFlBLuJK6ZV/+h16CEh7b/buHPPe6sFly9z+fDZixatGbNlwhYRIiigufMBnhguWKBg+kHnArRgT7jhwSuSiQfi/2jVUNYKVX3TD9SaA0aNgonCsgb77fa8ULVtz9td70a9/v7xxoU5yiBjzTXOOEMHHbngMk4SBMFywAbZlXLAAtEtZMEDCcGyAQewaAELBxuEiNADG64UhAwwVBUaAAi9GGNoBrGigxaywAADeQPJpJFGiFTQzz/zrJKffv79l6SSAt0CDDnHVGMPM8y4oQYed2zxSy9WMEdCdtpxcMBCr2zwHXcbDLRBmgjxwMN0ojR0pnp0rnSjQCzaQBAiBhhQwCRdVSAOkUYSFMc/N8zzn5L15LANN5Bo0UU5xuxyjT0L9rEFFlhkcUU4SnhZ4QALkLEQCSQsxAEHA62akAVaXP+wAKwLSQNAnAixMUQcDUnF40IvihZsZFoMyxlBz8xwQw03wOCCAwRttAkmlAwDzzylHCnQofwxGs856PCzTiMD0rIFL9C0oYYuehiBxRJTjHOElwsIMIAAHkijUCknlLIQBhgMBDBConigRSnT+asQDwBcoFArM4D2mRaTVVbsZnV2ZEYOsbDCSiwuRKCnQBthYog74HSA32hE7sbfO+m0A6463AzYhR28tOHGGnTwkYcYTEQxThEEBUBAAAcHIICpCRFAAENKDyQA0geRcCYCCxisEAIMm2iQKzigxlArK9zEkIwHoW2Q2ngWVIYDERx0sjvsmAJmQdwuWg88MWv/Ygkk3GhxxTi26LLHF5yQMgYYYYxBCiejIFH0AVQHMMCYBBPAtEIBUK1F5wdJs8AFpD+gwAD6IrSKB7EAwANCQszwQsa0G6TDCx0MpEoDEUQAgUGDDGKCBgkgdOgNyN9ASt+XVHKIQLX8QkwdT3TijzzvjDGGPNh3EsJApQQwAYylCKA5QrE47XVCDAjgb/kKHCSCB6+U8gosp2t9kAce8HDA07W72LAkhjZjwWggz4gFVQaiwFis7yHcUtQ7vNEOTTRvG7yRQjmaoAJ4jOACJ+iECk6wgRS8QwWZgUwANleQARDgfy5cSCwy8JgMLLAgHCKIDwhQPIQgQCBkAIDC9QoyhCHgoCGs+MEqAlgSQTjxiVCMoiAkQcUqWvGKkrAN8kiRjW5YsBKF2M1AZqEIFHACHnOwQCrgkYpTWKAK7+AEExEiDREgIIda8MQB9hg/g2TgAP7yAQAAeZAhiI1GWviBEKAlwMukEGNpQ+TaaCTFSj4Ri5isYloWdYh9OIIRj8DGfnijhSmUAAUetIAFVqVKEJywTpIUCCxmGaFZPjAicmgRQ1jhgFDMsSOWtGQmM5mW5P1BHZEARCCSR0otQAEDnTjFKT6hAhV8QpqfAMwvaxe7X23TKsGs5DAxWRAK+KER2lgIKjBwgnZ+wAkqQEE7tRAQADs=")
}

.x-html-editor-tip .x-tip-bd .x-tip-bd-inner {
    padding: 5px;
    padding-bottom: 1px
}

.x-html-editor-tb .x-font-select {
    font-size: 11px;
    font-family: inherit
}

.x-html-editor-wrap textarea {
    font: normal 12px tahoma, arial, verdana, sans-serif;
    background-color: #fff;
    resize: none
}

.x-form-text-default.x-tagfield {
    padding: 2px 0 0 4px
}

.x-form-text-default .x-tagfield-input {
    margin: 0 4px 2px 0
}

.x-form-text-default .x-tagfield-input-field {
    height: 16px;
    line-height: 16px
}

.x-form-text-default .x-tagfield-item {
    -webkit-border-radius: 3px;
    -moz-border-radius: 3px;
    -ms-border-radius: 3px;
    -o-border-radius: 3px;
    border-radius: 3px;
    background-color: #dfe9f6;
    border: 1px solid #99bce8;
    padding: 0 18px 0 5px;
    margin: 0 4px 2px 0;
    color: #000;
    line-height: 14px
}

.x-form-text-default .x-tagfield-item:hover {
    background-color: #afc9e9;
    border-color: #679bdd;
    color: #000
}

.x-form-text-default .x-tagfield-item.x-tagfield-item-selected {
    background-color: #6f96c7;
    border-color: #2d6cbb;
    color: #fff
}

.x-form-text-default .x-tagfield-item-close {
    width: 11px;
    height: 11px;
    top: 1px;
    right: 1px;
    background-image: url("data:image/gif;R0lGODlhIQAWAMQAAAAAAP///1R6r1uAs2KGuGiLvG+RwI2y45m76Mfb88/k+9bp/tLn/Pv9//T6/+Hz//D5/+j2//f8/////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAABMALAAAAAAhABYAAAX/4DQhZImIolmio3qmQSwHLzLL9R2f9pNAwMSD1vsFh6SADwgREhsJgwEiTTRIUCnVYMVGp9UrQhIpmM0RCYl8RqvH5Xaa5Hg8CHi7g27HE/R8d3kPewgPCgOJiQoPJIeKi42GiJCMjgcCAgyZB5IPmJqcnqCbAp2OCwcLq6qeqauvrqqsC40jdrh2Nbm4u7y2KS4sLi/BKsPCKMTIxzA6Oc/ONzxKRk1IRUxOSUtHT19bXQhZYFxi5OFibHJv62dzcG0F8HWCf4SBfoAI9fr4k5AGWAJYyRMlRQM/ZSp1yhApUZcWQjT0ipYsWK1QzYrF4xcwQ7988Sq2TFkyYyZEAoQAADs=")
}

.x-form-text-default .x-tagfield-item-close:hover {
    background-position: -11px 0
}

.x-form-text-default .x-tagfield-item-close:active {
    background-position: -22px 0
}

.x-form-text-default .x-tagfield-item-selected .x-tagfield-item-close {
    background-position: 0 -11px
}

.x-form-text-default .x-tagfield-item-selected .x-tagfield-item-close:hover {
    background-position: -11px -11px
}

.x-form-text-default .x-tagfield-item-selected .x-tagfield-item-close:active {
    background-position: -22px -11px
}

.x-form-text-toolbar.x-tagfield {
    padding: 0 3px 0
}

.x-form-text-toolbar .x-tagfield-input {
    margin: 1px 4px 1px 0
}

.x-form-text-toolbar .x-tagfield-input-field {
    height: 16px;
    line-height: 16px
}

.x-form-text-toolbar .x-tagfield-item {
    -webkit-border-radius: 3px;
    -moz-border-radius: 3px;
    -ms-border-radius: 3px;
    -o-border-radius: 3px;
    border-radius: 3px;
    background-color: #dfe9f6;
    border: 1px solid #99bce8;
    padding: 0 18px 0 5px;
    margin: 1px 4px 1px 0;
    color: #000;
    line-height: 14px
}

.x-form-text-toolbar .x-tagfield-item:hover {
    background-color: #afc9e9;
    border-color: #679bdd;
    color: #000
}

.x-form-text-toolbar .x-tagfield-item.x-tagfield-item-selected {
    background-color: #6f96c7;
    border-color: #2d6cbb;
    color: #fff
}

.x-form-text-toolbar .x-tagfield-item-close {
    width: 11px;
    height: 11px;
    top: 1px;
    right: 1px;
    background-image: url("data:image/gif;R0lGODlhIQAWAMQAAAAAAP///1R6r1uAs2KGuGiLvG+RwI2y45m76Mfb88/k+9bp/tLn/Pv9//T6/+Hz//D5/+j2//f8/////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAABMALAAAAAAhABYAAAX/4DQhZImIolmio3qmQSwHLzLL9R2f9pNAwMSD1vsFh6SADwgREhsJgwEiTTRIUCnVYMVGp9UrQhIpmM0RCYl8RqvH5Xaa5Hg8CHi7g27HE/R8d3kPewgPCgOJiQoPJIeKi42GiJCMjgcCAgyZB5IPmJqcnqCbAp2OCwcLq6qeqauvrqqsC40jdrh2Nbm4u7y2KS4sLi/BKsPCKMTIxzA6Oc/ONzxKRk1IRUxOSUtHT19bXQhZYFxi5OFibHJv62dzcG0F8HWCf4SBfoAI9fr4k5AGWAJYyRMlRQM/ZSp1yhApUZcWQjT0ipYsWK1QzYrF4xcwQ7988Sq2TFkyYyZEAoQAADs=")
}

.x-form-text-toolbar .x-tagfield-item-close:hover {
    background-position: -11px 0
}

.x-form-text-toolbar .x-tagfield-item-close:active {
    background-position: -22px 0
}

.x-form-text-toolbar .x-tagfield-item-selected .x-tagfield-item-close {
    background-position: 0 -11px
}

.x-form-text-toolbar .x-tagfield-item-selected .x-tagfield-item-close:hover {
    background-position: -11px -11px
}

.x-form-text-toolbar .x-tagfield-item-selected .x-tagfield-item-close:active {
    background-position: -22px -11px
}

.x-grid-view, .x-tree-view {
    z-index: 1
}

.x-grid-body {
    background: #fff;
    border-width: 1px;
    border-style: solid;
    border-color: #99bce8
}

.x-grid-empty {
    padding: 10px;
    color: grey;
    background-color: #fff;
    font: normal 11px tahoma, arial, verdana, sans-serif
}

.x-grid-item {
    color: #000;
    font: normal 11px/13px tahoma, arial, verdana, sans-serif;
    background-color: #fff
}

.x-grid-item-alt {
    background-color: #fafafa
}

.x-grid-item-over {
    color: #000;
    background-color: #efefef
}

.x-grid-item-focused {
    outline: 0;
    color: #000
}

.x-grid-item-focused .x-grid-cell-inner {
    z-index: 1
}

.x-grid-item-focused .x-grid-cell-inner:before {
    content: "";
    position: absolute;
    z-index: -1;
    top: 0px;
    right: 0px;
    bottom: 0px;
    left: 0px;
    pointer-events: none;
    border: 1px dotted #464646
}

.x-grid-item-selected {
    color: #000;
    background-color: #dfe8f6
}

.x-grid-with-row-lines .x-grid-item {
    border-style: solid;
    border-width: 1px 0 0;
    border-color: #ededed
}

.x-grid-with-row-lines .x-grid-item:first-child {
    border-top-color: #fff
}

.x-grid-with-row-lines .x-grid-item.x-grid-item-over {
    border-style: solid;
    border-color: #ddd
}

.x-grid-with-row-lines .x-grid-item-over + .x-grid-item {
    border-top-style: solid;
    border-top-color: #ddd
}

.x-grid-with-row-lines .x-grid-item.x-grid-item-selected {
    border-style: dotted;
    border-color: #a3bae9
}

.x-grid-with-row-lines .x-grid-item-selected + .x-grid-item {
    border-top-style: dotted;
    border-top-color: #a3bae9
}

.x-grid-with-row-lines .x-grid-item:last-child {
    border-bottom-width: 1px
}

.x-ie8 .x-grid-with-row-lines .x-grid-item {
    border-width: 1px 0;
    margin-top: -1px
}

.x-ie8 .x-grid-with-row-lines .x-grid-item:first-child {
    margin-top: 0
}

.x-grid-cell-inner {
    position: relative;
    text-overflow: ellipsis;
    padding: 3px 6px 4px
}

.x-grid-cell-special {
    border-color: #d0d0d0;
    border-style: solid;
    border-right-width: 1px;
    background-image: none;
    background-color: #f6f6f6;
    background-image: -webkit-gradient(linear, top, bottom, color-stop(0%, #f6f6f6), color-stop(0%, #e9e9e9));
    background-image: -webkit-linear-gradient(top, #f6f6f6, #e9e9e9);
    background-image: -moz-linear-gradient(top, #f6f6f6, #e9e9e9);
    background-image: -o-linear-gradient(top, #f6f6f6, #e9e9e9);
    background-image: -ms-linear-gradient(top, #f6f6f6, #e9e9e9);
    background-image: linear-gradient(top, #f6f6f6, #e9e9e9)
}

.x-grid-item-selected .x-grid-cell-special {
    border-right-color: #aaccf6;
    background-image: none;
    background-color: #dfe8f6;
    background-image: -webkit-gradient(linear, top, bottom, color-stop(0%, #dfe8f6), color-stop(0%, #cbdaf0));
    background-image: -webkit-linear-gradient(left, #dfe8f6, #cbdaf0);
    background-image: -moz-linear-gradient(left, #dfe8f6, #cbdaf0);
    background-image: -o-linear-gradient(left, #dfe8f6, #cbdaf0);
    background-image: -ms-linear-gradient(left, #dfe8f6, #cbdaf0);
    background-image: linear-gradient(left, #dfe8f6, #cbdaf0)
}

.x-nlg .x-grid-cell-special {
    background-repeat: repeat-y;
    background-image: url("data:image/gif;R0lGODlhNwMBAPf/AOjo6Orq6vT09PLy8vDw8O7u7uzs7P///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////yH5BAEAAAcALAAAAAA3AwEAh+jo6Orq6vT09PLy8vDw8O7u7uzs7P///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////whBAAUIFDig4AACCAsoLGDAQICHACJKnEixosWLGDNq3Mixo8ePIEOKHEmypMmTKFOqXMmypcuXMGPKnEmzps2SAQEAOw==")
}

.x-nlg .x-grid-item-selected .x-grid-cell-special {
    background-image: url("data:image/gif;R0lGODlhNwMBAPf/AMra8NDe8N7m9Nzm9Nrk9Njk9Nji9Nbi8tTg8tLe8sza8NDc8M7c8P///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////yH5BAEAAA0ALAAAAAA3AwEAh8ra8NDe8N7m9Nzm9Nrk9Njk9Nji9Nbi8tTg8tLe8sza8NDc8M7c8P///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////whFAAUIGECQAIECBg4oRIAgQYCHDBgoUACgosWLGDNq3Mixo8ePIEOKHEmypMmTKFOqXMmypcuXMGPKnEmzps2bOHPqRBkQADs=")
}

.x-grid-cell-special .x-cmd-slicer.x-grid-cell-special:before {
    display: none;
    content: "x-slicer:, bg:url("data:image/gif;R0lGODlhNwMBAPf/AOjo6Orq6vT09PLy8vDw8O7u7uzs7P///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////yH5BAEAAAcALAAAAAA3AwEAh+jo6Orq6vT09PLy8vDw8O7u7uzs7P///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////whBAAUIFDig4AACCAsoLGDAQICHACJKnEixosWLGDNq3Mixo8ePIEOKHEmypMmTKFOqXMmypcuXMGPKnEmzps2SAQEAOw==")" !important
}

.x-grid-cell-special .x-cmd-slicer.x-grid-cell-special-selected:before {
    display: none;
    content: "x-slicer:, bg:url("data:image/gif;R0lGODlhNwMBAPf/AMra8NDe8N7m9Nzm9Nrk9Njk9Nji9Nbi8tTg8tLe8sza8NDc8M7c8P///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////yH5BAEAAA0ALAAAAAA3AwEAh8ra8NDe8N7m9Nzm9Nrk9Njk9Nji9Nbi8tTg8tLe8sza8NDc8M7c8P///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////whFAAUIGECQAIECBg4oRIAgQYCHDBgoUACgosWLGDNq3Mixo8ePIEOKHEmypMmTKFOqXMmypcuXMGPKnEmzps2bOHPqRBkQADs=")" !important
}

.x-grid-dirty-cell {
    background: url("data:image/gif;R0lGODlhCgAKAIcAAMAAAP///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAMAAAEALAAAAAAKAAoAAAgdAAEIFBigYMGBAAwaHKhwYcKGByFKnEixosWJAQEAOw==") no-repeat 0 0
}

.x-grid-row .x-grid-cell-selected {
    color: #000;
    background-color: #b8cfee
}

.x-grid-with-col-lines .x-grid-cell {
    border-style: solid;
    border-color: #d0d0d0;
    border-width: 0 1px 0 0
}

.x-grid-with-col-lines .x-grid-item-over .x-grid-cell {
    border-color: #ddd;
    border-style: solid
}

.x-grid-with-col-lines .x-grid-item-selected .x-grid-cell {
    border-color: #a3bae9;
    border-style: dotted
}

.x-grid-resize-marker {
    width: 1px;
    background-color: #0f0f0f
}

.x-grid-drop-indicator {
    position: absolute;
    height: 1px;
    line-height: 0px;
    background-color: #77bc71;
    overflow: visible;
    pointer-events: none
}

.x-grid-drop-indicator .x-grid-drop-indicator-left {
    position: absolute;
    top: -8px;
    left: -12px;
    background-image: url("data:image/gif;iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABGdBTUEAAK/INwWK6QAAABl0RVh0U29mdHdhcmUAQWRvYmUgSW1hZ2VSZWFkeXHJZTwAAADvSURBVDjLY/z//z8DJYCJgUIwxAwImOWx22uSExvZBvz68cvm5/dfV5HFGEGxUHoiExwVf//8Zfjz+w/D719/GH79/A3UAMK/GH4CMYiWFJJk+PXrN8PN27cunWq/oA/SwwIzyUrYluHvP6AB//7A8e+/f4H4N8Pvf0D8Fyb2h+HLl696WllqJ69Nu2XOArMZpBCuGajoN1jxbwT9FyH36/dvkCt/w10Acvb+h3uxOhvoZzCbi4OLQVJSiuH1q9cMt2/cvXB7zj0beBgQAwwKtS2AFuwH2vwIqFmd5Fi40H/1BFDzQaBrdTFiYYTnBQAI58A33Wys0AAAAABJRU5ErkJggg==");
    height: 16px;
    width: 16px
}

.x-grid-drop-indicator .x-grid-drop-indicator-right {
    position: absolute;
    top: -8px;
    right: -11px;
    background-image: url("data:image/gif;iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABGdBTUEAAK/INwWK6QAAABl0RVh0U29mdHdhcmUAQWRvYmUgSW1hZ2VSZWFkeXHJZTwAAADrSURBVDjLY/z//z8DJYCJgUIwyAwoPZHJBsS7STGABY1/9e+fvzKkGMAIiwWgzRfF2ST0/vz5w/Dw/UOGXz9/M/z6AcK/GH4CMZj+jmCD5C70X2VkgWo+KcYqrqfArcTw598fBhluOTD9++9fIP7N8PsfEP/9AxUD0b8ZVq9ci/AC0Nm//zD+Yfj19xdY0R+got9gxb8RNNQAkNyf/0CxX39QvZC5M+68MJuIAQczJ8PDlw8ZXr9/g9XZIK+BNP/5/Yfh/sJHjIzIKTF2VchNoEI5oAbHDWk7TpAcjUDNukDNB4nVjOKFEZwXAOOhu7x6WtPJAAAAAElFTkSuQmCC");
    height: 16px;
    width: 16px
}

.x-col-move-top, .x-col-move-bottom {
    width: 9px;
    height: 9px
}

.x-col-move-top {
    background-image: url("data:image/gif;R0lGODlhCQAJAIcAADBQoDBYoDBYsEBgsEBosEBowFBwwFB4wFB40FB44AD/AFCA4FCI4FCI8GCI0GCQ8GCQ/3CQ4HCY4HCY8HCg8HCg/4Co/4Cw/5Cw/5C4/6DA/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAMAAAoALAAAAAAJAAkAAAhCABUooCAhggMHAgVK0JABg4GECiJosPCAAEQHFyA0GCCQYASKCwAMsHhgQgUGCAoASChgQQKVEBUIKBAgpkABEAMCADs=")
}

.x-col-move-bottom {
    background-image: url("data:image/gif;R0lGODlhCQAJAIcAACBIkCBIoCBQoDBQoDBYoDBYsDBo0EBwwEBw0EB40FB40AD/AFCA0FCA4GCI4GCQ8GCY8HCY4HCg8HCg/4Co8JCw/6DA/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAMAAAsALAAAAAAJAAkAAAhBABcIXBBhoEEJFggYXICwgoMBAyNYqDDhQQKIERAYqAABQgEBAAQ2sADBgQCDDSg4UBAApQMGB0IObDAAgE2BAQEAOw==")
}

.x-grid-header-ct {
    border: 1px solid #99bce8;
    border-bottom-color: #c5c5c5;
    background-color: #c5c5c5;
    background-image: none;
    background-color: #c5c5c5;
    background-image: -webkit-gradient(linear, top, bottom, color-stop(0%, #f9f9f9), color-stop(0%, #e6e3e3));
    background-image: -webkit-linear-gradient(top, #f9f9f9, #e6e3e3);
    background-image: -moz-linear-gradient(top, #f9f9f9, #e6e3e3);
    background-image: -o-linear-gradient(top, #f9f9f9, #e6e3e3);
    background-image: -ms-linear-gradient(top, #f9f9f9, #e6e3e3);
    background-image: linear-gradient(top, #f9f9f9, #e6e3e3)
}

.x-accordion-item .x-grid-header-ct {
    border-width: 0 0 1px !important
}

.x-grid-header-ct-hidden {
    border-top: 0 !important;
    border-bottom: 0 !important
}

.x-grid-body {
    border-top-color: #c5c5c5
}

.x-hmenu-sort-asc {
    background-image: url("data:image/gif;R0lGODlhEAAQAPcAAAAAACkxOTE5SnM5KUJSY1Jje1prezFSlDFalDlalEprlEJrtUprtVJ7rVJzvVp7vVJzxlJ7xnuMpXOMtXOUvXuUtWOExnuU1oQxIYQ5KZQ5OYxCOZRCQpRKUpRSWpxjY5xja5xzc6Vze5xrhJx7lKV7hKWEnLWEnK2MpbWUrbWcrbWttZSlxpStxgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAP8ALAAAAAAQABAAAAh+AP8JhCCwYMECBv9dWMAi4T8WACoYjOAggUMBAAIYZPDvQEKIAABMEPjAAYUEDQwakBCRgECOAj0mBFDQAoIW/xIcUDDToU+BNAuaIIGCBAgVPQuWEOhhg8OgBk9gWPHUYYcPPqEKHOE0q8EUHJD+E5FUoIYBIT5kCFH258+AADs=")
}

.x-hmenu-sort-desc {
    background-image: url("data:image/gif;R0lGODlhEAAQAPcAAAAAAAD/ACkxOTE5SjFCczFKhDlKezlSe0JSY0JapUpajEpjpVJje1JrnFJzrVpre1pztWN7tWuMvXM5KXOMtXuMpXuUtYQxIYQ5KYxCOYycxpQ5OZRCOZRCQpRKUpRSWpSlxpStxpStzpxjY5xja5xrhJxzc5x7lJy11qVze6V7hKV7lKWEnK2Mpa3G57WEnLWUrbWcrbWttbXG572lrb3G1r3W98bG3s7O3s7e79be9////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////yH5BAEAAAEALAAAAAAQABAAAAh/AAOwONHiBIkYARImBKAwgIqEHzI0XDgxwIsLMioynOhhRMUAGxWWkPgxZAAYHRAGSDHR5IYJJkZgMNHyo02TCheUrCghgQaNFR00MNDwQQUAFhA01EmgYQgAUCkohNCAgoEGDQcAELBUYVOFIJAqjFAARAADBBQ0ZGCzbcKAAAA7")
}

.x-cols-icon {
    background-image: url("data:image/gif;R0lGODlhEAAQAIcAAFFxqVFyqVNzqVNzqlR1q1R1rFZ2rVd5rlh6sFh7sVp8slx+tFx+tUB240D/QF6Bt1+DuWCFumGFu2OHvWSIvlaG5WaLwGiOw2ySyGyUyW6Uym+Wy2+XzHCRwXCZznKaz3Oc0XOd0nWe1Hag1Xmi2Hmj2Xqk2nqk23qm3Hun3JGRkZWVlZ6enrCwsLq6ur6+voCex4yhxoat3ZK03pK56LbD28DAwMLCwsbGxsjIyMrKyszMzN3d3dji9v///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAA4ALAAAAAAQABAAAAifAB0IHEiwoMGDBGvMSIHCBIkRIkJ88LAhQwYYNWTQ2MixY8cOKUKKHEnSwgkfKEv0WLmyBEqUE1zu0KGygs0eJVrwaOAjAomXKlni9NGA54MRPnLgqHmzRFGeDEQAFTq0qA8FIHzcsMG0Ak4WO30g4DBVqMuXBTT4eOGiK84VKlT4GIChLMuzKAPEuGCBggQICxQkOGCAgAABAGIgRBgQADs=")
}

.x-column-header {
    border-right: 1px solid #c5c5c5;
    color: #000;
    font: normal 11px/13px tahoma, arial, verdana, sans-serif;
    outline: 0;
    background-image: none;
    background-color: #c5c5c5;
    background-image: -webkit-gradient(linear, top, bottom, color-stop(0%, #f9f9f9), color-stop(0%, #e6e3e3));
    background-image: -webkit-linear-gradient(top, #f9f9f9, #e6e3e3);
    background-image: -moz-linear-gradient(top, #f9f9f9, #e6e3e3);
    background-image: -o-linear-gradient(top, #f9f9f9, #e6e3e3);
    background-image: -ms-linear-gradient(top, #f9f9f9, #e6e3e3);
    background-image: linear-gradient(top, #f9f9f9, #e6e3e3)
}

.x-group-sub-header {
    background: transparent;
    border-top: 1px solid #c5c5c5
}

.x-group-sub-header .x-column-header-inner {
    padding: 3px 6px 5px 6px
}

.x-column-header-inner {
    padding: 4px 6px 5px
}

.x-column-header-inner-empty {
    text-overflow: clip
}

.x-column-header.x-column-header-focus {
    color: #000
}

.x-column-header.x-column-header-focus .x-column-header-inner:after {
    content: "";
    position: absolute;
    z-index: 5;
    top: 0px;
    right: 0px;
    bottom: 0px;
    left: 0px;
    border: 1px dotted #333;
    pointer-events: none
}

.x-column-header.x-column-header-focus.x-group-sub-header .x-column-header-inner:before {
    bottom: 0px
}

.x-column-header-over {
    background-image: none;
    background-color: #aaccf6;
    background-image: -webkit-gradient(linear, top, bottom, color-stop(0%, #ebf3fd), color-stop(39%, #ebf3fd), color-stop(40%, #d9e8fb), color-stop(0%, #d9e8fb));
    background-image: -webkit-linear-gradient(top, #ebf3fd, #ebf3fd 39%, #d9e8fb 40%, #d9e8fb);
    background-image: -moz-linear-gradient(top, #ebf3fd, #ebf3fd 39%, #d9e8fb 40%, #d9e8fb);
    background-image: -o-linear-gradient(top, #ebf3fd, #ebf3fd 39%, #d9e8fb 40%, #d9e8fb);
    background-image: -ms-linear-gradient(top, #ebf3fd, #ebf3fd 39%, #d9e8fb 40%, #d9e8fb);
    background-image: linear-gradient(top, #ebf3fd, #ebf3fd 39%, #d9e8fb 40%, #d9e8fb)
}

.x-column-header-sort-ASC, .x-column-header-sort-DESC {
    background-image: none;
    background-color: #aaccf6;
    background-image: -webkit-gradient(linear, top, bottom, color-stop(0%, #ebf3fd), color-stop(39%, #ebf3fd), color-stop(40%, #d9e8fb), color-stop(0%, #d9e8fb));
    background-image: -webkit-linear-gradient(top, #ebf3fd, #ebf3fd 39%, #d9e8fb 40%, #d9e8fb);
    background-image: -moz-linear-gradient(top, #ebf3fd, #ebf3fd 39%, #d9e8fb 40%, #d9e8fb);
    background-image: -o-linear-gradient(top, #ebf3fd, #ebf3fd 39%, #d9e8fb 40%, #d9e8fb);
    background-image: -ms-linear-gradient(top, #ebf3fd, #ebf3fd 39%, #d9e8fb 40%, #d9e8fb);
    background-image: linear-gradient(top, #ebf3fd, #ebf3fd 39%, #d9e8fb 40%, #d9e8fb)
}

.x-nlg .x-grid-header-ct, .x-nlg .x-column-header {
    background-image: url("data:image/gif;R0lGODlhAQAgA/QAAObk5Ofl5ejl5enn5+rn5+vp6ezp6ezr6+3r6+7t7e/t7fDv7/Hv7/Lx8fPx8fPz8/Tz8/X19fb19ff39/j39/n5+f///+bk5Obk5Obk5Obk5Obk5Obk5Obk5Obk5Obk5CH5BAEAABYALAAAAAABACADRAhIACs0KACgoMGDCBMqXMiwocOHEBNGSBAgosWLGDNinPBgwYEBGkOKHEmypMmTFilIgOCAgQIEBggIQEmzps2bOHPq3Mmzp8+AADs=")
}

.x-nlg .x-column-header-over, .x-nlg .x-column-header-sort-ASC, .x-nlg .x-column-header-sort-DESC {
    background-image: url("data:image/gif;R0lGODlhAQAgA/EAANno++vz/f///9no+yH5BAEAAAIALAAAAAABACADQQg5AAMEAECwoMGDCBMqXMiwocOHCQdCnEixokWLAi9q3Mixo8ePIDEKlBiypMmTKFOqXMmypcuXBgMCADs=")
}

.x-column-header-open {
    background-color: transparent
}

.x-column-header-open .x-column-header-trigger {
    background-color: transparent
}

.x-column-header-over .x-column-header-trigger, .x-column-header-open .x-column-header-trigger {
    width: 14px;
    cursor: pointer;
    background: transparent url("data:image/gif;R0lGODlhHAAyAIcAABU7hCJFh8Pa+cXf/8fg/8vi/8rm/83j/8zn/9Dm/9Dq/9Po/9Lr/9bp/9bu/9jq/9rs/97t/9jw/9zx/9/z/+Dw/+Py/+H1/+bz/+X2/+f5/+n1/+v2/+v7/+78//H///T//////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAAAAP8ALAAAAAAcADIAAAj/AAWE4ECwoEGCAkEoXMhQocCDEDkkbEjxYUSDEykytHgRYQiNDTl2zAgShMiLJEGejJhS40qILSsO7Oix5MKXB2OGnElT50aeIz/aNAkUpVCbODEeLZm0oM+bRVkuVRkV5lSXVXNelbmhq9evXQV+GEu27FiBGNKqXZtWoIe3cOO+FWihrt27dQV22Mu3716BFQILHhxYoIbDiBMfFhghQojHkEM0jiAwQ4bIkC1nEAghRIDPoAOEgABB4IUQAFKrBhDiwgWBDx54Dh0i9gOBFCigXh0iNwWBDYLPFh08uMAJyHezRo5c4ILnCzyHgP5coITrElCHwH5dYILv30OAqgcv0IF58yHOnxd4oL379+0FMphPv/58gQXy69+fX6CC/wAG+J9ABBRo4IEFCoTAggw2uKBAA0Qo4YQRCmTAhRhmeCGEFHZooYYgctjhhB+CmKGII1YYgokaophiiSwa4OKIMLI4o4crxrhhCCmSmKOON1JYo4lB+qjjjj1KOGSIPCY5wJItNpkklCdK2SOVGBap5I8xaqnikTJa+SKXNopJI5lEmokjmAEBADs=") no-repeat 0 center
}

.x-column-header-align-right .x-column-header-text {
    margin-right: 9px
}

.x-column-header-sort-ASC .x-column-header-text-inner, .x-column-header-sort-DESC .x-column-header-text-inner {
    padding-right: 12px;
    background-position: right center
}

.x-column-header-sort-ASC .x-column-header-text-inner {
    background-image: url("data:image/gif;R0lGODlhCQAFAKEDAGGQzUD/QOPu+////yH5BAEKAAMALAAAAAAJAAUAAAIMnAenwIrcDJxD2HsLADs=")
}

.x-column-header-sort-DESC .x-column-header-text-inner {
    background-image: url("data:image/gif;R0lGODlhCQAFAKEDAGGQzUD/QOPu+////yH5BAEKAAMALAAAAAAJAAUAAAIMFI4gY7nD0INxUnYLADs=")
}

.x-no-header-borders .x-column-header {
    border: 0 none
}

.x-no-header-borders .x-column-header .x-column-header-inner {
    padding-top: 4px
}

.x-cmd-slicer.x-column-header:before {
    display: none;
    content: "x-slicer:, bg:url("data:image/gif;R0lGODlhAQAgA/QAAObk5Ofl5ejl5enn5+rn5+vp6ezp6ezr6+3r6+7t7e/t7fDv7/Hv7/Lx8fPx8fPz8/Tz8/X19fb19ff39/j39/n5+f///+bk5Obk5Obk5Obk5Obk5Obk5Obk5Obk5Obk5CH5BAEAABYALAAAAAABACADRAhIACs0KACgoMGDCBMqXMiwocOHEBNGSBAgosWLGDNinPBgwYEBGkOKHEmypMmTFilIgOCAgQIEBggIQEmzps2bOHPq3Mmzp8+AADs="), stretch:bottom" !important
}

.x-cmd-slicer.x-column-header-over:before {
    display: none;
    content: "x-slicer:, bg:url("data:image/gif;R0lGODlhAQAgA/EAANno++vz/f///9no+yH5BAEAAAIALAAAAAABACADQQg5AAMEAECwoMGDCBMqXMiwocOHCQdCnEixokWLAi9q3Mixo8ePIDEKlBiypMmTKFOqXMmypcuXBgMCADs="), stretch:bottom" !important
}

.x-grid-cell-inner-action-col {
    padding: 2px 2px 2px 2px
}

.x-grid-no-row-lines .x-grid-row-focused .x-grid-cell-inner-action-col {
    padding-top: 1px;
    padding-bottom: 1px
}

.x-action-col-cell .x-item-disabled {
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=30)";
    opacity: 0.3
}

.x-action-col-icon {
    color: gray;
    font-size: 16px;
    height: 16px;
    width: 16px;
    cursor: pointer
}

.x-column-header-checkbox .x-column-header-inner, .x-grid-checkcolumn-cell-inner {
    padding: 4px 4px 3px 4px;
    text-overflow: clip
}

.x-grid-no-row-lines .x-grid-row-focused .x-column-header-checkbox .x-column-header-inner, .x-grid-no-row-lines .x-grid-row-focused .x-grid-checkcolumn-cell-inner {
    padding-top: 3px;
    padding-bottom: 2px
}

.x-column-header-checkbox {
    border-color: #c5c5c5
}

.x-column-header-checkbox .x-column-header-text {
    overflow: visible
}

.x-column-header-checkbox .x-column-header-checkbox:after, .x-grid-checkcolumn:after {
    content: " ";
    height: 13px;
    width: 13px;
    background-image: url("data:image/gif;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");
    display: inline-block
}

.x-item-disabled .x-column-header-checkbox .x-column-header-checkbox, .x-item-disabled .x-grid-checkcolumn {
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=30)";
    opacity: 0.3
}

.x-grid-hd-checker-on .x-column-header-checkbox:after, .x-grid-checkcolumn-checked:after {
    background-position: 0 -13px
}

.x-grid-item-selected .x-selmodel-column .x-grid-checkcolumn:after {
    background-position: 0 -13px
}

.x-grid-cell-row-numberer {
    background-image: none;
    background-color: #c5c5c5;
    background-image: -webkit-gradient(linear, top, bottom, color-stop(0%, #f9f9f9), color-stop(0%, #e6e3e3));
    background-image: -webkit-linear-gradient(top, #f9f9f9, #e6e3e3);
    background-image: -moz-linear-gradient(top, #f9f9f9, #e6e3e3);
    background-image: -o-linear-gradient(top, #f9f9f9, #e6e3e3);
    background-image: -ms-linear-gradient(top, #f9f9f9, #e6e3e3);
    background-image: linear-gradient(top, #f9f9f9, #e6e3e3)
}

.x-grid-cell-inner-row-numberer {
    padding: 3px 5px 4px 3px
}

.x-form-text-field-body-grid-cell {
    min-width: 150px;
    max-width: 150px
}

.x-form-text-wrap-grid-cell {
    border-width: 1px;
    border-style: solid;
    border-color: #b5b8c8
}

.x-form-text-wrap-grid-cell.x-form-text-wrap-focus {
    border-color: #7eadd9
}

.x-form-text-wrap-grid-cell.x-form-text-wrap-invalid {
    border-color: #c30
}

.x-form-text-grid-cell {
    color: #000;
    padding: 1px 5px 2px 5px;
    background-color: #fff;
    background-image: url("data:image/gif;R0lGODlhAQASAIcAAN7j5vDz8/P19fX39/f5+fn7+/z8/f3+/v///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAAAAP8ALAAAAAABABIAAAgQAAEEEDCAQAEDBxAoXMgwIAA7");
    font: normal 11px/15px tahoma, arial, verdana, sans-serif;
    min-height: 18px
}

.x-ie8 .x-form-text-grid-cell {
    min-height: 15px
}

.x-form-text-grid-cell.x-form-textarea {
    line-height: 14px;
    min-height: 56px
}

.x-ie8 .x-form-text-grid-cell.x-form-textarea {
    min-height: 53px
}

.x-form-text-grid-cell.x-form-text-file {
    color: grey
}

.x-placeholder-label-grid-cell {
    padding: 1px 5px 2px 5px
}

.x-form-empty-field-grid-cell + .x-placeholder-label-grid-cell {
    color: grey
}

.x-form-text-grid-cell:-ms-input-placeholder {
    color: grey
}

.x-form-invalid-field-grid-cell {
    background-color: #fff;
    background-image: url("data:image/gif;R0lGODlhBAADAIcAAAD/AP8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAAAALAAAAAAEAAMAAAgMAAMAGAhAoMCCAAICADs=");
    background-repeat: repeat-x;
    background-position: bottom
}

.x-form-trigger-grid-cell {
    width: 17px;
    background: 0 0 transparent url("data:image/gif;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") no-repeat;
    border-width: 0 0 1px;
    border-color: #b5b8c8;
    border-style: solid
}

.x-form-trigger-grid-cell.x-form-trigger-over {
    background-position: -17px 0
}

.x-form-trigger-grid-cell.x-form-trigger-over.x-form-trigger-focus {
    background-position: -68px 0
}

.x-form-trigger-grid-cell.x-form-trigger-focus {
    background-position: -51px 0
}

.x-form-trigger.x-form-trigger-grid-cell.x-form-trigger-click {
    background-position: -34px 0
}

.x-textfield-grid-cell-cell > .x-grid-cell-inner {
    padding-top: 0px;
    padding-bottom: 0px
}

.x-form-text-grid-cell.x-tagfield {
    padding: 0 3px 0
}

.x-form-text-grid-cell .x-tagfield-input {
    margin: 1px 4px 1px 0
}

.x-form-text-grid-cell .x-tagfield-input-field {
    height: 16px;
    line-height: 16px
}

.x-form-text-grid-cell .x-tagfield-item {
    -webkit-border-radius: 3px;
    -moz-border-radius: 3px;
    -ms-border-radius: 3px;
    -o-border-radius: 3px;
    border-radius: 3px;
    background-color: #dfe9f6;
    border: 1px solid #99bce8;
    padding: 0 18px 0 5px;
    margin: 1px 4px 1px 0;
    color: #000;
    line-height: 14px
}

.x-form-text-grid-cell .x-tagfield-item:hover {
    background-color: #afc9e9;
    border-color: #679bdd;
    color: #000
}

.x-form-text-grid-cell .x-tagfield-item.x-tagfield-item-selected {
    background-color: #6f96c7;
    border-color: #2d6cbb;
    color: #fff
}

.x-form-text-grid-cell .x-tagfield-item-close {
    width: 11px;
    height: 11px;
    top: 1px;
    right: 1px;
    background-image: url("data:image/gif;R0lGODlhIQAWAMQAAAAAAP///1R6r1uAs2KGuGiLvG+RwI2y45m76Mfb88/k+9bp/tLn/Pv9//T6/+Hz//D5/+j2//f8/////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAABMALAAAAAAhABYAAAX/4DQhZImIolmio3qmQSwHLzLL9R2f9pNAwMSD1vsFh6SADwgREhsJgwEiTTRIUCnVYMVGp9UrQhIpmM0RCYl8RqvH5Xaa5Hg8CHi7g27HE/R8d3kPewgPCgOJiQoPJIeKi42GiJCMjgcCAgyZB5IPmJqcnqCbAp2OCwcLq6qeqauvrqqsC40jdrh2Nbm4u7y2KS4sLi/BKsPCKMTIxzA6Oc/ONzxKRk1IRUxOSUtHT19bXQhZYFxi5OFibHJv62dzcG0F8HWCf4SBfoAI9fr4k5AGWAJYyRMlRQM/ZSp1yhApUZcWQjT0ipYsWK1QzYrF4xcwQ7988Sq2TFkyYyZEAoQAADs=")
}

.x-form-text-grid-cell .x-tagfield-item-close:hover {
    background-position: -11px 0
}

.x-form-text-grid-cell .x-tagfield-item-close:active {
    background-position: -22px 0
}

.x-form-text-grid-cell .x-tagfield-item-selected .x-tagfield-item-close {
    background-position: 0 -11px
}

.x-form-text-grid-cell .x-tagfield-item-selected .x-tagfield-item-close:hover {
    background-position: -11px -11px
}

.x-form-text-grid-cell .x-tagfield-item-selected .x-tagfield-item-close:active {
    background-position: -22px -11px
}

.x-form-trigger-spinner-grid-cell {
    width: 17px;
    border: 0
}

.x-form-spinner-grid-cell {
    background-image: url("data:image/gif;R0lGODlhZgAUAMQAADFQi36s2YCu2bS4x7W4yLnP57vQ573R6Mrb5cve9M7e6M/g9NDe6NLh6dLh8tja39rm89/0/+L0/+f4/+n3/+n5/u3t7e3w8e/v8PDw8PH1+fX4+/v8/QAAAAAAAAAAACH5BAkAAB0ALAAAAABmABQAAAX/ICGOZEl0QaqubIC2Qpu+skzX7I2rHef/wOBjECwCDwGEctm4NJZLQ8BIRVKNSKiyoXlqpZmwOMMZh30Eh3oN0UDWal8S2tgANl5oAK5uv+FyFYKDFRyEgnJadXd5SwFmZABlkGlwEHYbf2scc1t2AIxae5aYmnEBh4WSqZx0n6F6FrIWkaBlsxYclX2vmYCdi6CgeHqkwr6bARPLE6q2FcwTrZ7Cw40Bs7XCt7K6bK/DmtPBksd5ow6X1XfiARLvFBzrHBTvEuOv8taOstr6khm6EUiQwEG+Yw4I4uNArA7DcwQNbkOo0N27fxjtLWy44SE/Wj8ugPSBQWDEjhsS/xpkmDDBNAQKYi6JqUDPSZYFUbbkFCHCPR8SfP4IGuGlAgY1ldCMhatpU10EC6qJuiaqUaQzZTqiOjViV5cW7Ykde6/T0aQwtSoJYKItiR1w48qdS3eH07smvbaUuvellr9rue6tWpGs4YudAP/FhtcpVL2CrZpVu3Qr5MtgDxs2SlktAsZkfIgMzaFkroE5ca5MWTEr2sqBU7NevTNAz58cguImevW1Z9AYtwU8vWCBRFsIi2984pDY2uLHyw1zoDxscFsa5zRnjvJctn+2hp/+tg6ZA3wT960lX808J3vOtlXITg25+s9mMObfla6XqZfk3PeZMeH8cghGBwIDDmQsa0EizyRm8NcfO3z4RY5zjvChjnmnsLJKgq6YIwokZDjojYZuVOgXAotgmCGKppzHSSqFsLJii42sdUURDxCwYxAFJLZFF38F+SMQRh7pQ5B/cZEjAkG6JWVdNcRA5ZVYshACADs=");
    background-color: #fff;
    width: 17px;
    height: 10px
}

.x-form-spinner-up-grid-cell {
    background-position: 0 0
}

.x-form-spinner-up-grid-cell.x-form-spinner-over {
    background-position: -17px 0
}

.x-form-spinner-up-grid-cell.x-form-spinner-over.x-form-spinner-focus {
    background-position: -68px 0
}

.x-form-spinner-up-grid-cell.x-form-spinner-focus {
    background-position: -51px 0
}

.x-form-spinner-up-grid-cell.x-form-spinner.x-form-spinner-click {
    background-position: -34px 0
}

.x-form-spinner-down-grid-cell {
    background-position: 0 -10px
}

.x-form-spinner-down-grid-cell.x-form-spinner-over {
    background-position: -17px -10px
}

.x-form-spinner-down-grid-cell.x-form-spinner-over.x-form-spinner-focus {
    background-position: -68px -10px
}

.x-form-spinner-down-grid-cell.x-form-spinner-focus {
    background-position: -51px -10px
}

.x-form-spinner-down-grid-cell.x-form-spinner.x-form-spinner-click {
    background-position: -34px -10px
}

.x-form-cb-wrap-grid-cell {
    height: 20px;
    min-width: 13px
}

.x-form-cb-grid-cell {
    margin-top: 4px
}

.x-form-checkbox-grid-cell, .x-form-radio-grid-cell {
    width: 13px;
    height: 13px
}

.x-form-radio-grid-cell {
    background: url("data:image/gif;R0lGODlhMwAaAOeuAA02WQ0+XRUyRxYySBc0ShgzRxgzSBg0ShE4WB0+Vx0+WBRAXB5AWg1DZxVGZCBAWCREXTBLXyVGYCZIYi5KYDZRZjVSaEZkekhjeAdUgwlWhA9ZhA9fjRZdhBRijRlljS5iijNjiEZshkptiFFxiTyEqQ+Dxw6ExheKxxiY0Q2g8xKi8h2q8x6+/yKPxiCd0Sii0Sqw8ijE/zLK/1iEnkCFrEeLrkqLsUyQt1aFoVeUt1KYvFqbvWWFmGqGl2mGmH2NmGuduWyauX6lvF2ixmOfx2ajzGyhwGmrznqlwXKx1nSz2HW12nq/5V3O3WnC1H/m7nT//4qLi4uMjIWTn4mXoo6apI+cppGaopejrJihppmjq6Kioqawuam0vK64v7S5vrm6uoCqw4yvxY6zyY+3yJGyxpG4yZi3ypy6zLu+wpzC0J7E3IPL+ZLM7ZjK5JDV5ZnT75TU+pXZ/JnW+pzZ+aDH3r3Bxb7DyanS6a/a7aTc+qzd/bfX6r3d5bHb8bbd87Hf/bve8b7g77Th/L7h87zl/L3o+7H2+sPDw8fHx8DFycXIzMjLzs3NzcnO087R1dDQ0NTU1NTW2dbZ3Nra2tzc3Nze4cfj7sHk9sHo/Mns/M/x+tHt/d/o9tP0+tbx/dj09tnx/dv2+N34+uHh4eXl5enp6evs7O/v8OP1/un3/vHx8fT09P///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////yH5BAEKAP8ALAAAAAAzABoAAAj+AP8J5DKl4BQuAhMK1OIjRw4fWhQmxEICBAgSWCQKlMRRUiRJEqWEqcSKVaUwUiT2KONn1Cg/ZXpIHCGETaFCbISMkBjJ1CmfqExFSiglESpGYMA0QpUopcAeaz7VadOmzqc1MgWKSCKVqtUkIhJG+mnKZ9lTQ7mEOQXmzqNHjO6gCoNQSxlObeTw4UOnDacyEbEI+ZN3b19AQjJKKuvzFKrHPyVJscQIzyNIlC5xtJTShx86dAIFImRozx4/Pv6RYANaNGnTbEj8G9v4cSpUjiNNYQUG0iRLjSOxmvIvx6g2ow1pWk5nVI5/IAohJ71cE51CIP5JOuXYdsnHknb+q6FU6lSq85ZSETfehtByUKJEBQpFA7p095rgyxcUQjt3VOeVxMpt4Vnim3mttIKbJcT94Ecde2wCiiqqiLKJHz+oZgeEElJooR2yRYJbKgK2wgqAkaiFiiOlpGIiKqzQ9Y8WZ3AihyGiVNjJKGcEJgQgN+YoSieZJDYbUAIOGBRIRbFSik8uNpUQVJ8cokknoJCCVUJbVXlllmCJ9d93uA0lkEiVJGgJSiqd4QcppPhxRlZc1pRJJjmFpVBPAJ4nlEQEFSQFQhox5BBEGv1DkUUYJeoRRx8lKumklFZqaaAFESqRoQ9FpNGiF2WkUSSNlNqImUSNVNJJTk3Jkkv+MNEpEE024aSTRIpUgkqCqFSiCFFGqUEFFXJJ+VRUbhRRhBtX0bkVIErccMMSgIQpkCKnsHJKKeVp+6tap1QhAQYVPGDFXHXdZcQEF1jAgBF/+fjHDRJcUIECOCCWUSQklfJRJCyaFMlkakBghiZPLJCAI5z945kbEKSxChQOKBAHaqqxocQDQ8xhAwIKNBHbP0uhZUoqpTjiyGON7AZEBHA4AQMKBlwxXHGj8BABIlHMwIIBRzhnXw0UEFHCBxsIoAN2JLdiyVilVFIJi620zAoVBbjwQgonGJCFejjzYEAMMrSwggFJ0De0AB14wIEGAwTBX9MpSy11wC1bskiwAgGYYEIAD1jC4D8OuqGAAyuo0IACg2CoIRMKAKBBBgAokAeI/yiSyikq371yKoqouEUCBxyQwBcx1lUjEgqUrkAaPPoIyA4JEEBAAmYUuW+/KqtsSiuVDNWkJF14cUkrxv5DpR5koIGJls4mUcgbYozRRybWZp5tUCe3csqvZ46kJpsK9eAmnHLK+o8IduIphJ4J5bqrgr4CatCgiXKK6KcVhZooqaZClaUGSEBLBQQAOw==") no-repeat
}

.x-form-cb-checked .x-form-radio-grid-cell {
    background-position: 0 -13px
}

.x-form-checkbox-grid-cell {
    background: url("data:image/gif;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") no-repeat
}

.x-form-cb-checked .x-form-checkbox-grid-cell {
    background-position: 0 -13px
}

.x-form-checkbox-focus.x-form-radio-grid-cell {
    background-position: -13px 0
}

.x-form-cb-checked .x-form-checkbox-focus.x-form-radio-grid-cell {
    background-position: -13px -13px
}

.x-form-checkbox-focus.x-form-checkbox-grid-cell {
    background-position: -13px 0
}

.x-form-cb-checked .x-form-checkbox-focus.x-form-checkbox-grid-cell {
    background-position: -13px -13px
}

.x-form-cb-label-grid-cell {
    margin-top: 3px;
    font: normal 12px/14px tahoma, arial, verdana, sans-serif;
    color: #000
}

.x-form-cb-label-grid-cell.x-form-cb-label-before {
    padding-right: 17px
}

.x-form-cb-label-grid-cell.x-form-cb-label-after {
    padding-left: 17px
}

.x-checkbox-grid-cell-cell > .x-grid-cell-inner {
    padding-top: 0px;
    padding-bottom: 0px
}

.x-btn-grid-cell-small {
    -webkit-border-radius: 3px;
    -moz-border-radius: 3px;
    -ms-border-radius: 3px;
    -o-border-radius: 3px;
    border-radius: 3px;
    padding: 2px 2px 2px 2px;
    border-width: 1px;
    border-style: solid;
    background-image: none;
    background-color: #fff;
    background-image: -webkit-gradient(linear, top, bottom, color-stop(0%, #fff), color-stop(48%, #f9f9f9), color-stop(52%, #e2e2e2), color-stop(0%, #e7e7e7));
    background-image: -webkit-linear-gradient(top, #fff, #f9f9f9 48%, #e2e2e2 52%, #e7e7e7);
    background-image: -moz-linear-gradient(top, #fff, #f9f9f9 48%, #e2e2e2 52%, #e7e7e7);
    background-image: -o-linear-gradient(top, #fff, #f9f9f9 48%, #e2e2e2 52%, #e7e7e7);
    background-image: -ms-linear-gradient(top, #fff, #f9f9f9 48%, #e2e2e2 52%, #e7e7e7);
    background-image: linear-gradient(top, #fff, #f9f9f9 48%, #e2e2e2 52%, #e7e7e7)
}

.x-btn-grid-cell-small-mc {
    background-image: url(images/btn/btn-grid-cell-small-fbg.gif);
    background-position: 0 top;
    background-color: #fff
}

.x-nbr .x-btn-grid-cell-small {
    padding: 0 !important;
    border-width: 0 !important;
    -webkit-border-radius: 0px;
    -moz-border-radius: 0px;
    -ms-border-radius: 0px;
    -o-border-radius: 0px;
    border-radius: 0px;
    background-color: transparent !important;
    background-image: none;
    box-shadow: none !important
}

.x-btn-grid-cell-small-frameInfo {
    font-family: th-3-3-3-3-1-1-1-1-2-2-2-2
}

.x-btn-grid-cell-small-tl {
    background-position: 0 -6px
}

.x-btn-grid-cell-small-tr {
    background-position: right -9px
}

.x-btn-grid-cell-small-bl {
    background-position: 0 -12px
}

.x-btn-grid-cell-small-br {
    background-position: right -15px
}

.x-btn-grid-cell-small-ml {
    background-position: 0 top
}

.x-btn-grid-cell-small-mr {
    background-position: right top
}

.x-btn-grid-cell-small-tc {
    background-position: 0 0
}

.x-btn-grid-cell-small-bc {
    background-position: 0 -3px
}

.x-btn-grid-cell-small-tr, .x-btn-grid-cell-small-br, .x-btn-grid-cell-small-mr {
    padding-right: 3px
}

.x-btn-grid-cell-small-tl, .x-btn-grid-cell-small-bl, .x-btn-grid-cell-small-ml {
    padding-left: 3px
}

.x-btn-grid-cell-small-tc {
    height: 3px
}

.x-btn-grid-cell-small-bc {
    height: 3px
}

.x-btn-grid-cell-small-tl, .x-btn-grid-cell-small-bl, .x-btn-grid-cell-small-tr, .x-btn-grid-cell-small-br, .x-btn-grid-cell-small-tc, .x-btn-grid-cell-small-bc, .x-btn-grid-cell-small-ml, .x-btn-grid-cell-small-mr {
    background-image: url(images/btn/btn-grid-cell-small-corners.gif)
}

.x-btn-grid-cell-small-ml, .x-btn-grid-cell-small-mr {
    background-image: url(images/btn/btn-grid-cell-small-sides.gif)
}

.x-btn-grid-cell-small-mc {
    padding: 0px 0px 0px 0px
}

.x-cmd-slicer.x-btn-grid-cell-small:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, frame-bg:url(images/btn/btn-grid-cell-small-fbg.gif), corners:url(images/btn/btn-grid-cell-small-corners.gif), sides:url(images/btn/btn-grid-cell-small-sides.gif)" !important
}

.x-btn-grid-cell-small {
    border-color: #d1d1d1
}

.x-btn-button-grid-cell-small {
    min-height: 12px
}

.x-ie9m .x-btn-button-grid-cell-small {
    min-height: auto;
    height: 12px
}

.x-btn-inner-grid-cell-small {
    font: normal 11px/12px tahoma, arial, verdana, sans-serif;
    color: #333;
    padding: 0 4px;
    max-width: 100%
}

.x-btn-icon-right > .x-btn-inner-grid-cell-small, .x-btn-icon-left > .x-btn-inner-grid-cell-small {
    max-width: calc(100% - 12px)
}

.x-ie10p .x-btn-inner-grid-cell-small {
    max-width: none
}

.x-btn-icon-el-grid-cell-small {
    font-size: 12px;
    height: 12px;
    color: #333;
    line-height: 12px
}

.x-btn-icon-left > .x-btn-icon-el-grid-cell-small, .x-btn-icon-right > .x-btn-icon-el-grid-cell-small {
    width: 12px
}

.x-btn-icon-top > .x-btn-icon-el-grid-cell-small, .x-btn-icon-bottom > .x-btn-icon-el-grid-cell-small {
    min-width: 12px
}

.x-btn-icon-el-grid-cell-small.x-btn-glyph {
    opacity: 0.5
}

.x-ie8 .x-btn-icon-el-grid-cell-small.x-btn-glyph {
    color: #999
}

.x-btn-text.x-btn-icon-left > .x-btn-icon-el-grid-cell-small {
    margin-right: 0px
}

.x-btn-text.x-btn-icon-right > .x-btn-icon-el-grid-cell-small {
    margin-left: 0px
}

.x-btn-text.x-btn-icon-top > .x-btn-icon-el-grid-cell-small {
    margin-bottom: 4px
}

.x-btn-text.x-btn-icon-bottom > .x-btn-icon-el-grid-cell-small {
    margin-top: 4px
}

.x-btn-arrow-right > .x-btn-icon.x-btn-no-text.x-btn-button-grid-cell-small {
    padding-right: 4px
}

.x-btn-arrow-right > .x-btn-text.x-btn-icon-right > .x-btn-icon-el-grid-cell-small {
    margin-right: 4px
}

.x-btn-arrow-bottom > .x-btn-button-grid-cell-small, .x-btn-split-bottom > .x-btn-button-grid-cell-small {
    padding-bottom: 2px
}

.x-btn-wrap-grid-cell-small.x-btn-arrow-right:after {
    width: 8px;
    background-image: url("data:image/gif;R0lGODlhCgAKAIcAAAAAAP///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAAEALAAAAAAKAAoAAAgZAAMIHEiwoMGDCA0CWLhQYcODABJKnFgwIAA7");
    padding-right: 8px
}

.x-btn-wrap-grid-cell-small.x-btn-arrow-bottom:after {
    height: 8px;
    background-image: url("data:image/gif;R0lGODlhCgAKAIcAAAAAAP///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAAEALAAAAAAKAAoAAAgZAAMIHEiwoMGDCA0CWLhQYcODABJKnFgwIAA7")
}

.x-btn-wrap-grid-cell-small.x-btn-split-right:after {
    width: 14px;
    background-image: url("data:image/gif;R0lGODlhDgBIAMIEAAAAAMnJycLa9vX19f///////////////yH5BAEKAAIALAAAAAAOAEgAAANcGCPczupJEaerFq6sefdYFlrjVErnk14btzbv57YiTdomjuoqz3oUH0woqwFjwSMxCVoinzSAVDp8TH/WnnLb5M68xq74Ow6Tz+b0Dbwut9FvdY49d9fhd/kOmAAAOw==");
    padding-right: 14px
}

.x-btn-wrap-grid-cell-small.x-btn-split-bottom:after {
    height: 14px;
    background-image: url("data:image/gif;R0lGODlhyAAOAMIDAAAAAMTExMLa9v///////////////////yH5BAEKAAIALAAAAADIAA4AAANdGLrc/jDKSau9OOsth/9gKI5kaZ5oqq5s676mIM90bd94ru987//AoHBILBqPyKRyyWw6n9CodEqtWq/YrHbL7XqBgHD4Sy6bZeKzeq0FsN/wuHxOr9vv+Lx+v04AADs=")
}

.x-btn-over > .x-btn-wrap-grid-cell-small.x-btn-split-right:after {
    background-image: url("data:image/gif;R0lGODlhDgBIAMIEAAAAAKrI8cLa9tru/////////////////yH5BAEKAAIALAAAAAAOAEgAAANcGCPczupJEaerFq6sefdYFlrjVErnk14btzbv57YiTdomjuoqz3oUH0woqwFjwSMxCVoinzSAVDp8TH/WnnLb5M68xq74Ow6Tz+b0Dbwut9FvdY49d9fhd/kOmAAAOw==")
}

.x-btn-over > .x-btn-wrap-grid-cell-small.x-btn-split-bottom:after {
    background-image: url("data:image/gif;R0lGODlhyAAOAKEDAAAAAKrI8e/4/////yH5BAEKAAMALAAAAADIAA4AAAJbjI+py+0Po5y02uuE3rz7D4biSJbmiabqKg7uC8fyTNf2jef6zvf+DwwKh8Si8YhMKpfMpvMJjUqn1Kr1is1qeYBudwsOi13esflsBaDX7Lb7DY/L5/S6/X4uAAA7")
}

.x-btn-split-right > .x-btn-icon.x-btn-no-text.x-btn-button-grid-cell-small {
    padding-right: 4px
}

.x-btn-split-right > .x-btn-text.x-btn-icon-right > .x-btn-icon-el-grid-cell-small {
    margin-right: 4px
}

.x-btn-focus.x-btn-grid-cell-small {
    border-color: #ebebeb;
    background-image: none;
    background-color: #fff;
    background-image: -webkit-gradient(linear, top, bottom, color-stop(0%, #fff), color-stop(48%, #f9f9f9), color-stop(52%, #e7e7e7), color-stop(0%, #ececec));
    background-image: -webkit-linear-gradient(top, #fff, #f9f9f9 48%, #e7e7e7 52%, #ececec);
    background-image: -moz-linear-gradient(top, #fff, #f9f9f9 48%, #e7e7e7 52%, #ececec);
    background-image: -o-linear-gradient(top, #fff, #f9f9f9 48%, #e7e7e7 52%, #ececec);
    background-image: -ms-linear-gradient(top, #fff, #f9f9f9 48%, #e7e7e7 52%, #ececec);
    background-image: linear-gradient(top, #fff, #f9f9f9 48%, #e7e7e7 52%, #ececec)
}

.x-btn-focus.x-btn-grid-cell-small .x-btn-wrap {
    outline: 1px dotted #333
}

.x-btn-grid-cell-small .x-btn-arrow-el {
    position: absolute;
    top: 0;
    right: 0;
    height: 100%;
    width: 16px;
    pointer-events: none
}

.x-btn-over.x-btn-grid-cell-small {
    border-color: #ebebeb;
    background-image: none;
    background-color: #fff;
    background-image: -webkit-gradient(linear, top, bottom, color-stop(0%, #fff), color-stop(48%, #f9f9f9), color-stop(52%, #e7e7e7), color-stop(0%, #ececec));
    background-image: -webkit-linear-gradient(top, #fff, #f9f9f9 48%, #e7e7e7 52%, #ececec);
    background-image: -moz-linear-gradient(top, #fff, #f9f9f9 48%, #e7e7e7 52%, #ececec);
    background-image: -o-linear-gradient(top, #fff, #f9f9f9 48%, #e7e7e7 52%, #ececec);
    background-image: -ms-linear-gradient(top, #fff, #f9f9f9 48%, #e7e7e7 52%, #ececec);
    background-image: linear-gradient(top, #fff, #f9f9f9 48%, #e7e7e7 52%, #ececec)
}

.x-btn.x-btn-menu-active.x-btn-grid-cell-small, .x-btn.x-btn-pressed.x-btn-grid-cell-small {
    border-color: #b8b8b8;
    background-image: none;
    background-color: #e6e6e6;
    background-image: -webkit-gradient(linear, top, bottom, color-stop(0%, #e6e6e6), color-stop(48%, #ebebeb), color-stop(52%, #e8cbcb), color-stop(0%, #ebd3d3));
    background-image: -webkit-linear-gradient(top, #e6e6e6, #ebebeb 48%, #e8cbcb 52%, #ebd3d3);
    background-image: -moz-linear-gradient(top, #e6e6e6, #ebebeb 48%, #e8cbcb 52%, #ebd3d3);
    background-image: -o-linear-gradient(top, #e6e6e6, #ebebeb 48%, #e8cbcb 52%, #ebd3d3);
    background-image: -ms-linear-gradient(top, #e6e6e6, #ebebeb 48%, #e8cbcb 52%, #ebd3d3);
    background-image: linear-gradient(top, #e6e6e6, #ebebeb 48%, #e8cbcb 52%, #ebd3d3)
}

.x-btn.x-btn-disabled.x-btn-grid-cell-small {
    border-color: #fff;
    background-image: none;
    background-color: #fff;
    background-image: -webkit-gradient(linear, top, bottom, color-stop(0%, #fff), color-stop(48%, #f9f9f9), color-stop(52%, #e2e2e2), color-stop(0%, #e7e7e7));
    background-image: -webkit-linear-gradient(top, #fff, #f9f9f9 48%, #e2e2e2 52%, #e7e7e7);
    background-image: -moz-linear-gradient(top, #fff, #f9f9f9 48%, #e2e2e2 52%, #e7e7e7);
    background-image: -o-linear-gradient(top, #fff, #f9f9f9 48%, #e2e2e2 52%, #e7e7e7);
    background-image: -ms-linear-gradient(top, #fff, #f9f9f9 48%, #e2e2e2 52%, #e7e7e7);
    background-image: linear-gradient(top, #fff, #f9f9f9 48%, #e2e2e2 52%, #e7e7e7)
}

.x-btn-focus .x-btn-grid-cell-small-tl, .x-btn-focus .x-btn-grid-cell-small-bl, .x-btn-focus .x-btn-grid-cell-small-tr, .x-btn-focus .x-btn-grid-cell-small-br, .x-btn-focus .x-btn-grid-cell-small-tc, .x-btn-focus .x-btn-grid-cell-small-bc {
    background-image: url(images/btn/btn-grid-cell-small-focus-corners.gif)
}

.x-btn-focus .x-btn-grid-cell-small-ml, .x-btn-focus .x-btn-grid-cell-small-mr {
    background-image: url(images/btn/btn-grid-cell-small-focus-sides.gif)
}

.x-btn-focus .x-btn-grid-cell-small-mc {
    background-color: #fff;
    background-image: url(images/btn/btn-grid-cell-small-focus-fbg.gif)
}

.x-btn-over .x-btn-grid-cell-small-tl, .x-btn-over .x-btn-grid-cell-small-bl, .x-btn-over .x-btn-grid-cell-small-tr, .x-btn-over .x-btn-grid-cell-small-br, .x-btn-over .x-btn-grid-cell-small-tc, .x-btn-over .x-btn-grid-cell-small-bc {
    background-image: url(images/btn/btn-grid-cell-small-over-corners.gif)
}

.x-btn-over .x-btn-grid-cell-small-ml, .x-btn-over .x-btn-grid-cell-small-mr {
    background-image: url(images/btn/btn-grid-cell-small-over-sides.gif)
}

.x-btn-over .x-btn-grid-cell-small-mc {
    background-color: #fff;
    background-image: url(images/btn/btn-grid-cell-small-over-fbg.gif)
}

.x-btn-focus.x-btn-over .x-btn-grid-cell-small-tl, .x-btn-focus.x-btn-over .x-btn-grid-cell-small-bl, .x-btn-focus.x-btn-over .x-btn-grid-cell-small-tr, .x-btn-focus.x-btn-over .x-btn-grid-cell-small-br, .x-btn-focus.x-btn-over .x-btn-grid-cell-small-tc, .x-btn-focus.x-btn-over .x-btn-grid-cell-small-bc {
    background-image: url(images/btn/btn-grid-cell-small-focus-over-corners.gif)
}

.x-btn-focus.x-btn-over .x-btn-grid-cell-small-ml, .x-btn-focus.x-btn-over .x-btn-grid-cell-small-mr {
    background-image: url(images/btn/btn-grid-cell-small-focus-over-sides.gif)
}

.x-btn-focus.x-btn-over .x-btn-grid-cell-small-mc {
    background-color: #fff;
    background-image: url(images/btn/btn-grid-cell-small-focus-over-fbg.gif)
}

.x-btn.x-btn-menu-active .x-btn-grid-cell-small-tl, .x-btn.x-btn-menu-active .x-btn-grid-cell-small-bl, .x-btn.x-btn-menu-active .x-btn-grid-cell-small-tr, .x-btn.x-btn-menu-active .x-btn-grid-cell-small-br, .x-btn.x-btn-menu-active .x-btn-grid-cell-small-tc, .x-btn.x-btn-menu-active .x-btn-grid-cell-small-bc, .x-btn.x-btn-pressed .x-btn-grid-cell-small-tl, .x-btn.x-btn-pressed .x-btn-grid-cell-small-bl, .x-btn.x-btn-pressed .x-btn-grid-cell-small-tr, .x-btn.x-btn-pressed .x-btn-grid-cell-small-br, .x-btn.x-btn-pressed .x-btn-grid-cell-small-tc, .x-btn.x-btn-pressed .x-btn-grid-cell-small-bc {
    background-image: url(images/btn/btn-grid-cell-small-pressed-corners.gif)
}

.x-btn.x-btn-menu-active .x-btn-grid-cell-small-ml, .x-btn.x-btn-menu-active .x-btn-grid-cell-small-mr, .x-btn.x-btn-pressed .x-btn-grid-cell-small-ml, .x-btn.x-btn-pressed .x-btn-grid-cell-small-mr {
    background-image: url(images/btn/btn-grid-cell-small-pressed-sides.gif)
}

.x-btn.x-btn-menu-active .x-btn-grid-cell-small-mc, .x-btn.x-btn-pressed .x-btn-grid-cell-small-mc {
    background-color: #e6e6e6;
    background-image: url(images/btn/btn-grid-cell-small-pressed-fbg.gif)
}

.x-btn-focus.x-btn-menu-active .x-btn-grid-cell-small-tl, .x-btn-focus.x-btn-menu-active .x-btn-grid-cell-small-bl, .x-btn-focus.x-btn-menu-active .x-btn-grid-cell-small-tr, .x-btn-focus.x-btn-menu-active .x-btn-grid-cell-small-br, .x-btn-focus.x-btn-menu-active .x-btn-grid-cell-small-tc, .x-btn-focus.x-btn-menu-active .x-btn-grid-cell-small-bc, .x-btn-focus.x-btn-pressed .x-btn-grid-cell-small-tl, .x-btn-focus.x-btn-pressed .x-btn-grid-cell-small-bl, .x-btn-focus.x-btn-pressed .x-btn-grid-cell-small-tr, .x-btn-focus.x-btn-pressed .x-btn-grid-cell-small-br, .x-btn-focus.x-btn-pressed .x-btn-grid-cell-small-tc, .x-btn-focus.x-btn-pressed .x-btn-grid-cell-small-bc {
    background-image: url(images/btn/btn-grid-cell-small-focus-pressed-corners.gif)
}

.x-btn-focus.x-btn-menu-active .x-btn-grid-cell-small-ml, .x-btn-focus.x-btn-menu-active .x-btn-grid-cell-small-mr, .x-btn-focus.x-btn-pressed .x-btn-grid-cell-small-ml, .x-btn-focus.x-btn-pressed .x-btn-grid-cell-small-mr {
    background-image: url(images/btn/btn-grid-cell-small-focus-pressed-sides.gif)
}

.x-btn-focus.x-btn-menu-active .x-btn-grid-cell-small-mc, .x-btn-focus.x-btn-pressed .x-btn-grid-cell-small-mc {
    background-color: #e6e6e6;
    background-image: url(images/btn/btn-grid-cell-small-focus-pressed-fbg.gif)
}

.x-btn.x-btn-disabled .x-btn-grid-cell-small-tl, .x-btn.x-btn-disabled .x-btn-grid-cell-small-bl, .x-btn.x-btn-disabled .x-btn-grid-cell-small-tr, .x-btn.x-btn-disabled .x-btn-grid-cell-small-br, .x-btn.x-btn-disabled .x-btn-grid-cell-small-tc, .x-btn.x-btn-disabled .x-btn-grid-cell-small-bc {
    background-image: url(images/btn/btn-grid-cell-small-disabled-corners.gif)
}

.x-btn.x-btn-disabled .x-btn-grid-cell-small-ml, .x-btn.x-btn-disabled .x-btn-grid-cell-small-mr {
    background-image: url(images/btn/btn-grid-cell-small-disabled-sides.gif)
}

.x-btn.x-btn-disabled .x-btn-grid-cell-small-mc {
    background-color: #fff;
    background-image: url(images/btn/btn-grid-cell-small-disabled-fbg.gif)
}

.x-nbr .x-btn-grid-cell-small {
    background-image: none
}

.x-btn-disabled.x-btn-grid-cell-small .x-btn-inner, .x-btn-disabled.x-btn-grid-cell-small .x-btn-icon-el {
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=50)";
    opacity: 0.5
}

.x-nbr .x-segmented-button-item-horizontal.x-btn-grid-cell-small.x-segmented-button-first {
    border-right-width: 1px !important
}

.x-nbr .x-segmented-button-item-horizontal.x-btn-grid-cell-small.x-segmented-button-first .x-btn-grid-cell-small-mc {
    padding-right: 2px !important
}

.x-nbr .x-segmented-button-item-horizontal.x-btn-grid-cell-small.x-segmented-button-middle {
    border-right-width: 1px !important
}

.x-nbr .x-segmented-button-item-horizontal.x-btn-grid-cell-small.x-segmented-button-middle .x-btn-grid-cell-small-mc {
    padding-right: 2px !important;
    padding-left: 2px !important
}

.x-nbr .x-segmented-button-item-horizontal.x-btn-grid-cell-small.x-segmented-button-last .x-btn-grid-cell-small-mc {
    padding-left: 2px !important
}

.x-nbr .x-segmented-button-item-vertical.x-btn-grid-cell-small.x-segmented-button-first {
    border-bottom-width: 1px !important
}

.x-nbr .x-segmented-button-item-vertical.x-btn-grid-cell-small.x-segmented-button-first .x-btn-grid-cell-small-mc {
    padding-bottom: 2px !important
}

.x-nbr .x-segmented-button-item-vertical.x-btn-grid-cell-small.x-segmented-button-middle {
    border-bottom-width: 1px !important
}

.x-nbr .x-segmented-button-item-vertical.x-btn-grid-cell-small.x-segmented-button-middle .x-btn-grid-cell-small-mc {
    padding-top: 2px !important;
    padding-bottom: 2px !important
}

.x-nbr .x-segmented-button-item-vertical.x-btn-grid-cell-small.x-segmented-button-last .x-btn-grid-cell-small-mc {
    padding-top: 2px !important
}

.x-nbr .x-segmented-button-item.x-btn-grid-cell-small:after {
    content: ' ';
    border-style: solid;
    border-width: 0;
    position: absolute
}

.x-nbr .x-segmented-button-item-horizontal.x-btn-grid-cell-small:after {
    top: 1px;
    right: 0;
    bottom: 1px;
    left: 0
}

.x-nbr .x-segmented-button-item-horizontal.x-btn-grid-cell-small.x-segmented-button-first:after {
    left: 1px
}

.x-nbr .x-segmented-button-item-horizontal.x-btn-grid-cell-small.x-segmented-button-last:after {
    right: 1px
}

.x-nbr .x-segmented-button-item-vertical.x-btn-grid-cell-small:after {
    top: 0;
    right: 1px;
    bottom: 0;
    left: 1px
}

.x-nbr .x-segmented-button-item-vertical.x-btn-grid-cell-small.x-segmented-button-first:after {
    top: 1px
}

.x-nbr .x-segmented-button-item-vertical.x-btn-grid-cell-small.x-segmented-button-last:after {
    bottom: 1px
}

.x-cmd-slicer.x-btn-focus.x-btn-grid-cell-small:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url(images/btn/btn-grid-cell-small-focus-corners.gif), sides:url(images/btn/btn-grid-cell-small-focus-sides.gif), frame-bg:url(images/btn/btn-grid-cell-small-focus-fbg.gif)" !important
}

.x-cmd-slicer.x-btn-over.x-btn-grid-cell-small:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url(images/btn/btn-grid-cell-small-over-corners.gif), sides:url(images/btn/btn-grid-cell-small-over-sides.gif), frame-bg:url(images/btn/btn-grid-cell-small-over-fbg.gif)" !important
}

.x-cmd-slicer.x-btn-focus.x-btn-over.x-btn-grid-cell-small:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url(images/btn/btn-grid-cell-small-focus-over-corners.gif), sides:url(images/btn/btn-grid-cell-small-focus-over-sides.gif), frame-bg:url(images/btn/btn-grid-cell-small-focus-over-fbg.gif)" !important
}

.x-cmd-slicer.x-btn-pressed.x-btn-grid-cell-small:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url(images/btn/btn-grid-cell-small-pressed-corners.gif), sides:url(images/btn/btn-grid-cell-small-pressed-sides.gif), frame-bg:url(images/btn/btn-grid-cell-small-pressed-fbg.gif)" !important
}

.x-cmd-slicer.x-btn-focus.x-btn-pressed.x-btn-grid-cell-small:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url(images/btn/btn-grid-cell-small-focus-pressed-corners.gif), sides:url(images/btn/btn-grid-cell-small-focus-pressed-sides.gif), frame-bg:url(images/btn/btn-grid-cell-small-focus-pressed-fbg.gif)" !important
}

.x-cmd-slicer.x-btn-disabled.x-btn-grid-cell-small:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url(images/btn/btn-grid-cell-small-disabled-corners.gif), sides:url(images/btn/btn-grid-cell-small-disabled-sides.gif), frame-bg:url(images/btn/btn-grid-cell-small-disabled-fbg.gif)" !important
}

.x-button-grid-cell-small-cell > .x-grid-cell-inner {
    padding-top: 1px;
    padding-bottom: 1px
}

.x-button-grid-cell-small-cell > .x-grid-cell-inner > .x-btn-grid-cell-small {
    vertical-align: top
}

.x-grid-widgetcolumn-cell-inner {
    text-overflow: clip
}

.x-grid-group-hd {
    border-width: 0 0 2px 0;
    border-style: solid;
    border-color: #99bbe8;
    padding: 10px 4px 4px 4px;
    background: #fff;
    cursor: pointer
}

.x-grid-group-hd-not-collapsible {
    cursor: default
}

.x-grid-group-hd-collapsible .x-grid-group-title {
    padding: 0 0 0 14px;
    background: url("data:image/gif;R0lGODlhCQAJAPcAADFKY5SlvZylvZytxqW11qm92r3GxrXI48bS59Te8efv9+vz/////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACwAAAAACQAJAAAIQgATDBgoQECAAAYGMFi4cIECAAoZOjwAUaKCBAUACGAAoGPHjAEYOEyQAAEBAAFGljxwMoACBAcKEJgJwIDHmwYCAgA7") no-repeat left center
}

.x-grid-group-title {
    color: #3764a0;
    font: bold 11px/13px tahoma, arial, verdana, sans-serif
}

.x-grid-group-hd-collapsed .x-grid-group-title {
    background-image: url("data:image/gif;R0lGODlhCQAJAPcAADFKY5SlvZylvZytxqW11qm92r3GxrXI48bS59Te8efv9+vz/////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACwAAAAACQAJAAAIRQATDBgoQECAAAYGMFi4cIECAAoXAnCIACJDAAoSFAAggAGAjx83BmDgEEACBAQABHCYAACCAykDKHhZgIBNAAZA6jQQEAA7")
}

.x-group-by-icon {
    background-image: url("data:image/gif;R0lGODlhEAAQAIcAAED/QFaG5WWV82qZ9XGd9Xei9n2n+Iuq6oSr+Yuw+pC1+5a5/Jq9/Z/A/qLC/8DAwNDg8ODg8ODo8PDw8PDw//D4///4/////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAMAAAAALAAAAAAQABAAAAhyAAEIHEiwoMGDBQ8oXMhwYQCBBxw0YLBAQQIEBgoQGCDgIYCGIBV6dHChpEmTFSpQGHkh5EIJLE+WTElBAkyBJB88uKBTJ88HEWLKnKmSpUuFNwGQHErTJkufPXfqDIpTpgWVEyREgDAygNevYL8iHBsQADs=")
}

.x-grid-rowbody {
    font: normal 11px/13px tahoma, arial, verdana, sans-serif;
    padding: 5px 6px 5px 6px
}

.x-grid-no-row-lines .x-grid-row-focused .x-grid-rowbody {
    padding-top: 6px;
    padding-bottom: 4px
}

.x-docked-summary {
    border-width: 1px;
    border-color: #99bce8;
    border-style: solid;
    background: #fff !important
}

.x-docked-summary .x-grid-table {
    border: 0 none
}

.x-grid-row-summary .x-grid-cell, .x-grid-row-summary .x-grid-rowwrap, .x-grid-row-summary .x-grid-cell-rowbody {
    border-color: #ededed;
    background-color: #fff !important;
    border-top: 1px solid #ededed;
    font: normal 11px/13px tahoma, arial, verdana, sans-serif
}

.x-docked-summary .x-grid-item, .x-docked-summary .x-grid-row-summary .x-grid-cell {
    border-bottom: 0 none;
    border-top: 0 none
}

.x-docked-summary > :first-child {
    background-color: #fff
}

.x-grid-row-summary .x-grid-cell-inner-row-expander {
    display: none
}

.x-menu-default {
    border-style: solid;
    border-width: 1px;
    border-color: #99bce8
}

.x-menu-body-default {
    background: #f0f0f0;
    padding: 2px
}

.x-menu-icon-separator-default {
    left: 24px;
    border-left: solid 1px #e0e0e0;
    background-color: #fff;
    width: 2px
}

.x-menu-item-default {
    border-width: 1px;
    cursor: pointer
}

.x-menu-item-default.x-menu-item-focus, .x-menu-item-default.x-menu-item-active {
    background-image: none;
    background-color: #d9e8fb;
    background-image: -webkit-gradient(linear, top, bottom, color-stop(0%, #e7f0fc), color-stop(0%, #c7ddf9));
    background-image: -webkit-linear-gradient(top, #e7f0fc, #c7ddf9);
    background-image: -moz-linear-gradient(top, #e7f0fc, #c7ddf9);
    background-image: -o-linear-gradient(top, #e7f0fc, #c7ddf9);
    background-image: -ms-linear-gradient(top, #e7f0fc, #c7ddf9);
    background-image: linear-gradient(top, #e7f0fc, #c7ddf9);
    -webkit-border-radius: 3px;
    -moz-border-radius: 3px;
    -ms-border-radius: 3px;
    -o-border-radius: 3px;
    border-radius: 3px;
    border-color: #a9cbf5
}

.x-nlg .x-menu-item-default.x-menu-item-focus, .x-nlg .x-menu-item-default.x-menu-item-active {
    background: #d9e8fb repeat-x left top;
    background-image: url(images/menu/menu-item-default-active-bg.gif)
}

.x-menu-item-default.x-menu-item-disabled {
    cursor: default
}

.x-menu-item-default.x-menu-item-disabled a {
    cursor: default
}

.x-menu-item-default.x-menu-item-separator {
    height: 2px;
    border-top: solid 1px #e0e0e0;
    background-color: #fff;
    margin: 2px 0;
    padding: 0
}

.x-menu-item-default.x-menu-item-disabled {
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=50)";
    opacity: 0.5
}

.x-ie9m .x-menu-item-default.x-menu-item-disabled .x-menu-item-icon-ui {
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=50)";
    opacity: 0.5
}

.x-ie9m .x-menu-item-default.x-menu-item-disabled .x-menu-item-text-default {
    background-color: transparent
}

.x-menu-item-default .x-form-item-label {
    font-size: 11px;
    color: #222
}

.x-menu-item-text-default, .x-menu-item-cmp-default {
    margin: 0 4px 0 4px
}

.x-menu-item-text-default {
    font: normal 11px tahoma, arial, verdana, sans-serif;
    line-height: 21px;
    padding-top: 1px;
    color: #222;
    cursor: pointer
}

.x-menu-item-focus .x-menu-item-text-default, .x-menu-item-active .x-menu-item-text-default {
    color: #000
}

.x-menu-item-text-default.x-menu-item-indent {
    margin-left: 30px
}

.x-menu-item-text-default.x-menu-item-indent-no-separator {
    margin-left: 24px
}

.x-menu-item-text-default.x-menu-item-indent-right-icon {
    margin-right: 28px
}

.x-menu-item-text-default.x-menu-item-indent-right-arrow {
    margin-right: 21px
}

.x-menu-item-disabled .x-menu-item-text-default {
    cursor: default
}

.x-menu-item-indent-default {
    margin-left: 30px
}

.x-menu-item-icon-default {
    width: 16px;
    height: 16px;
    top: 4px;
    left: 3px;
    line-height: 16px;
    font-size: 16px;
    color: #222;
    background-position: center center
}

.x-menu-item-icon-default.x-menu-item-glyph {
    opacity: 0.5
}

.x-ie8 .x-menu-item-icon-default.x-menu-item-glyph {
    color: #898989
}

.x-menu-item-icon-default.x-menu-item-icon-right {
    width: 16px;
    height: 16px;
    top: 4px;
    right: 5px;
    left: auto;
    background-position: center center
}

.x-menu-item-checked .x-menu-item-icon-default.x-menu-item-checkbox {
    background-image: url("data:image/gif;R0lGODlhEAAQAIcAAENZkkRZkkZblEdclUhdlkhelklel0pfl0tgmFZpnV1woWBypGN1pWR2pWZ3p21+qkD/QHaGq46Pj4uZu4yZupCdva6zuZ2nwKOuyK+4z7C50be/1bm/0LrB1bzD1sbIysXJzcrLzMnM0MvP1c3P0cnP3czQ1s3R1tXV1tXY3NXZ3dra29vc3Nzd3s/U4tzf5N7g4d/i5d7h6d/i6eHi4uDi5ubm5ufn6Onp6uvr7Ozt7e3u7urs8O3u8fLz9PLz9vT09PX19fb29vj4+Pn5+fj5+gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAMAABAALAAAAAAQABAAAAicACEIHEiwoMGDBSUoXMhw4UAJQCJKBDKEiBAgEh4CscCRo4gLEV4EySgQooURKE30SACAgxCSEEyiPFEjQ4AGNzBqtKAiRgofCgR4YKGzJBAQJTDs6ECAwRAURWMCgfFAgAsHBzYIaREVIgkZAwocWFAECI2uQD7wmGAAgQaLNtCGWDGDQoUfOnLgQBsxCJEhQSbCbEhYIcLDEAICADs=")
}

.x-menu-item-unchecked .x-menu-item-icon-default.x-menu-item-checkbox {
    background-image: url("data:image/gif;R0lGODlhEAAQAIcAAED/QI6Pj66zua+0urK3vLS5vbi7v7u+wby/wsHDxcLExsbHyMrLzMzNzcvP1c3R1s3R19TU1dTV1tDT2NDU2dLV2tTX29XY3Njb3tvb3Nrc39vd39zd3t3f4eDh4eDh4+Hi4uHi4+Lj5OPk5eTl5eXm5ubm5ubn5+jo6Onp6enp6urq6urr6+vr7Ovs7Ozs7O3t7e/v7/Dw8PLy8vT09PX19fb29gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAMAAAAALAAAAAAQABAAAAiKAAEIHEiwoMGDBQMoXMhw4cAANCJKnEgjwEMaAjJqHFDgQMWLAhyIdDDhwoYEHwVCDOngQQUMHUQsSAlgJQQKFjaEKIGiAU2IBC5o+IDiBQwYEn7SMNCBxIoYM6JyUIpgRAoYM2jUoAFCqYKrMmjYGGtCKYMIGTycYOGihQqlFClaVNmw7lyECAMCADs=")
}

.x-menu-item-checked .x-menu-item-icon-default.x-menu-group-icon {
    background-image: url("data:image/gif;R0lGODlhEAAQAIcAAAI0cAM3cQI2cgM5cwA7egVGfgZHfQxKfw1LfwBCgQBCggBDggBEgwBFhABGhQBHhwBIhwBJhwBKiABLigBMiwBNjABOjABSjQFSjQZUjQZVjQhVjQhWjRFZjR1cjR1djR5djSNciiBdjSRcii1ijUJmkEBllEVnkUJpk0ZrlEBsnEBtnEZxmUdxmU95nU55nkx8o////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAMAADEALAAAAAAQABAAAAhYAGMIHEiwoMGDCBMqXEjwxYECLRbCCPFBQwQVCV2MIOEhQwUFKRAiEAGiw4UJDQYgNMBhA4YKEBIEQMhCggUKDxYQOJFwBQMHCgiYWIhCAIASDJMqXco0IAA7")
}

.x-menu-item-unchecked .x-menu-item-icon-default.x-menu-group-icon {
    background-image: none
}

.x-menu-item-arrow-default {
    width: 12px;
    height: 9px;
    top: 6px;
    right: -1px;
    background-image: url("data:image/gif;R0lGODlhDAAJAIcAACluvipxvzJ1vyxwwCt1yjp6zkD/QDiC1jmE0zyE0z2I3UeLyUGJ2VWUzlKg7FSg6Weg1WKq8Y7D9orD/JXL/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAMAAAYALAAAAAAMAAkAAAgzAA8YGEiwoAEFCQwaJEABgUKCBCRMYPDQAIEHESAIeEjAQYMAFQksAFDR4oCSBgqgNBAQADs=")
}

.x-menu-item-focus .x-menu-item-arrow-default, .x-menu-item-active .x-menu-item-arrow-default {
    top: 6px;
    right: -1px
}

.x-menu-default-scroller .x-box-scroller-body-horizontal {
    margin-left: 14px
}

.x-menu-default-vertical-scroller .x-box-scroller-body-vertical {
    margin-top: 11px
}

.x-box-scroller-menu-default {
    cursor: pointer;
    color: #eee
}

.x-box-scroller-menu-default.x-box-scroller-disabled {
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=50)";
    opacity: 0.5;
    cursor: default
}

.x-box-scroller-menu-default.x-box-scroller-top, .x-box-scroller-menu-default.x-box-scroller-bottom {
    height: 5px;
    width: 35px;
    left: 50%;
    margin-left: -17px
}

.x-box-scroller-menu-default.x-box-scroller-top {
    margin-top: 4px;
    margin-right: 0;
    margin-bottom: 4px;
    background-image: url("data:image/gif;R0lGODlhIwAKAMIEAENDQ9HR0evr6/r6+v///////////////yH5BAEKAAQALAAAAAAjAAoAAAM9SErR/jDGRcO4OGOg+w0U43VAOWqgYp1babIfI810XdU4FKpC7/8+AHDYSy0CxKErCTQimUGXEFqU5a6zBAA7");
    background-position: 0 -5px
}

.x-box-scroller-menu-default.x-box-scroller-top.x-box-scroller-hover {
    background-position: 0 0
}

.x-box-scroller-menu-default.x-box-scroller-bottom {
    margin-top: 4px;
    margin-right: 0;
    margin-bottom: 4px;
    background-image: url("data:image/gif;R0lGODlhIwAKAMIEAENDQ9HR0evr6/r6+v///////////////yH5BAEKAAQALAAAAAAjAAoAAAM8GLrc/o8EQautIOfLaSDg1F3aeH1gaFrAWqFpCM1zTN+4Ig187/eazG/IgwWIQw3yBwstfYBnr5nKWWMJADs=");
    background-position: 0 0
}

.x-box-scroller-menu-default.x-box-scroller-bottom.x-box-scroller-hover {
    background-position: 0 -5px
}

.x-ie8 .x-box-scroller-menu-default {
    background-color: #f0f0f0
}

.x-cmd-slicer.x-menu-item-default-active:before {
    display: none;
    content: "x-slicer:, bg:url(images/menu/menu-item-default-active-bg.gif), stretch:bottom" !important
}

.x-menu-default-menubar {
    border-style: solid;
    border-width: 1px;
    border-color: #99bce8
}

.x-menu-body-default-menubar {
    background: #f0f0f0;
    padding: 2px
}

.x-menu-icon-separator-default-menubar {
    left: 24px;
    border-left: solid 1px #e0e0e0;
    background-color: #fff;
    width: 2px
}

.x-menu-item-default-menubar {
    border-width: 1px;
    cursor: pointer
}

.x-menu-item-default-menubar.x-menu-item-focus, .x-menu-item-default-menubar.x-menu-item-active {
    background-image: none;
    background-color: #d9e8fb;
    background-image: -webkit-gradient(linear, top, bottom, color-stop(0%, #e7f0fc), color-stop(0%, #c7ddf9));
    background-image: -webkit-linear-gradient(top, #e7f0fc, #c7ddf9);
    background-image: -moz-linear-gradient(top, #e7f0fc, #c7ddf9);
    background-image: -o-linear-gradient(top, #e7f0fc, #c7ddf9);
    background-image: -ms-linear-gradient(top, #e7f0fc, #c7ddf9);
    background-image: linear-gradient(top, #e7f0fc, #c7ddf9);
    -webkit-border-radius: 3px;
    -moz-border-radius: 3px;
    -ms-border-radius: 3px;
    -o-border-radius: 3px;
    border-radius: 3px;
    border-color: #a9cbf5
}

.x-nlg .x-menu-item-default-menubar.x-menu-item-focus, .x-nlg .x-menu-item-default-menubar.x-menu-item-active {
    background: #d9e8fb repeat-x left top;
    background-image: url(images/menu/menu-item-default-menubar-active-bg.gif)
}

.x-menu-item-default-menubar.x-menu-item-disabled {
    cursor: default
}

.x-menu-item-default-menubar.x-menu-item-disabled a {
    cursor: default
}

.x-menu-item-default-menubar.x-menu-item-separator {
    height: 2px;
    border-top: solid 1px #e0e0e0;
    background-color: #fff;
    margin: 2px 0;
    padding: 0
}

.x-menu-item-default-menubar.x-menu-item-disabled {
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=50)";
    opacity: 0.5
}

.x-ie9m .x-menu-item-default-menubar.x-menu-item-disabled .x-menu-item-icon-ui {
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=50)";
    opacity: 0.5
}

.x-ie9m .x-menu-item-default-menubar.x-menu-item-disabled .x-menu-item-text-default-menubar {
    background-color: transparent
}

.x-menu-item-default-menubar .x-form-item-label {
    font-size: 11px;
    color: #222
}

.x-menu-item-text-default-menubar, .x-menu-item-cmp-default-menubar {
    margin: 0 4px 0 4px
}

.x-menu-item-text-default-menubar {
    font: normal 11px tahoma, arial, verdana, sans-serif;
    line-height: 21px;
    padding-top: 1px;
    color: #222;
    cursor: pointer
}

.x-menu-item-focus .x-menu-item-text-default-menubar, .x-menu-item-active .x-menu-item-text-default-menubar {
    color: #000
}

.x-menu-item-text-default-menubar.x-menu-item-indent {
    margin-left: 30px
}

.x-menu-item-text-default-menubar.x-menu-item-indent-no-separator {
    margin-left: 24px
}

.x-menu-item-text-default-menubar.x-menu-item-indent-right-icon {
    margin-right: 28px
}

.x-menu-item-text-default-menubar.x-menu-item-indent-right-arrow {
    margin-right: 23px
}

.x-menu-item-disabled .x-menu-item-text-default-menubar {
    cursor: default
}

.x-menu-item-indent-default-menubar {
    margin-left: 30px
}

.x-menu-item-icon-default-menubar {
    width: 16px;
    height: 16px;
    top: 4px;
    left: 3px;
    line-height: 16px;
    font-size: 16px;
    color: #222;
    background-position: center center
}

.x-menu-item-icon-default-menubar.x-menu-item-glyph {
    opacity: 0.5
}

.x-ie8 .x-menu-item-icon-default-menubar.x-menu-item-glyph {
    color: #898989
}

.x-menu-item-icon-default-menubar.x-menu-item-icon-right {
    width: 16px;
    height: 16px;
    top: 4px;
    right: 5px;
    left: auto;
    background-position: center center
}

.x-menu-item-checked .x-menu-item-icon-default-menubar.x-menu-item-checkbox {
    background-image: url(images/menu/default-menubar-checked.gif)
}

.x-menu-item-unchecked .x-menu-item-icon-default-menubar.x-menu-item-checkbox {
    background-image: url(images/menu/default-menubar-unchecked.gif)
}

.x-menu-item-checked .x-menu-item-icon-default-menubar.x-menu-group-icon {
    background-image: url(images/menu/default-menubar-group-checked.gif)
}

.x-menu-item-unchecked .x-menu-item-icon-default-menubar.x-menu-group-icon {
    background-image: none
}

.x-menu-item-arrow-default-menubar {
    width: 9px;
    height: 6px;
    top: 10px;
    right: 4px;
    background-image: url("data:image/gif;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")
}

.x-menu-item-focus .x-menu-item-arrow-default-menubar, .x-menu-item-active .x-menu-item-arrow-default-menubar {
    top: 10px;
    right: 4px
}

.x-menu-default-menubar-scroller .x-box-scroller-body-horizontal {
    margin-left: 14px
}

.x-menu-default-menubar-vertical-scroller .x-box-scroller-body-vertical {
    margin-top: 11px
}

.x-box-scroller-menu-default-menubar {
    cursor: pointer;
    color: #eee
}

.x-box-scroller-menu-default-menubar.x-box-scroller-disabled {
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=50)";
    opacity: 0.5;
    cursor: default
}

.x-box-scroller-menu-default-menubar.x-box-scroller-top, .x-box-scroller-menu-default-menubar.x-box-scroller-bottom {
    height: 5px;
    width: 35px;
    left: 50%;
    margin-left: -17px
}

.x-box-scroller-menu-default-menubar.x-box-scroller-top {
    margin-top: 4px;
    margin-right: 0;
    margin-bottom: 4px;
    background-image: url(images/menu/default-menubar-scroll-top.gif);
    background-position: 0 -5px
}

.x-box-scroller-menu-default-menubar.x-box-scroller-top.x-box-scroller-hover {
    background-position: 0 0
}

.x-box-scroller-menu-default-menubar.x-box-scroller-bottom {
    margin-top: 4px;
    margin-right: 0;
    margin-bottom: 4px;
    background-image: url(images/menu/default-menubar-scroll-bottom.gif);
    background-position: 0 0
}

.x-box-scroller-menu-default-menubar.x-box-scroller-bottom.x-box-scroller-hover {
    background-position: 0 -5px
}

.x-ie8 .x-box-scroller-menu-default-menubar {
    background-color: #f0f0f0
}

.x-cmd-slicer.x-menu-item-default-menubar-active:before {
    display: none;
    content: "x-slicer:, bg:url(images/menu/menu-item-default-menubar-active-bg.gif), stretch:bottom" !important
}

.x-grid-filters-filtered-column {
    font-style: italic;
    font-weight: bold;
    text-decoration: inherit
}

.x-grid-filters-icon {
    background-repeat: no-repeat;
    background-position: center center;
    color: #222;
    text-align: center
}

.x-grid-filters-find {
    background-image: url("data:image/gif;iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABGdBTUEAAK/INwWK6QAAABl0RVh0U29mdHdhcmUAQWRvYmUgSW1hZ2VSZWFkeXHJZTwAAAIlSURBVDjLY/j//z8DJZiB6gY09895tGTDnv+tE+f+B/EnL1gHZofGpt4iyoCK5r5H63YcBmkAG5BRVPO/b/aK/0CDn+A1ICm75H/X9CX/azun/m+bNP+/iaUd2AAHN5//WSV1/wuqWsFiVvauyxWUVHkEhUWZwAYsWLOTo6i23aOpbzbYqYXVbf89/MP+u3gF/M8pa/gfm5b3PyKn6X/txGX/S1qmgOW4uXmq2NjZGcEGTJi7mmXKwvUPF63b9T+3vAmMqyeu+j9l+a7/fUu2/2qcvuF/be/8/9G5zf/DkwvBLmRmYXnAwMDADDYA6FxWkM3TFm/8n11a/x/k55Tc8v/RyTn/1bT0wDaCXAITj0svAOpi+AfErGAD0goqWf1CY35a2Dr99wqM+G9sYftfW9/4v6yC8lMRMXEDSRm5rWISUv+B/v4vKi75n5eP/z8jI+M7oAFM8ED0CYo6DAq4XYfP/F+15cD/7hnLQAG2AiSnqqmzorJlwv+1Ow6B5UAxwscveBglFtx8gv/kVzSDDQC66H98RuF/PWPzqyA5oM1XQTEAMiA1v+J/emH1fw5Orj8oBji6+/6HGQBTpKGt/1NRRZ1RQlr2HSjgYAaAwoKVle0/igHWjm7geAYlIJACUGDqGpn9B/qfX0lV4wrIAFAsweSAYYBqACiBGJhYggMP6Of/QJv/S8sq/AcGohTQv7c5ubj/A+MdFH2gGABj2mUmUjEAnjJojQ5aPHUAAAAASUVORK5CYII=")
}

.x-grid-filters-gt {
    background-image: url("data:image/gif;iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAAB90RVh0U29mdHdhcmUATWFjcm9tZWRpYSBGaXJld29ya3MgOLVo0ngAAAAWdEVYdENyZWF0aW9uIFRpbWUAMDQvMDYvMDdRnQkMAAAAvElEQVQ4jcXTPUpDURDF8V8khZYS0osLsHHKV6UL2MQNuAnXpU3gbcBCcGzcgCkDwbRJ5bN5DwTflXwInvJy53/PmZk7aJrGMTo5qvovAMO+w4i4QYV5Zj4d4qDCPR4i4voQwBxrjFFHRFUCDEpTaF+uMcICs8x829WBzHzFLZa4xMs+ETptcNa53QvQ5q5xjhUmffd6exARV3jEBT4wbSP9UO8e4BmneMddqfg3wCe2Cp3/ruIYd9X/f6YvPUs2bGi/VQoAAAAASUVORK5CYII=")
}

.x-grid-filters-lt {
    background-image: url("data:image/gif;iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAAB90RVh0U29mdHdhcmUATWFjcm9tZWRpYSBGaXJld29ya3MgOLVo0ngAAAAWdEVYdENyZWF0aW9uIFRpbWUAMDQvMDYvMDdRnQkMAAAAt0lEQVQ4jdXTMU5CURCF4Q+jCSZWJCSWrsDGMbFgAyRUboANsRYs6awoKIaGBcgCCKGk41lw7bj4CDZOfeafc07u7TRN45q5uWr7LwC3vwki4hkLHDLz4SIHETHAB7o1bRUQES+Y4glrvLUGlMsz9LHFODNXp7S1Dj5xhx2GmbmsOa1F+Hkce9zXls8BXvGFR0xLH+0BJe/YMX8fs9JLawcyc44hNuhhdBGgQJZ4xwTzU5rO//9M34wgLw6RYDlTAAAAAElFTkSuQmCC")
}

.x-grid-filters-eq {
    background-image: url("data:image/gif;iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAAB90RVh0U29mdHdhcmUATWFjcm9tZWRpYSBGaXJld29ya3MgOLVo0ngAAAAWdEVYdENyZWF0aW9uIFRpbWUAMDQvMDYvMDdRnQkMAAAALklEQVQ4jWP8//8/AyWAiSLdw8MAFmSOiYkJUSF65swZRqq5gHHAo3E0DIaFAQASphEZbkX8DgAAAABJRU5ErkJggg==")
}

.x-grid-locked .x-grid-inner-locked {
    border-width: 0 1px 0 0;
    border-style: solid
}

.x-grid-locked-split .x-grid-inner-normal {
    border-width: 0 0 0 1px;
    border-style: solid;
    border-left-color: #99bce8
}

.x-grid-locking-body {
    border-width: 1px
}

.x-grid-locking-body > .x-splitter {
    background-color: #dfe8f6
}

.x-grid-locking-body > .x-splitter-active {
    background-color: #b4b4b4
}

.x-grid-inner-locked {
    border-right-color: #99bce8
}

.x-grid-inner-locked .x-column-header-last, .x-grid-inner-locked .x-grid-cell-last {
    border-right-width: 0 !important
}

.x-hmenu-lock {
    background-image: url("data:image/gif;R0lGODlhEAAQAIcAAE9SW2hZQGxubmdpcGpsc29wdHN1end3fG5xgIduF7iIDL6NCb+NCKiPUMGPC8KQC8aUC8uXAc6ZAMycCsmaF9OfAcieMM2hB86mDN2qAN6rAN+sANqqCt61Gdi1N965N+KuAOm1AOm2AOy4AOCzFOO3GuG/I+G/JuC6KM+mRNiwSdKwV+fCF+vGH+/LGvbDAPnEAP/TAP/VAP/ZAOTBI+XEIuvIMuvKO+vYN//nAP/rAP/uAP/8AP//AP/mOv/nPufTUf/nSv/vRf/sW///Q///Rv//TIGBhIaIjIqLjpCQk5eXl5iYmJmZmbKmhKenp6qqqrq5qbm4tb6+vry9wujRjP//q9bW1tnZ2dvb297f5v//w///xf//xv//yuPj4+zs7P/+5PPz8/b29v379P/99/j4+P/9+P/++Pz8/P///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAMAAGoALAAAAAAQABAAAAiYANUIHEiwoEE1WaZAeYLl4MAvSQwcOMLkikM1SpAIBLOkyUUCBKkUcKgFAUEpAw5uiSIAxw0bLZwAUGHwR4MAQIYE8YEigQKDLIS46FCCBIcKEiAYrOGlSA8dMmCM0PDAIA0uRHjkiPFCRAYHBk1g1crV6wKDJ7pk3dp1AwODH6wY6bFjRggQEVIcrOIBw4UJFCysuEhYTUAAOw==")
}

.x-hmenu-unlock {
    background-image: url("data:image/gif;R0lGODlhEAAQAIcAAHZ0aXFxcXNzc3R0dLZ5AJSEP5CIdMqVAM+fF9WmBdijAd6rAN+sANqrC9ShGtWkG9alHNimHNimHd22A9KlI9mnINerNd+6LuGtAOe0AOi0AOi1AOu3APC9AM+rT+DEDfTAAPXCAPrJAPzJAP/LCfLHHv/RAP/SAP/XAPrbAPvVEP/YGuvNPPLXKPHXLvPYJ/ffK//XJvbSM/bTNPnXN//kAP/mAP/rAPzwAP/8AP/+AP//AP/yOP/+N///Of//OuPJQvrbRf/eRebLef/rTf/vU///Q///U//uYv//ZoODg4SEhIaGhoeHh4iIiI2NjY+QkpGRkZSUlJmZmZubm56enp+fn4mRr5yepaCgoKGhoaSkpKSkpaampqenp6ioqLCwsLGxsb+/v+rauv//kP//vcvLy8zMzNzd5vnr0P//x///yP//yf//zeLi4uPj5vv15/Ly8vPz8/b29vf39///8Pn5+f7+/v///v///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAMAAHkALAAAAAAQABAAAAioAPMIHEiwoEGCYqZI+XKQ4BkqT5hkadJQIBgnAsNE8dLwDZclA7coaYgGC5SBXQYMJJPkCI8YF64YSCPQSgCBRRAQoIGEyAwABSoIrCJAoIoVJIQEkVEiwQEJAs1oEQijTQ8cKUSA4IAhgsEXa37osHEihIYFEAy2UOMjRw0TITIweGDQBZsfbuFuwODAIIsyRnbcQDGigwILB4cA+TChAQUPYypKHhgQADs=")
}

.x-grid-scrollbar-clipper > .x-grid-view, .x-grid-scrollbar-clipper > .x-tree-view {
    background-color: #fff
}

.x-grid-scrollbar-clipper-locked, .x-grid-scrollbar-locked {
    border-width: 0 1px 0 0;
    border-style: solid;
    border-color: #99bce8
}

.x-grid-scroll-container {
    background-color: #fff
}

.x-form-display-field-grid-cell {
    min-height: 20px;
    font: normal 11px/13px tahoma, arial, verdana, sans-serif;
    color: #000;
    margin-top: 4px
}

.x-form-display-field-grid-cell.x-field-form-focus {
    outline: 1px solid #7eadd9;
    outline-offset: -1px
}

.x-ie .x-form-display-field-grid-cell.x-field-form-focus, .x-ie10p .x-form-display-field-grid-cell.x-field-form-focus, .x-edge .x-form-display-field-grid-cell.x-field-form-focus {
    outline: none
}

.x-ie .x-form-display-field-grid-cell.x-field-form-focus:after, .x-ie10p .x-form-display-field-grid-cell.x-field-form-focus:after, .x-edge .x-form-display-field-grid-cell.x-field-form-focus:after {
    position: absolute;
    content: ' ';
    top: 0px;
    right: 0px;
    bottom: 0px;
    left: 0px;
    border: 1px solid #7eadd9;
    pointer-events: none
}

.x-ie8 .x-form-display-field-grid-cell.x-field-form-focus {
    position: relative
}

.x-grid-editor .x-form-display-field {
    text-overflow: ellipsis
}

.x-grid-editor .x-form-action-col-field {
    padding: 2px 2px 2px 2px
}

.x-grid-editor .x-form-text {
    padding-left: 5px;
    padding-right: 5px
}

.x-tree-cell-editor .x-form-text {
    padding-left: 2px;
    padding-right: 2px
}

.x-grid-row-editor .x-field {
    margin: 0 1px 0 1px
}

.x-grid-row-editor .x-form-display-field {
    padding: 3px 5px 4px 5px;
    line-height: 13px
}

.x-ie9m .x-grid-row-editor .x-form-display-field {
    min-height: 13px
}

.x-grid-row-editor .x-form-action-col-field {
    padding: 2px 1px 2px 1px
}

.x-grid-row-editor .x-form-text {
    padding: 1px 4px 2px 4px
}

.x-gecko .x-grid-row-editor .x-form-text {
    padding-left: 3px;
    padding-right: 3px
}

.x-grid-row-editor .x-panel-body {
    border-top: 1px solid #99bce8 !important;
    border-bottom: 1px solid #99bce8 !important;
    padding: 4px 0 4px 0;
    background-color: #eaf1fb
}

.x-grid-with-col-lines .x-grid-row-editor .x-form-cb {
    margin-right: 1px
}

.x-grid-row-editor-buttons-default-bottom {
    -moz-border-radius-topleft: 0;
    -webkit-border-top-left-radius: 0;
    border-top-left-radius: 0;
    -moz-border-radius-topright: 0;
    -webkit-border-top-right-radius: 0;
    border-top-right-radius: 0;
    -moz-border-radius-bottomright: 5px;
    -webkit-border-bottom-right-radius: 5px;
    border-bottom-right-radius: 5px;
    -moz-border-radius-bottomleft: 5px;
    -webkit-border-bottom-left-radius: 5px;
    border-bottom-left-radius: 5px;
    padding: 4px 4px 4px 4px;
    border-width: 0 1px 1px 1px;
    border-style: solid;
    background-color: #eaf1fb
}

.x-grid-row-editor-buttons-default-bottom-mc {
    background-color: #eaf1fb
}

.x-nbr .x-grid-row-editor-buttons-default-bottom {
    padding: 0 !important;
    border-width: 0 !important;
    -webkit-border-radius: 0px;
    -moz-border-radius: 0px;
    -ms-border-radius: 0px;
    -o-border-radius: 0px;
    border-radius: 0px;
    background-color: transparent !important;
    box-shadow: none !important
}

.x-grid-row-editor-buttons-default-bottom-frameInfo {
    font-family: th-0-5-5-5-0-1-1-1-4-4-4-4
}

.x-grid-row-editor-buttons-default-bottom-tl {
    background-position: 0 -10px
}

.x-grid-row-editor-buttons-default-bottom-tr {
    background-position: right -15px
}

.x-grid-row-editor-buttons-default-bottom-bl {
    background-position: 0 -20px
}

.x-grid-row-editor-buttons-default-bottom-br {
    background-position: right -25px
}

.x-grid-row-editor-buttons-default-bottom-ml {
    background-position: 0 top
}

.x-grid-row-editor-buttons-default-bottom-mr {
    background-position: right top
}

.x-grid-row-editor-buttons-default-bottom-tc {
    background-position: 0 0
}

.x-grid-row-editor-buttons-default-bottom-bc {
    background-position: 0 -5px
}

.x-grid-row-editor-buttons-default-bottom-tr, .x-grid-row-editor-buttons-default-bottom-br, .x-grid-row-editor-buttons-default-bottom-mr {
    padding-right: 5px
}

.x-grid-row-editor-buttons-default-bottom-tl, .x-grid-row-editor-buttons-default-bottom-bl, .x-grid-row-editor-buttons-default-bottom-ml {
    padding-left: 5px
}

.x-grid-row-editor-buttons-default-bottom-tc {
    height: 0
}

.x-grid-row-editor-buttons-default-bottom-bc {
    height: 5px
}

.x-grid-row-editor-buttons-default-bottom-tl, .x-grid-row-editor-buttons-default-bottom-bl, .x-grid-row-editor-buttons-default-bottom-tr, .x-grid-row-editor-buttons-default-bottom-br, .x-grid-row-editor-buttons-default-bottom-tc, .x-grid-row-editor-buttons-default-bottom-bc, .x-grid-row-editor-buttons-default-bottom-ml, .x-grid-row-editor-buttons-default-bottom-mr {
    background-image: url("data:image/gif;R0lGODlhBQAeAPMAAJm86KLC6qPC6qPC67bP7rfP7s7e887f9OLr+eLs+eTu+eXu+Obt+erx+////wAAACH5BAEAAA4ALAAAAAAFAB4AQwhLABsIHEiQIAAHDhgQEFAQAMEACQYiODDAgIOCDQ1iFAiAwQAFBQ8Q2EiyIYCTJzVudDiQJccCBwY6MDDgAAKJDBsoGLBAAAEGCAMCADs=")
}

.x-grid-row-editor-buttons-default-bottom-ml, .x-grid-row-editor-buttons-default-bottom-mr {
    background-image: url("data:image/gif;R0lGODlhCgAVAPEAAJm86Orx+////5m86CH5BAEAAAIALAAAAAAKABUAQQg1AAEEGEhwIACBBQkeTKgQIcOFDANAfOgw4USLFQte1JixYUSJHQ2GBPlxo8eIJkWWHJlSYkAAOw==");
    background-repeat: repeat-y
}

.x-grid-row-editor-buttons-default-bottom-mc {
    padding: 4px 0px 0px 0px
}

.x-cmd-slicer.x-grid-row-editor-buttons-default-bottom:before {
    display: none;
    content: "x-slicer:, frame:0 5px 5px 5px, corners:url("data:image/gif;R0lGODlhBQAeAPMAAJm86KLC6qPC6qPC67bP7rfP7s7e887f9OLr+eLs+eTu+eXu+Obt+erx+////wAAACH5BAEAAA4ALAAAAAAFAB4AQwhLABsIHEiQIAAHDhgQEFAQAMEACQYiODDAgIOCDQ1iFAiAwQAFBQ8Q2EiyIYCTJzVudDiQJccCBwY6MDDgAAKJDBsoGLBAAAEGCAMCADs="), sides:url("data:image/gif;R0lGODlhCgAVAPEAAJm86Orx+////5m86CH5BAEAAAIALAAAAAAKABUAQQg1AAEEGEhwIACBBQkeTKgQIcOFDANAfOgw4USLFQte1JixYUSJHQ2GBPlxo8eIJkWWHJlSYkAAOw==")" !important
}

.x-grid-row-editor-buttons-default-top {
    -moz-border-radius-topleft: 5px;
    -webkit-border-top-left-radius: 5px;
    border-top-left-radius: 5px;
    -moz-border-radius-topright: 5px;
    -webkit-border-top-right-radius: 5px;
    border-top-right-radius: 5px;
    -moz-border-radius-bottomright: 0;
    -webkit-border-bottom-right-radius: 0;
    border-bottom-right-radius: 0;
    -moz-border-radius-bottomleft: 0;
    -webkit-border-bottom-left-radius: 0;
    border-bottom-left-radius: 0;
    padding: 4px 4px 4px 4px;
    border-width: 1px 1px 0 1px;
    border-style: solid;
    background-color: #eaf1fb
}

.x-grid-row-editor-buttons-default-top-mc {
    background-color: #eaf1fb
}

.x-nbr .x-grid-row-editor-buttons-default-top {
    padding: 0 !important;
    border-width: 0 !important;
    -webkit-border-radius: 0px;
    -moz-border-radius: 0px;
    -ms-border-radius: 0px;
    -o-border-radius: 0px;
    border-radius: 0px;
    background-color: transparent !important;
    box-shadow: none !important
}

.x-grid-row-editor-buttons-default-top-frameInfo {
    font-family: th-5-5-0-5-1-1-0-1-4-4-4-4
}

.x-grid-row-editor-buttons-default-top-tl {
    background-position: 0 -10px
}

.x-grid-row-editor-buttons-default-top-tr {
    background-position: right -15px
}

.x-grid-row-editor-buttons-default-top-bl {
    background-position: 0 -20px
}

.x-grid-row-editor-buttons-default-top-br {
    background-position: right -25px
}

.x-grid-row-editor-buttons-default-top-ml {
    background-position: 0 top
}

.x-grid-row-editor-buttons-default-top-mr {
    background-position: right top
}

.x-grid-row-editor-buttons-default-top-tc {
    background-position: 0 0
}

.x-grid-row-editor-buttons-default-top-bc {
    background-position: 0 -5px
}

.x-grid-row-editor-buttons-default-top-tr, .x-grid-row-editor-buttons-default-top-br, .x-grid-row-editor-buttons-default-top-mr {
    padding-right: 5px
}

.x-grid-row-editor-buttons-default-top-tl, .x-grid-row-editor-buttons-default-top-bl, .x-grid-row-editor-buttons-default-top-ml {
    padding-left: 5px
}

.x-grid-row-editor-buttons-default-top-tc {
    height: 5px
}

.x-grid-row-editor-buttons-default-top-bc {
    height: 0
}

.x-grid-row-editor-buttons-default-top-tl, .x-grid-row-editor-buttons-default-top-bl, .x-grid-row-editor-buttons-default-top-tr, .x-grid-row-editor-buttons-default-top-br, .x-grid-row-editor-buttons-default-top-tc, .x-grid-row-editor-buttons-default-top-bc, .x-grid-row-editor-buttons-default-top-ml, .x-grid-row-editor-buttons-default-top-mr {
    background-image: url("data:image/gif;R0lGODlhBQAeAPMAAJm86KLC6qPC6qPC67bP7rfP7s7e887f9OLr+eLs+eTu+ebt+erx+////wAAAJm86CH5BAEAAA0ALAAAAAAFAB4AQwhLAAEIFMigYMEEBwYYaADAoMOCCwYoKNjwIUWLDhs0WFAgQIAEFg8QqGiRJMaTGBsYGHAgQYEDBgMUWKCxoIIBCwwiEGDSpMOePwMCADs=")
}

.x-grid-row-editor-buttons-default-top-ml, .x-grid-row-editor-buttons-default-top-mr {
    background-image: url("data:image/gif;R0lGODlhCgAVAPEAAJm86Orx+////5m86CH5BAEAAAIALAAAAAAKABUAQQg1AAEEGEhwIACBBQkeTKgQIcOFDANAfOgw4USLFQte1JixYUSJHQ2GBPlxo8eIJkWWHJlSYkAAOw==");
    background-repeat: repeat-y
}

.x-grid-row-editor-buttons-default-top-mc {
    padding: 0px 0px 4px 0px
}

.x-cmd-slicer.x-grid-row-editor-buttons-default-top:before {
    display: none;
    content: "x-slicer:, frame:5px 5px 0 5px, corners:url("data:image/gif;R0lGODlhBQAeAPMAAJm86KLC6qPC6qPC67bP7rfP7s7e887f9OLr+eLs+eTu+ebt+erx+////wAAAJm86CH5BAEAAA0ALAAAAAAFAB4AQwhLAAEIFMigYMEEBwYYaADAoMOCCwYoKNjwIUWLDhs0WFAgQIAEFg8QqGiRJMaTGBsYGHAgQYEDBgMUWKCxoIIBCwwiEGDSpMOePwMCADs="), sides:url("data:image/gif;R0lGODlhCgAVAPEAAJm86Orx+////5m86CH5BAEAAAIALAAAAAAKABUAQQg1AAEEGEhwIACBBQkeTKgQIcOFDANAfOgw4USLFQte1JixYUSJHQ2GBPlxo8eIJkWWHJlSYkAAOw==")" !important
}

.x-grid-row-editor-buttons {
    border-color: #99bce8
}

.x-row-editor-update-button {
    margin-right: 2px
}

.x-row-editor-cancel-button {
    margin-left: 2px
}

.x-grid-row-editor-errors .x-tip-body {
    padding: 5px
}

.x-grid-row-editor-errors-item {
    list-style: disc;
    margin-left: 15px
}

.x-grid-cell-inner-row-expander {
    padding: 6px 7px 5px 7px
}

.x-grid-no-row-lines .x-grid-row-focused .x-grid-cell-inner-row-expander {
    padding-top: 5px;
    padding-bottom: 4px
}

.x-grid-row-expander {
    width: 9px;
    height: 9px;
    cursor: pointer;
    background-image: url("data:image/gif;R0lGODlhCQAJAPcAADFKY5SlvZylvZytxqW11qm92r3GxrXI48bS59Te8efv9+vz/////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACwAAAAACQAJAAAIQgATDBgoQECAAAYGMFi4cIECAAoZOjwAUaKCBAUACGAAoGPHjAEYOEyQAAEBAAFGljxwMoACBAcKEJgJwIDHmwYCAgA7")
}

.x-grid-row-collapsed .x-grid-row-expander {
    background-image: url("data:image/gif;R0lGODlhCQAJAPcAADFKY5SlvZylvZytxqW11qm92r3GxrXI48bS59Te8efv9+vz/////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACwAAAAACQAJAAAIRQATDBgoQECAAAYGMFi4cIECAAoXAnCIACJDAAoSFAAggAGAjx83BmDgEEACBAQABHCYAACCAykDKHhZgIBNAAZA6jQQEAA7")
}

.x-grid-cell-inner-property-name {
    background-image: url("data:image/gif;R0lGODlhGAAQAOMJANDQ0Ovs7uzt7+3u8O7v8e/w8vDx8/Hy9Pn5+f///////////////////////////ywAAAAAGAAQAAAEUBDJSc8xuBQyhggBQI2IhRka54EiOZnZ1n2h+16xSrc2jMqrmq2E++lYQ+IpNUMOfcwgzwUF7pLVo7BXjF6fXauTuxRvqWHtlJRtntlpNyACADs=");
    background-repeat: no-repeat;
    background-position: -16px 2px;
    padding-left: 12px
}

.x-ssm-row-numberer-hd {
    cursor: se-resize !important
}

.x-ssm-row-numberer-cell {
    cursor: e-resize
}

.x-ssm-column-select .x-column-header {
    cursor: s-resize
}

.x-ssm-extender-drag-handle {
    height: 7px;
    width: 7px;
    background-color: #c0d4ed
}

.x-ssm-extender-mask {
    border: 1px dotted #c0d4ed
}

.x-accordion-layout-ct {
    background-color: #fff;
    padding: 0
}

.x-accordion-hd .x-panel-header-title {
    color: #000;
    font-weight: normal;
    font-family: tahoma, arial, verdana, sans-serif;
    text-transform: none
}

.x-accordion-item {
    margin: 0
}

.x-accordion-item .x-accordion-hd {
    background: #d9e7f8;
    border-width: 1px 0;
    border-color: #f3f7fb #99bce8 #99bce8;
    padding: 4px 5px 5px 5px
}

.x-accordion-item .x-accordion-hd-sibling-expanded {
    border-top-color: #99bce8;
    border-top-width: 1px
}

.x-accordion-item .x-accordion-hd-last-collapsed {
    border-bottom-color: #d9e7f8
}

.x-accordion-item .x-accordion-body {
    border-width: 0
}

.x-accordion-hd .x-tool-img {
    background-color: #d9e7f8
}

.x-accordion-hd .x-tool-collapse-top, .x-accordion-hd .x-tool-collapse-bottom {
    background-position: 0 -255px
}

.x-tool-over .x-accordion-hd .x-tool-collapse-top, .x-tool-over .x-accordion-hd .x-tool-collapse-bottom {
    background-position: -15px -255px
}

.x-accordion-hd .x-tool-expand-top, .x-accordion-hd .x-tool-expand-bottom {
    background-position: 0 -240px
}

.x-tool-over .x-accordion-hd .x-tool-expand-top, .x-tool-over .x-accordion-hd .x-tool-expand-bottom {
    background-position: -15px -240px
}

body.x-border-layout-ct, div.x-border-layout-ct {
    background-color: #dfe8f6
}

.x-form-layout-wrap {
    border-spacing: 5px
}

.x-resizable-handle {
    position: absolute;
    z-index: 100;
    font-size: 1px;
    line-height: 6px;
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=0)";
    opacity: 0;
    background-color: #99bce8
}

.x-collapsed .x-resizable-handle {
    display: none
}

.x-resizable-handle-southeast {
    cursor: se-resize
}

.x-resizable-handle-northwest {
    cursor: nw-resize
}

.x-resizable-handle-northeast {
    cursor: ne-resize
}

.x-resizable-handle-southwest {
    cursor: sw-resize
}

.x-resizable-handle-east {
    cursor: e-resize;
    width: 6px;
    right: 0;
    top: 0;
    bottom: 0
}

.x-resizable-handle-south {
    cursor: s-resize;
    height: 6px;
    left: 0;
    right: 0;
    bottom: 0
}

.x-resizable-handle-west {
    cursor: w-resize;
    width: 6px;
    left: 0;
    top: 0;
    bottom: 0
}

.x-resizable-handle-north {
    cursor: n-resize;
    height: 6px;
    left: 0;
    right: 0;
    top: 0
}

.x-resizable-handle-southeast {
    width: 6px;
    height: 6px;
    right: 0;
    bottom: 0;
    z-index: 101
}

.x-resizable-handle-northwest {
    width: 6px;
    height: 6px;
    left: 0;
    top: 0;
    z-index: 101
}

.x-resizable-handle-northeast {
    width: 6px;
    height: 6px;
    right: 0;
    top: 0;
    z-index: 101
}

.x-resizable-handle-southwest {
    width: 6px;
    height: 6px;
    left: 0;
    bottom: 0;
    z-index: 101
}

.x-tablet .x-resizable-handle-north, .x-tablet .x-resizable-handle-south {
    height: 12px
}

.x-tablet .x-resizable-handle-east, .x-tablet .x-resizable-handle-west {
    width: 12px
}

.x-tablet .x-resizable-handle-northwest, .x-tablet .x-resizable-handle-northeast, .x-tablet .x-resizable-handle-southwest, .x-tablet .x-resizable-handle-southeast {
    width: 12px;
    height: 12px
}

.x-window .x-window-handle {
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=0)";
    opacity: 0
}

.x-window-collapsed .x-window-handle {
    display: none
}

.x-resizable-proxy {
    border: 1px dashed #3b5a82;
    position: absolute;
    overflow: hidden;
    z-index: 50000
}

.x-resizable-handle-over, .x-resizable-pinned .x-resizable-handle {
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=100)";
    opacity: 1
}

.x-resizable-handle-east-over, .x-resizable-handle-west-over, .x-resizable-pinned > .x-resizable-handle-east, .x-resizable-pinned > .x-resizable-handle-west {
    background-image: url("data:image/gif;R0lGODlhCgDQB4cAAHas8sPa+cre+tDj/Nbo/d3s/v///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAAAAP8ALAAAAAAKANAHAAj/AAsQGCAggMGDAgkeRDiw4MIACR0ujPgQYsOKFB9mnHhRY0eOCj2GBCmR4UiTJQ1uRInxI0uRKS2eVOmS5kyZMVfazFkTZ8ubOn3C/MkTaM+gSI8qNcq0qFOiUIdKJRmV6tSXVrNi3bqzKlehWrteFRsW7NekTb2SPbv06Viza+PCnYvWbdm6aum2zYv3bd+7e/0GBpxWcGHCdtkeVpxY7l/GfAdDNtxY72LHkjFftlz5sebOmTlH3uxZNOXRoEmHLs16tWvVsFPLRk37tG3EtXHfnqy7N+/fn3MDN+07+G7jxYkPbx1bOPLlr2cfV/68OvXrzKUnz+4ce/Tu3KeH/9/+XXx58s3Np0evHfp69+2tj4cP/jx99fG9v5dvn/9+/fnN51+A/QFY338CGojfgQQiWGCCED4ooYMUNmghgxguqCF7GXK44X0ehgjiiAN2SKKCIpb4oYoponhihBWayOKLE164oosz5ojjjjDa2GKPMvJYY5BA3ljkj0MamSSSMSrZJJM+0viklFHqeCSVRC6JpZNVCjmllVqC+aWXXV4pZplhkpnlmGaqyeWaaLKZZpt0zmmnnHjGqSecfL7pJ5R9AvrnloIWSuihZwaKqJuGJjqoo40yumideSoK6aR37vmopJd2yumnlGoaaaiWgpppqaRumuqop6ra6o8AAP+QU6wGtGRArX7FOisAuHJ0K0YVIaQrRrTa2itCwao0rEbFevSrq5VCKyqm0bJaLbXTeroqtqi+yq203V6rrbfjimuquduWm+2566bLbrjtkvsuuPRaGy+68rqrb7784uvvvQDDK3C939o7sMEEq3twwQwrnPC8CEfcMMQT7/vvwg5LnHHF/Qb8sMUea0zxxiSPbDLIGJ/cccoof7yyyxfDHDLHMYvcss0v41wzzTOXfDPPLOcMtMxB7+yz0EcbrbLSPyfd89JPNw110VEjPTXRWOtcNdNWS+1112BzLfbWZFNtdtZDa3222mg7vXbacLvd9tVs1x033Xd/PfbbctsP3XfeYZc9t96C+423pwEBADs=")
}

.x-resizable-handle-south-over, .x-resizable-handle-north-over, .x-resizable-pinned > .x-resizable-handle-south, .x-resizable-pinned > .x-resizable-handle-north {
    background-image: url("data:image/gif;R0lGODlh0AcKAIcAAHas8sPa+cre+tDj/Nbo/d3s/v///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAAAAP8ALAAAAADQBwoAAAj/AAsIHEiwoMGDCBMqXMiwocOHECNKnEixosWLGDNq3Mixo8ePIEOKHEmypMmTKFOqXMmypcuXMGPKnEmzps2bOHPq3Mmzp8+XBIIKHUq0qNGjSJMqXcq0qdOnUKNKnUq1qtWrWLNq3cq1q9evYMOKHUu2rNmzaNOqXSsUAICgbuG+JRCXrd27ePPq3cu3r9+/gAMLHky4sGGuAxIrXsy4sePHkCNLnky5suXLmDNr3sy5s+fPoEOLHk26tOnTqFOrXs26tevXsGPLnq3YrYEBtnEDuJ2btu/fwIMLH068uPHjyJMrX868ufPRAqJLn069uvXr2LNr3869u/fv4MOL/x9Pvrz58+jTq1/Pvr379/Djy59Pv779+/jz698/3YCB6P4B+J8AAfJn4IEIJqjgggw26OCDEEYo4YQUVmjhegFkqOGGHHbo4YcghijiiCSWaOKJKKao4oostujiizDGKOOMNNZo44045qjjjjz26OOPQAYp5JBEFmnkkUgmqeSSTDbp5JNQRinllFRWaeWVWGap5ZZcdunll2CGKeaYZJZp5plopqnmmmy26eabcMYp55x01mnnnXjmqeeefPbp55+ABirooIQWauihiCaq6KKMNuroo5BGKumklFZq6aWYZqrpppx26umnoIYq6qiklmrqqaimquqqrLbq6quwxgOKZUAAOw==")
}

.x-resizable-handle-southeast-over, .x-resizable-pinned > .x-resizable-handle-southeast {
    background-position: top left;
    background-image: url("data:image/gif;R0lGODlhCgAKAIcAAHas8sPa+cnd+tDj/NPl/dbo/djp/tnq/tzr/t3s/v///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAAAAP8ALAAAAAAKAAoAAAgyABMgMAAAwIAACAMgOFCgoIKEAQwUIDBAwcOEBQcUFADRoUOIFRUIsAixpMmTKFOWDAgAOw==")
}

.x-resizable-handle-northwest-over, .x-resizable-pinned > .x-resizable-handle-northwest {
    background-position: bottom right;
    background-image: url("data:image/gif;R0lGODlhCgAKAIcAAHas8sPa+cnd+tDj/NPl/dbo/djp/tnq/tzr/t3s/v///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAAAAP8ALAAAAAAKAAoAAAgyAAMIHEiwoMGDCBEqUCBg4QCCCgAAiAiAoACJAyRCVDCAQAEDECUWOICAYEYABhAkCAgAOw==")
}

.x-resizable-handle-northeast-over, .x-resizable-pinned > .x-resizable-handle-northeast {
    background-position: bottom left;
    background-image: url("data:image/gif;R0lGODlhCgAKAIcAAHas8sPa+cnd+tDj/NPl/dbo/djp/tnq/tzr/t3s/v///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAAAAP8ALAAAAAAKAAoAAAgzAAMIHEiwoMGDCAkOUKBAAEOCAAAoiKgAIoABEQUQNFCAwMKKAxEcKECRYAIEBiIOIBgQADs=")
}

.x-resizable-handle-southwest-over, .x-resizable-pinned > .x-resizable-handle-southwest {
    background-position: top right;
    background-image: url("data:image/gif;R0lGODlhCgAKAIcAAHas8sPa+cnd+tDj/NPl/dbo/djp/tnq/tzr/t3s/v///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAAAAP8ALAAAAAAKAAoAAAg0AAMIDDAAAAADCBIMDKDAYIEDCBYqUDCAQAEDCwUYLAhAosGGHQdOFDBxwMKTKFOqXBkgIAA7")
}

.x-slider-horz {
    padding-left: 7px;
    background: no-repeat 0 -15px;
    margin: 4px 0 3px
}

.x-slider-horz .x-slider-end {
    padding-right: 7px;
    background: no-repeat right -30px
}

.x-slider-horz .x-slider-inner {
    height: 15px
}

.x-slider-horz .x-slider-thumb {
    width: 14px;
    height: 15px;
    margin-left: -7px;
    background-image: url("data:image/gif;iVBORw0KGgoAAAANSUhEUgAAAFQAAABaCAMAAAARv4GDAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyRpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuMy1jMDExIDY2LjE0NTY2MSwgMjAxMi8wMi8wNi0xNDo1NjoyNyAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENTNiAoTWFjaW50b3NoKSIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDo4RUQ2N0YzQTBDNjExMUU0QjNDODk2QzFFQjg5MDhGMyIgeG1wTU06RG9jdW1lbnRJRD0ieG1wLmRpZDo4RUQ2N0YzQjBDNjExMUU0QjNDODk2QzFFQjg5MDhGMyI+IDx4bXBNTTpEZXJpdmVkRnJvbSBzdFJlZjppbnN0YW5jZUlEPSJ4bXAuaWlkOjhFRDY3RjM4MEM2MTExRTRCM0M4OTZDMUVCODkwOEYzIiBzdFJlZjpkb2N1bWVudElEPSJ4bXAuZGlkOjhFRDY3RjM5MEM2MTExRTRCM0M4OTZDMUVCODkwOEYzIi8+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kPSJyIj8+n8c+zwAAAX1QTFRF////rcrpl7fpoLrdscvr3fH/zuX/1Or/b5TS8v//ttHursvpss3rqt7/lMn/nczzrt//2v//0f//yfr/x/r/bKLn8P//wvX/v/L/u/D/wfT/vPH/t+z/suj/sej/uO7/sun/rOP/qOH/xPf/wfP/ue7/pd//z///zP3/yfv/xPb/vfH/p+D/1///1f//0///zf7/sOf/reT/3v//3f//tuv/4///4v//4f//3///y/z/xff/6f//6P//5///5P//3P//1P//zv7/s+b/6///6v//5v//4P//2P//rN//r+H/y+P/yuP/xd//wdz/vtr/xN7/v9v/utf/tdP/tNP/u9n/tdT/rs//q83/x+H/w93/vNn/qMv/0uj/z+b/y+T/x+D/wNv/qsz/2u3/2Oz/1er/0Of/s9L/sND/4PL/3/L/3fD/udf/uNb/5vb/5fb/5PX/4fP/yOH/6/r/6vn/6fj/5/f/3vD/1ur/0ef/7vv/7fv/6Pf/4/T/2+7/PQJYuQAAAAF0Uk5TAEDm2GYAAAGZSURBVHja7NfZO0JBHMbxHJxmwiGaUYSQXbJlyb5vKUtCdsmWkLIvf7szN0cPt68Lj/lenMvPc67m+b0mk0UxKjSBsigvr+nM2/X7ReJDKQChSjpz/3Cbeow9PauqgkKvb25TCULVu2g0CkMvLhOxOKHBq2QyCUNjJ/HTAKFn53owdG//4PCI0GMRDA1sR3cihO6KYOhycCOySeiWCIaurK6thwkNi4B/GgqFCA2JYOhSQI9Q8Q3AUHNWKDRPyTdSclEvSs7XKwUzvzWlGS3izOmZ4ZHZvrke67y2AEK14ZHRsYHBcc/EpN+vodC+/oFBK+P+IbfbDUN7eq0eL+N2p8/ng6GeDm+njfGubj0Y2tTc0trGeLsIhtrq3Q0uxhtFMLTcXuOqZbxOBEMrKp1V1YxXi4B/6nA4GHeIYGiZTY9x8bXB0NKsUGiJZjXSilEvStHXKwUzf1xvv3ERqka4i1DNSoGi+kUoUYn+T9RshqJ/9iKU01hOYzmN5TSW01hOYzmN5TSW01hOYzmN5eKSqJzGf+Yi/BRgAPPCjc+zY661AAAAAElFTkSuQmCC")
}

.x-slider-horz.x-slider-focus .x-slider-thumb {
    background-position: -42px -45px
}

.x-slider-horz .x-slider-thumb-over {
    background-position: -14px -15px
}

.x-slider-horz.x-slider-focus .x-slider-thumb-over {
    background-position: -56px -60px
}

.x-slider-horz .x-slider-thumb-drag {
    background-position: -28px -30px
}

.x-slider-horz.x-slider-focus .x-slider-thumb-drag {
    background-position: -70px -75px
}

.x-slider-ct-vert {
    height: 100%
}

.x-slider-vert {
    padding-top: 7px;
    background: no-repeat -30px 0;
    height: 100%
}

.x-slider-vert > .x-slider-end {
    height: 100%
}

.x-slider-vert > .x-slider-end > .x-slider-inner {
    height: 100%
}

.x-slider-vert .x-slider-end {
    padding-bottom: 7px;
    background: no-repeat -15px bottom;
    width: 15px
}

.x-slider-vert .x-slider-inner {
    width: 15px
}

.x-slider-vert .x-slider-thumb {
    width: 15px;
    height: 14px;
    margin-bottom: -7px;
    background-image: url("data:image/gif;iVBORw0KGgoAAAANSUhEUgAAAFoAAABUCAMAAAA1fNBAAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyRpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuMy1jMDExIDY2LjE0NTY2MSwgMjAxMi8wMi8wNi0xNDo1NjoyNyAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENTNiAoTWFjaW50b3NoKSIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDo4RUQ2N0YzRTBDNjExMUU0QjNDODk2QzFFQjg5MDhGMyIgeG1wTU06RG9jdW1lbnRJRD0ieG1wLmRpZDo4RUQ2N0YzRjBDNjExMUU0QjNDODk2QzFFQjg5MDhGMyI+IDx4bXBNTTpEZXJpdmVkRnJvbSBzdFJlZjppbnN0YW5jZUlEPSJ4bXAuaWlkOjhFRDY3RjNDMEM2MTExRTRCM0M4OTZDMUVCODkwOEYzIiBzdFJlZjpkb2N1bWVudElEPSJ4bXAuZGlkOjhFRDY3RjNEMEM2MTExRTRCM0M4OTZDMUVCODkwOEYzIi8+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kPSJyIj8+EcnRLgAAAX1QTFRF////oLrdl7fprsvpzuX/ss3r3fH/1Or/8v//b5TSrcrpttHuscvrnczzlMn/rN//0f//x/r/u/D/sej/qOH/pd//p+D/reT/tuv/wfP/y/z/r+H/2v//2P//zv7/t+z/xff/1P//3v//sOf/v/L/1///4P//8P//3P//4///bKLn3///5v//rOP/sun/vfH/0///4f//6P//suj/ue7/xPb/zf7/5P//6f//uO7/yfv/5///6v//vPH/xPf/zP3/1f//3f//4v//6///qt7/yfr/wvX/wfT/z///s+b/rt//yuP/vtr/tNP/q83/qMv/qsz/sND/uNb/w93/2+7/0ef/3fD/udf/yOH/1ur/4PL/s9L/wdz/2u3/4/T/3vD/5vb/4fP/6Pf/rs//tdT/wNv/1er/5PX/6vn/tdP/vNn/x+D/0Of/5/f/6/r/utf/u9n/y+T/6fj/7fv/v9v/x+H/z+b/2Oz/3/L/5fb/7vv/y+P/xd//xN7/0uj/k0jX/AAAAAF0Uk5TAEDm2GYAAAFiSURBVHja7NdXU8JAFIbhsEaxrsQORlFMVERRsWHFiiV2FBUTBUXFhr2jv11u4sb7sxeZOd8PeCazMzDnFYRywlYmQK6UOL9y3zntx0gks7A2KXJq+rP+8vr2/pH5JND06t197OE8fvH4BE9fpq+ub4zUbRaeXjtNn2n5z85A0yXmUifQdLG54ySHB1nf2DzUReOID721t3+Q4ERvx3bj3GhxB5R2EAtNCgVYm61A4LkVyrYMKs9T10J0MSotqT5/GNamsktSJpWpyPTMbGiOQtNV3lH3WJ/cPz4BTw8EB4eG1cBIGJ6u7gn2SvnPDkHTXeYC3dB0h7lOP4cHqamta1M8ajsfut7b0urjRDe4m2VutKcJlK6gFpo2CrA2WyXXP0KeF6HIBn0RilYbaa40uwjh6b+LEN/atrTj3w/drhchpjGmMaYxpjGmMaYxpjGmMaYxpjGmMdKYxkjbII1/BRgAE4SHl4mgVV0AAAAASUVORK5CYII=")
}

.x-slider-vert.x-slider-focus .x-slider-thumb {
    background-position: -45px -42px
}

.x-slider-vert .x-slider-thumb-over {
    background-position: -15px -14px
}

.x-slider-vert.x-slider-focus .x-slider-thumb-over {
    background-position: -60px -56px
}

.x-slider-vert .x-slider-thumb-drag {
    background-position: -30px -28px
}

.x-slider-vert.x-slider-focus .x-slider-thumb-drag {
    background-position: -75px -70px
}

.x-slider-horz, .x-slider-horz .x-slider-end, .x-slider-horz .x-slider-inner {
    background-image: url("data:image/gif;iVBORw0KGgoAAAANSUhEUgAAAAcAAAAtCAYAAABiZXGDAAAC/2lDQ1BJQ0MgUHJvZmlsZQAAOMuNVM1PE0EUfy3LYgLxIiI2xmw8aGOALGgUYkRbWpoC1qZ8CMTEbLfTdmW7XWe35SMcDBdvisa78SOe/AOI4eCNk4GEoDEhnjVGY4LhYrC+2Q92UfyYZHZ+895vfu/Nm50BqH8o6boaFABKmkkziagwPjEpNLyDIByFRghBoyQbeiSdHgJsjAu/te03EGDjevv+/r+2xhwxZIDAAcTlnCGXEM8A1I3JOjUBuDW0d0+bOuJ6xmmmmCDiYwwXbCwynLVxzOKMZPoQjyM+KBelHOIi4rasz17wYTsHqzUniEaoIgusFmlazisq8aX7D/d/tpJaceMdwt6km9EMjiexf8vT/lEcw1iH0Fxx5BriFsRRxUyOOPZxLZu6avMDt6fKgxmH8zxHYnG2T8TLRnU47nLmin0ph/PhpjSQRhxC/EM3045OsFVTU0O2frCXGPFh155X+pOOPa+r1n+A+sG7tJJheZ5A/FKi8YTD3yTaqLO2LpiTYoOIOxCHIQ0EKORBARUEyEACojgm0KrBR/QoIEMZWRS/LquAHtd7CyrIZSvHILoYqoQ9lQV6Q5FX733ds7rsi1KwopDdKAnf3ICpXWY76J7Cyvxyq6exwS1dX29amYcIaquWYgm7YukYPgVfDnltMeQpsAzJndR2ChbaPKv4VvwsboiPxWfipz/UqPBLjSK++MyzX/YEORPY3Qz3Z7E4CoyiV4FpK7YBEto0mEW+vucsrNXcca6TS3LdXA8I3CXuMtfLxXB2gRtyGXycj/EREPjTfA/fyQ8w7O6EP4W+HvzG95yA7Nur/wSJj0V8FWmHrFXzKWt11fIZ+AWTzJjsUvWV9VmqFIqm0CWK54UIPktESGpyR5sgqapguQyBEoPQKsl1AHvz7Ou4lbHeskDLqmczrwBc/IL/8Jpnm6wAvDAAjpz1bGG8U4cfASydkyu06tzvQOA1gJE/02XPmqL45ryv1bbwfjQ8ANi5X6t9f1Kr7TxF/U2AV+pPqSMK1r8mJ98AAAAGYktHRAD/AP8A/6C9p5MAAAAJcEhZcwAADsIAAA7CARUoSoAAAAAHdElNRQfdARkCADkuhMiSAAAArklEQVQ4y2NgGGSAcdWShf9xSbJIaRrg1MkiycuGU5IJn50szz//wi35491zhlGAL8oYGBgY9uze+f/dyxeYkof37/z/4cMHBkE5Dcyw/fDhA4OkpASDIJaowx9lAgICDM+fv2D4wSqAy0E7/o/GDSm5TFJBgcHWxp6R8cjZixiS7x/dYBAQEMCeyzgkJBiev3iBPcpY2Nhw57L3jx5BjMWWyzh5+BlsHd0ZByKEAGI1NuAucDgWAAAAAElFTkSuQmCC")
}

.x-slider-vert, .x-slider-vert .x-slider-end, .x-slider-vert .x-slider-inner {
    background-image: url("data:image/gif;iVBORw0KGgoAAAANSUhEUgAAAC0AAAAHBAMAAABuA9n5AAAAJFBMVEUAAACqpKHEzdHd2te8u7jDv7mzr6m8u7nMyMHDxMHMx8HQzcdjeKXgAAAAAXRSTlMAQObYZgAAAAFiS0dEAIgFHUgAAAAJcEhZcwAADsIAAA7CARUoSoAAAAAHdElNRQfdARkCAQf2/uR4AAAAMUlEQVQI12NgYGBUNnJgAAIhYxUQxRCWCqbQxTmztjlgE4dxyRYv60jBKs6aFoDgAgBANQ1XOBp0OAAAAABJRU5ErkJggg==")
}

.x-slider-default-cell > .x-grid-cell-inner, .x-sliderwidget-default-cell > .x-grid-cell-inner {
    padding-top: 0;
    padding-bottom: 0px
}

.x-tab-default-top {
    -moz-border-radius-topleft: 4px;
    -webkit-border-top-left-radius: 4px;
    border-top-left-radius: 4px;
    -moz-border-radius-topright: 4px;
    -webkit-border-top-right-radius: 4px;
    border-top-right-radius: 4px;
    -moz-border-radius-bottomright: 0;
    -webkit-border-bottom-right-radius: 0;
    border-bottom-right-radius: 0;
    -moz-border-radius-bottomleft: 0;
    -webkit-border-bottom-left-radius: 0;
    border-bottom-left-radius: 0;
    padding: 3px 9px 3px 9px;
    border-width: 1px 1px 0;
    border-style: solid;
    background-image: none;
    background-color: #deecfd;
    background-image: -webkit-gradient(linear, top, bottom, color-stop(0%, #ccdef6), color-stop(25%, #d6e6fa), color-stop(45%, #deecfd));
    background-image: -webkit-linear-gradient(top, #ccdef6, #d6e6fa 25%, #deecfd 45%);
    background-image: -moz-linear-gradient(top, #ccdef6, #d6e6fa 25%, #deecfd 45%);
    background-image: -o-linear-gradient(top, #ccdef6, #d6e6fa 25%, #deecfd 45%);
    background-image: -ms-linear-gradient(top, #ccdef6, #d6e6fa 25%, #deecfd 45%);
    background-image: linear-gradient(top, #ccdef6, #d6e6fa 25%, #deecfd 45%)
}

.x-tab-default-top-mc {
    background-image: url("data:image/gif;R0lGODlhAQAgA/MAANLj+NTk+dbm+tfn+tno+9vq/N3r/N7s/f///9Lj+NLj+NLj+NLj+NLj+NLj+NLj+CH5BAEAAAgALAAAAAABACADQwg6AAEcGEiwoMGDCBMqXMiwocOEBB5KnEixokUBBixq3Mixo8ePICsGGFAgpMmTKFOqXMmypcuXMBEGBAA7");
    background-position: 0 top;
    background-color: #deecfd
}

.x-nbr .x-tab-default-top {
    padding: 0 !important;
    border-width: 0 !important;
    -webkit-border-radius: 0px;
    -moz-border-radius: 0px;
    -ms-border-radius: 0px;
    -o-border-radius: 0px;
    border-radius: 0px;
    background-color: transparent !important;
    background-image: none;
    box-shadow: none !important
}

.x-tab-default-top-frameInfo {
    font-family: th-4-4-0-4-1-1-0-1-3-9-3-9
}

.x-tab-default-top-tl {
    background-position: 0 -8px
}

.x-tab-default-top-tr {
    background-position: right -12px
}

.x-tab-default-top-bl {
    background-position: 0 -16px
}

.x-tab-default-top-br {
    background-position: right -20px
}

.x-tab-default-top-ml {
    background-position: 0 top
}

.x-tab-default-top-mr {
    background-position: right top
}

.x-tab-default-top-tc {
    background-position: 0 0
}

.x-tab-default-top-bc {
    background-position: 0 -4px
}

.x-tab-default-top-tr, .x-tab-default-top-br, .x-tab-default-top-mr {
    padding-right: 4px
}

.x-tab-default-top-tl, .x-tab-default-top-bl, .x-tab-default-top-ml {
    padding-left: 4px
}

.x-tab-default-top-tc {
    height: 4px
}

.x-tab-default-top-bc {
    height: 0
}

.x-tab-default-top-tl, .x-tab-default-top-bl, .x-tab-default-top-tr, .x-tab-default-top-br, .x-tab-default-top-tc, .x-tab-default-top-bc, .x-tab-default-top-ml, .x-tab-default-top-mr {
    background-image: url("data:image/gif;R0lGODlhBAAYAPQAAI2z45e65Zi65Z2957PM7c7g99Dh99Pj+NXk+N7s/e70+/H2/fL2/Pz9/v///////wAAAI2z442z442z442z442z442z442z442z442z442z442z442z442z442z442z4yH5BAEAAA8ALAAAAAAEABgARAhMAAEIBPCAAYEAABwkWMgwAAEGDxY6AFCgYgGGCQgoWHDgwAIFBBJinOigpAMDKA1gxMhggIIGARogMNBAwQAGBhA0ECAyQU+JAIAGBAA7")
}

.x-tab-default-top-ml, .x-tab-default-top-mr {
    background-image: url("data:image/gif;R0lGODlhCAAgA/MAAI2z49Lj+NTk+dbm+tfn+tno+9vq/N3r/N7s/f///////42z442z442z442z442z4yH5BAEAAAoALAAAAAAIACADQwj/AAEkCEAwQAIAAhEoRHAw4cKGCRYyRBjxIUWJEDFetOhQYUaOFT1uFNlxYsmPJEOaVIlypcaTI12CfMkyZsubNnPC3FmTJ82fM4OmBDpUqMyiSI8qxenTKNOeUIku1RnVKVWpT7Fetdo0aVauVb1uFdt1atmvZMOaVYt2rVaBBeIWaEt3rFuwb9narXt2r9++gPUGzksYr+G0hREfvqu4MePHfAVLTgz57+TFkSlnxmxZc2fOg0EOGD0A4oHTBzY7Vl059OrPr123vhyb9mzPslnrhn0btO3duXkD/y28ePDjxJHjTs58uXPfz2tH7y0duvXq2KlrHz6d+/Xtxpt/jfeenTx45ePDd6cooL0AiATiE4BooL4B8/jVp0dfXn9//ueJ95+AAa4HYH4H+lfgfgQi2KCCDhr4YIIUTmihhBgymOGAGy7IoYYgfiiihyRGGGKJEKZYYYcmjtgiiiue+OKMKl4oY40s4nhjjC7q2COPMNr4o5BB5ggkjUf6WOSORCLZpJJOGvlkkn0FBAA7")
}

.x-tab-default-top-mc {
    padding: 0px 6px 3px 6px
}

.x-cmd-slicer.x-tab-default-top:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:4px 4px 0 4px, frame-bg:url("data:image/gif;R0lGODlhAQAgA/MAANLj+NTk+dbm+tfn+tno+9vq/N3r/N7s/f///9Lj+NLj+NLj+NLj+NLj+NLj+NLj+CH5BAEAAAgALAAAAAABACADQwg6AAEcGEiwoMGDCBMqXMiwocOEBB5KnEixokUBBixq3Mixo8ePICsGGFAgpMmTKFOqXMmypcuXMBEGBAA7"), corners:url("data:image/gif;R0lGODlhBAAYAPQAAI2z45e65Zi65Z2957PM7c7g99Dh99Pj+NXk+N7s/e70+/H2/fL2/Pz9/v///////wAAAI2z442z442z442z442z442z442z442z442z442z442z442z442z442z442z4yH5BAEAAA8ALAAAAAAEABgARAhMAAEIBPCAAYEAABwkWMgwAAEGDxY6AFCgYgGGCQgoWHDgwAIFBBJinOigpAMDKA1gxMhggIIGARogMNBAwQAGBhA0ECAyQU+JAIAGBAA7"), sides:url("data:image/gif;R0lGODlhCAAgA/MAAI2z49Lj+NTk+dbm+tfn+tno+9vq/N3r/N7s/f///////42z442z442z442z442z4yH5BAEAAAoALAAAAAAIACADQwj/AAEkCEAwQAIAAhEoRHAw4cKGCRYyRBjxIUWJEDFetOhQYUaOFT1uFNlxYsmPJEOaVIlypcaTI12CfMkyZsubNnPC3FmTJ82fM4OmBDpUqMyiSI8qxenTKNOeUIku1RnVKVWpT7Fetdo0aVauVb1uFdt1atmvZMOaVYt2rVaBBeIWaEt3rFuwb9narXt2r9++gPUGzksYr+G0hREfvqu4MePHfAVLTgz57+TFkSlnxmxZc2fOg0EOGD0A4oHTBzY7Vl059OrPr123vhyb9mzPslnrhn0btO3duXkD/y28ePDjxJHjTs58uXPfz2tH7y0duvXq2KlrHz6d+/Xtxpt/jfeenTx45ePDd6cooL0AiATiE4BooL4B8/jVp0dfXn9//ueJ95+AAa4HYH4H+lfgfgQi2KCCDhr4YIIUTmihhBgymOGAGy7IoYYgfiiihyRGGGKJEKZYYYcmjtgiiiue+OKMKl4oY40s4nhjjC7q2COPMNr4o5BB5ggkjUf6WOSORCLZpJJOGvlkkn0FBAA7")" !important
}

.x-tab-default-bottom {
    -moz-border-radius-topleft: 0;
    -webkit-border-top-left-radius: 0;
    border-top-left-radius: 0;
    -moz-border-radius-topright: 0;
    -webkit-border-top-right-radius: 0;
    border-top-right-radius: 0;
    -moz-border-radius-bottomright: 4px;
    -webkit-border-bottom-right-radius: 4px;
    border-bottom-right-radius: 4px;
    -moz-border-radius-bottomleft: 4px;
    -webkit-border-bottom-left-radius: 4px;
    border-bottom-left-radius: 4px;
    padding: 4px 9px 3px 9px;
    border-width: 0 1px 1px 1px;
    border-style: solid;
    background-image: none;
    background-color: #deecfd;
    background-image: -webkit-gradient(linear, top, bottom, color-stop(0%, #ccdef6), color-stop(25%, #d6e6fa), color-stop(45%, #deecfd));
    background-image: -webkit-linear-gradient(bottom, #ccdef6, #d6e6fa 25%, #deecfd 45%);
    background-image: -moz-linear-gradient(bottom, #ccdef6, #d6e6fa 25%, #deecfd 45%);
    background-image: -o-linear-gradient(bottom, #ccdef6, #d6e6fa 25%, #deecfd 45%);
    background-image: -ms-linear-gradient(bottom, #ccdef6, #d6e6fa 25%, #deecfd 45%);
    background-image: linear-gradient(bottom, #ccdef6, #d6e6fa 25%, #deecfd 45%)
}

.x-tab-default-bottom-mc {
    background-image: url("data:image/gif;R0lGODlhAQAgA/MAANLi+NPk+dXl+dfm+tno+9rp+9zq/N7s/f///9Li+NLi+NLi+NLi+NLi+NLi+NLi+CH5BAEAAAgALAAAAAABACADQwg5AA8IHEiwoMGDCBMqXMiwocOHECNKnJhwAMWLGDNq3Mixo8ICATyKHEmypMmTKFOqXGnSAAEBAAICADs=");
    background-position: 0 bottom;
    background-color: #deecfd
}

.x-nbr .x-tab-default-bottom {
    padding: 0 !important;
    border-width: 0 !important;
    -webkit-border-radius: 0px;
    -moz-border-radius: 0px;
    -ms-border-radius: 0px;
    -o-border-radius: 0px;
    border-radius: 0px;
    background-color: transparent !important;
    background-image: none;
    box-shadow: none !important
}

.x-tab-default-bottom-frameInfo {
    font-family: th-4-4-4-4-0-1-1-1-4-9-3-9
}

.x-tab-default-bottom-tl {
    background-position: 0 -8px
}

.x-tab-default-bottom-tr {
    background-position: right -12px
}

.x-tab-default-bottom-bl {
    background-position: 0 -16px
}

.x-tab-default-bottom-br {
    background-position: right -20px
}

.x-tab-default-bottom-ml {
    background-position: 0 bottom
}

.x-tab-default-bottom-mr {
    background-position: right bottom
}

.x-tab-default-bottom-tc {
    background-position: 0 0
}

.x-tab-default-bottom-bc {
    background-position: 0 -4px
}

.x-tab-default-bottom-tr, .x-tab-default-bottom-br, .x-tab-default-bottom-mr {
    padding-right: 4px
}

.x-tab-default-bottom-tl, .x-tab-default-bottom-bl, .x-tab-default-bottom-ml {
    padding-left: 4px
}

.x-tab-default-bottom-tc {
    height: 4px
}

.x-tab-default-bottom-bc {
    height: 4px
}

.x-tab-default-bottom-tl, .x-tab-default-bottom-bl, .x-tab-default-bottom-tr, .x-tab-default-bottom-br, .x-tab-default-bottom-tc, .x-tab-default-bottom-bc, .x-tab-default-bottom-ml, .x-tab-default-bottom-mr {
    background-image: url("data:image/gif;R0lGODlhBAAYAPQAAI2z45e65Zi65Z2955696LPM7c7g99Dh99Pj+NXk+N7s/e70+/H2/fL2/Pz9/v///////wAAAI2z442z442z442z442z442z442z442z442z442z442z442z442z442z4yH5BAEAABAALAAAAAAEABgARAhLABUIVADggcAADhIcWLhQ4AMABxI4EDBQwYOLDw0OfNhgwAIHDhYQaFCxooGTBgCoVKmxYMWHDgEUWMAAAYQGBQQgYLAgZ4EGEAICADs=")
}

.x-tab-default-bottom-ml, .x-tab-default-bottom-mr {
    background-image: url("data:image/gif;R0lGODlhCAAgA/MAAI2z49Li+NPk+dXl+dfm+tno+9rp+9zq/N7s/f///////42z442z442z442z442z4yH5BAEAAAoALAAAAAAIACADQwj/AAEkQEAQQQIAAgsaRDiw4MGEDhkqfNiQIMWJEiNCtJiR48aFHy9qrAiSpEiPJjuWxBhS5cmVI1mmbElzpk2ZOGPqRJmT506YPoMCHfqyqMujNXsSRXrzp9GkTpkqfdpUKNWpUqNCtZqV69alX69qrQqWrFivZruWxRpW7dm1Y9mmbUt3rl25eOPqRZuX7164fgMDHvy2sNvDdfsSRnz3r+HEjhkrftxYMOXJkscS2EzgcmTIljOHBr2YtOfRlUunPq0as2nRrT+vhs26Nu3br3PP1u16t+/ewGUHRz08NnHhyI8rN87cNu/kzXH/hu58+vLqxbFTl56d+3aBBsIbjaAooLwA7de9p3++3np09u/do4/fHf78++rpf5efH7/9/gD+JyB/A9ZH4IEGJrifgu0xqF+DC0YI4YQPVugfghJaGCCGFF7ooIcZgtjhhh+SGKKJIxZ4ooopcqghiy+6KGKMJcI4440o0riijDniaGOPQP4oJI81HWDkARQVoGQBFA3g5AAUBSBlAAcFBAA7")
}

.x-tab-default-bottom-mc {
    padding: 0px 6px 0px 6px
}

.x-cmd-slicer.x-tab-default-bottom:before {
    display: none;
    content: "x-slicer:, stretch:top, frame:4px 4px 4px 4px, frame-bg:url("data:image/gif;R0lGODlhAQAgA/MAANLi+NPk+dXl+dfm+tno+9rp+9zq/N7s/f///9Li+NLi+NLi+NLi+NLi+NLi+NLi+CH5BAEAAAgALAAAAAABACADQwg5AA8IHEiwoMGDCBMqXMiwocOHECNKnJhwAMWLGDNq3Mixo8ICATyKHEmypMmTKFOqXGnSAAEBAAICADs="), corners:url("data:image/gif;R0lGODlhBAAYAPQAAI2z45e65Zi65Z2955696LPM7c7g99Dh99Pj+NXk+N7s/e70+/H2/fL2/Pz9/v///////wAAAI2z442z442z442z442z442z442z442z442z442z442z442z442z442z4yH5BAEAABAALAAAAAAEABgARAhLABUIVADggcAADhIcWLhQ4AMABxI4EDBQwYOLDw0OfNhgwAIHDhYQaFCxooGTBgCoVKmxYMWHDgEUWMAAAYQGBQQgYLAgZ4EGEAICADs="), sides:url("data:image/gif;R0lGODlhCAAgA/MAAI2z49Li+NPk+dXl+dfm+tno+9rp+9zq/N7s/f///////42z442z442z442z442z4yH5BAEAAAoALAAAAAAIACADQwj/AAEkQEAQQQIAAgsaRDiw4MGEDhkqfNiQIMWJEiNCtJiR48aFHy9qrAiSpEiPJjuWxBhS5cmVI1mmbElzpk2ZOGPqRJmT506YPoMCHfqyqMujNXsSRXrzp9GkTpkqfdpUKNWpUqNCtZqV69alX69qrQqWrFivZruWxRpW7dm1Y9mmbUt3rl25eOPqRZuX7164fgMDHvy2sNvDdfsSRnz3r+HEjhkrftxYMOXJkscS2EzgcmTIljOHBr2YtOfRlUunPq0as2nRrT+vhs26Nu3br3PP1u16t+/ewGUHRz08NnHhyI8rN87cNu/kzXH/hu58+vLqxbFTl56d+3aBBsIbjaAooLwA7de9p3++3np09u/do4/fHf78++rpf5efH7/9/gD+JyB/A9ZH4IEGJrifgu0xqF+DC0YI4YQPVugfghJaGCCGFF7ooIcZgtjhhh+SGKKJIxZ4ooopcqghiy+6KGKMJcI4440o0riijDniaGOPQP4oJI81HWDkARQVoGQBFA3g5AAUBSBlAAcFBAA7")" !important
}

.x-tab-default-left {
    -moz-border-radius-topleft: 4px;
    -webkit-border-top-left-radius: 4px;
    border-top-left-radius: 4px;
    -moz-border-radius-topright: 0;
    -webkit-border-top-right-radius: 0;
    border-top-right-radius: 0;
    -moz-border-radius-bottomright: 0;
    -webkit-border-bottom-right-radius: 0;
    border-bottom-right-radius: 0;
    -moz-border-radius-bottomleft: 4px;
    -webkit-border-bottom-left-radius: 4px;
    border-bottom-left-radius: 4px;
    padding: 3px 9px 3px 9px;
    border-width: 1px 0 1px 1px;
    border-style: solid;
    background-image: none;
    background-color: #deecfd;
    background-image: -webkit-gradient(linear, top, bottom, color-stop(0%, #ccdef6), color-stop(25%, #d6e6fa), color-stop(45%, #deecfd));
    background-image: -webkit-linear-gradient(top, #ccdef6, #d6e6fa 25%, #deecfd 45%);
    background-image: -moz-linear-gradient(top, #ccdef6, #d6e6fa 25%, #deecfd 45%);
    background-image: -o-linear-gradient(top, #ccdef6, #d6e6fa 25%, #deecfd 45%);
    background-image: -ms-linear-gradient(top, #ccdef6, #d6e6fa 25%, #deecfd 45%);
    background-image: linear-gradient(top, #ccdef6, #d6e6fa 25%, #deecfd 45%)
}

.x-tab-default-left-mc {
    background-image: url("data:image/gif;R0lGODlhAQAgA/MAANLj+NTk+dbm+tfn+tno+9vq/N3r/N7s/f///9Lj+NLj+NLj+NLj+NLj+NLj+NLj+CH5BAEAAAgALAAAAAABACADQwg6AAEcGEiwoMGDCBMqXMiwocOEBB5KnEixokUBBixq3Mixo8ePICsGGFAgpMmTKFOqXMmypcuXMBEGBAA7");
    background-position: 0 top;
    background-color: #deecfd
}

.x-nbr .x-tab-default-left {
    padding: 0 !important;
    border-width: 0 !important;
    -webkit-border-radius: 0px;
    -moz-border-radius: 0px;
    -ms-border-radius: 0px;
    -o-border-radius: 0px;
    border-radius: 0px;
    background-color: transparent !important;
    background-image: none;
    box-shadow: none !important
}

.x-tab-default-left-frameInfo {
    font-family: th-4-4-4-4-1-0-1-1-3-9-3-9
}

.x-tab-default-left-tl {
    background-position: 0 -8px
}

.x-tab-default-left-tr {
    background-position: right -12px
}

.x-tab-default-left-bl {
    background-position: 0 -16px
}

.x-tab-default-left-br {
    background-position: right -20px
}

.x-tab-default-left-ml {
    background-position: 0 top
}

.x-tab-default-left-mr {
    background-position: right top
}

.x-tab-default-left-tc {
    background-position: 0 0
}

.x-tab-default-left-bc {
    background-position: 0 -4px
}

.x-tab-default-left-tr, .x-tab-default-left-br, .x-tab-default-left-mr {
    padding-right: 4px
}

.x-tab-default-left-tl, .x-tab-default-left-bl, .x-tab-default-left-ml {
    padding-left: 4px
}

.x-tab-default-left-tc {
    height: 4px
}

.x-tab-default-left-bc {
    height: 4px
}

.x-tab-default-left-tl, .x-tab-default-left-bl, .x-tab-default-left-tr, .x-tab-default-left-br, .x-tab-default-left-tc, .x-tab-default-left-bc, .x-tab-default-left-ml, .x-tab-default-left-mr {
    background-image: url("data:image/gif;R0lGODlhBAAYAPQAAI2z45e65Zi65Zu75p2857PM7c7g99Dh99Pj+NXk+N7q+N7s/eHr+eHu/efx/O31/u70+/H2/fL2/Pv9//z9/v///////wAAAI2z442z442z442z442z442z442z442z4yH5BAEAABYALAAAAAAEABgARAhHAAEIBGBBQoEAASY0WMCQ4UAADRcYmGhgIcMCECIgoGhAwgAFDiJWGFnhgMkDER9KIACBQgAKCQ6QLHmyAIMHCwoWEJByYEAAOw==")
}

.x-tab-default-left-ml, .x-tab-default-left-mr {
    background-image: url("data:image/gif;R0lGODlhCAAgA/MAAI2z49Lj+NTk+dbm+tfn+tno+9vq/N3r/N7s/f///////42z442z442z442z442z4yH5BAEAAAoALAAAAAAIACADQwj/AAEkCECwoEAECBMeTIhwIUOHChMwbChxIkSKExFc1FjxYceIGTeK/IjRIkmOIU+OTMnSZEuPL0G6nAmTpsyaOG/qLJmT506UNn0KBdqT6M+VQY0ORVqU6VGVUGMujZrU6VSpSrNa1Uq1adenWLeK/Xq1KlmuKQuoXTs27Nm2Zt3KjUvX61y7dcHmLYu3r16/fP8KDkwY7V7DgBEPVlwYbmLHiyE3fkv5buTKhyVzHMC5s8ADoENrHo35cenLlienZsya9GrXmU+rjv1admvbsE3X3k27t27fqIHP/k08ePHhxpMjX36b9/HmwqE/z61cenXqzLFbz467u/Pr3qNrgyctoLx5gQTSqxdooL378eGnxwf/nXv97fjh39cvfr79/vv5l5+A/MkX4IEAJmiggvQx+N+CEDYY4YMSVkjhhQMiOGGGDnK4YYEWehgiiBiSKGKJBKao4Ygqdmjiiy1+GCOLK6JY44k4wnijji7OaGOPO/qYo5A8yhjkkUAmaaSSiwUEADs=")
}

.x-tab-default-left-mc {
    padding: 0px 5px 0px 6px
}

.x-cmd-slicer.x-tab-default-left:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:4px 4px 4px 4px, frame-bg:url("data:image/gif;R0lGODlhAQAgA/MAANLj+NTk+dbm+tfn+tno+9vq/N3r/N7s/f///9Lj+NLj+NLj+NLj+NLj+NLj+NLj+CH5BAEAAAgALAAAAAABACADQwg6AAEcGEiwoMGDCBMqXMiwocOEBB5KnEixokUBBixq3Mixo8ePICsGGFAgpMmTKFOqXMmypcuXMBEGBAA7"), corners:url("data:image/gif;R0lGODlhBAAYAPQAAI2z45e65Zi65Zu75p2857PM7c7g99Dh99Pj+NXk+N7q+N7s/eHr+eHu/efx/O31/u70+/H2/fL2/Pv9//z9/v///////wAAAI2z442z442z442z442z442z442z442z4yH5BAEAABYALAAAAAAEABgARAhHAAEIBGBBQoEAASY0WMCQ4UAADRcYmGhgIcMCECIgoGhAwgAFDiJWGFnhgMkDER9KIACBQgAKCQ6QLHmyAIMHCwoWEJByYEAAOw=="), sides:url("data:image/gif;R0lGODlhCAAgA/MAAI2z49Lj+NTk+dbm+tfn+tno+9vq/N3r/N7s/f///////42z442z442z442z442z4yH5BAEAAAoALAAAAAAIACADQwj/AAEkCECwoEAECBMeTIhwIUOHChMwbChxIkSKExFc1FjxYceIGTeK/IjRIkmOIU+OTMnSZEuPL0G6nAmTpsyaOG/qLJmT506UNn0KBdqT6M+VQY0ORVqU6VGVUGMujZrU6VSpSrNa1Uq1adenWLeK/Xq1KlmuKQuoXTs27Nm2Zt3KjUvX61y7dcHmLYu3r16/fP8KDkwY7V7DgBEPVlwYbmLHiyE3fkv5buTKhyVzHMC5s8ADoENrHo35cenLlienZsya9GrXmU+rjv1admvbsE3X3k27t27fqIHP/k08ePHhxpMjX36b9/HmwqE/z61cenXqzLFbz467u/Pr3qNrgyctoLx5gQTSqxdooL378eGnxwf/nXv97fjh39cvfr79/vv5l5+A/MkX4IEAJmiggvQx+N+CEDYY4YMSVkjhhQMiOGGGDnK4YYEWehgiiBiSKGKJBKao4Ygqdmjiiy1+GCOLK6JY44k4wnijji7OaGOPO/qYo5A8yhjkkUAmaaSSiwUEADs=")" !important
}

.x-tab-default-right {
    -moz-border-radius-topleft: 0;
    -webkit-border-top-left-radius: 0;
    border-top-left-radius: 0;
    -moz-border-radius-topright: 4px;
    -webkit-border-top-right-radius: 4px;
    border-top-right-radius: 4px;
    -moz-border-radius-bottomright: 4px;
    -webkit-border-bottom-right-radius: 4px;
    border-bottom-right-radius: 4px;
    -moz-border-radius-bottomleft: 0;
    -webkit-border-bottom-left-radius: 0;
    border-bottom-left-radius: 0;
    padding: 3px 9px 3px 9px;
    border-width: 1px 1px 1px 0;
    border-style: solid;
    background-image: none;
    background-color: #deecfd;
    background-image: -webkit-gradient(linear, top, bottom, color-stop(0%, #ccdef6), color-stop(25%, #d6e6fa), color-stop(45%, #deecfd));
    background-image: -webkit-linear-gradient(top, #ccdef6, #d6e6fa 25%, #deecfd 45%);
    background-image: -moz-linear-gradient(top, #ccdef6, #d6e6fa 25%, #deecfd 45%);
    background-image: -o-linear-gradient(top, #ccdef6, #d6e6fa 25%, #deecfd 45%);
    background-image: -ms-linear-gradient(top, #ccdef6, #d6e6fa 25%, #deecfd 45%);
    background-image: linear-gradient(top, #ccdef6, #d6e6fa 25%, #deecfd 45%)
}

.x-tab-default-right-mc {
    background-image: url("data:image/gif;R0lGODlhAQAgA/MAANLj+NTk+dbm+tfn+tno+9vq/N3r/N7s/f///9Lj+NLj+NLj+NLj+NLj+NLj+NLj+CH5BAEAAAgALAAAAAABACADQwg6AAEcGEiwoMGDCBMqXMiwocOEBB5KnEixokUBBixq3Mixo8ePICsGGFAgpMmTKFOqXMmypcuXMBEGBAA7");
    background-position: 0 top;
    background-color: #deecfd
}

.x-nbr .x-tab-default-right {
    padding: 0 !important;
    border-width: 0 !important;
    -webkit-border-radius: 0px;
    -moz-border-radius: 0px;
    -ms-border-radius: 0px;
    -o-border-radius: 0px;
    border-radius: 0px;
    background-color: transparent !important;
    background-image: none;
    box-shadow: none !important
}

.x-tab-default-right-frameInfo {
    font-family: th-4-4-4-4-1-1-1-0-3-9-3-9
}

.x-tab-default-right-tl {
    background-position: 0 -8px
}

.x-tab-default-right-tr {
    background-position: right -12px
}

.x-tab-default-right-bl {
    background-position: 0 -16px
}

.x-tab-default-right-br {
    background-position: right -20px
}

.x-tab-default-right-ml {
    background-position: 0 top
}

.x-tab-default-right-mr {
    background-position: right top
}

.x-tab-default-right-tc {
    background-position: 0 0
}

.x-tab-default-right-bc {
    background-position: 0 -4px
}

.x-tab-default-right-tr, .x-tab-default-right-br, .x-tab-default-right-mr {
    padding-right: 4px
}

.x-tab-default-right-tl, .x-tab-default-right-bl, .x-tab-default-right-ml {
    padding-left: 4px
}

.x-tab-default-right-tc {
    height: 4px
}

.x-tab-default-right-bc {
    height: 4px
}

.x-tab-default-right-tl, .x-tab-default-right-bl, .x-tab-default-right-tr, .x-tab-default-right-br, .x-tab-default-right-tc, .x-tab-default-right-bc, .x-tab-default-right-ml, .x-tab-default-right-mr {
    background-image: url("data:image/gif;R0lGODlhBAAYAPQAAI2z45e65Zi65Zu75p2857PM7c7g99Dh99Pj+NXk+N7q+N7s/eHr+eHu/efx/O31/u70+/H2/fL2/Pv9//z9/v///////wAAAI2z442z442z442z442z442z442z442z4yH5BAEAABYALAAAAAAEABgARAhFAAEIHChwgcGDBgMUkGBhQYMJAgxINIBwogEEESAUQOhAwQAJFUJWOEDyAEKCIkeWpACBgIQDCSgIODlwwQMGBQQstBAQADs=")
}

.x-tab-default-right-ml, .x-tab-default-right-mr {
    background-image: url("data:image/gif;R0lGODlhCAAgA/MAAI2z49Lj+NTk+dbm+tfn+tno+9vq/N3r/N7s/f///////42z442z442z442z442z4yH5BAEAAAoALAAAAAAIACADQwj/AAMIHJgAAIKDCAsiTGhwIQKFDiEulMjQ4cOGEzFWjKjxIEWPHS9a/CiS48iQJFOiXHmypcmXGV3GhLlxps2aOEHKzFnypk6aP3325KlyZ1CiLIEOPcp0qdOiSqEKlYrU6NOkU7FWjaq1KVWvXa9a/SqW69iVBdKqJcs2bNuzcM3KzRqX7tytdvPi3Qu2Lt+yevveFRwY8N+3gw0TPuy2sd/FkBVLRlyYMuPHk1cO2My54IHPoC1HFp0ZM+nTjhOjNp26cuvLql+Pll06NuvbtnO7xr1bN+zewH8Ln817eO3gxH0nR37c+GrlzZc7p/2cefXpxaVrj879+nbv3amLghdAvnxBAujTFzTAvj349+Kzh5cPn3586PXx37e+H7t++wD+JyB/ARI4oH8GJojggt/112CBDM534IMTSqgghRdaGGF+GXK4oYMaYvghhCKWGOKJHpqYIoogruhiizCSyKKML9IYY4U14nhjhzuOqKONQP4oJI9BEjmkj0YmiSRDAQEAOw==")
}

.x-tab-default-right-mc {
    padding: 0px 6px 0px 5px
}

.x-cmd-slicer.x-tab-default-right:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:4px 4px 4px 4px, frame-bg:url("data:image/gif;R0lGODlhAQAgA/MAANLj+NTk+dbm+tfn+tno+9vq/N3r/N7s/f///9Lj+NLj+NLj+NLj+NLj+NLj+NLj+CH5BAEAAAgALAAAAAABACADQwg6AAEcGEiwoMGDCBMqXMiwocOEBB5KnEixokUBBixq3Mixo8ePICsGGFAgpMmTKFOqXMmypcuXMBEGBAA7"), corners:url("data:image/gif;R0lGODlhBAAYAPQAAI2z45e65Zi65Zu75p2857PM7c7g99Dh99Pj+NXk+N7q+N7s/eHr+eHu/efx/O31/u70+/H2/fL2/Pv9//z9/v///////wAAAI2z442z442z442z442z442z442z442z4yH5BAEAABYALAAAAAAEABgARAhFAAEIHChwgcGDBgMUkGBhQYMJAgxINIBwogEEESAUQOhAwQAJFUJWOEDyAEKCIkeWpACBgIQDCSgIODlwwQMGBQQstBAQADs="), sides:url("data:image/gif;R0lGODlhCAAgA/MAAI2z49Lj+NTk+dbm+tfn+tno+9vq/N3r/N7s/f///////42z442z442z442z442z4yH5BAEAAAoALAAAAAAIACADQwj/AAMIHJgAAIKDCAsiTGhwIQKFDiEulMjQ4cOGEzFWjKjxIEWPHS9a/CiS48iQJFOiXHmypcmXGV3GhLlxps2aOEHKzFnypk6aP3325KlyZ1CiLIEOPcp0qdOiSqEKlYrU6NOkU7FWjaq1KVWvXa9a/SqW69iVBdKqJcs2bNuzcM3KzRqX7tytdvPi3Qu2Lt+yevveFRwY8N+3gw0TPuy2sd/FkBVLRlyYMuPHk1cO2My54IHPoC1HFp0ZM+nTjhOjNp26cuvLql+Pll06NuvbtnO7xr1bN+zewH8Ln817eO3gxH0nR37c+GrlzZc7p/2cefXpxaVrj879+nbv3amLghdAvnxBAujTFzTAvj349+Kzh5cPn3586PXx37e+H7t++wD+JyB/ARI4oH8GJojggt/112CBDM534IMTSqgghRdaGGF+GXK4oYMaYvghhCKWGOKJHpqYIoogruhiizCSyKKML9IYY4U14nhjhzuOqKONQP4oJI9BEjmkj0YmiSRDAQEAOw==")" !important
}

.x-tab-default {
    border-color: #8db3e3;
    cursor: pointer;
    -webkit-box-shadow: #fff 0 1px 0px 0 inset, #fff -1px 0 0px 0 inset, #fff 1px 0 0px 0 inset;
    -moz-box-shadow: #fff 0 1px 0px 0 inset, #fff -1px 0 0px 0 inset, #fff 1px 0 0px 0 inset;
    box-shadow: #fff 0 1px 0px 0 inset, #fff -1px 0 0px 0 inset, #fff 1px 0 0px 0 inset
}

.x-tab-default-top {
    margin: 0 0 0 2px;
    -webkit-box-shadow: #fff 0 1px 0px 0 inset, #fff -1px 0 0px 0 inset, #fff 1px 0 0px 0 inset;
    -moz-box-shadow: #fff 0 1px 0px 0 inset, #fff -1px 0 0px 0 inset, #fff 1px 0 0px 0 inset;
    box-shadow: #fff 0 1px 0px 0 inset, #fff -1px 0 0px 0 inset, #fff 1px 0 0px 0 inset
}

.x-tab-default-top.x-tab-rotate-left {
    margin: 0 2px 0 0
}

.x-tab-default-top.x-tab-focus {
    -webkit-box-shadow: #fff 0 1px 0px 0 inset, #fff -1px 0 0px 0 inset, #fff 1px 0 0px 0 inset;
    -moz-box-shadow: #fff 0 1px 0px 0 inset, #fff -1px 0 0px 0 inset, #fff 1px 0 0px 0 inset;
    box-shadow: #fff 0 1px 0px 0 inset, #fff -1px 0 0px 0 inset, #fff 1px 0 0px 0 inset
}

.x-tab-default-top.x-tab-over {
    -webkit-box-shadow: #fff 0 1px 0px 0 inset, #fff -1px 0 0px 0 inset, #fff 1px 0 0px 0 inset;
    -moz-box-shadow: #fff 0 1px 0px 0 inset, #fff -1px 0 0px 0 inset, #fff 1px 0 0px 0 inset;
    box-shadow: #fff 0 1px 0px 0 inset, #fff -1px 0 0px 0 inset, #fff 1px 0 0px 0 inset
}

.x-tab-default-top.x-tab.x-tab-active {
    -webkit-box-shadow: #fff 0 1px 0px 0 inset, #fff -1px 0 0px 0 inset, #fff 1px 0 0px 0 inset;
    -moz-box-shadow: #fff 0 1px 0px 0 inset, #fff -1px 0 0px 0 inset, #fff 1px 0 0px 0 inset;
    box-shadow: #fff 0 1px 0px 0 inset, #fff -1px 0 0px 0 inset, #fff 1px 0 0px 0 inset
}

.x-tab-default-top.x-tab.x-tab-disabled {
    -webkit-box-shadow: #fff 0 1px 0px 0 inset, #fff -1px 0 0px 0 inset, #fff 1px 0 0px 0 inset;
    -moz-box-shadow: #fff 0 1px 0px 0 inset, #fff -1px 0 0px 0 inset, #fff 1px 0 0px 0 inset;
    box-shadow: #fff 0 1px 0px 0 inset, #fff -1px 0 0px 0 inset, #fff 1px 0 0px 0 inset
}

.x-tab-default-right {
    margin: 2px 0 0 0;
    -webkit-box-shadow: #fff 0 1px 0px 0 inset, #fff -1px 0 0px 0 inset;
    -moz-box-shadow: #fff 0 1px 0px 0 inset, #fff -1px 0 0px 0 inset;
    box-shadow: #fff 0 1px 0px 0 inset, #fff -1px 0 0px 0 inset
}

.x-tab-default-right.x-tab-rotate-right {
    margin: 0 0 2px 0
}

.x-tab-default-right.x-tab-focus {
    -webkit-box-shadow: #fff 0 1px 0px 0 inset, #fff -1px 0 0px 0 inset;
    -moz-box-shadow: #fff 0 1px 0px 0 inset, #fff -1px 0 0px 0 inset;
    box-shadow: #fff 0 1px 0px 0 inset, #fff -1px 0 0px 0 inset
}

.x-tab-default-right.x-tab-over {
    -webkit-box-shadow: #fff 0 1px 0px 0 inset, #fff -1px 0 0px 0 inset;
    -moz-box-shadow: #fff 0 1px 0px 0 inset, #fff -1px 0 0px 0 inset;
    box-shadow: #fff 0 1px 0px 0 inset, #fff -1px 0 0px 0 inset
}

.x-tab-default-right.x-tab.x-tab-active {
    -webkit-box-shadow: #fff 0 1px 0px 0 inset, #fff -1px 0 0px 0 inset;
    -moz-box-shadow: #fff 0 1px 0px 0 inset, #fff -1px 0 0px 0 inset;
    box-shadow: #fff 0 1px 0px 0 inset, #fff -1px 0 0px 0 inset
}

.x-tab-default-right.x-tab.x-tab-disabled {
    -webkit-box-shadow: #fff 0 1px 0px 0 inset, #fff -1px 0 0px 0 inset;
    -moz-box-shadow: #fff 0 1px 0px 0 inset, #fff -1px 0 0px 0 inset;
    box-shadow: #fff 0 1px 0px 0 inset, #fff -1px 0 0px 0 inset
}

.x-tab-default-bottom {
    margin: 0 0 0 2px;
    -webkit-box-shadow: #fff 0 -1px 0px 0 inset, #fff -1px 0 0px 0 inset, #fff 1px 0 0px 0 inset;
    -moz-box-shadow: #fff 0 -1px 0px 0 inset, #fff -1px 0 0px 0 inset, #fff 1px 0 0px 0 inset;
    box-shadow: #fff 0 -1px 0px 0 inset, #fff -1px 0 0px 0 inset, #fff 1px 0 0px 0 inset
}

.x-tab-default-bottom.x-tab-rotate-left {
    margin: 0 2px 0 0
}

.x-tab-default-bottom.x-tab-focus {
    -webkit-box-shadow: #fff 0 -1px 0px 0 inset, #fff -1px 0 0px 0 inset, #fff 1px 0 0px 0 inset;
    -moz-box-shadow: #fff 0 -1px 0px 0 inset, #fff -1px 0 0px 0 inset, #fff 1px 0 0px 0 inset;
    box-shadow: #fff 0 -1px 0px 0 inset, #fff -1px 0 0px 0 inset, #fff 1px 0 0px 0 inset
}

.x-tab-default-bottom.x-tab-over {
    -webkit-box-shadow: #fff 0 -1px 0px 0 inset, #fff -1px 0 0px 0 inset, #fff 1px 0 0px 0 inset;
    -moz-box-shadow: #fff 0 -1px 0px 0 inset, #fff -1px 0 0px 0 inset, #fff 1px 0 0px 0 inset;
    box-shadow: #fff 0 -1px 0px 0 inset, #fff -1px 0 0px 0 inset, #fff 1px 0 0px 0 inset
}

.x-tab-default-bottom.x-tab.x-tab-active {
    -webkit-box-shadow: #fff 0 -1px 0px 0 inset, #fff -1px 0 0px 0 inset, #fff 1px 0 0px 0 inset;
    -moz-box-shadow: #fff 0 -1px 0px 0 inset, #fff -1px 0 0px 0 inset, #fff 1px 0 0px 0 inset;
    box-shadow: #fff 0 -1px 0px 0 inset, #fff -1px 0 0px 0 inset, #fff 1px 0 0px 0 inset
}

.x-tab-default-bottom.x-tab.x-tab-disabled {
    -webkit-box-shadow: #fff 0 -1px 0px 0 inset, #fff -1px 0 0px 0 inset, #fff 1px 0 0px 0 inset;
    -moz-box-shadow: #fff 0 -1px 0px 0 inset, #fff -1px 0 0px 0 inset, #fff 1px 0 0px 0 inset;
    box-shadow: #fff 0 -1px 0px 0 inset, #fff -1px 0 0px 0 inset, #fff 1px 0 0px 0 inset
}

.x-tab-default-left {
    margin: 2px 0 0 0;
    -webkit-box-shadow: #fff 0 1px 0px 0 inset, #fff 1px 0 0px 0 inset;
    -moz-box-shadow: #fff 0 1px 0px 0 inset, #fff 1px 0 0px 0 inset;
    box-shadow: #fff 0 1px 0px 0 inset, #fff 1px 0 0px 0 inset
}

.x-tab-default-left.x-tab-rotate-right {
    margin: 0 0 2px 0
}

.x-tab-default-left.x-tab-focus {
    -webkit-box-shadow: #fff 0 1px 0px 0 inset, #fff 1px 0 0px 0 inset;
    -moz-box-shadow: #fff 0 1px 0px 0 inset, #fff 1px 0 0px 0 inset;
    box-shadow: #fff 0 1px 0px 0 inset, #fff 1px 0 0px 0 inset
}

.x-tab-default-left.x-tab-over {
    -webkit-box-shadow: #fff 0 1px 0px 0 inset, #fff 1px 0 0px 0 inset;
    -moz-box-shadow: #fff 0 1px 0px 0 inset, #fff 1px 0 0px 0 inset;
    box-shadow: #fff 0 1px 0px 0 inset, #fff 1px 0 0px 0 inset
}

.x-tab-default-left.x-tab.x-tab-active {
    -webkit-box-shadow: #fff 0 1px 0px 0 inset, #fff 1px 0 0px 0 inset;
    -moz-box-shadow: #fff 0 1px 0px 0 inset, #fff 1px 0 0px 0 inset;
    box-shadow: #fff 0 1px 0px 0 inset, #fff 1px 0 0px 0 inset
}

.x-tab-default-left.x-tab.x-tab-disabled {
    -webkit-box-shadow: #fff 0 1px 0px 0 inset, #fff 1px 0 0px 0 inset;
    -moz-box-shadow: #fff 0 1px 0px 0 inset, #fff 1px 0 0px 0 inset;
    box-shadow: #fff 0 1px 0px 0 inset, #fff 1px 0 0px 0 inset
}

.x-tab-button-default {
    height: 16px
}

.x-tab-inner-default {
    font: bold 11px/13px tahoma, arial, verdana, sans-serif;
    color: #416da3;
    max-width: 100%
}

.x-tab-icon-right > .x-tab-inner-default, .x-tab-icon-left > .x-tab-inner-default {
    max-width: calc(100% - 16px)
}

.x-tab-icon-el-default {
    min-height: 16px;
    background-position: center center;
    font-size: 16px;
    line-height: 16px;
    color: #416da3
}

.x-tab-icon-left > .x-tab-icon-el-default, .x-tab-icon-right > .x-tab-icon-el-default {
    width: 16px
}

.x-tab-icon-top > .x-tab-icon-el-default, .x-tab-icon-bottom > .x-tab-icon-el-default {
    min-width: 16px
}

.x-tab-icon-el-default.x-tab-glyph {
    opacity: 0.5
}

.x-ie8 .x-tab-icon-el-default.x-tab-glyph {
    color: #90acd0
}

.x-tab-text.x-tab-icon-left > .x-tab-icon-el-default {
    margin-right: 4px
}

.x-tab-text.x-tab-icon-right > .x-tab-icon-el-default {
    margin-left: 4px
}

.x-tab-text.x-tab-icon-top > .x-tab-icon-el-default {
    margin-bottom: 4px
}

.x-tab-text.x-tab-icon-bottom > .x-tab-icon-el-default {
    margin-top: 4px
}

.x-tab-focus.x-tab-default {
    border-color: #8db3e3;
    background-color: #deecfd
}

.x-tab-focus.x-tab-default .x-tab-button:before {
    position: absolute;
    content: ' ';
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    pointer-events: none;
    outline: 1px dotted #416da3
}

.x-tab-focus.x-tab-default.x-tab-closable .x-tab-button:before {
    right: 14px
}

.x-tab-over.x-tab-default {
    border-color: #8db3e3;
    background-color: #e8f2ff
}

.x-tab-over.x-tab-default-top, .x-tab-over.x-tab-default-left, .x-tab-over.x-tab-default-right {
    background-image: none;
    background-color: #e8f2ff;
    background-image: -webkit-gradient(linear, top, bottom, color-stop(0%, #d7e5fd), color-stop(25%, #e0edff), color-stop(45%, #e8f2ff));
    background-image: -webkit-linear-gradient(top, #d7e5fd, #e0edff 25%, #e8f2ff 45%);
    background-image: -moz-linear-gradient(top, #d7e5fd, #e0edff 25%, #e8f2ff 45%);
    background-image: -o-linear-gradient(top, #d7e5fd, #e0edff 25%, #e8f2ff 45%);
    background-image: -ms-linear-gradient(top, #d7e5fd, #e0edff 25%, #e8f2ff 45%);
    background-image: linear-gradient(top, #d7e5fd, #e0edff 25%, #e8f2ff 45%)
}

.x-tab-over.x-tab-default-bottom {
    background-image: none;
    background-color: #e8f2ff;
    background-image: -webkit-gradient(linear, top, bottom, color-stop(0%, #d7e5fd), color-stop(25%, #e0edff), color-stop(45%, #e8f2ff));
    background-image: -webkit-linear-gradient(bottom, #d7e5fd, #e0edff 25%, #e8f2ff 45%);
    background-image: -moz-linear-gradient(bottom, #d7e5fd, #e0edff 25%, #e8f2ff 45%);
    background-image: -o-linear-gradient(bottom, #d7e5fd, #e0edff 25%, #e8f2ff 45%);
    background-image: -ms-linear-gradient(bottom, #d7e5fd, #e0edff 25%, #e8f2ff 45%);
    background-image: linear-gradient(bottom, #d7e5fd, #e0edff 25%, #e8f2ff 45%)
}

.x-tab-focus.x-tab-over.x-tab-default {
    border-color: #8db3e3;
    background-color: #e8f2ff
}

.x-tab.x-tab-active.x-tab-default {
    border-color: #8db3e3;
    background-color: #deecfd
}

.x-tab.x-tab-active.x-tab-default .x-tab-inner-default {
    color: #15498b
}

.x-tab.x-tab-active.x-tab-default .x-tab-icon-el {
    color: #15498b
}

.x-ie8 .x-tab.x-tab-active.x-tab-default .x-tab-icon-el {
    color: #7a9bc4
}

.x-tab.x-tab-active.x-tab-default-top, .x-tab.x-tab-active.x-tab-default-left, .x-tab.x-tab-active.x-tab-default-right {
    background-image: none;
    background-color: #deecfd;
    background-image: -webkit-gradient(linear, top, bottom, color-stop(0%, #fff), color-stop(25%, #f5f9fe), color-stop(45%, #deecfd));
    background-image: -webkit-linear-gradient(top, #fff, #f5f9fe 25%, #deecfd 45%);
    background-image: -moz-linear-gradient(top, #fff, #f5f9fe 25%, #deecfd 45%);
    background-image: -o-linear-gradient(top, #fff, #f5f9fe 25%, #deecfd 45%);
    background-image: -ms-linear-gradient(top, #fff, #f5f9fe 25%, #deecfd 45%);
    background-image: linear-gradient(top, #fff, #f5f9fe 25%, #deecfd 45%)
}

.x-tab.x-tab-active.x-tab-default-bottom {
    background-image: none;
    background-color: #deecfd;
    background-image: -webkit-gradient(linear, top, bottom, color-stop(0%, #fff), color-stop(25%, #f5f9fe), color-stop(45%, #deecfd));
    background-image: -webkit-linear-gradient(bottom, #fff, #f5f9fe 25%, #deecfd 45%);
    background-image: -moz-linear-gradient(bottom, #fff, #f5f9fe 25%, #deecfd 45%);
    background-image: -o-linear-gradient(bottom, #fff, #f5f9fe 25%, #deecfd 45%);
    background-image: -ms-linear-gradient(bottom, #fff, #f5f9fe 25%, #deecfd 45%);
    background-image: linear-gradient(bottom, #fff, #f5f9fe 25%, #deecfd 45%)
}

.x-tab-focus.x-tab-active.x-tab-default {
    border-color: #8db3e3;
    background-color: #deecfd
}

.x-tab.x-tab-disabled.x-tab-default {
    border-color: #bbd2ef;
    background-color: #e1ecfa;
    cursor: default
}

.x-tab.x-tab-disabled.x-tab-default .x-tab-inner-default {
    color: #c3b3b3
}

.x-tab.x-tab-disabled.x-tab-default .x-tab-icon-el-default {
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=50)";
    opacity: 0.5
}

.x-tab.x-tab-disabled.x-tab-default .x-tab-icon-el {
    color: #c3b3b3;
    opacity: 0.3;
    filter: none
}

.x-ie8 .x-tab.x-tab-disabled.x-tab-default .x-tab-icon-el {
    color: #d8dbe5
}

.x-tab.x-tab-disabled.x-tab-default-top, .x-tab.x-tab-disabled.x-tab-default-left, .x-tab.x-tab-disabled.x-tab-default-right {
    background-image: none;
    background-color: #e1ecfa;
    background-image: -webkit-gradient(linear, top, bottom, color-stop(0%, #e1ecfa), color-stop(0%, #ecf4fe));
    background-image: -webkit-linear-gradient(top, #e1ecfa, #ecf4fe);
    background-image: -moz-linear-gradient(top, #e1ecfa, #ecf4fe);
    background-image: -o-linear-gradient(top, #e1ecfa, #ecf4fe);
    background-image: -ms-linear-gradient(top, #e1ecfa, #ecf4fe);
    background-image: linear-gradient(top, #e1ecfa, #ecf4fe)
}

.x-tab.x-tab-disabled.x-tab-default-bottom {
    background-image: none;
    background-color: #e1ecfa;
    background-image: -webkit-gradient(linear, top, bottom, color-stop(0%, #e1ecfa), color-stop(0%, #ecf4fe));
    background-image: -webkit-linear-gradient(bottom, #e1ecfa, #ecf4fe);
    background-image: -moz-linear-gradient(bottom, #e1ecfa, #ecf4fe);
    background-image: -o-linear-gradient(bottom, #e1ecfa, #ecf4fe);
    background-image: -ms-linear-gradient(bottom, #e1ecfa, #ecf4fe);
    background-image: linear-gradient(bottom, #e1ecfa, #ecf4fe)
}

.x-nbr .x-tab-default {
    background-image: none
}

.x-tab-over .x-tab-default-top-tl, .x-tab-over .x-tab-default-top-bl, .x-tab-over .x-tab-default-top-tr, .x-tab-over .x-tab-default-top-br, .x-tab-over .x-tab-default-top-tc, .x-tab-over .x-tab-default-top-bc {
    background-image: url("data:image/gif;R0lGODlhBAAYAPQAAI2z45e65Zi65Z2957PM7dnn/dvo/d3p/d/q/ejy/+/1/PD1/PL2/PT4/vz9//39/////////wAAAI2z442z442z442z442z442z442z442z442z442z442z442z442z4yH5BAEAABEALAAAAAAEABgARAhMAAEIBBCBAYEAACAkWMgwAAEGERZCAFCgYgGGCQgoaHDgQAMFBBJinAihJAQDKA1gxMhgwAIHAR4gMOBgwQAGBhA8ECAyQU+JAIAGBAA7")
}

.x-tab-over .x-tab-default-top-ml, .x-tab-over .x-tab-default-top-mr {
    background-image: url("data:image/gif;R0lGODlhCAAgA/MAAI2z49zq/t7r/uDt/+Hu/+Pv/+Xw/+fx/+jy/////////42z442z442z442z442z4yH5BAEAAAoALAAAAAAIACADQwj/AAEkCEAwQAIAAhEoRHAw4cKGCRYyRBjxIUWJEDFetOhQYUaOFT1uFNlxYsmPJEOaVIlypcaTI12CfMkyZsubNnPC3FmTJ82fM4OmBDpUqMyiSI8qxenTKNOeUIku1RnVKVWpT7Fetdo0aVauVb1uFdt1atmvZMOaVYt2rVaBBeIWaEt3rFuwb9narXt2r9++gPUGzksYr+G0hREfvqu4MePHfAVLTgz57+TFkSlnxmxZc2fOg0EOGD0A4oHTBzY7Vl059OrPr123vhyb9mzPslnrhn0btO3duXkD/y28ePDjxJHjTs58uXPfz2tH7y0duvXq2KlrHz6d+/Xtxpt/jfeenTx45ePDd6cooL0AiATiE4BooL4B8/jVp0dfXn9//ueJ95+AAa4HYH4H+lfgfgQi2KCCDhr4YIIUTmihhBgymOGAGy7IoYYgfiiihyRGGGKJEKZYYYcmjtgiiiue+OKMKl4oY40s4nhjjC7q2COPMNr4o5BB5ggkjUf6WOSORCLZpJJOGvlkkn0FBAA7")
}

.x-tab-over .x-tab-default-top-mc {
    background-repeat: repeat-x;
    background-image: url("data:image/gif;R0lGODlhAQAgA/MAANzq/t7r/uDt/+Hu/+Pv/+Xw/+fx/+jy/////9zq/tzq/tzq/tzq/tzq/tzq/tzq/iH5BAEAAAgALAAAAAABACADQwg6AAEcGEiwoMGDCBMqXMiwocOEBB5KnEixokUBBixq3Mixo8ePICsGGFAgpMmTKFOqXMmypcuXMBEGBAA7")
}

.x-tab-focus .x-tab-default-top-tl, .x-tab-focus .x-tab-default-top-bl, .x-tab-focus .x-tab-default-top-tr, .x-tab-focus .x-tab-default-top-br, .x-tab-focus .x-tab-default-top-tc, .x-tab-focus .x-tab-default-top-bc {
    background-image: url("data:image/gif;R0lGODlhBAAYAPQAAI2z45e65Zi65Z2957PM7c7g99Dh99Pj+NXk+N7s/e70+/H2/fL2/Pz9/v///////wAAAI2z442z442z442z442z442z442z442z442z442z442z442z442z442z442z4yH5BAEAAA8ALAAAAAAEABgARAhMAAEIBPCAAYEAABwkWMgwAAEGDxY6AFCgYgGGCQgoWHDgwAIFBBJinOigpAMDKA1gxMhggIIGARogMNBAwQAGBhA0ECAyQU+JAIAGBAA7")
}

.x-tab-focus .x-tab-default-top-ml, .x-tab-focus .x-tab-default-top-mr {
    background-image: url("data:image/gif;R0lGODlhCAAgA/MAAI2z49Lj+NTk+dbm+tfn+tno+9vq/N3r/N7s/f///////42z442z442z442z442z4yH5BAEAAAoALAAAAAAIACADQwj/AAEkCEAwQAIAAhEoRHAw4cKGCRYyRBjxIUWJEDFetOhQYUaOFT1uFNlxYsmPJEOaVIlypcaTI12CfMkyZsubNnPC3FmTJ82fM4OmBDpUqMyiSI8qxenTKNOeUIku1RnVKVWpT7Fetdo0aVauVb1uFdt1atmvZMOaVYt2rVaBBeIWaEt3rFuwb9narXt2r9++gPUGzksYr+G0hREfvqu4MePHfAVLTgz57+TFkSlnxmxZc2fOg0EOGD0A4oHTBzY7Vl059OrPr123vhyb9mzPslnrhn0btO3duXkD/y28ePDjxJHjTs58uXPfz2tH7y0duvXq2KlrHz6d+/Xtxpt/jfeenTx45ePDd6cooL0AiATiE4BooL4B8/jVp0dfXn9//ueJ95+AAa4HYH4H+lfgfgQi2KCCDhr4YIIUTmihhBgymOGAGy7IoYYgfiiihyRGGGKJEKZYYYcmjtgiiiue+OKMKl4oY40s4nhjjC7q2COPMNr4o5BB5ggkjUf6WOSORCLZpJJOGvlkkn0FBAA7")
}

.x-tab-focus .x-tab-default-top-mc {
    background-repeat: repeat-x;
    background-image: url("data:image/gif;R0lGODlhAQAgA/MAANLj+NTk+dbm+tfn+tno+9vq/N3r/N7s/f///9Lj+NLj+NLj+NLj+NLj+NLj+NLj+CH5BAEAAAgALAAAAAABACADQwg6AAEcGEiwoMGDCBMqXMiwocOEBB5KnEixokUBBixq3Mixo8ePICsGGFAgpMmTKFOqXMmypcuXMBEGBAA7")
}

.x-tab-focus.x-tab-over .x-tab-default-top-tl, .x-tab-focus.x-tab-over .x-tab-default-top-bl, .x-tab-focus.x-tab-over .x-tab-default-top-tr, .x-tab-focus.x-tab-over .x-tab-default-top-br, .x-tab-focus.x-tab-over .x-tab-default-top-tc, .x-tab-focus.x-tab-over .x-tab-default-top-bc {
    background-image: url("data:image/gif;R0lGODlhBAAYAPQAAI2z45e65Zi65Z2957PM7dnn/dvo/d3p/d/q/ejy/+/1/PD1/PL2/PT4/vz9//39/////////wAAAI2z442z442z442z442z442z442z442z442z442z442z442z442z4yH5BAEAABEALAAAAAAEABgARAhMAAEIBBCBAYEAACAkWMgwAAEGERZCAFCgYgGGCQgoaHDgQAMFBBJinAihJAQDKA1gxMhgwAIHAR4gMOBgwQAGBhA8ECAyQU+JAIAGBAA7")
}

.x-tab-focus.x-tab-over .x-tab-default-top-ml, .x-tab-focus.x-tab-over .x-tab-default-top-mr {
    background-image: url("data:image/gif;R0lGODlhCAAgA/MAAI2z49zq/t7r/uDt/+Hu/+Pv/+Xw/+fx/+jy/////////42z442z442z442z442z4yH5BAEAAAoALAAAAAAIACADQwj/AAEkCEAwQAIAAhEoRHAw4cKGCRYyRBjxIUWJEDFetOhQYUaOFT1uFNlxYsmPJEOaVIlypcaTI12CfMkyZsubNnPC3FmTJ82fM4OmBDpUqMyiSI8qxenTKNOeUIku1RnVKVWpT7Fetdo0aVauVb1uFdt1atmvZMOaVYt2rVaBBeIWaEt3rFuwb9narXt2r9++gPUGzksYr+G0hREfvqu4MePHfAVLTgz57+TFkSlnxmxZc2fOg0EOGD0A4oHTBzY7Vl059OrPr123vhyb9mzPslnrhn0btO3duXkD/y28ePDjxJHjTs58uXPfz2tH7y0duvXq2KlrHz6d+/Xtxpt/jfeenTx45ePDd6cooL0AiATiE4BooL4B8/jVp0dfXn9//ueJ95+AAa4HYH4H+lfgfgQi2KCCDhr4YIIUTmihhBgymOGAGy7IoYYgfiiihyRGGGKJEKZYYYcmjtgiiiue+OKMKl4oY40s4nhjjC7q2COPMNr4o5BB5ggkjUf6WOSORCLZpJJOGvlkkn0FBAA7")
}

.x-tab-focus.x-tab-over .x-tab-default-top-mc {
    background-repeat: repeat-x;
    background-image: url("data:image/gif;R0lGODlhAQAgA/MAANzq/t7r/uDt/+Hu/+Pv/+Xw/+fx/+jy/////9zq/tzq/tzq/tzq/tzq/tzq/tzq/iH5BAEAAAgALAAAAAABACADQwg6AAEcGEiwoMGDCBMqXMiwocOEBB5KnEixokUBBixq3Mixo8ePICsGGFAgpMmTKFOqXMmypcuXMBEGBAA7")
}

.x-tab.x-tab-active .x-tab-default-top-tl, .x-tab.x-tab-active .x-tab-default-top-bl, .x-tab.x-tab-active .x-tab-default-top-tr, .x-tab.x-tab-active .x-tab-default-top-br, .x-tab.x-tab-active .x-tab-default-top-tc, .x-tab.x-tab-active .x-tab-default-top-bc {
    background-image: url("data:image/gif;R0lGODlhBAAYAPQAAI2z45e65Zi65Z6+57PM7d7s/fL2/PP3/PT4/Pr8/vv8/vz9/v7+/v7+//7//////////wAAAI2z442z442z442z442z442z442z442z442z442z442z442z442z442z4yH5BAEAABAALAAAAAAEABgARAhKAAEIBADBAIEAAB4UWMgwAAEDEBY+ALCg4gKGBQgcYFCRwQECCTFOfEDyQYKTCTBiNDAAgYMADU46QDDAQAIFDQSELLBTIgCfAQEAOw==")
}

.x-tab.x-tab-active .x-tab-default-top-ml, .x-tab.x-tab-active .x-tab-default-top-mr {
    background-image: url("data:image/gif;R0lGODlhCAAgA/MAAI2z497s/eDt/eXw/erz/e/2/fT4/fb6/vj7/v///////42z442z442z442z442z4yH5BAEAAAoALAAAAAAIACADQwj/AAEkQEAQQQIAAgMoDHAw4cKGCRYyRBjxIUWJEDFetOhQYUaOFT1uFNlxYsmPJEOaVIlypcaTI12CfMkyZsubNnPC3FmTJ82fM4OmBDpUqMyiSI8qxenTKNOeUIku1RnVKVWpT7Fetdo0aVauVb1uFdt1atmvZMOaVYt2rVaBBOISaEt3rFuwb9narXt2r9++gPUGzksYr+G0hREfvqu4MePHfAVLTgz57+TFkSlnxmxZc2fOg0EaGG0AooDTAjY7Vl059OrPr123vhyb9mzPslnrhn0btO3duXkD/y28ePDjxJHjTs58uXPfz2tH7y0duvXq2KlrHz6d+/Xtxpt/jfeenTx45ePDd6d4oP0BiAXiF4A4oP4A8/jVp0dfXn9//ueJ95+AAa4HYH4H+lfgfgQi2KCCDhr4YIIUTmihhBgymOGAGy7IoYYgfiiihyRGGGKJEKZYYYcmjtgiiiue+OKMKl4oY40s4nhjjC7q2COPMNr4o5BB5ggkjUf6WOSORCLZpJJOGvlkkn0FBAA7")
}

.x-tab.x-tab-active .x-tab-default-top-mc {
    background-repeat: repeat-x;
    background-image: url("data:image/gif;R0lGODlhAQAgA/MAAN7s/eDt/eXw/erz/e/2/fT4/fb6/vj7/v///97s/d7s/d7s/d7s/d7s/d7s/d7s/SH5BAEAAAgALAAAAAABACADQwg6AA8AGEiwoMGDCBMqXMiwocOEAx5KnEixosUCASxq3Mixo8ePICsaICAgpMmTKFOqXMmypcuXMBEGBAA7")
}

.x-tab-focus.x-tab-active .x-tab-default-top-tl, .x-tab-focus.x-tab-active .x-tab-default-top-bl, .x-tab-focus.x-tab-active .x-tab-default-top-tr, .x-tab-focus.x-tab-active .x-tab-default-top-br, .x-tab-focus.x-tab-active .x-tab-default-top-tc, .x-tab-focus.x-tab-active .x-tab-default-top-bc {
    background-image: url("data:image/gif;R0lGODlhBAAYAPQAAI2z45e65Zi65Z6+57PM7d7s/fL2/PP3/PT4/Pr8/vv8/vz9/v7+/v7+//7//////////wAAAI2z442z442z442z442z442z442z442z442z442z442z442z442z442z4yH5BAEAABAALAAAAAAEABgARAhKAAEIBADBAIEAAB4UWMgwAAEDEBY+ALCg4gKGBQgcYFCRwQECCTFOfEDyQYKTCTBiNDAAgYMADU46QDDAQAIFDQSELLBTIgCfAQEAOw==")
}

.x-tab-focus.x-tab-active .x-tab-default-top-ml, .x-tab-focus.x-tab-active .x-tab-default-top-mr {
    background-image: url("data:image/gif;R0lGODlhCAAgA/MAAI2z497s/eDt/eXw/erz/e/2/fT4/fb6/vj7/v///////42z442z442z442z442z4yH5BAEAAAoALAAAAAAIACADQwj/AAEkQEAQQQIAAgMoDHAw4cKGCRYyRBjxIUWJEDFetOhQYUaOFT1uFNlxYsmPJEOaVIlypcaTI12CfMkyZsubNnPC3FmTJ82fM4OmBDpUqMyiSI8qxenTKNOeUIku1RnVKVWpT7Fetdo0aVauVb1uFdt1atmvZMOaVYt2rVaBBOISaEt3rFuwb9narXt2r9++gPUGzksYr+G0hREfvqu4MePHfAVLTgz57+TFkSlnxmxZc2fOg0EaGG0AooDTAjY7Vl059OrPr123vhyb9mzPslnrhn0btO3duXkD/y28ePDjxJHjTs58uXPfz2tH7y0duvXq2KlrHz6d+/Xtxpt/jfeenTx45ePDd6d4oP0BiAXiF4A4oP4A8/jVp0dfXn9//ueJ95+AAa4HYH4H+lfgfgQi2KCCDhr4YIIUTmihhBgymOGAGy7IoYYgfiiihyRGGGKJEKZYYYcmjtgiiiue+OKMKl4oY40s4nhjjC7q2COPMNr4o5BB5ggkjUf6WOSORCLZpJJOGvlkkn0FBAA7")
}

.x-tab-focus.x-tab-active .x-tab-default-top-mc {
    background-repeat: repeat-x;
    background-image: url("data:image/gif;R0lGODlhAQAgA/MAAN7s/eDt/eXw/erz/e/2/fT4/fb6/vj7/v///97s/d7s/d7s/d7s/d7s/d7s/d7s/SH5BAEAAAgALAAAAAABACADQwg6AA8AGEiwoMGDCBMqXMiwocOEAx5KnEixosUCASxq3Mixo8ePICsaICAgpMmTKFOqXMmypcuXMBEGBAA7")
}

.x-tab.x-tab-disabled .x-tab-default-top-tl, .x-tab.x-tab-disabled .x-tab-default-top-bl, .x-tab.x-tab-disabled .x-tab-default-top-tr, .x-tab.x-tab-disabled .x-tab-default-top-br, .x-tab.x-tab-disabled .x-tab-default-top-tc, .x-tab.x-tab-disabled .x-tab-default-top-bc {
    background-image: url("data:image/gif;R0lGODlhBAAYAPQAALvS78HW8MHW8cba8tLg8+Lt+uXv+uXv++rz/evz/uz0/vX4/fX5/fb6/ff5/Pf6/f3+/v3+/////////wAAALvS77vS77vS77vS77vS77vS77vS77vS77vS77vS77vS7yH5BAEAABMALAAAAAAEABgARAhRAAEIBDDhAQEBACQgWMhQAAEHExZKAFCgYoEEGBMQWNDAgIEGCwgkzJhgooSTEixezKigpQIHAxhEEADBQIEIDAY4KHAAQoCRCRK2xDix5cSAADs=")
}

.x-tab.x-tab-disabled .x-tab-default-top-ml, .x-tab.x-tab-disabled .x-tab-default-top-mr {
    background-image: url("data:image/gif;R0lGODlhCAAgA/MAALvS7+Pt++Pu++Tu++Xv++Xv/Obv/Obw/Ofw/Ofx/Ojx/Ojx/eny/ery/f///////yH5BAEAAA8ALAAAAAAIACADQwj/AAE4CEAwgAMAAhEoRHBQYIOHDRo6gBgR4USIEilmxGhRY0eODkFefLiR5EeTIVGOrJiS5cqSLj22hEnzZEyRMl/arDlzp8+eQHUGzUkUp1GVRZEevam0KdOnPIVKTQr159SlUalmxWpVa1euQ8FedbqV7FezYdGOrZqW7dqybr0GJUCXgEQGeBnA3Xs2rli5b/vybTs4MGHBiA8rNswYsOO/kNU+lhzZL+XLljMXnqw5cePKm0F75hwac+nOAgeoHiDRgGsDEhXIVnC69mjRi0nfNr0b9WfeuXH/9q07OPDhto0TF14cee/kzpVDb06dufXj1bFfX669O/fv07eHqvc+Hvzz89LRR1+f3Xz69+zFq29fHrqA+wIkrmZtsYD/AhIdIOABEiVgYAISLaDgAnflVd988sFHH4TkUehefBVKGCGGF06oYYYcPvhhhxt6GKKFIp44YoomtljiiyC6GCOMJM5oY404skijjjfymCOKQK4YpIpEyvijkEgWueOQRvroJJNLJtkklD1SeaSSVUoZJZZXTqllllw++WWXW3oZppVinjkmXwEBADs=")
}

.x-tab.x-tab-disabled .x-tab-default-top-mc {
    background-repeat: repeat-x;
    background-image: url("data:image/gif;R0lGODlhAQAgA/MAAOPt++Pu++Tu++Xv++Xv/Obv/Obw/Ofw/Ofx/Ojx/Ojx/eny/ery/f///+Pt++Pt+yH5BAEAAA0ALAAAAAABACADQwhCAAEcYECwoMGDCBMqXMiwocOHCQcsgEixosWLFwUUSICxo8ePIEOKHGkxgAACBhAomEiypcuXMGPKnEmzps2bBAMCADs=")
}

.x-tab-over .x-tab-default-right-tl, .x-tab-over .x-tab-default-right-bl, .x-tab-over .x-tab-default-right-tr, .x-tab-over .x-tab-default-right-br, .x-tab-over .x-tab-default-right-tc, .x-tab-over .x-tab-default-right-bc {
    background-image: url("data:image/gif;R0lGODlhBAAYAPQAAI2z45e65Zi65Zu85p2857PM7dnn/dvo/d3p/d/q/eHr+eTt+ejy/+rz/+z0/e/0/O/1/PL2/PP4//T4/vz9//39/////////wAAAI2z442z442z442z442z442z442z4yH5BAEAABcALAAAAAAEABgARAhFAAEIHCiQgcGDBgMUiHCBQQMKAgxINIBwogEEEyAUQOhAwYAIFkJaOEDyAEKCIkeWpPCAQIQDCSoIODmQgYQFBQQsvBAQADs=")
}

.x-tab-over .x-tab-default-right-ml, .x-tab-over .x-tab-default-right-mr {
    background-image: url("data:image/gif;R0lGODlhCAAQAPMAAI2z49zq/t7r/uDt/+Hu/+Pv/+Xw/+fx/+jy/////////42z442z442z442z442z4yH5BAEAAAoALAAAAAAIABAAQwg7AAMIHJgAAIKDCAsWWMiwIMKEAAZInFjwgMWLDh8iyPiwoICPIAsSGEmyoIGTKDlC1LjRoEaVB2G2DAgAOw==")
}

.x-tab-over .x-tab-default-right-mc {
    background-repeat: repeat-x;
    background-image: url("data:image/gif;R0lGODlhAQAQAPMAANzq/t7r/uDt/+Hu/+Pv/+Xw/+fx/+jy/////9zq/tzq/tzq/tzq/tzq/tzq/tzq/iH5BAEAAAgALAAAAAABABAAQwgRAAEcIHBAgIEDBwIMKICwYUAAOw==")
}

.x-tab-focus .x-tab-default-right-tl, .x-tab-focus .x-tab-default-right-bl, .x-tab-focus .x-tab-default-right-tr, .x-tab-focus .x-tab-default-right-br, .x-tab-focus .x-tab-default-right-tc, .x-tab-focus .x-tab-default-right-bc {
    background-image: url("data:image/gif;R0lGODlhBAAYAPQAAI2z45e65Zi65Zu75p2857PM7c7g99Dh99Pj+NXk+N7q+N7s/eHr+eHu/efx/O31/u70+/H2/fL2/Pv9//z9/v///////wAAAI2z442z442z442z442z442z442z442z4yH5BAEAABYALAAAAAAEABgARAhFAAEIHChwgcGDBgMUkGBhQYMJAgxINIBwogEEESAUQOhAwQAJFUJWOEDyAEKCIkeWpACBgIQDCSgIODlwwQMGBQQstBAQADs=")
}

.x-tab-focus .x-tab-default-right-ml, .x-tab-focus .x-tab-default-right-mr {
    background-image: url("data:image/gif;R0lGODlhCAAQAPMAAI2z49Lj+NTk+dbm+tfn+tno+9vq/N3r/N7s/f///////42z442z442z442z442z4yH5BAEAAAoALAAAAAAIABAAQwg7AAMIHJgAAIKDCAsWWMiwIMKEAAZInFjwgMWLDh8iyPiwoICPIAsSGEmyoIGTKDlC1LjRoEaVB2G2DAgAOw==")
}

.x-tab-focus .x-tab-default-right-mc {
    background-repeat: repeat-x;
    background-image: url("data:image/gif;R0lGODlhAQAQAPMAANLj+NTk+dbm+tfn+tno+9vq/N3r/N7s/f///9Lj+NLj+NLj+NLj+NLj+NLj+NLj+CH5BAEAAAgALAAAAAABABAAQwgRAAEcIHBAgIEDBwIMKICwYUAAOw==")
}

.x-tab-focus.x-tab-over .x-tab-default-right-tl, .x-tab-focus.x-tab-over .x-tab-default-right-bl, .x-tab-focus.x-tab-over .x-tab-default-right-tr, .x-tab-focus.x-tab-over .x-tab-default-right-br, .x-tab-focus.x-tab-over .x-tab-default-right-tc, .x-tab-focus.x-tab-over .x-tab-default-right-bc {
    background-image: url("data:image/gif;R0lGODlhBAAYAPQAAI2z45e65Zi65Zu85p2857PM7dnn/dvo/d3p/d/q/eHr+eTt+ejy/+rz/+z0/e/0/O/1/PL2/PP4//T4/vz9//39/////////wAAAI2z442z442z442z442z442z442z4yH5BAEAABcALAAAAAAEABgARAhFAAEIHCiQgcGDBgMUiHCBQQMKAgxINIBwogEEEyAUQOhAwYAIFkJaOEDyAEKCIkeWpPCAQIQDCSoIODmQgYQFBQQsvBAQADs=")
}

.x-tab-focus.x-tab-over .x-tab-default-right-ml, .x-tab-focus.x-tab-over .x-tab-default-right-mr {
    background-image: url("data:image/gif;R0lGODlhCAAQAPMAAI2z49zq/t7r/uDt/+Hu/+Pv/+Xw/+fx/+jy/////////42z442z442z442z442z4yH5BAEAAAoALAAAAAAIABAAQwg7AAMIHJgAAIKDCAsWWMiwIMKEAAZInFjwgMWLDh8iyPiwoICPIAsSGEmyoIGTKDlC1LjRoEaVB2G2DAgAOw==")
}

.x-tab-focus.x-tab-over .x-tab-default-right-mc {
    background-repeat: repeat-x;
    background-image: url("data:image/gif;R0lGODlhAQAQAPMAANzq/t7r/uDt/+Hu/+Pv/+Xw/+fx/+jy/////9zq/tzq/tzq/tzq/tzq/tzq/tzq/iH5BAEAAAgALAAAAAABABAAQwgRAAEcIHBAgIEDBwIMKICwYUAAOw==")
}

.x-tab.x-tab-active .x-tab-default-right-tl, .x-tab.x-tab-active .x-tab-default-right-bl, .x-tab.x-tab-active .x-tab-default-right-tr, .x-tab.x-tab-active .x-tab-default-right-br, .x-tab.x-tab-active .x-tab-default-right-tc, .x-tab.x-tab-active .x-tab-default-right-bc {
    background-image: url("data:image/gif;R0lGODlhBAAYAPQAAI2z45e65Zi65Zu75p2957PM7d7q+N7s/eHr+eHu/efx/O31/vL2/PP3/PT3/Pr8/vv8/vv9//z9/v7+/v7+//7//////////wAAAI2z442z442z442z442z442z442z4yH5BAEAABcALAAAAAAEABgARAhEAAEIHCjwgMGDBgMUYHDhQIIIAiRIlIBwosQJDQogVGBgAAMLIC08GPkAIcGQIklWcECAwQMIFASYHHhgAYICAhZeCAgAOw==")
}

.x-tab.x-tab-active .x-tab-default-right-ml, .x-tab.x-tab-active .x-tab-default-right-mr {
    background-image: url("data:image/gif;R0lGODlhCAAQAPMAAI2z497s/eDt/eXw/erz/e/2/fT4/fb6/vj7/v///////42z442z442z442z442z4yH5BAEAAAoALAAAAAAIABAAQwg7ABEIHJgAQICDCAsSWMiwIMKEAAxInFhQgMWLDh8GyPiw4IGPIAsWGEmy4ICTKDlC1LjRoEaVB2G2DAgAOw==")
}

.x-tab.x-tab-active .x-tab-default-right-mc {
    background-repeat: repeat-x;
    background-image: url("data:image/gif;R0lGODlhAQAQAPMAAN7s/eDt/eXw/erz/e/2/fT4/fb6/vj7/v///97s/d7s/d7s/d7s/d7s/d7s/d7s/SH5BAEAAAgALAAAAAABABAAQwgRAA8AGACgQAAAAAwQEICwYUAAOw==")
}

.x-tab-focus.x-tab-active .x-tab-default-right-tl, .x-tab-focus.x-tab-active .x-tab-default-right-bl, .x-tab-focus.x-tab-active .x-tab-default-right-tr, .x-tab-focus.x-tab-active .x-tab-default-right-br, .x-tab-focus.x-tab-active .x-tab-default-right-tc, .x-tab-focus.x-tab-active .x-tab-default-right-bc {
    background-image: url("data:image/gif;R0lGODlhBAAYAPQAAI2z45e65Zi65Zu75p2957PM7d7q+N7s/eHr+eHu/efx/O31/vL2/PP3/PT3/Pr8/vv8/vv9//z9/v7+/v7+//7//////////wAAAI2z442z442z442z442z442z442z4yH5BAEAABcALAAAAAAEABgARAhEAAEIHCjwgMGDBgMUYHDhQIIIAiRIlIBwosQJDQogVGBgAAMLIC08GPkAIcGQIklWcECAwQMIFASYHHhgAYICAhZeCAgAOw==")
}

.x-tab-focus.x-tab-active .x-tab-default-right-ml, .x-tab-focus.x-tab-active .x-tab-default-right-mr {
    background-image: url("data:image/gif;R0lGODlhCAAQAPMAAI2z497s/eDt/eXw/erz/e/2/fT4/fb6/vj7/v///////42z442z442z442z442z4yH5BAEAAAoALAAAAAAIABAAQwg7ABEIHJgAQICDCAsSWMiwIMKEAAxInFhQgMWLDh8GyPiw4IGPIAsWGEmy4ICTKDlC1LjRoEaVB2G2DAgAOw==")
}

.x-tab-focus.x-tab-active .x-tab-default-right-mc {
    background-repeat: repeat-x;
    background-image: url("data:image/gif;R0lGODlhAQAQAPMAAN7s/eDt/eXw/erz/e/2/fT4/fb6/vj7/v///97s/d7s/d7s/d7s/d7s/d7s/d7s/SH5BAEAAAgALAAAAAABABAAQwgRAA8AGACgQAAAAAwQEICwYUAAOw==")
}

.x-tab.x-tab-disabled .x-tab-default-right-tl, .x-tab.x-tab-disabled .x-tab-default-right-bl, .x-tab.x-tab-disabled .x-tab-default-right-tr, .x-tab.x-tab-disabled .x-tab-default-right-br, .x-tab.x-tab-disabled .x-tab-default-right-tc, .x-tab.x-tab-disabled .x-tab-default-right-bc {
    background-image: url("data:image/gif;R0lGODlhBAAYAPQAALvS78HW8MHW8cTZ8cXZ8tLg8+Lt+uXv+uXv++vz/uzy++z0/u30++30/vH3/fT5/vX4/fb6/ff5/P3+/v3+/////////wAAALvS77vS77vS77vS77vS77vS77vS77vS7yH5BAEAABYALAAAAAAEABgARAhGAAEIHCgwgcGDBgUUkGAhQQMKAQxINLCg4oKJBg5EgFDA4gIHCgZIqECyAkaEBEuanEgBAgEJBhBMCIByYIIHDAoEWGghIAA7")
}

.x-tab.x-tab-disabled .x-tab-default-right-ml, .x-tab.x-tab-disabled .x-tab-default-right-mr {
    background-image: url("data:image/gif;R0lGODlhCAAQAPQAALvS7+Pt++Pu++Tu++Xv++Xv/Obv/Obw/Ofw/Ofx/Ojx/Ojx/eny/ery/erz/f///////7vS77vS77vS77vS77vS77vS77vS77vS77vS77vS77vS77vS77vS77vS77vS7yH5BAEAABAALAAAAAAIABAARAhKAAMIHPgAAIKDCAsSWMiwIIOHEAsOmEixoIGLGAsq2MixYIOPIAsKGElSIsWJBQuoXFnwgMuXBRPInFlwgc2bDiE+LOigp8+CAQEAOw==")
}

.x-tab.x-tab-disabled .x-tab-default-right-mc {
    background-repeat: repeat-x;
    background-image: url("data:image/gif;R0lGODlhAQAQAPMAAOPt++Pu++Tu++Xv++Xv/Obv/Obw/Ofw/Ofx/Ojx/Ojx/eny/ery/erz/f///+Pt+yH5BAEAAA4ALAAAAAABABAAQwgVAAEcGLBAQIEEDAIIIGAAgYIFDQICADs=")
}

.x-tab-over .x-tab-default-bottom-tl, .x-tab-over .x-tab-default-bottom-bl, .x-tab-over .x-tab-default-bottom-tr, .x-tab-over .x-tab-default-bottom-br, .x-tab-over .x-tab-default-bottom-tc, .x-tab-over .x-tab-default-bottom-bc {
    background-image: url("data:image/gif;R0lGODlhBAAYAPQAAI2z45e65Zi65Z2955696LPM7dnn/dro/d3p/d7q/ejy/+/1/PD1/PL2/PT4/vz9//39/////////wAAAI2z442z442z442z442z442z442z442z442z442z442z442z4yH5BAEAABIALAAAAAAEABgARAhLABUIVAAggsAAEBIcWLhQYAQABxJAEDBQQYSLDw0OfNhgAIMHDxgQaFCxooGTBgCoVKmxYMWHDgEUWOAAgYQGBQQgcLAgZ4EGEgICADs=")
}

.x-tab-over .x-tab-default-bottom-ml, .x-tab-over .x-tab-default-bottom-mr {
    background-image: url("data:image/gif;R0lGODlhCAAgA/MAAI2z49zp/t7r/t/s/uHt/+Pu/+Tv/+bx/+jy/////////42z442z442z442z442z4yH5BAEAAAoALAAAAAAIACADQwj/AAEkQEAQQQIAAgsaRDiw4MGEDhkqfNiQIMWJEiNCtJiR48aFHy9qrAiSpEiPJjuWxBhS5cmVI1mmbElzpk2ZOGPqRJmT506YPoMCHfqyqMujNXsSRXrzp9GkTpkqfdpUKNWpUqNCtZqV69alX69qrQqWrFivZruWxRpW7dm1Y9mmbUt3rl25eOPqRZuX7164fgMDHvy2sNvDdfsSRnz3r+HEjhkrftxYMOXJkscS2EzgcmTIljOHBr2YtOfRlUunPq0as2nRrT+vhs26Nu3br3PP1u16t+/ewGUHRz08NnHhyI8rN87cNu/kzXH/hu58+vLqxbFTl56d+3aBBsIbjaAooLwA7de9p3++3np09u/do4/fHf78++rpf5efH7/9/gD+JyB/A9ZH4IEGJrifgu0xqF+DC0YI4YQPVugfghJaGCCGFF7ooIcZgtjhhh+SGKKJIxZ4ooopcqghiy+6KGKMJcI4440o0riijDniaGOPQP4oJI81HWDkARQVoGQBFA3g5AAUBSBlAAcFBAA7")
}

.x-tab-over .x-tab-default-bottom-mc {
    background-repeat: repeat-x;
    background-image: url("data:image/gif;R0lGODlhAQAgA/MAANzp/t7r/t/s/uHt/+Pu/+Tv/+bx/+jy/////9zp/tzp/tzp/tzp/tzp/tzp/tzp/iH5BAEAAAgALAAAAAABACADQwg5AA8IHEiwoMGDCBMqXMiwocOHECNKnJhwAMWLGDNq3Mixo8ICATyKHEmypMmTKFOqXGnSAAEBAAICADs=")
}

.x-tab-focus .x-tab-default-bottom-tl, .x-tab-focus .x-tab-default-bottom-bl, .x-tab-focus .x-tab-default-bottom-tr, .x-tab-focus .x-tab-default-bottom-br, .x-tab-focus .x-tab-default-bottom-tc, .x-tab-focus .x-tab-default-bottom-bc {
    background-image: url("data:image/gif;R0lGODlhBAAYAPQAAI2z45e65Zi65Z2955696LPM7c7g99Dh99Pj+NXk+N7s/e70+/H2/fL2/Pz9/v///////wAAAI2z442z442z442z442z442z442z442z442z442z442z442z442z442z4yH5BAEAABAALAAAAAAEABgARAhLABUIVADggcAADhIcWLhQ4AMABxI4EDBQwYOLDw0OfNhgwAIHDhYQaFCxooGTBgCoVKmxYMWHDgEUWMAAAYQGBQQgYLAgZ4EGEAICADs=")
}

.x-tab-focus .x-tab-default-bottom-ml, .x-tab-focus .x-tab-default-bottom-mr {
    background-image: url("data:image/gif;R0lGODlhCAAgA/MAAI2z49Li+NPk+dXl+dfm+tno+9rp+9zq/N7s/f///////42z442z442z442z442z4yH5BAEAAAoALAAAAAAIACADQwj/AAEkQEAQQQIAAgsaRDiw4MGEDhkqfNiQIMWJEiNCtJiR48aFHy9qrAiSpEiPJjuWxBhS5cmVI1mmbElzpk2ZOGPqRJmT506YPoMCHfqyqMujNXsSRXrzp9GkTpkqfdpUKNWpUqNCtZqV69alX69qrQqWrFivZruWxRpW7dm1Y9mmbUt3rl25eOPqRZuX7164fgMDHvy2sNvDdfsSRnz3r+HEjhkrftxYMOXJkscS2EzgcmTIljOHBr2YtOfRlUunPq0as2nRrT+vhs26Nu3br3PP1u16t+/ewGUHRz08NnHhyI8rN87cNu/kzXH/hu58+vLqxbFTl56d+3aBBsIbjaAooLwA7de9p3++3np09u/do4/fHf78++rpf5efH7/9/gD+JyB/A9ZH4IEGJrifgu0xqF+DC0YI4YQPVugfghJaGCCGFF7ooIcZgtjhhh+SGKKJIxZ4ooopcqghiy+6KGKMJcI4440o0riijDniaGOPQP4oJI81HWDkARQVoGQBFA3g5AAUBSBlAAcFBAA7")
}

.x-tab-focus .x-tab-default-bottom-mc {
    background-repeat: repeat-x;
    background-image: url("data:image/gif;R0lGODlhAQAgA/MAANLi+NPk+dXl+dfm+tno+9rp+9zq/N7s/f///9Li+NLi+NLi+NLi+NLi+NLi+NLi+CH5BAEAAAgALAAAAAABACADQwg5AA8IHEiwoMGDCBMqXMiwocOHECNKnJhwAMWLGDNq3Mixo8ICATyKHEmypMmTKFOqXGnSAAEBAAICADs=")
}

.x-tab-focus.x-tab-over .x-tab-default-bottom-tl, .x-tab-focus.x-tab-over .x-tab-default-bottom-bl, .x-tab-focus.x-tab-over .x-tab-default-bottom-tr, .x-tab-focus.x-tab-over .x-tab-default-bottom-br, .x-tab-focus.x-tab-over .x-tab-default-bottom-tc, .x-tab-focus.x-tab-over .x-tab-default-bottom-bc {
    background-image: url("data:image/gif;R0lGODlhBAAYAPQAAI2z45e65Zi65Z2955696LPM7dnn/dro/d3p/d7q/ejy/+/1/PD1/PL2/PT4/vz9//39/////////wAAAI2z442z442z442z442z442z442z442z442z442z442z442z4yH5BAEAABIALAAAAAAEABgARAhLABUIVAAggsAAEBIcWLhQYAQABxJAEDBQQYSLDw0OfNhgAIMHDxgQaFCxooGTBgCoVKmxYMWHDgEUWOAAgYQGBQQgcLAgZ4EGEgICADs=")
}

.x-tab-focus.x-tab-over .x-tab-default-bottom-ml, .x-tab-focus.x-tab-over .x-tab-default-bottom-mr {
    background-image: url("data:image/gif;R0lGODlhCAAgA/MAAI2z49zp/t7r/t/s/uHt/+Pu/+Tv/+bx/+jy/////////42z442z442z442z442z4yH5BAEAAAoALAAAAAAIACADQwj/AAEkQEAQQQIAAgsaRDiw4MGEDhkqfNiQIMWJEiNCtJiR48aFHy9qrAiSpEiPJjuWxBhS5cmVI1mmbElzpk2ZOGPqRJmT506YPoMCHfqyqMujNXsSRXrzp9GkTpkqfdpUKNWpUqNCtZqV69alX69qrQqWrFivZruWxRpW7dm1Y9mmbUt3rl25eOPqRZuX7164fgMDHvy2sNvDdfsSRnz3r+HEjhkrftxYMOXJkscS2EzgcmTIljOHBr2YtOfRlUunPq0as2nRrT+vhs26Nu3br3PP1u16t+/ewGUHRz08NnHhyI8rN87cNu/kzXH/hu58+vLqxbFTl56d+3aBBsIbjaAooLwA7de9p3++3np09u/do4/fHf78++rpf5efH7/9/gD+JyB/A9ZH4IEGJrifgu0xqF+DC0YI4YQPVugfghJaGCCGFF7ooIcZgtjhhh+SGKKJIxZ4ooopcqghiy+6KGKMJcI4440o0riijDniaGOPQP4oJI81HWDkARQVoGQBFA3g5AAUBSBlAAcFBAA7")
}

.x-tab-focus.x-tab-over .x-tab-default-bottom-mc {
    background-repeat: repeat-x;
    background-image: url("data:image/gif;R0lGODlhAQAgA/MAANzp/t7r/t/s/uHt/+Pu/+Tv/+bx/+jy/////9zp/tzp/tzp/tzp/tzp/tzp/tzp/iH5BAEAAAgALAAAAAABACADQwg5AA8IHEiwoMGDCBMqXMiwocOHECNKnJhwAMWLGDNq3Mixo8ICATyKHEmypMmTKFOqXGnSAAEBAAICADs=")
}

.x-tab.x-tab-active .x-tab-default-bottom-tl, .x-tab.x-tab-active .x-tab-default-bottom-bl, .x-tab.x-tab-active .x-tab-default-bottom-tr, .x-tab.x-tab-active .x-tab-default-bottom-br, .x-tab.x-tab-active .x-tab-default-bottom-tc, .x-tab.x-tab-active .x-tab-default-bottom-bc {
    background-image: url("data:image/gif;R0lGODlhBAAYAPQAAI2z45e65Zi65Z6+55++6LPM7d7s/fL2/PP3/PT4/Pr8/vv8/vz9/v7+/v7+//7//////////wAAAI2z442z442z442z442z442z442z442z442z442z442z442z442z4yH5BAEAABEALAAAAAAEABgARAhKAA0INAAAgsAADhQoXCgQAgAFCxwIGGgAgkWHBgc6PDAgwYMHCQgcoEiRgUkGAFKmzFiQosOGAAogaMAgwoECAhg0QICzwIEIAQEAOw==")
}

.x-tab.x-tab-active .x-tab-default-bottom-ml, .x-tab.x-tab-active .x-tab-default-bottom-mr {
    background-image: url("data:image/gif;R0lGODlhCAAgA/MAAI2z497s/eLu/efx/ez0/fH2/fX5/vf6/vj7/v///////42z442z442z442z442z4yH5BAEAAAoALAAAAAAIACADQwj/AAEkCEAwQAIAAgsaRDiw4MGEDhkqfNiQIMWJEiNCtJiR48aFHy9qrAiSpEiPJjuWxBhS5cmVI1mmbElzpk2ZOGPqRJmT506YPoMCHfqyqMujNXsSRXrzp9GkTpkqfdpUKNWpUqNCtZqV69alX69qrQqWrFivZruWxRpW7dm1Y9mmbUt3rl25eOPqRZuX7164fgMDHvy2sNvDdfsSRnz3r+HEjhkrftxYMOXJkscW2FzgcmTIljOHBr2YtOfRlUunPq0as2nRrT+vhs26Nu3br3PP1u16t+/ewGUHRz08NnHhyI8rN87cNu/kzXH/hu58+vLqxbFTl56d+3aBA8IPjaB4oPwB7de9p3++3np09u/do4/fHf78++rpf5efH7/9/gD+JyB/A9ZH4IEGJrifgu0xqF+DC0YI4YQPVugfghJaGCCGFF7ooIcZgtjhhh+SGKKJIxZ4ooopcqghiy+6KGKMJcI4440o0riijDniaGOPQP4oJI81CWCkABQRoCQBFBngpAEUISAlAgcFBAA7")
}

.x-tab.x-tab-active .x-tab-default-bottom-mc {
    background-repeat: repeat-x;
    background-image: url("data:image/gif;R0lGODlhAQAgA/MAAN7s/eLu/efx/ez0/fH2/fX5/vf6/vj7/v///97s/d7s/d7s/d7s/d7s/d7s/d7s/SH5BAEAAAgALAAAAAABACADQwg5AAEIHEiwoMGDCBMqXMiwocOHECNKnJiQAMWLGDNq3Mixo0IBBjyKHEmypMmTKFOqXGkywIACBwICADs=")
}

.x-tab-focus.x-tab-active .x-tab-default-bottom-tl, .x-tab-focus.x-tab-active .x-tab-default-bottom-bl, .x-tab-focus.x-tab-active .x-tab-default-bottom-tr, .x-tab-focus.x-tab-active .x-tab-default-bottom-br, .x-tab-focus.x-tab-active .x-tab-default-bottom-tc, .x-tab-focus.x-tab-active .x-tab-default-bottom-bc {
    background-image: url("data:image/gif;R0lGODlhBAAYAPQAAI2z45e65Zi65Z6+55++6LPM7d7s/fL2/PP3/PT4/Pr8/vv8/vz9/v7+/v7+//7//////////wAAAI2z442z442z442z442z442z442z442z442z442z442z442z442z4yH5BAEAABEALAAAAAAEABgARAhKAA0INAAAgsAADhQoXCgQAgAFCxwIGGgAgkWHBgc6PDAgwYMHCQgcoEiRgUkGAFKmzFiQosOGAAogaMAgwoECAhg0QICzwIEIAQEAOw==")
}

.x-tab-focus.x-tab-active .x-tab-default-bottom-ml, .x-tab-focus.x-tab-active .x-tab-default-bottom-mr {
    background-image: url("data:image/gif;R0lGODlhCAAgA/MAAI2z497s/eLu/efx/ez0/fH2/fX5/vf6/vj7/v///////42z442z442z442z442z4yH5BAEAAAoALAAAAAAIACADQwj/AAEkCEAwQAIAAgsaRDiw4MGEDhkqfNiQIMWJEiNCtJiR48aFHy9qrAiSpEiPJjuWxBhS5cmVI1mmbElzpk2ZOGPqRJmT506YPoMCHfqyqMujNXsSRXrzp9GkTpkqfdpUKNWpUqNCtZqV69alX69qrQqWrFivZruWxRpW7dm1Y9mmbUt3rl25eOPqRZuX7164fgMDHvy2sNvDdfsSRnz3r+HEjhkrftxYMOXJkscW2FzgcmTIljOHBr2YtOfRlUunPq0as2nRrT+vhs26Nu3br3PP1u16t+/ewGUHRz08NnHhyI8rN87cNu/kzXH/hu58+vLqxbFTl56d+3aBA8IPjaB4oPwB7de9p3++3np09u/do4/fHf78++rpf5efH7/9/gD+JyB/A9ZH4IEGJrifgu0xqF+DC0YI4YQPVugfghJaGCCGFF7ooIcZgtjhhh+SGKKJIxZ4ooopcqghiy+6KGKMJcI4440o0riijDniaGOPQP4oJI81CWCkABQRoCQBFBngpAEUISAlAgcFBAA7")
}

.x-tab-focus.x-tab-active .x-tab-default-bottom-mc {
    background-repeat: repeat-x;
    background-image: url("data:image/gif;R0lGODlhAQAgA/MAAN7s/eLu/efx/ez0/fH2/fX5/vf6/vj7/v///97s/d7s/d7s/d7s/d7s/d7s/d7s/SH5BAEAAAgALAAAAAABACADQwg5AAEIHEiwoMGDCBMqXMiwocOHECNKnJiQAMWLGDNq3Mixo0IBBjyKHEmypMmTKFOqXGkywIACBwICADs=")
}

.x-tab.x-tab-disabled .x-tab-default-bottom-tl, .x-tab.x-tab-disabled .x-tab-default-bottom-bl, .x-tab.x-tab-disabled .x-tab-default-bottom-tr, .x-tab.x-tab-disabled .x-tab-default-bottom-br, .x-tab.x-tab-disabled .x-tab-default-bottom-tc, .x-tab.x-tab-disabled .x-tab-default-bottom-bc {
    background-image: url("data:image/gif;R0lGODlhBAAYAPQAALvS78HW8MHW8cba8tLg8+Lt+uXv+uXv++rz/evz/uz0/vX4/fX5/fb6/ff5/P3+/v3+/////////wAAALvS77vS77vS77vS77vS77vS77vS77vS77vS77vS77vS77vS7yH5BAEAABIALAAAAAAEABgARAhQABUIVAAggkABDwwUWLhQYAQABQ48CJCgYoIIGB9GsHgRgIMBDCBAYDDAAUcEKBEwLACgZcuNCQqirPgQ5UMCCxockOCAQIADDRb4JOBAQkAAOw==")
}

.x-tab.x-tab-disabled .x-tab-default-bottom-ml, .x-tab.x-tab-disabled .x-tab-default-bottom-mr {
    background-image: url("data:image/gif;R0lGODlhCAAgA/MAALvS7+Pt++Pu++Tu++Xv++bv/Obw/Ofw/Ofx/Ojx/eny/f///////7vS77vS77vS7yH5BAEAAAwALAAAAAAIACADQwj/AAEsUEBQwQIAAgsaRDiw4MGEDhkqfNiQIMWJEiNCtJiR48aFHy9qrAiSpEiPJjuWxBhS5cmVI1mmbElzpk2ZOGPqRJmT506YPoMCHfqyqMujNXsSRXrzp9GkTpkqfdpUKNWpUqNCtZqV69alX69qrQqWrFivZruWNcDWwNmyWMOqfUt3rl25eNPmjau3L9+/YwGjFQw3sOHBhwsjXqy4cd29iR/7jXx3MmPJhDFThowygecEFAeIHqD5cuXMpzdbdpzaNGfWr0vDXi27duvZqGPftq27N+3dwH3n/i1c9fDjxpO7Js4c+XLnuJVHfy6dd/Pqwa9T3z69u3Xo37EXoecenjzDA+gPUCTAngBFAfAFlPeeHXx98drpj9eff77/++bt95+AAPJnH4EI9lfggAomeGCDED4oIX4TBhghhRhaWKGBGXKoYYcMbhgiiAuW6CCJJ36ooocsjriiiy2aeOGLMopYI4ozxpiijjnC6OONNO74o5BA8mgjkUj2WOSQSib54GegMYTAlAhQlJ56DBWgZQHrtRfaaBQFIGYABwUEADs=")
}

.x-tab.x-tab-disabled .x-tab-default-bottom-mc {
    background-repeat: repeat-x;
    background-image: url("data:image/gif;R0lGODlhAQAgA/MAAOPt++Pu++Tu++Xv++bv/Obw/Ofw/Ofx/Ojx/eny/ery/f///+Pt++Pt++Pt++Pt+yH5BAEAAAsALAAAAAABACADQwhDABUIHEiwoMGDCBMqXMiwIcICDiNKnEiRIgIBFTNq3Mixo8ePEhMYGBAApMmTKFOqXMmypcuXMAUmQHDAAIEBAgAEBAA7")
}

.x-tab-over .x-tab-default-left-tl, .x-tab-over .x-tab-default-left-bl, .x-tab-over .x-tab-default-left-tr, .x-tab-over .x-tab-default-left-br, .x-tab-over .x-tab-default-left-tc, .x-tab-over .x-tab-default-left-bc {
    background-image: url("data:image/gif;R0lGODlhBAAYAPQAAI2z45e65Zi65Zu85p2857PM7dnn/dvo/d3p/d/q/eHr+eTt+ejy/+rz/+z0/e/0/O/1/PL2/PP4//T4/vz9//39/////////wAAAI2z442z442z442z442z442z442z4yH5BAEAABcALAAAAAAEABgARAhHAAEIBHAhQoEAASg0YMCQ4UAADRkYmGhgIcMCECYgoGggwgAFDiJaGGnhgMkDER9GIPCAQoAKCQ6QLHmywAIJDAoWEJByYEAAOw==")
}

.x-tab-over .x-tab-default-left-ml, .x-tab-over .x-tab-default-left-mr {
    background-image: url("data:image/gif;R0lGODlhCAAQAPMAAI2z49zq/t7r/uDt/+Hu/+Pv/+Xw/+fx/+jy/////////42z442z442z442z442z4yH5BAEAAAoALAAAAAAIABAAQwg8AAEkCECwoEAECBMKLMCw4cGECAUOmEhR4IGLGB9C1KgwgYCPIAUSGElSoIGTKDlGTABxZUsEKmGybBkQADs=")
}

.x-tab-over .x-tab-default-left-mc {
    background-repeat: repeat-x;
    background-image: url("data:image/gif;R0lGODlhAQAQAPMAANzq/t7r/uDt/+Hu/+Pv/+Xw/+fx/+jy/////9zq/tzq/tzq/tzq/tzq/tzq/tzq/iH5BAEAAAgALAAAAAABABAAQwgRAAEcIHBAgIEDBwIMKICwYUAAOw==")
}

.x-tab-focus .x-tab-default-left-tl, .x-tab-focus .x-tab-default-left-bl, .x-tab-focus .x-tab-default-left-tr, .x-tab-focus .x-tab-default-left-br, .x-tab-focus .x-tab-default-left-tc, .x-tab-focus .x-tab-default-left-bc {
    background-image: url("data:image/gif;R0lGODlhBAAYAPQAAI2z45e65Zi65Zu75p2857PM7c7g99Dh99Pj+NXk+N7q+N7s/eHr+eHu/efx/O31/u70+/H2/fL2/Pv9//z9/v///////wAAAI2z442z442z442z442z442z442z442z4yH5BAEAABYALAAAAAAEABgARAhHAAEIBGBBQoEAASY0WMCQ4UAADRcYmGhgIcMCECIgoGhAwgAFDiJWGFnhgMkDER9KIACBQgAKCQ6QLHmyAIMHCwoWEJByYEAAOw==")
}

.x-tab-focus .x-tab-default-left-ml, .x-tab-focus .x-tab-default-left-mr {
    background-image: url("data:image/gif;R0lGODlhCAAQAPMAAI2z49Lj+NTk+dbm+tfn+tno+9vq/N3r/N7s/f///////42z442z442z442z442z4yH5BAEAAAoALAAAAAAIABAAQwg8AAEkCECwoEAECBMKLMCw4cGECAUOmEhR4IGLGB9C1KgwgYCPIAUSGElSoIGTKDlGTABxZUsEKmGybBkQADs=")
}

.x-tab-focus .x-tab-default-left-mc {
    background-repeat: repeat-x;
    background-image: url("data:image/gif;R0lGODlhAQAQAPMAANLj+NTk+dbm+tfn+tno+9vq/N3r/N7s/f///9Lj+NLj+NLj+NLj+NLj+NLj+NLj+CH5BAEAAAgALAAAAAABABAAQwgRAAEcIHBAgIEDBwIMKICwYUAAOw==")
}

.x-tab-focus.x-tab-over .x-tab-default-left-tl, .x-tab-focus.x-tab-over .x-tab-default-left-bl, .x-tab-focus.x-tab-over .x-tab-default-left-tr, .x-tab-focus.x-tab-over .x-tab-default-left-br, .x-tab-focus.x-tab-over .x-tab-default-left-tc, .x-tab-focus.x-tab-over .x-tab-default-left-bc {
    background-image: url("data:image/gif;R0lGODlhBAAYAPQAAI2z45e65Zi65Zu85p2857PM7dnn/dvo/d3p/d/q/eHr+eTt+ejy/+rz/+z0/e/0/O/1/PL2/PP4//T4/vz9//39/////////wAAAI2z442z442z442z442z442z442z4yH5BAEAABcALAAAAAAEABgARAhHAAEIBHAhQoEAASg0YMCQ4UAADRkYmGhgIcMCECYgoGggwgAFDiJaGGnhgMkDER9GIPCAQoAKCQ6QLHmywAIJDAoWEJByYEAAOw==")
}

.x-tab-focus.x-tab-over .x-tab-default-left-ml, .x-tab-focus.x-tab-over .x-tab-default-left-mr {
    background-image: url("data:image/gif;R0lGODlhCAAQAPMAAI2z49zq/t7r/uDt/+Hu/+Pv/+Xw/+fx/+jy/////////42z442z442z442z442z4yH5BAEAAAoALAAAAAAIABAAQwg8AAEkCECwoEAECBMKLMCw4cGECAUOmEhR4IGLGB9C1KgwgYCPIAUSGElSoIGTKDlGTABxZUsEKmGybBkQADs=")
}

.x-tab-focus.x-tab-over .x-tab-default-left-mc {
    background-repeat: repeat-x;
    background-image: url("data:image/gif;R0lGODlhAQAQAPMAANzq/t7r/uDt/+Hu/+Pv/+Xw/+fx/+jy/////9zq/tzq/tzq/tzq/tzq/tzq/tzq/iH5BAEAAAgALAAAAAABABAAQwgRAAEcIHBAgIEDBwIMKICwYUAAOw==")
}

.x-tab.x-tab-active .x-tab-default-left-tl, .x-tab.x-tab-active .x-tab-default-left-bl, .x-tab.x-tab-active .x-tab-default-left-tr, .x-tab.x-tab-active .x-tab-default-left-br, .x-tab.x-tab-active .x-tab-default-left-tc, .x-tab.x-tab-active .x-tab-default-left-bc {
    background-image: url("data:image/gif;R0lGODlhBAAYAPQAAI2z45e65Zi65Zu75p2957PM7d7q+N7s/eHr+eHu/efx/O31/vL2/PP3/PT3/Pr8/vv9//z9/v7+/v7+//7//////////wAAAI2z442z442z442z442z442z442z442z4yH5BAEAABYALAAAAAAEABgARAhFAAEIBGCBQYEAASAkOMCQ4UAADQ9EmBhhIcMCDSRQnMhggAEFESuIrPCg5IOIDxkQcEAhwISSI0maLIBgwYGCBQSgHBgQADs=")
}

.x-tab.x-tab-active .x-tab-default-left-ml, .x-tab.x-tab-active .x-tab-default-left-mr {
    background-image: url("data:image/gif;R0lGODlhCAAQAPMAAI2z497s/eDt/eXw/erz/e/2/fT4/fb6/vj7/v///////42z442z442z442z442z4yH5BAEAAAoALAAAAAAIABAAQwg8AAEkQECwoMAACBMKJMCw4cGECAUamEhRoICLGB9C1KgwwYGPIAUWGElS4ICTKDlGTABxZcsAKmGybBkQADs=")
}

.x-tab.x-tab-active .x-tab-default-left-mc {
    background-repeat: repeat-x;
    background-image: url("data:image/gif;R0lGODlhAQAQAPMAAN7s/eDt/eXw/erz/e/2/fT4/fb6/vj7/v///97s/d7s/d7s/d7s/d7s/d7s/d7s/SH5BAEAAAgALAAAAAABABAAQwgRAA8AGACgQAAAAAwQEICwYUAAOw==")
}

.x-tab-focus.x-tab-active .x-tab-default-left-tl, .x-tab-focus.x-tab-active .x-tab-default-left-bl, .x-tab-focus.x-tab-active .x-tab-default-left-tr, .x-tab-focus.x-tab-active .x-tab-default-left-br, .x-tab-focus.x-tab-active .x-tab-default-left-tc, .x-tab-focus.x-tab-active .x-tab-default-left-bc {
    background-image: url("data:image/gif;R0lGODlhBAAYAPQAAI2z45e65Zi65Zu75p2957PM7d7q+N7s/eHr+eHu/efx/O31/vL2/PP3/PT3/Pr8/vv9//z9/v7+/v7+//7//////////wAAAI2z442z442z442z442z442z442z442z4yH5BAEAABYALAAAAAAEABgARAhFAAEIBGCBQYEAASAkOMCQ4UAADQ9EmBhhIcMCDSRQnMhggAEFESuIrPCg5IOIDxkQcEAhwISSI0maLIBgwYGCBQSgHBgQADs=")
}

.x-tab-focus.x-tab-active .x-tab-default-left-ml, .x-tab-focus.x-tab-active .x-tab-default-left-mr {
    background-image: url("data:image/gif;R0lGODlhCAAQAPMAAI2z497s/eDt/eXw/erz/e/2/fT4/fb6/vj7/v///////42z442z442z442z442z4yH5BAEAAAoALAAAAAAIABAAQwg8AAEkQECwoMAACBMKJMCw4cGECAUamEhRoICLGB9C1KgwwYGPIAUWGElS4ICTKDlGTABxZcsAKmGybBkQADs=")
}

.x-tab-focus.x-tab-active .x-tab-default-left-mc {
    background-repeat: repeat-x;
    background-image: url("data:image/gif;R0lGODlhAQAQAPMAAN7s/eDt/eXw/erz/e/2/fT4/fb6/vj7/v///97s/d7s/d7s/d7s/d7s/d7s/d7s/SH5BAEAAAgALAAAAAABABAAQwgRAA8AGACgQAAAAAwQEICwYUAAOw==")
}

.x-tab.x-tab-disabled .x-tab-default-left-tl, .x-tab.x-tab-disabled .x-tab-default-left-bl, .x-tab.x-tab-disabled .x-tab-default-left-tr, .x-tab.x-tab-disabled .x-tab-default-left-br, .x-tab.x-tab-disabled .x-tab-default-left-tc, .x-tab.x-tab-disabled .x-tab-default-left-bc {
    background-image: url("data:image/gif;R0lGODlhBAAYAPQAALvS78HW8MHW8cTZ8cXZ8tLg8+Lt+uXv+uvz/uzy++z0/u30++30/u71/vH3/fT5/vX4/fb6/ff5/Pf6/f3+/v3+/////////wAAALvS77vS77vS77vS77vS77vS77vS7yH5BAEAABcALAAAAAAEABgARAhHAAEIBHBhQgEBAiowQMCQ4UAADREYmGiggYKLBSBEOEDRgIQBCRxcvGihpIWOER9KIAChggAKHE2epFhgwQMEFyQUCJByYEAAOw==")
}

.x-tab.x-tab-disabled .x-tab-default-left-ml, .x-tab.x-tab-disabled .x-tab-default-left-mr {
    background-image: url("data:image/gif;R0lGODlhCAAQAPQAALvS7+Pt++Pu++Tu++Xv++Xv/Obv/Obw/Ofw/Ofx/Ojx/Ojx/eny/ery/erz/f///////7vS77vS77vS77vS77vS77vS77vS77vS77vS77vS77vS77vS77vS77vS77vS7yH5BAEAABAALAAAAAAIABAARAhKAAE8CECwoEAECBMKJMCwoUAGECMKHECxokADGDMKVMCxo8AGIEMKFECy5MSKFAUWWMlS4IGXMAUmmElT4IKbOB9GhCjQgc+fAQEAOw==")
}

.x-tab.x-tab-disabled .x-tab-default-left-mc {
    background-repeat: repeat-x;
    background-image: url("data:image/gif;R0lGODlhAQAQAPMAAOPt++Pu++Tu++Xv++Xv/Obv/Obw/Ofw/Ofx/Ojx/Ojx/eny/ery/erz/f///+Pt+yH5BAEAAA4ALAAAAAABABAAQwgVAAEcGLBAQIEEDAIIIGAAgYIFDQICADs=")
}

.x-tab-default-tl, .x-tab-default-bl, .x-tab-default-tr, .x-tab-default-br {
    -ms-filter: "progid:DXImageTransform.Microsoft.gradient(startColorstr=#00FFFFFF,endColorstr=#00FFFFFF)"
}

.x-tab-default .x-tab-close-btn {
    top: 2px;
    right: 2px;
    width: 11px;
    height: 11px;
    background: url("data:image/gif;R0lGODlhCwALAIcAAFR6r0D/QFuAs2KGuGiLvG+RwI2y45m76Mfb88/k+9Ln/Nbp/uHz/+j2//D5//T6//f8//v9/////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAMAAAEALAAAAAALAAsAAAhdAAMEOECw4AGBAyUoXCjh4AEJDBA4mIiAQcMDERAUKOBgI4IIBCE0IECSZAMIBB8wYDCg5coHBBkkEECTZgIGMQ0AAKBgpwGcBxgsMLCgKFGcA1cqXXlQoMGCAgMCADs=") 0 0;
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=60)";
    opacity: 0.6
}

.x-tab-default .x-tab-close-btn-over {
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=100)";
    opacity: 1
}

.x-tab-default.x-tab-active .x-tab-close-btn {
    background-position: 0 -11px
}

.x-tab-default.x-tab-disabled .x-tab-close-btn {
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=30)";
    opacity: 0.3
}

.x-tab-closable.x-tab-default .x-tab-button {
    padding-right: 14px
}

.x-cmd-slicer.x-tab-focus.x-tab-default-top:before {
    display: none;
    content: "x-slicer:, corners:url("data:image/gif;R0lGODlhBAAYAPQAAI2z45e65Zi65Z2957PM7c7g99Dh99Pj+NXk+N7s/e70+/H2/fL2/Pz9/v///////wAAAI2z442z442z442z442z442z442z442z442z442z442z442z442z442z442z4yH5BAEAAA8ALAAAAAAEABgARAhMAAEIBPCAAYEAABwkWMgwAAEGDxY6AFCgYgGGCQgoWHDgwAIFBBJinOigpAMDKA1gxMhggIIGARogMNBAwQAGBhA0ECAyQU+JAIAGBAA7"), sides:url("data:image/gif;R0lGODlhCAAgA/MAAI2z49Lj+NTk+dbm+tfn+tno+9vq/N3r/N7s/f///////42z442z442z442z442z4yH5BAEAAAoALAAAAAAIACADQwj/AAEkCEAwQAIAAhEoRHAw4cKGCRYyRBjxIUWJEDFetOhQYUaOFT1uFNlxYsmPJEOaVIlypcaTI12CfMkyZsubNnPC3FmTJ82fM4OmBDpUqMyiSI8qxenTKNOeUIku1RnVKVWpT7Fetdo0aVauVb1uFdt1atmvZMOaVYt2rVaBBeIWaEt3rFuwb9narXt2r9++gPUGzksYr+G0hREfvqu4MePHfAVLTgz57+TFkSlnxmxZc2fOg0EOGD0A4oHTBzY7Vl059OrPr123vhyb9mzPslnrhn0btO3duXkD/y28ePDjxJHjTs58uXPfz2tH7y0duvXq2KlrHz6d+/Xtxpt/jfeenTx45ePDd6cooL0AiATiE4BooL4B8/jVp0dfXn9//ueJ95+AAa4HYH4H+lfgfgQi2KCCDhr4YIIUTmihhBgymOGAGy7IoYYgfiiihyRGGGKJEKZYYYcmjtgiiiue+OKMKl4oY40s4nhjjC7q2COPMNr4o5BB5ggkjUf6WOSORCLZpJJOGvlkkn0FBAA7"), frame-bg:url("data:image/gif;R0lGODlhAQAgA/MAANLj+NTk+dbm+tfn+tno+9vq/N3r/N7s/f///9Lj+NLj+NLj+NLj+NLj+NLj+NLj+CH5BAEAAAgALAAAAAABACADQwg6AAEcGEiwoMGDCBMqXMiwocOEBB5KnEixokUBBixq3Mixo8ePICsGGFAgpMmTKFOqXMmypcuXMBEGBAA7"), frame:4px 4px 4px 4px, stretch:bottom" !important
}

.x-cmd-slicer.x-tab-focus.x-tab-default-right:before {
    display: none;
    content: "x-slicer:, corners:url("data:image/gif;R0lGODlhBAAYAPQAAI2z45e65Zi65Zu75p2857PM7c7g99Dh99Pj+NXk+N7q+N7s/eHr+eHu/efx/O31/u70+/H2/fL2/Pv9//z9/v///////wAAAI2z442z442z442z442z442z442z442z4yH5BAEAABYALAAAAAAEABgARAhFAAEIHChwgcGDBgMUkGBhQYMJAgxINIBwogEEESAUQOhAwQAJFUJWOEDyAEKCIkeWpACBgIQDCSgIODlwwQMGBQQstBAQADs="), sides:url("data:image/gif;R0lGODlhCAAQAPMAAI2z49Lj+NTk+dbm+tfn+tno+9vq/N3r/N7s/f///////42z442z442z442z442z4yH5BAEAAAoALAAAAAAIABAAQwg7AAMIHJgAAIKDCAsWWMiwIMKEAAZInFjwgMWLDh8iyPiwoICPIAsSGEmyoIGTKDlC1LjRoEaVB2G2DAgAOw=="), frame-bg:url("data:image/gif;R0lGODlhAQAQAPMAANLj+NTk+dbm+tfn+tno+9vq/N3r/N7s/f///9Lj+NLj+NLj+NLj+NLj+NLj+NLj+CH5BAEAAAgALAAAAAABABAAQwgRAAEcIHBAgIEDBwIMKICwYUAAOw=="), frame:4px 4px 4px 4px, stretch:left" !important
}

.x-cmd-slicer.x-tab-focus.x-tab-default-bottom:before {
    display: none;
    content: "x-slicer:, corners:url("data:image/gif;R0lGODlhBAAYAPQAAI2z45e65Zi65Z2955696LPM7c7g99Dh99Pj+NXk+N7s/e70+/H2/fL2/Pz9/v///////wAAAI2z442z442z442z442z442z442z442z442z442z442z442z442z442z4yH5BAEAABAALAAAAAAEABgARAhLABUIVADggcAADhIcWLhQ4AMABxI4EDBQwYOLDw0OfNhgwAIHDhYQaFCxooGTBgCoVKmxYMWHDgEUWMAAAYQGBQQgYLAgZ4EGEAICADs="), sides:url("data:image/gif;R0lGODlhCAAgA/MAAI2z49Li+NPk+dXl+dfm+tno+9rp+9zq/N7s/f///////42z442z442z442z442z4yH5BAEAAAoALAAAAAAIACADQwj/AAEkQEAQQQIAAgsaRDiw4MGEDhkqfNiQIMWJEiNCtJiR48aFHy9qrAiSpEiPJjuWxBhS5cmVI1mmbElzpk2ZOGPqRJmT506YPoMCHfqyqMujNXsSRXrzp9GkTpkqfdpUKNWpUqNCtZqV69alX69qrQqWrFivZruWxRpW7dm1Y9mmbUt3rl25eOPqRZuX7164fgMDHvy2sNvDdfsSRnz3r+HEjhkrftxYMOXJkscS2EzgcmTIljOHBr2YtOfRlUunPq0as2nRrT+vhs26Nu3br3PP1u16t+/ewGUHRz08NnHhyI8rN87cNu/kzXH/hu58+vLqxbFTl56d+3aBBsIbjaAooLwA7de9p3++3np09u/do4/fHf78++rpf5efH7/9/gD+JyB/A9ZH4IEGJrifgu0xqF+DC0YI4YQPVugfghJaGCCGFF7ooIcZgtjhhh+SGKKJIxZ4ooopcqghiy+6KGKMJcI4440o0riijDniaGOPQP4oJI81HWDkARQVoGQBFA3g5AAUBSBlAAcFBAA7"), frame-bg:url("data:image/gif;R0lGODlhAQAgA/MAANLi+NPk+dXl+dfm+tno+9rp+9zq/N7s/f///9Li+NLi+NLi+NLi+NLi+NLi+NLi+CH5BAEAAAgALAAAAAABACADQwg5AA8IHEiwoMGDCBMqXMiwocOHECNKnJhwAMWLGDNq3Mixo8ICATyKHEmypMmTKFOqXGnSAAEBAAICADs="), frame:4px 4px 4px 4px, stretch:top" !important
}

.x-cmd-slicer.x-tab-focus.x-tab-default-left:before {
    display: none;
    content: "x-slicer:, corners:url("data:image/gif;R0lGODlhBAAYAPQAAI2z45e65Zi65Zu75p2857PM7c7g99Dh99Pj+NXk+N7q+N7s/eHr+eHu/efx/O31/u70+/H2/fL2/Pv9//z9/v///////wAAAI2z442z442z442z442z442z442z442z4yH5BAEAABYALAAAAAAEABgARAhHAAEIBGBBQoEAASY0WMCQ4UAADRcYmGhgIcMCECIgoGhAwgAFDiJWGFnhgMkDER9KIACBQgAKCQ6QLHmyAIMHCwoWEJByYEAAOw=="), sides:url("data:image/gif;R0lGODlhCAAQAPMAAI2z49Lj+NTk+dbm+tfn+tno+9vq/N3r/N7s/f///////42z442z442z442z442z4yH5BAEAAAoALAAAAAAIABAAQwg8AAEkCECwoEAECBMKLMCw4cGECAUOmEhR4IGLGB9C1KgwgYCPIAUSGElSoIGTKDlGTABxZUsEKmGybBkQADs="), frame-bg:url("data:image/gif;R0lGODlhAQAQAPMAANLj+NTk+dbm+tfn+tno+9vq/N3r/N7s/f///9Lj+NLj+NLj+NLj+NLj+NLj+NLj+CH5BAEAAAgALAAAAAABABAAQwgRAAEcIHBAgIEDBwIMKICwYUAAOw=="), frame:4px 4px 4px 4px, stretch:right" !important
}

.x-cmd-slicer.x-tab-over.x-tab-default-top:before {
    display: none;
    content: "x-slicer:, corners:url("data:image/gif;R0lGODlhBAAYAPQAAI2z45e65Zi65Z2957PM7dnn/dvo/d3p/d/q/ejy/+/1/PD1/PL2/PT4/vz9//39/////////wAAAI2z442z442z442z442z442z442z442z442z442z442z442z442z4yH5BAEAABEALAAAAAAEABgARAhMAAEIBBCBAYEAACAkWMgwAAEGERZCAFCgYgGGCQgoaHDgQAMFBBJinAihJAQDKA1gxMhgwAIHAR4gMOBgwQAGBhA8ECAyQU+JAIAGBAA7"), sides:url("data:image/gif;R0lGODlhCAAgA/MAAI2z49zq/t7r/uDt/+Hu/+Pv/+Xw/+fx/+jy/////////42z442z442z442z442z4yH5BAEAAAoALAAAAAAIACADQwj/AAEkCEAwQAIAAhEoRHAw4cKGCRYyRBjxIUWJEDFetOhQYUaOFT1uFNlxYsmPJEOaVIlypcaTI12CfMkyZsubNnPC3FmTJ82fM4OmBDpUqMyiSI8qxenTKNOeUIku1RnVKVWpT7Fetdo0aVauVb1uFdt1atmvZMOaVYt2rVaBBeIWaEt3rFuwb9narXt2r9++gPUGzksYr+G0hREfvqu4MePHfAVLTgz57+TFkSlnxmxZc2fOg0EOGD0A4oHTBzY7Vl059OrPr123vhyb9mzPslnrhn0btO3duXkD/y28ePDjxJHjTs58uXPfz2tH7y0duvXq2KlrHz6d+/Xtxpt/jfeenTx45ePDd6cooL0AiATiE4BooL4B8/jVp0dfXn9//ueJ95+AAa4HYH4H+lfgfgQi2KCCDhr4YIIUTmihhBgymOGAGy7IoYYgfiiihyRGGGKJEKZYYYcmjtgiiiue+OKMKl4oY40s4nhjjC7q2COPMNr4o5BB5ggkjUf6WOSORCLZpJJOGvlkkn0FBAA7"), frame-bg:url("data:image/gif;R0lGODlhAQAgA/MAANzq/t7r/uDt/+Hu/+Pv/+Xw/+fx/+jy/////9zq/tzq/tzq/tzq/tzq/tzq/tzq/iH5BAEAAAgALAAAAAABACADQwg6AAEcGEiwoMGDCBMqXMiwocOEBB5KnEixokUBBixq3Mixo8ePICsGGFAgpMmTKFOqXMmypcuXMBEGBAA7"), frame:4px 4px 4px 4px, stretch:bottom" !important
}

.x-cmd-slicer.x-tab-over.x-tab-default-right:before {
    display: none;
    content: "x-slicer:, corners:url("data:image/gif;R0lGODlhBAAYAPQAAI2z45e65Zi65Zu85p2857PM7dnn/dvo/d3p/d/q/eHr+eTt+ejy/+rz/+z0/e/0/O/1/PL2/PP4//T4/vz9//39/////////wAAAI2z442z442z442z442z442z442z4yH5BAEAABcALAAAAAAEABgARAhFAAEIHCiQgcGDBgMUiHCBQQMKAgxINIBwogEEEyAUQOhAwYAIFkJaOEDyAEKCIkeWpPCAQIQDCSoIODmQgYQFBQQsvBAQADs="), sides:url("data:image/gif;R0lGODlhCAAQAPMAAI2z49zq/t7r/uDt/+Hu/+Pv/+Xw/+fx/+jy/////////42z442z442z442z442z4yH5BAEAAAoALAAAAAAIABAAQwg7AAMIHJgAAIKDCAsWWMiwIMKEAAZInFjwgMWLDh8iyPiwoICPIAsSGEmyoIGTKDlC1LjRoEaVB2G2DAgAOw=="), frame-bg:url("data:image/gif;R0lGODlhAQAQAPMAANzq/t7r/uDt/+Hu/+Pv/+Xw/+fx/+jy/////9zq/tzq/tzq/tzq/tzq/tzq/tzq/iH5BAEAAAgALAAAAAABABAAQwgRAAEcIHBAgIEDBwIMKICwYUAAOw=="), frame:4px 4px 4px 4px, stretch:left" !important
}

.x-cmd-slicer.x-tab-over.x-tab-default-bottom:before {
    display: none;
    content: "x-slicer:, corners:url("data:image/gif;R0lGODlhBAAYAPQAAI2z45e65Zi65Z2955696LPM7dnn/dro/d3p/d7q/ejy/+/1/PD1/PL2/PT4/vz9//39/////////wAAAI2z442z442z442z442z442z442z442z442z442z442z442z4yH5BAEAABIALAAAAAAEABgARAhLABUIVAAggsAAEBIcWLhQYAQABxJAEDBQQYSLDw0OfNhgAIMHDxgQaFCxooGTBgCoVKmxYMWHDgEUWOAAgYQGBQQgcLAgZ4EGEgICADs="), sides:url("data:image/gif;R0lGODlhCAAgA/MAAI2z49zp/t7r/t/s/uHt/+Pu/+Tv/+bx/+jy/////////42z442z442z442z442z4yH5BAEAAAoALAAAAAAIACADQwj/AAEkQEAQQQIAAgsaRDiw4MGEDhkqfNiQIMWJEiNCtJiR48aFHy9qrAiSpEiPJjuWxBhS5cmVI1mmbElzpk2ZOGPqRJmT506YPoMCHfqyqMujNXsSRXrzp9GkTpkqfdpUKNWpUqNCtZqV69alX69qrQqWrFivZruWxRpW7dm1Y9mmbUt3rl25eOPqRZuX7164fgMDHvy2sNvDdfsSRnz3r+HEjhkrftxYMOXJkscS2EzgcmTIljOHBr2YtOfRlUunPq0as2nRrT+vhs26Nu3br3PP1u16t+/ewGUHRz08NnHhyI8rN87cNu/kzXH/hu58+vLqxbFTl56d+3aBBsIbjaAooLwA7de9p3++3np09u/do4/fHf78++rpf5efH7/9/gD+JyB/A9ZH4IEGJrifgu0xqF+DC0YI4YQPVugfghJaGCCGFF7ooIcZgtjhhh+SGKKJIxZ4ooopcqghiy+6KGKMJcI4440o0riijDniaGOPQP4oJI81HWDkARQVoGQBFA3g5AAUBSBlAAcFBAA7"), frame-bg:url("data:image/gif;R0lGODlhAQAgA/MAANzp/t7r/t/s/uHt/+Pu/+Tv/+bx/+jy/////9zp/tzp/tzp/tzp/tzp/tzp/tzp/iH5BAEAAAgALAAAAAABACADQwg5AA8IHEiwoMGDCBMqXMiwocOHECNKnJhwAMWLGDNq3Mixo8ICATyKHEmypMmTKFOqXGnSAAEBAAICADs="), frame:4px 4px 4px 4px, stretch:top" !important
}

.x-cmd-slicer.x-tab-over.x-tab-default-left:before {
    display: none;
    content: "x-slicer:, corners:url("data:image/gif;R0lGODlhBAAYAPQAAI2z45e65Zi65Zu85p2857PM7dnn/dvo/d3p/d/q/eHr+eTt+ejy/+rz/+z0/e/0/O/1/PL2/PP4//T4/vz9//39/////////wAAAI2z442z442z442z442z442z442z4yH5BAEAABcALAAAAAAEABgARAhHAAEIBHAhQoEAASg0YMCQ4UAADRkYmGhgIcMCECYgoGggwgAFDiJaGGnhgMkDER9GIPCAQoAKCQ6QLHmywAIJDAoWEJByYEAAOw=="), sides:url("data:image/gif;R0lGODlhCAAQAPMAAI2z49zq/t7r/uDt/+Hu/+Pv/+Xw/+fx/+jy/////////42z442z442z442z442z4yH5BAEAAAoALAAAAAAIABAAQwg8AAEkCECwoEAECBMKLMCw4cGECAUOmEhR4IGLGB9C1KgwgYCPIAUSGElSoIGTKDlGTABxZUsEKmGybBkQADs="), frame-bg:url("data:image/gif;R0lGODlhAQAQAPMAANzq/t7r/uDt/+Hu/+Pv/+Xw/+fx/+jy/////9zq/tzq/tzq/tzq/tzq/tzq/tzq/iH5BAEAAAgALAAAAAABABAAQwgRAAEcIHBAgIEDBwIMKICwYUAAOw=="), frame:4px 4px 4px 4px, stretch:right" !important
}

.x-cmd-slicer.x-tab-active.x-tab-default-top:before {
    display: none;
    content: "x-slicer:, corners:url("data:image/gif;R0lGODlhBAAYAPQAAI2z45e65Zi65Z6+57PM7d7s/fL2/PP3/PT4/Pr8/vv8/vz9/v7+/v7+//7//////////wAAAI2z442z442z442z442z442z442z442z442z442z442z442z442z442z4yH5BAEAABAALAAAAAAEABgARAhKAAEIBADBAIEAAB4UWMgwAAEDEBY+ALCg4gKGBQgcYFCRwQECCTFOfEDyQYKTCTBiNDAAgYMADU46QDDAQAIFDQSELLBTIgCfAQEAOw=="), sides:url("data:image/gif;R0lGODlhCAAgA/MAAI2z497s/eDt/eXw/erz/e/2/fT4/fb6/vj7/v///////42z442z442z442z442z4yH5BAEAAAoALAAAAAAIACADQwj/AAEkQEAQQQIAAgMoDHAw4cKGCRYyRBjxIUWJEDFetOhQYUaOFT1uFNlxYsmPJEOaVIlypcaTI12CfMkyZsubNnPC3FmTJ82fM4OmBDpUqMyiSI8qxenTKNOeUIku1RnVKVWpT7Fetdo0aVauVb1uFdt1atmvZMOaVYt2rVaBBOISaEt3rFuwb9narXt2r9++gPUGzksYr+G0hREfvqu4MePHfAVLTgz57+TFkSlnxmxZc2fOg0EaGG0AooDTAjY7Vl059OrPr123vhyb9mzPslnrhn0btO3duXkD/y28ePDjxJHjTs58uXPfz2tH7y0duvXq2KlrHz6d+/Xtxpt/jfeenTx45ePDd6d4oP0BiAXiF4A4oP4A8/jVp0dfXn9//ueJ95+AAa4HYH4H+lfgfgQi2KCCDhr4YIIUTmihhBgymOGAGy7IoYYgfiiihyRGGGKJEKZYYYcmjtgiiiue+OKMKl4oY40s4nhjjC7q2COPMNr4o5BB5ggkjUf6WOSORCLZpJJOGvlkkn0FBAA7"), frame-bg:url("data:image/gif;R0lGODlhAQAgA/MAAN7s/eDt/eXw/erz/e/2/fT4/fb6/vj7/v///97s/d7s/d7s/d7s/d7s/d7s/d7s/SH5BAEAAAgALAAAAAABACADQwg6AA8AGEiwoMGDCBMqXMiwocOEAx5KnEixosUCASxq3Mixo8ePICsaICAgpMmTKFOqXMmypcuXMBEGBAA7"), frame:4px 4px 4px 4px, stretch:bottom" !important
}

.x-cmd-slicer.x-tab-active.x-tab-default-right:before {
    display: none;
    content: "x-slicer:, corners:url("data:image/gif;R0lGODlhBAAYAPQAAI2z45e65Zi65Zu75p2957PM7d7q+N7s/eHr+eHu/efx/O31/vL2/PP3/PT3/Pr8/vv8/vv9//z9/v7+/v7+//7//////////wAAAI2z442z442z442z442z442z442z4yH5BAEAABcALAAAAAAEABgARAhEAAEIHCjwgMGDBgMUYHDhQIIIAiRIlIBwosQJDQogVGBgAAMLIC08GPkAIcGQIklWcECAwQMIFASYHHhgAYICAhZeCAgAOw=="), sides:url("data:image/gif;R0lGODlhCAAQAPMAAI2z497s/eDt/eXw/erz/e/2/fT4/fb6/vj7/v///////42z442z442z442z442z4yH5BAEAAAoALAAAAAAIABAAQwg7ABEIHJgAQICDCAsSWMiwIMKEAAxInFhQgMWLDh8GyPiw4IGPIAsWGEmy4ICTKDlC1LjRoEaVB2G2DAgAOw=="), frame-bg:url("data:image/gif;R0lGODlhAQAQAPMAAN7s/eDt/eXw/erz/e/2/fT4/fb6/vj7/v///97s/d7s/d7s/d7s/d7s/d7s/d7s/SH5BAEAAAgALAAAAAABABAAQwgRAA8AGACgQAAAAAwQEICwYUAAOw=="), frame:4px 4px 4px 4px, stretch:left" !important
}

.x-cmd-slicer.x-tab-active.x-tab-default-bottom:before {
    display: none;
    content: "x-slicer:, corners:url("data:image/gif;R0lGODlhBAAYAPQAAI2z45e65Zi65Z6+55++6LPM7d7s/fL2/PP3/PT4/Pr8/vv8/vz9/v7+/v7+//7//////////wAAAI2z442z442z442z442z442z442z442z442z442z442z442z442z4yH5BAEAABEALAAAAAAEABgARAhKAA0INAAAgsAADhQoXCgQAgAFCxwIGGgAgkWHBgc6PDAgwYMHCQgcoEiRgUkGAFKmzFiQosOGAAogaMAgwoECAhg0QICzwIEIAQEAOw=="), sides:url("data:image/gif;R0lGODlhCAAgA/MAAI2z497s/eLu/efx/ez0/fH2/fX5/vf6/vj7/v///////42z442z442z442z442z4yH5BAEAAAoALAAAAAAIACADQwj/AAEkCEAwQAIAAgsaRDiw4MGEDhkqfNiQIMWJEiNCtJiR48aFHy9qrAiSpEiPJjuWxBhS5cmVI1mmbElzpk2ZOGPqRJmT506YPoMCHfqyqMujNXsSRXrzp9GkTpkqfdpUKNWpUqNCtZqV69alX69qrQqWrFivZruWxRpW7dm1Y9mmbUt3rl25eOPqRZuX7164fgMDHvy2sNvDdfsSRnz3r+HEjhkrftxYMOXJkscW2FzgcmTIljOHBr2YtOfRlUunPq0as2nRrT+vhs26Nu3br3PP1u16t+/ewGUHRz08NnHhyI8rN87cNu/kzXH/hu58+vLqxbFTl56d+3aBA8IPjaB4oPwB7de9p3++3np09u/do4/fHf78++rpf5efH7/9/gD+JyB/A9ZH4IEGJrifgu0xqF+DC0YI4YQPVugfghJaGCCGFF7ooIcZgtjhhh+SGKKJIxZ4ooopcqghiy+6KGKMJcI4440o0riijDniaGOPQP4oJI81CWCkABQRoCQBFBngpAEUISAlAgcFBAA7"), frame-bg:url("data:image/gif;R0lGODlhAQAgA/MAAN7s/eLu/efx/ez0/fH2/fX5/vf6/vj7/v///97s/d7s/d7s/d7s/d7s/d7s/d7s/SH5BAEAAAgALAAAAAABACADQwg5AAEIHEiwoMGDCBMqXMiwocOHECNKnJiQAMWLGDNq3Mixo0IBBjyKHEmypMmTKFOqXGkywIACBwICADs="), frame:4px 4px 4px 4px, stretch:top" !important
}

.x-cmd-slicer.x-tab-active.x-tab-default-left:before {
    display: none;
    content: "x-slicer:, corners:url("data:image/gif;R0lGODlhBAAYAPQAAI2z45e65Zi65Zu75p2957PM7d7q+N7s/eHr+eHu/efx/O31/vL2/PP3/PT3/Pr8/vv9//z9/v7+/v7+//7//////////wAAAI2z442z442z442z442z442z442z442z4yH5BAEAABYALAAAAAAEABgARAhFAAEIBGCBQYEAASAkOMCQ4UAADQ9EmBhhIcMCDSRQnMhggAEFESuIrPCg5IOIDxkQcEAhwISSI0maLIBgwYGCBQSgHBgQADs="), sides:url("data:image/gif;R0lGODlhCAAQAPMAAI2z497s/eDt/eXw/erz/e/2/fT4/fb6/vj7/v///////42z442z442z442z442z4yH5BAEAAAoALAAAAAAIABAAQwg8AAEkQECwoMAACBMKJMCw4cGECAUamEhRoICLGB9C1KgwwYGPIAUWGElS4ICTKDlGTABxZcsAKmGybBkQADs="), frame-bg:url("data:image/gif;R0lGODlhAQAQAPMAAN7s/eDt/eXw/erz/e/2/fT4/fb6/vj7/v///97s/d7s/d7s/d7s/d7s/d7s/d7s/SH5BAEAAAgALAAAAAABABAAQwgRAA8AGACgQAAAAAwQEICwYUAAOw=="), frame:4px 4px 4px 4px, stretch:right" !important
}

.x-cmd-slicer.x-tab-focus.x-tab-over.x-tab-default-top:before {
    display: none;
    content: "x-slicer:, corners:url("data:image/gif;R0lGODlhBAAYAPQAAI2z45e65Zi65Z2957PM7dnn/dvo/d3p/d/q/ejy/+/1/PD1/PL2/PT4/vz9//39/////////wAAAI2z442z442z442z442z442z442z442z442z442z442z442z442z4yH5BAEAABEALAAAAAAEABgARAhMAAEIBBCBAYEAACAkWMgwAAEGERZCAFCgYgGGCQgoaHDgQAMFBBJinAihJAQDKA1gxMhgwAIHAR4gMOBgwQAGBhA8ECAyQU+JAIAGBAA7"), sides:url("data:image/gif;R0lGODlhCAAgA/MAAI2z49zq/t7r/uDt/+Hu/+Pv/+Xw/+fx/+jy/////////42z442z442z442z442z4yH5BAEAAAoALAAAAAAIACADQwj/AAEkCEAwQAIAAhEoRHAw4cKGCRYyRBjxIUWJEDFetOhQYUaOFT1uFNlxYsmPJEOaVIlypcaTI12CfMkyZsubNnPC3FmTJ82fM4OmBDpUqMyiSI8qxenTKNOeUIku1RnVKVWpT7Fetdo0aVauVb1uFdt1atmvZMOaVYt2rVaBBeIWaEt3rFuwb9narXt2r9++gPUGzksYr+G0hREfvqu4MePHfAVLTgz57+TFkSlnxmxZc2fOg0EOGD0A4oHTBzY7Vl059OrPr123vhyb9mzPslnrhn0btO3duXkD/y28ePDjxJHjTs58uXPfz2tH7y0duvXq2KlrHz6d+/Xtxpt/jfeenTx45ePDd6cooL0AiATiE4BooL4B8/jVp0dfXn9//ueJ95+AAa4HYH4H+lfgfgQi2KCCDhr4YIIUTmihhBgymOGAGy7IoYYgfiiihyRGGGKJEKZYYYcmjtgiiiue+OKMKl4oY40s4nhjjC7q2COPMNr4o5BB5ggkjUf6WOSORCLZpJJOGvlkkn0FBAA7"), frame-bg:url("data:image/gif;R0lGODlhAQAgA/MAANzq/t7r/uDt/+Hu/+Pv/+Xw/+fx/+jy/////9zq/tzq/tzq/tzq/tzq/tzq/tzq/iH5BAEAAAgALAAAAAABACADQwg6AAEcGEiwoMGDCBMqXMiwocOEBB5KnEixokUBBixq3Mixo8ePICsGGFAgpMmTKFOqXMmypcuXMBEGBAA7"), frame:4px 4px 4px 4px, stretch:bottom" !important
}

.x-cmd-slicer.x-tab-focus.x-tab-over.x-tab-default-right:before {
    display: none;
    content: "x-slicer:, corners:url("data:image/gif;R0lGODlhBAAYAPQAAI2z45e65Zi65Zu85p2857PM7dnn/dvo/d3p/d/q/eHr+eTt+ejy/+rz/+z0/e/0/O/1/PL2/PP4//T4/vz9//39/////////wAAAI2z442z442z442z442z442z442z4yH5BAEAABcALAAAAAAEABgARAhFAAEIHCiQgcGDBgMUiHCBQQMKAgxINIBwogEEEyAUQOhAwYAIFkJaOEDyAEKCIkeWpPCAQIQDCSoIODmQgYQFBQQsvBAQADs="), sides:url("data:image/gif;R0lGODlhCAAQAPMAAI2z49zq/t7r/uDt/+Hu/+Pv/+Xw/+fx/+jy/////////42z442z442z442z442z4yH5BAEAAAoALAAAAAAIABAAQwg7AAMIHJgAAIKDCAsWWMiwIMKEAAZInFjwgMWLDh8iyPiwoICPIAsSGEmyoIGTKDlC1LjRoEaVB2G2DAgAOw=="), frame-bg:url("data:image/gif;R0lGODlhAQAQAPMAANzq/t7r/uDt/+Hu/+Pv/+Xw/+fx/+jy/////9zq/tzq/tzq/tzq/tzq/tzq/tzq/iH5BAEAAAgALAAAAAABABAAQwgRAAEcIHBAgIEDBwIMKICwYUAAOw=="), frame:4px 4px 4px 4px, stretch:left" !important
}

.x-cmd-slicer.x-tab-focus.x-tab-over.x-tab-default-bottom:before {
    display: none;
    content: "x-slicer:, corners:url("data:image/gif;R0lGODlhBAAYAPQAAI2z45e65Zi65Z2955696LPM7dnn/dro/d3p/d7q/ejy/+/1/PD1/PL2/PT4/vz9//39/////////wAAAI2z442z442z442z442z442z442z442z442z442z442z442z4yH5BAEAABIALAAAAAAEABgARAhLABUIVAAggsAAEBIcWLhQYAQABxJAEDBQQYSLDw0OfNhgAIMHDxgQaFCxooGTBgCoVKmxYMWHDgEUWOAAgYQGBQQgcLAgZ4EGEgICADs="), sides:url("data:image/gif;R0lGODlhCAAgA/MAAI2z49zp/t7r/t/s/uHt/+Pu/+Tv/+bx/+jy/////////42z442z442z442z442z4yH5BAEAAAoALAAAAAAIACADQwj/AAEkQEAQQQIAAgsaRDiw4MGEDhkqfNiQIMWJEiNCtJiR48aFHy9qrAiSpEiPJjuWxBhS5cmVI1mmbElzpk2ZOGPqRJmT506YPoMCHfqyqMujNXsSRXrzp9GkTpkqfdpUKNWpUqNCtZqV69alX69qrQqWrFivZruWxRpW7dm1Y9mmbUt3rl25eOPqRZuX7164fgMDHvy2sNvDdfsSRnz3r+HEjhkrftxYMOXJkscS2EzgcmTIljOHBr2YtOfRlUunPq0as2nRrT+vhs26Nu3br3PP1u16t+/ewGUHRz08NnHhyI8rN87cNu/kzXH/hu58+vLqxbFTl56d+3aBBsIbjaAooLwA7de9p3++3np09u/do4/fHf78++rpf5efH7/9/gD+JyB/A9ZH4IEGJrifgu0xqF+DC0YI4YQPVugfghJaGCCGFF7ooIcZgtjhhh+SGKKJIxZ4ooopcqghiy+6KGKMJcI4440o0riijDniaGOPQP4oJI81HWDkARQVoGQBFA3g5AAUBSBlAAcFBAA7"), frame-bg:url("data:image/gif;R0lGODlhAQAgA/MAANzp/t7r/t/s/uHt/+Pu/+Tv/+bx/+jy/////9zp/tzp/tzp/tzp/tzp/tzp/tzp/iH5BAEAAAgALAAAAAABACADQwg5AA8IHEiwoMGDCBMqXMiwocOHECNKnJhwAMWLGDNq3Mixo8ICATyKHEmypMmTKFOqXGnSAAEBAAICADs="), frame:4px 4px 4px 4px, stretch:top" !important
}

.x-cmd-slicer.x-tab-focus.x-tab-over.x-tab-default-left:before {
    display: none;
    content: "x-slicer:, corners:url("data:image/gif;R0lGODlhBAAYAPQAAI2z45e65Zi65Zu85p2857PM7dnn/dvo/d3p/d/q/eHr+eTt+ejy/+rz/+z0/e/0/O/1/PL2/PP4//T4/vz9//39/////////wAAAI2z442z442z442z442z442z442z4yH5BAEAABcALAAAAAAEABgARAhHAAEIBHAhQoEAASg0YMCQ4UAADRkYmGhgIcMCECYgoGggwgAFDiJaGGnhgMkDER9GIPCAQoAKCQ6QLHmywAIJDAoWEJByYEAAOw=="), sides:url("data:image/gif;R0lGODlhCAAQAPMAAI2z49zq/t7r/uDt/+Hu/+Pv/+Xw/+fx/+jy/////////42z442z442z442z442z4yH5BAEAAAoALAAAAAAIABAAQwg8AAEkCECwoEAECBMKLMCw4cGECAUOmEhR4IGLGB9C1KgwgYCPIAUSGElSoIGTKDlGTABxZUsEKmGybBkQADs="), frame-bg:url("data:image/gif;R0lGODlhAQAQAPMAANzq/t7r/uDt/+Hu/+Pv/+Xw/+fx/+jy/////9zq/tzq/tzq/tzq/tzq/tzq/tzq/iH5BAEAAAgALAAAAAABABAAQwgRAAEcIHBAgIEDBwIMKICwYUAAOw=="), frame:4px 4px 4px 4px, stretch:right" !important
}

.x-cmd-slicer.x-tab-focus.x-tab-active.x-tab-default-top:before {
    display: none;
    content: "x-slicer:, corners:url("data:image/gif;R0lGODlhBAAYAPQAAI2z45e65Zi65Z6+57PM7d7s/fL2/PP3/PT4/Pr8/vv8/vz9/v7+/v7+//7//////////wAAAI2z442z442z442z442z442z442z442z442z442z442z442z442z442z4yH5BAEAABAALAAAAAAEABgARAhKAAEIBADBAIEAAB4UWMgwAAEDEBY+ALCg4gKGBQgcYFCRwQECCTFOfEDyQYKTCTBiNDAAgYMADU46QDDAQAIFDQSELLBTIgCfAQEAOw=="), sides:url("data:image/gif;R0lGODlhCAAgA/MAAI2z497s/eDt/eXw/erz/e/2/fT4/fb6/vj7/v///////42z442z442z442z442z4yH5BAEAAAoALAAAAAAIACADQwj/AAEkQEAQQQIAAgMoDHAw4cKGCRYyRBjxIUWJEDFetOhQYUaOFT1uFNlxYsmPJEOaVIlypcaTI12CfMkyZsubNnPC3FmTJ82fM4OmBDpUqMyiSI8qxenTKNOeUIku1RnVKVWpT7Fetdo0aVauVb1uFdt1atmvZMOaVYt2rVaBBOISaEt3rFuwb9narXt2r9++gPUGzksYr+G0hREfvqu4MePHfAVLTgz57+TFkSlnxmxZc2fOg0EaGG0AooDTAjY7Vl059OrPr123vhyb9mzPslnrhn0btO3duXkD/y28ePDjxJHjTs58uXPfz2tH7y0duvXq2KlrHz6d+/Xtxpt/jfeenTx45ePDd6d4oP0BiAXiF4A4oP4A8/jVp0dfXn9//ueJ95+AAa4HYH4H+lfgfgQi2KCCDhr4YIIUTmihhBgymOGAGy7IoYYgfiiihyRGGGKJEKZYYYcmjtgiiiue+OKMKl4oY40s4nhjjC7q2COPMNr4o5BB5ggkjUf6WOSORCLZpJJOGvlkkn0FBAA7"), frame-bg:url("data:image/gif;R0lGODlhAQAgA/MAAN7s/eDt/eXw/erz/e/2/fT4/fb6/vj7/v///97s/d7s/d7s/d7s/d7s/d7s/d7s/SH5BAEAAAgALAAAAAABACADQwg6AA8AGEiwoMGDCBMqXMiwocOEAx5KnEixosUCASxq3Mixo8ePICsaICAgpMmTKFOqXMmypcuXMBEGBAA7"), frame:4px 4px 4px 4px, stretch:bottom" !important
}

.x-cmd-slicer.x-tab-focus.x-tab-active.x-tab-default-right:before {
    display: none;
    content: "x-slicer:, corners:url("data:image/gif;R0lGODlhBAAYAPQAAI2z45e65Zi65Zu75p2957PM7d7q+N7s/eHr+eHu/efx/O31/vL2/PP3/PT3/Pr8/vv8/vv9//z9/v7+/v7+//7//////////wAAAI2z442z442z442z442z442z442z4yH5BAEAABcALAAAAAAEABgARAhEAAEIHCjwgMGDBgMUYHDhQIIIAiRIlIBwosQJDQogVGBgAAMLIC08GPkAIcGQIklWcECAwQMIFASYHHhgAYICAhZeCAgAOw=="), sides:url("data:image/gif;R0lGODlhCAAQAPMAAI2z497s/eDt/eXw/erz/e/2/fT4/fb6/vj7/v///////42z442z442z442z442z4yH5BAEAAAoALAAAAAAIABAAQwg7ABEIHJgAQICDCAsSWMiwIMKEAAxInFhQgMWLDh8GyPiw4IGPIAsWGEmy4ICTKDlC1LjRoEaVB2G2DAgAOw=="), frame-bg:url("data:image/gif;R0lGODlhAQAQAPMAAN7s/eDt/eXw/erz/e/2/fT4/fb6/vj7/v///97s/d7s/d7s/d7s/d7s/d7s/d7s/SH5BAEAAAgALAAAAAABABAAQwgRAA8AGACgQAAAAAwQEICwYUAAOw=="), frame:4px 4px 4px 4px, stretch:left" !important
}

.x-cmd-slicer.x-tab-focus.x-tab-active.x-tab-default-bottom:before {
    display: none;
    content: "x-slicer:, corners:url("data:image/gif;R0lGODlhBAAYAPQAAI2z45e65Zi65Z6+55++6LPM7d7s/fL2/PP3/PT4/Pr8/vv8/vz9/v7+/v7+//7//////////wAAAI2z442z442z442z442z442z442z442z442z442z442z442z442z4yH5BAEAABEALAAAAAAEABgARAhKAA0INAAAgsAADhQoXCgQAgAFCxwIGGgAgkWHBgc6PDAgwYMHCQgcoEiRgUkGAFKmzFiQosOGAAogaMAgwoECAhg0QICzwIEIAQEAOw=="), sides:url("data:image/gif;R0lGODlhCAAgA/MAAI2z497s/eLu/efx/ez0/fH2/fX5/vf6/vj7/v///////42z442z442z442z442z4yH5BAEAAAoALAAAAAAIACADQwj/AAEkCEAwQAIAAgsaRDiw4MGEDhkqfNiQIMWJEiNCtJiR48aFHy9qrAiSpEiPJjuWxBhS5cmVI1mmbElzpk2ZOGPqRJmT506YPoMCHfqyqMujNXsSRXrzp9GkTpkqfdpUKNWpUqNCtZqV69alX69qrQqWrFivZruWxRpW7dm1Y9mmbUt3rl25eOPqRZuX7164fgMDHvy2sNvDdfsSRnz3r+HEjhkrftxYMOXJkscW2FzgcmTIljOHBr2YtOfRlUunPq0as2nRrT+vhs26Nu3br3PP1u16t+/ewGUHRz08NnHhyI8rN87cNu/kzXH/hu58+vLqxbFTl56d+3aBA8IPjaB4oPwB7de9p3++3np09u/do4/fHf78++rpf5efH7/9/gD+JyB/A9ZH4IEGJrifgu0xqF+DC0YI4YQPVugfghJaGCCGFF7ooIcZgtjhhh+SGKKJIxZ4ooopcqghiy+6KGKMJcI4440o0riijDniaGOPQP4oJI81CWCkABQRoCQBFBngpAEUISAlAgcFBAA7"), frame-bg:url("data:image/gif;R0lGODlhAQAgA/MAAN7s/eLu/efx/ez0/fH2/fX5/vf6/vj7/v///97s/d7s/d7s/d7s/d7s/d7s/d7s/SH5BAEAAAgALAAAAAABACADQwg5AAEIHEiwoMGDCBMqXMiwocOHECNKnJiQAMWLGDNq3Mixo0IBBjyKHEmypMmTKFOqXGkywIACBwICADs="), frame:4px 4px 4px 4px, stretch:top" !important
}

.x-cmd-slicer.x-tab-focus.x-tab-active.x-tab-default-left:before {
    display: none;
    content: "x-slicer:, corners:url("data:image/gif;R0lGODlhBAAYAPQAAI2z45e65Zi65Zu75p2957PM7d7q+N7s/eHr+eHu/efx/O31/vL2/PP3/PT3/Pr8/vv9//z9/v7+/v7+//7//////////wAAAI2z442z442z442z442z442z442z442z4yH5BAEAABYALAAAAAAEABgARAhFAAEIBGCBQYEAASAkOMCQ4UAADQ9EmBhhIcMCDSRQnMhggAEFESuIrPCg5IOIDxkQcEAhwISSI0maLIBgwYGCBQSgHBgQADs="), sides:url("data:image/gif;R0lGODlhCAAQAPMAAI2z497s/eDt/eXw/erz/e/2/fT4/fb6/vj7/v///////42z442z442z442z442z4yH5BAEAAAoALAAAAAAIABAAQwg8AAEkQECwoMAACBMKJMCw4cGECAUamEhRoICLGB9C1KgwwYGPIAUWGElS4ICTKDlGTABxZcsAKmGybBkQADs="), frame-bg:url("data:image/gif;R0lGODlhAQAQAPMAAN7s/eDt/eXw/erz/e/2/fT4/fb6/vj7/v///97s/d7s/d7s/d7s/d7s/d7s/d7s/SH5BAEAAAgALAAAAAABABAAQwgRAA8AGACgQAAAAAwQEICwYUAAOw=="), frame:4px 4px 4px 4px, stretch:right" !important
}

.x-cmd-slicer.x-tab-disabled.x-tab-default-top:before {
    display: none;
    content: "x-slicer:, corners:url("data:image/gif;R0lGODlhBAAYAPQAALvS78HW8MHW8cba8tLg8+Lt+uXv+uXv++rz/evz/uz0/vX4/fX5/fb6/ff5/Pf6/f3+/v3+/////////wAAALvS77vS77vS77vS77vS77vS77vS77vS77vS77vS77vS7yH5BAEAABMALAAAAAAEABgARAhRAAEIBDDhAQEBACQgWMhQAAEHExZKAFCgYoEEGBMQWNDAgIEGCwgkzJhgooSTEixezKigpQIHAxhEEADBQIEIDAY4KHAAQoCRCRK2xDix5cSAADs="), sides:url("data:image/gif;R0lGODlhCAAgA/MAALvS7+Pt++Pu++Tu++Xv++Xv/Obv/Obw/Ofw/Ofx/Ojx/Ojx/eny/ery/f///////yH5BAEAAA8ALAAAAAAIACADQwj/AAE4CEAwgAMAAhEoRHBQYIOHDRo6gBgR4USIEilmxGhRY0eODkFefLiR5EeTIVGOrJiS5cqSLj22hEnzZEyRMl/arDlzp8+eQHUGzUkUp1GVRZEevam0KdOnPIVKTQr159SlUalmxWpVa1euQ8FedbqV7FezYdGOrZqW7dqybr0GJUCXgEQGeBnA3Xs2rli5b/vybTs4MGHBiA8rNswYsOO/kNU+lhzZL+XLljMXnqw5cePKm0F75hwac+nOAgeoHiDRgGsDEhXIVnC69mjRi0nfNr0b9WfeuXH/9q07OPDhto0TF14cee/kzpVDb06dufXj1bFfX669O/fv07eHqvc+Hvzz89LRR1+f3Xz69+zFq29fHrqA+wIkrmZtsYD/AhIdIOABEiVgYAISLaDgAnflVd988sFHH4TkUehefBVKGCGGF06oYYYcPvhhhxt6GKKFIp44YoomtljiiyC6GCOMJM5oY404skijjjfymCOKQK4YpIpEyvijkEgWueOQRvroJJNLJtkklD1SeaSSVUoZJZZXTqllllw++WWXW3oZppVinjkmXwEBADs="), frame-bg:url("data:image/gif;R0lGODlhAQAgA/MAAOPt++Pu++Tu++Xv++Xv/Obv/Obw/Ofw/Ofx/Ojx/Ojx/eny/ery/f///+Pt++Pt+yH5BAEAAA0ALAAAAAABACADQwhCAAEcYECwoMGDCBMqXMiwocOHCQcsgEixosWLFwUUSICxo8ePIEOKHGkxgAACBhAomEiypcuXMGPKnEmzps2bBAMCADs="), frame:4px 4px 4px 4px, stretch:bottom" !important
}

.x-cmd-slicer.x-tab-disabled.x-tab-default-right:before {
    display: none;
    content: "x-slicer:, corners:url("data:image/gif;R0lGODlhBAAYAPQAALvS78HW8MHW8cTZ8cXZ8tLg8+Lt+uXv+uXv++vz/uzy++z0/u30++30/vH3/fT5/vX4/fb6/ff5/P3+/v3+/////////wAAALvS77vS77vS77vS77vS77vS77vS77vS7yH5BAEAABYALAAAAAAEABgARAhGAAEIHCgwgcGDBgUUkGAhQQMKAQxINLCg4oKJBg5EgFDA4gIHCgZIqECyAkaEBEuanEgBAgEJBhBMCIByYIIHDAoEWGghIAA7"), sides:url("data:image/gif;R0lGODlhCAAQAPQAALvS7+Pt++Pu++Tu++Xv++Xv/Obv/Obw/Ofw/Ofx/Ojx/Ojx/eny/ery/erz/f///////7vS77vS77vS77vS77vS77vS77vS77vS77vS77vS77vS77vS77vS77vS77vS7yH5BAEAABAALAAAAAAIABAARAhKAAMIHPgAAIKDCAsSWMiwIIOHEAsOmEixoIGLGAsq2MixYIOPIAsKGElSIsWJBQuoXFnwgMuXBRPInFlwgc2bDiE+LOigp8+CAQEAOw=="), frame-bg:url("data:image/gif;R0lGODlhAQAQAPMAAOPt++Pu++Tu++Xv++Xv/Obv/Obw/Ofw/Ofx/Ojx/Ojx/eny/ery/erz/f///+Pt+yH5BAEAAA4ALAAAAAABABAAQwgVAAEcGLBAQIEEDAIIIGAAgYIFDQICADs="), frame:4px 4px 4px 4px, stretch:left" !important
}

.x-cmd-slicer.x-tab-disabled.x-tab-default-bottom:before {
    display: none;
    content: "x-slicer:, corners:url("data:image/gif;R0lGODlhBAAYAPQAALvS78HW8MHW8cba8tLg8+Lt+uXv+uXv++rz/evz/uz0/vX4/fX5/fb6/ff5/P3+/v3+/////////wAAALvS77vS77vS77vS77vS77vS77vS77vS77vS77vS77vS77vS7yH5BAEAABIALAAAAAAEABgARAhQABUIVAAggkABDwwUWLhQYAQABQ48CJCgYoIIGB9GsHgRgIMBDCBAYDDAAUcEKBEwLACgZcuNCQqirPgQ5UMCCxockOCAQIADDRb4JOBAQkAAOw=="), sides:url("data:image/gif;R0lGODlhCAAgA/MAALvS7+Pt++Pu++Tu++Xv++bv/Obw/Ofw/Ofx/Ojx/eny/f///////7vS77vS77vS7yH5BAEAAAwALAAAAAAIACADQwj/AAEsUEBQwQIAAgsaRDiw4MGEDhkqfNiQIMWJEiNCtJiR48aFHy9qrAiSpEiPJjuWxBhS5cmVI1mmbElzpk2ZOGPqRJmT506YPoMCHfqyqMujNXsSRXrzp9GkTpkqfdpUKNWpUqNCtZqV69alX69qrQqWrFivZruWNcDWwNmyWMOqfUt3rl25eNPmjau3L9+/YwGjFQw3sOHBhwsjXqy4cd29iR/7jXx3MmPJhDFThowygecEFAeIHqD5cuXMpzdbdpzaNGfWr0vDXi27duvZqGPftq27N+3dwH3n/i1c9fDjxpO7Js4c+XLnuJVHfy6dd/Pqwa9T3z69u3Xo37EXoecenjzDA+gPUCTAngBFAfAFlPeeHXx98drpj9eff77/++bt95+AAPJnH4EI9lfggAomeGCDED4oIX4TBhghhRhaWKGBGXKoYYcMbhgiiAuW6CCJJ36ooocsjriiiy2aeOGLMopYI4ozxpiijjnC6OONNO74o5BA8mgjkUj2WOSQSib54GegMYTAlAhQlJ56DBWgZQHrtRfaaBQFIGYABwUEADs="), frame-bg:url("data:image/gif;R0lGODlhAQAgA/MAAOPt++Pu++Tu++Xv++bv/Obw/Ofw/Ofx/Ojx/eny/ery/f///+Pt++Pt++Pt++Pt+yH5BAEAAAsALAAAAAABACADQwhDABUIHEiwoMGDCBMqXMiwIcICDiNKnEiRIgIBFTNq3Mixo8ePEhMYGBAApMmTKFOqXMmypcuXMAUmQHDAAIEBAgAEBAA7"), frame:4px 4px 4px 4px, stretch:top" !important
}

.x-cmd-slicer.x-tab-disabled.x-tab-default-left:before {
    display: none;
    content: "x-slicer:, corners:url("data:image/gif;R0lGODlhBAAYAPQAALvS78HW8MHW8cTZ8cXZ8tLg8+Lt+uXv+uvz/uzy++z0/u30++30/u71/vH3/fT5/vX4/fb6/ff5/Pf6/f3+/v3+/////////wAAALvS77vS77vS77vS77vS77vS77vS7yH5BAEAABcALAAAAAAEABgARAhHAAEIBHBhQgEBAiowQMCQ4UAADREYmGiggYKLBSBEOEDRgIQBCRxcvGihpIWOER9KIAChggAKHE2epFhgwQMEFyQUCJByYEAAOw=="), sides:url("data:image/gif;R0lGODlhCAAQAPQAALvS7+Pt++Pu++Tu++Xv++Xv/Obv/Obw/Ofw/Ofx/Ojx/Ojx/eny/ery/erz/f///////7vS77vS77vS77vS77vS77vS77vS77vS77vS77vS77vS77vS77vS77vS77vS7yH5BAEAABAALAAAAAAIABAARAhKAAE8CECwoEAECBMKJMCwoUAGECMKHECxokADGDMKVMCxo8AGIEMKFECy5MSKFAUWWMlS4IGXMAUmmElT4IKbOB9GhCjQgc+fAQEAOw=="), frame-bg:url("data:image/gif;R0lGODlhAQAQAPMAAOPt++Pu++Tu++Xv++Xv/Obv/Obw/Ofw/Ofx/Ojx/Ojx/eny/ery/erz/f///+Pt+yH5BAEAAA4ALAAAAAABABAAQwgVAAEcGLBAQIEEDAIIIGAAgYIFDQICADs="), frame:4px 4px 4px 4px, stretch:right" !important
}

.x-tab-bar-default {
    background-color: #cbdbef;
    border-style: solid;
    border-color: #99bce8
}

.x-tab-bar-default-top {
    border-width: 1px 1px 0
}

.x-tab-bar-default-bottom {
    border-width: 0 1px 1px 1px
}

.x-tab-bar-default-left {
    border-width: 1px 0 1px 1px
}

.x-tab-bar-default-right {
    border-width: 1px 1px 1px 0
}

.x-tab-bar-default-top > .x-tab-bar-body-default {
    padding: 1px 0 0
}

.x-tab-bar-default-bottom > .x-tab-bar-body-default {
    padding: 0 0 1px 0
}

.x-tab-bar-default-left > .x-tab-bar-body-default {
    padding: 0 0 0 1px
}

.x-tab-bar-default-right > .x-tab-bar-body-default {
    padding: 0 1px 0 0
}

.x-tab-bar-plain.x-tab-bar-default-horizontal {
    border-top-color: transparent;
    border-bottom-color: transparent;
    border-left-width: 0;
    border-right-width: 0
}

.x-tab-bar-plain.x-tab-bar-default-vertical {
    border-right-color: transparent;
    border-left-color: transparent;
    border-top-width: 0;
    border-bottom-width: 0
}

.x-tab-bar-top > .x-tab-bar-body-default {
    padding-bottom: 2px
}

.x-tab-bar-bottom > .x-tab-bar-body-default {
    padding-top: 2px
}

.x-tab-bar-left > .x-tab-bar-body-default {
    padding-right: 2px
}

.x-tab-bar-right > .x-tab-bar-body-default {
    padding-left: 2px
}

.x-tab-bar-strip-default {
    border-style: solid;
    border-color: #99bce8;
    background-color: #deecfd
}

.x-tab-bar-top > .x-tab-bar-strip-default {
    border-width: 1px 0 0;
    height: 3px
}

.x-tab-bar-top.x-tab-bar-plain > .x-tab-bar-strip-default {
    border-width: 1px 1px 0 1px
}

.x-tab-bar-bottom > .x-tab-bar-strip-default {
    border-width: 0 0 1px 0;
    height: 3px
}

.x-tab-bar-bottom.x-tab-bar-plain > .x-tab-bar-strip-default {
    border-width: 0 1px 1px 1px
}

.x-tab-bar-left > .x-tab-bar-strip-default {
    border-width: 0 0 0 1px;
    width: 3px
}

.x-tab-bar-left.x-tab-bar-plain > .x-tab-bar-strip-default {
    border-width: 1px 0 1px 1px
}

.x-tab-bar-right > .x-tab-bar-strip-default {
    border-width: 0 1px 0 0;
    width: 3px
}

.x-tab-bar-right.x-tab-bar-plain > .x-tab-bar-strip-default {
    border-width: 1px 1px 1px 0
}

.x-tab-bar-horizontal > .x-tab-bar-body-default {
    min-height: 26px
}

.x-ie8m .x-tab-bar-horizontal > .x-tab-bar-body-default {
    min-height: 23px
}

.x-tab-bar-vertical > .x-tab-bar-body-default {
    min-width: 26px
}

.x-ie8m .x-tab-bar-vertical > .x-tab-bar-body-default {
    min-width: 23px
}

.x-tab-bar-default-top {
    background-image: none;
    background-color: #cbdbef;
    background-image: -webkit-gradient(linear, top, bottom, color-stop(0%, #dde8f5), color-stop(0%, #cbdbef));
    background-image: -webkit-linear-gradient(top, #dde8f5, #cbdbef);
    background-image: -moz-linear-gradient(top, #dde8f5, #cbdbef);
    background-image: -o-linear-gradient(top, #dde8f5, #cbdbef);
    background-image: -ms-linear-gradient(top, #dde8f5, #cbdbef);
    background-image: linear-gradient(top, #dde8f5, #cbdbef)
}

.x-nlg .x-tab-bar-default-top {
    background: url("data:image/gif;R0lGODlhAQAgA/QAAMvb78zc783c8M3d8M7d8M/e8NDe8dDf8dHf8dLg8dPh8tTh8tTi8tXi8tbj89fk89jk89jl9Nnl9Nrm9Nvm9Nvn9Nzn9d3o9f///8vb78vb78vb78vb78vb78vb78vb7yH5BAEAABgALAAAAAABACADRAhNAC88SBAAgMGDCBMqXMiwocOHECMmnMCggMSLGDNqzFghggMFBwZsHEmypMmTKFNKtEBBAgQHDRYkQGCAgACVOHPq3Mmzp8+fQIMCDQgAOw==")
}

.x-tab-bar-default-bottom {
    background-image: none;
    background-color: #cbdbef;
    background-image: -webkit-gradient(linear, top, bottom, color-stop(0%, #dde8f5), color-stop(0%, #cbdbef));
    background-image: -webkit-linear-gradient(bottom, #dde8f5, #cbdbef);
    background-image: -moz-linear-gradient(bottom, #dde8f5, #cbdbef);
    background-image: -o-linear-gradient(bottom, #dde8f5, #cbdbef);
    background-image: -ms-linear-gradient(bottom, #dde8f5, #cbdbef);
    background-image: linear-gradient(bottom, #dde8f5, #cbdbef)
}

.x-nlg .x-tab-bar-default-bottom {
    background: url("data:image/gif;R0lGODlhAQAgA/QAAMvb78zc783c8M3d8M7d8M/e8NDe8dDf8dHf8dLg8dPh8tTh8tTi8tXi8tbj89fk89jk89jl9Nnl9Nrm9Nvm9Nvn9Nzn9d3o9f///8vb78vb78vb78vb78vb78vb78vb7yH5BAEAABgALAAAAAABACADRAhNAAEIHEiwoMGDCBMqXMiwoUEBCSA4nEixosWKBhpQuMixo8ePIEOKdEgAwQIHEiyMXMmypcuXMGPKnElTZoABBQ4kUMDAwYMIEypcCAgAOw==") bottom 0
}

.x-tab-bar-default-left {
    background-image: none;
    background-color: #cbdbef;
    background-image: -webkit-gradient(linear, top, bottom, color-stop(0%, #dde8f5), color-stop(0%, #cbdbef));
    background-image: -webkit-linear-gradient(left, #dde8f5, #cbdbef);
    background-image: -moz-linear-gradient(left, #dde8f5, #cbdbef);
    background-image: -o-linear-gradient(left, #dde8f5, #cbdbef);
    background-image: -ms-linear-gradient(left, #dde8f5, #cbdbef);
    background-image: linear-gradient(left, #dde8f5, #cbdbef)
}

.x-nlg .x-tab-bar-default-left {
    background: url("data:image/gif;R0lGODlhIAMBAPQAAMvb78zc783c8M3d8M7d8M/e8NDe8dDf8dHf8dLg8dPh8tTh8tTi8tXi8tbj89fk89jk89jl9Nnl9Nrm9Nvm9Nvn9Nzn9d3o9f///8vb78vb78vb78vb78vb78vb78vb7yH5BAEAABgALAAAAAAgAwEARAhLAC9YqEBhgoQIEB44cNCAwQIFCRIgOGCgAIEBAgIA2Mixo8ePIEOKHEmypMmTKFOqXMmypcuXMGPKnEmzps2bOHPq3Mmzp8+fOwMCADs=")
}

.x-tab-bar-default-right {
    background-image: none;
    background-color: #cbdbef;
    background-image: -webkit-gradient(linear, top, bottom, color-stop(0%, #dde8f5), color-stop(0%, #cbdbef));
    background-image: -webkit-linear-gradient(right, #dde8f5, #cbdbef);
    background-image: -moz-linear-gradient(right, #dde8f5, #cbdbef);
    background-image: -o-linear-gradient(right, #dde8f5, #cbdbef);
    background-image: -ms-linear-gradient(right, #dde8f5, #cbdbef);
    background-image: linear-gradient(right, #dde8f5, #cbdbef)
}

.x-nlg .x-tab-bar-default-right {
    background: url("data:image/gif;R0lGODlhIAMBAPQAAMvb78zc783c8M3d8M7d8M/e8NDe8dDf8dHf8dLg8dPh8tTh8tTi8tXi8tbj89fk89jk89jl9Nnl9Nrm9Nvm9Nvn9Nzn9d3o9f///8vb78vb78vb78vb78vb78vb78vb7yH5BAEAABgALAAAAAAgAwEARAhLAAEIHEiwoMGDCBMqXMiwocOHECNKnEixosWLGDNq3Mixo8ePIEOKHEmypEmRAQQMIFDAwAEECRIoWMCggQMHDyBEkDCBQgULFwICADs=") 0 right
}

.x-tab-bar-default-scroller .x-box-scroller-body-horizontal {
    margin-left: 18px
}

.x-tab-bar-default-vertical-scroller .x-box-scroller-body-vertical {
    margin-top: 17px
}

.x-box-scroller-tab-bar-default {
    cursor: pointer;
    color: #eee
}

.x-box-scroller-tab-bar-default.x-box-scroller-disabled {
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=50)";
    opacity: 0.5;
    cursor: default
}

.x-box-scroller-tab-bar-default.x-box-scroller-left, .x-box-scroller-tab-bar-default.x-box-scroller-right {
    width: 18px;
    top: 0;
    bottom: 0
}

.x-box-scroller-tab-bar-default.x-box-scroller-left {
    margin: 0;
    background-position: -18px 0
}

.x-box-scroller-tab-bar-default.x-box-scroller-left.x-box-scroller-hover {
    background-position: 0 0
}

.x-box-scroller-tab-bar-default.x-box-scroller-right {
    margin: 0;
    background-position: 0 0
}

.x-box-scroller-tab-bar-default.x-box-scroller-right.x-box-scroller-hover {
    background-position: -18px 0
}

.x-box-scroller-tab-bar-default.x-box-scroller-top, .x-box-scroller-tab-bar-default.x-box-scroller-bottom {
    height: 18px;
    left: 0;
    right: 0
}

.x-box-scroller-tab-bar-default.x-box-scroller-top {
    margin: 0;
    background-position: 0 -18px
}

.x-box-scroller-tab-bar-default.x-box-scroller-top.x-box-scroller-hover {
    background-position: 0 0
}

.x-box-scroller-tab-bar-default.x-box-scroller-bottom {
    margin: 0;
    background-position: 0 0
}

.x-box-scroller-tab-bar-default.x-box-scroller-bottom.x-box-scroller-hover {
    background-position: 0 -18px
}

.x-tab-bar-more-icon {
    background-image: url("data:image/gif;R0lGODlhDAAQAIcAABVCi0D/QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAMAAAEALAAAAAAMABAAAAgqAAMIHEiwoMGDCBMqXIgQAACBDg9GDDCx4MSKEB9S1DjwIkeGIEOKPBgQADs=")
}

.x-tab-bar-plain.x-tab-bar-default-scroller .x-box-scroller-body-horizontal {
    margin-left: 18px
}

.x-tab-bar-plain.x-tab-bar-default-vertical-scroller .x-box-scroller-body-vertical {
    margin-top: 17px
}

.x-tab-bar-plain .x-box-scroller-tab-bar-default {
    color: #eee
}

.x-tab-bar-default-right .x-box-scroller-top {
    background-position: right -18px
}

.x-tab-bar-default-right .x-box-scroller-top.x-box-scroller-hover {
    background-position: right 0
}

.x-tab-bar-default-right .x-box-scroller-bottom {
    background-position: right 0
}

.x-tab-bar-default-right .x-box-scroller-bottom.x-box-scroller-hover {
    background-position: right -18px
}

.x-tab-bar-default-bottom .x-box-scroller-left {
    background-position: -18px bottom
}

.x-tab-bar-default-bottom .x-box-scroller-left.x-box-scroller-hover {
    background-position: 0 bottom
}

.x-tab-bar-default-bottom .x-box-scroller-right {
    background-position: 0 bottom
}

.x-tab-bar-default-bottom .x-box-scroller-right.x-box-scroller-hover {
    background-position: -18px bottom
}

.x-tab-bar-default-top .x-box-scroller-left {
    background-image: url("data:image/gif;R0lGODlhJAAqAMQAAExypFZ8rmqNunSXxI2y48LY9Mvd9Mzi/tHl/tTh89fo/trp/dvl8+Ho8+Lt/efw/evy/fD2/vb6/gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAkAABMALAAAAAAkACoAAAX/ICGOZGmeqKSubKsSbswSUG3fOCQRTe//wMYuR7TtgkjfsEjcMZ7QqJSxe1iv2OwDQph6oVyHeOyImMli7vcbRpsHZ7LaK/C2x+ZAwMxPExKAgQkAAIKBd2URent8EX6Gg4SQCVwLlnmLmRGWXIaEn5+HBJeKmZqcf4Ggq6KWC5ime6ieq5KAla6wjZsLXAa/wJ/Aw1wKxsaYu8a+w7+Ezb9cCNPUb2bU08zQAtAG0tjTfOAI2t3Q3+Pp5AQF7e7v8AXo6uBc8ffuXAf7/P3+B/bw3dP3r+C+gALhETT4D2HCfAQYFnT4UF5Eif4oPlyI8SC7ihA79tOYkGNHkgJNRmJEiU+lRJYDL4oE+BGkxZkebbZzyRBmPJ4GfSqUKVLoO6ATa4JE2lBpRaYZnW4kelJqSaorrabE+lJrS649vcbESVOnxRAAOw==")
}

.x-tab-bar-default-top .x-box-scroller-right {
    background-image: url("data:image/gif;R0lGODlhJAAqAMQAAExypFZ8rmqNunSXxI2y48LY9Mvd9Mzi/tHl/tTh89fo/trp/dvl8+Ho8+Lt/efw/evy/fD2/vb6/gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAkAABMALAAAAAAkACoAAAX/ICGOZGmeKCGtbOuu6iuzamPfeN6oUO//QEhNR7TxgsieisFsOp+MYzJIgECvzepjy+16H1UstuoomyNoszoMFYwhagd6kI5XE/h8AgDQ58lyaGgBAXVmd357fImAgoOEhg6IinyVfXpVCwsRhJ2daJoLk5akmBCanJ6eoKIQeaSVfpmbqp8RoVUGursGlby6s46phbe4EL+6fMgGVQoKwpARztO5yALLzBAI29tzaNzc1djIVeDd3+YIVQXs7e7vBeXp89vr8Pfs8vTp9vjwVQcCChxI8EA/f+4AFlwY8CDCfBAYMnT4UKFEghQRWrwoMKO/jRwNQnj4DiRHj/hMSV5EeU+lRJb/IobsOJJkO5cTa9qMJ3OmyJ0QfTbUaRPnQpgle85EmlBpSKY3nZ4kStJoQahBhWLlKfQnUKsYqVaUulKsRrISQwAAOw==")
}

.x-tab-bar-default-bottom .x-box-scroller-left {
    background-image: url("data:image/gif;R0lGODlhJAAqAIQTAExypFZ8rmqNunSXxI2y48LY9Mvd9Mzi/tHl/tTh89fo/trp/dvl8+Ho8+Lt/efw/evy/fD2/vb6/v///////////////////////////////////////////////////yH5BAEKAB8ALAAAAAAkACoAAAX+4CGOZHlARKGubFugZjyibr3CckzbNZ6XO17L95ulhENCEXhE3pRLo5NFXAan1eLVmf1tkd3cVxiWjXllXRMLjZ7W3Hb0bEub6D25FQ7Wa/lkfl6AaIJihHWGZoh5biJ4LnZMU08IlpeYmQiQSZqel5xUBJ4RpZooBqmqq6wGKJqlA6aYqK0GArYoCru7pQEBpcG7tawAALkEC8oLvr/BpcrEqsbHrSjLzb/awNEECd/f1OIA4NfMEdvpEd3gCePi5cnK2ers7e/G8Q77DtnPEftQtAuXb2ACFPz2NfsX0JvBggMRJuwXQRbAhCgYaNyoUQDHjRInBpvoIOPHkxxEUTxYybKlywcmUaJEAaGmzZs4IUggIFPmzpxAbe5sQLSo0aMNfgYFOhSpU6I7JUidSrWqVAJWs1IlwLWr169gw4olEAIAOw==")
}

.x-tab-bar-default-bottom .x-box-scroller-right {
    background-image: url("data:image/gif;R0lGODlhJAAqAIQTAExypFZ8rmqNunSXxI2y48LY9Mvd9Mzi/tHl/tTh89fo/trp/dvl8+Ho8+Lt/efw/evy/fD2/vb6/v///////////////////////////////////////////////////yH5BAEKAB8ALAAAAAAkACoAAAX+IAEVZGmehXisbOseIiqX6muv8SzX95vrJ16v9QPSIEPfyGgSJmFLJsmZLDKpQ6sR29MCuTevDmwTz8hK6fFJjErRLvMOyca5r/S6HAVvq6d5bHtBgU+DTYVVd1uJWYtfjV2PY5Fhk2cQCJqbnJ0Ih0eeopsiBqanqKkGIp4RrqKlqgKqpqycrgOvnbGpAAC0IgoKrsQBAa7Cybyovr+pIgsLxK7GxxHR0SIJ283dANvg0NLV5NbY2tzezeAJ4hHl5K7ZEODqvuztENHv8Obz+Om+4RPhwME0ftYKFkSH7x5AgganGXOlcCEEBhgzMhCgUSNEhbgoVnQgoqPJjh9GQYocWfKkSxEPYsqcSfMBAQkuX0qAwLOnz58QbjYYSrSo0QY3gSrtKfSo06FJlyq9KaGq1atYJVDNyrUqga9gw4odS7ZsCAA7")
}

.x-tab-bar-default-left .x-box-scroller-top {
    background-image: url("data:image/gif;R0lGODlhKgAkAIQTAExypFZ8rmqNunSXxI2y48LY9Mvd9Mzi/tHl/tTh89fo/trp/dvl8+Ho8+Lt/efw/evy/fD2/vb6/v///////////////////////////////////////////////////yH5BAEKAB8ALAAAAAAqACQAAAX+ICFB5OOczqIuCuIiRyzPdB2LJGSiK/vCtqANV0KlIqrWS8icEXXGiNS3bDafO4c0IFW6rNdRURsJmKU/MBNLNrvRX3UQu3W/I3F5jT6wuwd4QHo0dFJlZ4Z5gzJshneBgos3YlBtiGmSjJQ7dVyQkZJsZIZwiqGbRj1eoIuiJ6qYmQciErU5t7i5uru3BL6/wMHCw8TDEg0NDMoMCc3NBtAGBdPU1dbX1SLIy8zOCdHS2OLj2snL3t/R4+vX5dzo4Ozy0+7nzQDp0PPy9cr3AADi7VvXjxnAg+oGkjtmTtnBh/oUiusn4OFBAeEktmP4LgHChBqtFfwXEGRIaiMoPQIUeBIlR3sfI7ak99KfN5YzUzrD2VLnM5M9a9niRbRormJIkyoNAQA7")
}

.x-tab-bar-default-left .x-box-scroller-bottom {
    background-image: url("data:image/gif;R0lGODlhKgAkAIQTAExypFZ8rmqNunSXxI2y48LY9Mvd9Mzi/tHl/tTh89fo/trp/dvl8+Ho8+Lt/efw/evy/fD2/vb6/v///////////////////////////////////////////////////yH5BAEKAB8ALAAAAAAqACQAAAX+ICGOZGme6CmtEuS+cCzPNERITcPsTOL7hqChQCwaj0jjLcfr/RLCYXJKXep4T6iQykVamz6AONotE7/YhBhANnfRu/B46+bCnet2fQoXrP8CUntJd395goNHd2p/dImKOFdxjGyOj0WLYVpBl5BMaT96nQWZoZadpUCnl6mbiKgpsbKzLC01t7gyNy8PDr4OC8ELCgjFCAfIycrLzMi7Lr2/wsPGx83Xzc8Q0RHd3hHV2OLK2twRAejd4ePj5b7d6AHqxuztttsO3vHe9PXY5d/28bPmL9u9BxEGxFs4ABzBgssAnluYziFEg7zyTRTY7yK5g+82zivmMSLIkPIlIhDrWPKAu1/eqLEs+dLXggjBVpJs6eykTWE6H9L0CQzoOp4hAAA7")
}

.x-tab-bar-default-right .x-box-scroller-top {
    background-image: url("data:image/gif;R0lGODlhKgAkAIQTAExypFZ8rmqNunSXxI2y48LY9Mvd9Mzi/tHl/tTh89fo/trp/dvl8+Ho8+Lt/efw/evy/fD2/vb6/v///////////////////////////////////////////////////yH5BAEKAB8ALAAAAAAqACQAAAX+4CGOZGmKSIooS7s4sPNAtEScOK6u7hvPtVtuONqxFhEfDAixEZ9GZCQSk9GawmfOOA1Mf1endqvqBrxUa3BMRpjPaDWWrXNH4PgpU0wvpSIDeHADEXtZfUV2b1N6YYeIB2WLX4aQJDuTS46WiX93Z19yfJaYjIyaa5yRKkctVZWqUS6vjle2t7i5urYSvTYEwMHCw8TFxsQFycrLzM3LBtAGCdPTDNYMDQ02ztzdBdHS1AnX2NoE3ujP0eLj19nb6eng7OTv5/Ho8wDU9eb4+dEACKzmzt+/bgEFDuwH76AzaAojMrznsJkBAREVCijYsKI6iAPbWbPn0WLCfSIuy3Us+e0kwZEGWSYDp/ClSooy54mbKFOZTn4ccbL8adPerqNIc/n6daypU6chAAA7")
}

.x-tab-bar-default-right .x-box-scroller-bottom {
    background-image: url("data:image/gif;R0lGODlhKgAkAIQTAExypFZ8rmqNunSXxI2y48LY9Mvd9Mzi/tHl/tTh89fo/trp/dvl8+Ho8+Lt/efw/evy/fD2/vb6/v///////////////////////////////////////////////////yH5BAEKAB8ALAAAAAAqACQAAAX+ICGOZGmeqAmtbOu+cAxJtEQUeK7vvG78hoRQyCgyGg1bb8ksAIPDhPGYvDWvuWdUakQqsdgnYEzsVsFh4BhQLnqtaKaYzHWf43I1ffrGywVrgQJmX348P4FrfHeGO3prdVSFjVmPbZJwlDhabJd9mpU/W4uTmlpRpJmmQKOEqpSnQ6kptLW2Mri5MDU2B76/wMHCvgjFCAoLyQsOzA4PLL3D0sPGx8rLzc8r0dPdxMYR4eIRzNozBN7p1eEB7eHl0Ojp3esR7QHvzvHz9MXi9+L0bZPHjxqCcQDFmeNWMJi/AfciDoiwkGBDYP7sRXRHcd9Fhxk3vqv4EWRIjvApBpbEaEwBu3wCz638VQ1ZwGweZ9ZMFgFbSpkzD+xU1iwmw5JDkxWtGAIAOw==")
}

.x-cmd-slicer.x-tab-bar-default-top:before {
    display: none;
    content: "x-slicer:, bg:url("data:image/gif;R0lGODlhAQAgA/QAAMvb78zc783c8M3d8M7d8M/e8NDe8dDf8dHf8dLg8dPh8tTh8tTi8tXi8tbj89fk89jk89jl9Nnl9Nrm9Nvm9Nvn9Nzn9d3o9f///8vb78vb78vb78vb78vb78vb78vb7yH5BAEAABgALAAAAAABACADRAhNAC88SBAAgMGDCBMqXMiwocOHECMmnMCggMSLGDNqzFghggMFBwZsHEmypMmTKFNKtEBBAgQHDRYkQGCAgACVOHPq3Mmzp8+fQIMCDQgAOw=="), stretch:bottom" !important
}

.x-cmd-slicer.x-tab-bar-default-bottom:before {
    display: none;
    content: "x-slicer:, bg:url("data:image/gif;R0lGODlhAQAgA/QAAMvb78zc783c8M3d8M7d8M/e8NDe8dDf8dHf8dLg8dPh8tTh8tTi8tXi8tbj89fk89jk89jl9Nnl9Nrm9Nvm9Nvn9Nzn9d3o9f///8vb78vb78vb78vb78vb78vb78vb7yH5BAEAABgALAAAAAABACADRAhNAAEIHEiwoMGDCBMqXMiwoUEBCSA4nEixosWKBhpQuMixo8ePIEOKdEgAwQIHEiyMXMmypcuXMGPKnElTZoABBQ4kUMDAwYMIEypcCAgAOw=="), stretch:top" !important
}

.x-cmd-slicer.x-tab-bar-default-left:before {
    display: none;
    content: "x-slicer:, bg:url("data:image/gif;R0lGODlhIAMBAPQAAMvb78zc783c8M3d8M7d8M/e8NDe8dDf8dHf8dLg8dPh8tTh8tTi8tXi8tbj89fk89jk89jl9Nnl9Nrm9Nvm9Nvn9Nzn9d3o9f///8vb78vb78vb78vb78vb78vb78vb7yH5BAEAABgALAAAAAAgAwEARAhLAC9YqEBhgoQIEB44cNCAwQIFCRIgOGCgAIEBAgIA2Mixo8ePIEOKHEmypMmTKFOqXMmypcuXMGPKnEmzps2bOHPq3Mmzp8+fOwMCADs="), stretch:right" !important
}

.x-cmd-slicer.x-tab-bar-default-right:before {
    display: none;
    content: "x-slicer:, bg:url("data:image/gif;R0lGODlhIAMBAPQAAMvb78zc783c8M3d8M7d8M/e8NDe8dDf8dHf8dLg8dPh8tTh8tTi8tXi8tbj89fk89jk89jl9Nnl9Nrm9Nvm9Nvn9Nzn9d3o9f///8vb78vb78vb78vb78vb78vb78vb7yH5BAEAABgALAAAAAAgAwEARAhLAAEIHEiwoMGDCBMqXMiwocOHECNKnEixosWLGDNq3Mixo8ePIEOKHEmypEmRAQQMIFDAwAEECRIoWMCggQMHDyBEkDCBQgULFwICADs="), stretch:left" !important
}

.x-breadcrumb-btn-default {
    margin: 0 0 0 0px
}

.x-breadcrumb-icon-folder-default {
    background-image: url("data:image/gif;R0lGODlhEAAQAKU2ADFKY0L/QplnAZpoApxqBJ5sBqBuCKNxC6VzDad1D6h2EKt5E6x6FK58FrB+GLOBG7WCHbeEH7qHIr2KJcCNKMKPKsWSLceUL8iVMMmWMcuYM8yZNNu3Utu3cf/Ub//bdf/kf5SlvZylvZytxqW11qm92r3GxrnK5P/vif/4k///mf//nP//usDAwMvLy8zMzNPT09bW1sbW69jh8efv9+vz/////////////////////////////////////////yH5BAEAAD8ALAAAAAAQABAAAAZ8wJ9wSCwSNxtNBmM82p4sVqX523Q4WGxnIolAHg6h5kkukxmxX0a1arvfqsTrd1HZ73j7wfWzqFKAgYIqBnwVKiiJiosqBXwUKiCSk5QqBHwTKh+bnJ0qA3wSKh6kpaYqAnM/Xw4NCwoIBwYFBAItMEMwLru8vbhUwMFFQQA7")
}

.x-btn-menu-active .x-breadcrumb-icon-folder-default {
    background-image: url("data:image/gif;R0lGODlhEAAQAKU9ADFKY0L/QplnAZpoApxqBJ5sBqBuCKJwCqNxC6RyDKVzDad1D6x6FLB+GLOBG7WCHbeEH7qHIr2KJcaaGcaaGsKPKsiVMMmWMcuYM8yZNMmgIc+iJte4QNq/bOKzQ+LBUP3VcP/bdfDkev/kf5SlvZylvbe3t5ytxqW11qm92r3GxrnK5P/XhP/rhP/viffwif/4k///mf//nP//pcTExMXFxc3NzdHR0cbW69jh8efv9+vz//r7/P///////////yH5BAEAAD8ALAAAAAAQABAAAAaBwJ9wSCwSMxnMxWI89p48XqX5y/RkWGxPEoE8HA0h5prNPp+M2+/Sg7nfcNmiNqnb7/VPC0GbxMplMR0TLAZ9f3BvMi8TIAU0P34uk5STMxoeBJB+MiOenyMzHBsDkJExIamqqSIUAjVCEwqzswkHBgUEAyY2QzY0wMHCvVTFxkVBADs=")
}

.x-breadcrumb-icon-leaf-default {
    background-image: url("data:image/gif;R0lGODlhEAAQAIcAAAAAADVJYzZKZC9iyDFlzTly4j5240B240Z75Ep940D/QE6B5FaG5ViH5WKO5myU526X52WV82qZ9Xab6Hqf6XGd9X+h6Xei9n2n+ICAgJOit5alupqpvp6uw4Sl6Yam6ouq6oSr+Yuw+pC1+5a5/Jq9/aOyyKe2zJ/A/qLC/9Dg8ODg8ODo8PDw8PDw//D4///4/////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAMAAAoALAAAAAAQABAAAAiOABUIHEiwoMGDBUEoBPHBwoQHDhosQGCggEAQKVCUIDFCRAgMFypIiEDgokIPFCA4YJDgQIGXAwSeiEGzZs0XL1wIEGgiBoCfP2nidMEigMAONm/mZFFUIIeaGaJKjbrCqIINSW0OtarBJ1AAQpdyzRpjKNOxNKdOrSqwq00YOVuwWKGCa4C7ePPiRcg3IAA7")
}

.x-breadcrumb-btn .x-btn-wrap-default-toolbar-small.x-btn-arrow:after {
    width: 14px;
    background-image: url("data:image/gif;R0lGODlhCgAKAIABAAAAAP///yH5BAEKAAEALAAAAAAKAAoAAAIOjI+pq8AB3IoyRVafPgUAOw==")
}

.x-btn-menu-active.x-breadcrumb-btn .x-btn-wrap-default-toolbar-small.x-btn-arrow:after {
    background-image: url("data:image/gif;R0lGODlhCgAKAIABAAAAAP///yH5BAEKAAEALAAAAAAKAAoAAAIMjI+pywv/FGSg2YsKADs=")
}

.x-breadcrumb-btn .x-btn-wrap-default-toolbar-small.x-btn-split:after {
    width: 14px;
    background-image: url("data:image/gif;R0lGODlhDgBIAIABAAAAAP///yH5BAEKAAEALAAAAAAOAEgAAAImjI+py+0Po5y02ouz3rz7D4biBURA+Zxoc0LrCMfyTNf2jee6VwAAOw==")
}

.x-btn-over.x-breadcrumb-btn .x-btn-wrap-default-toolbar-small.x-btn-split:after {
    background-image: url("data:image/gif;R0lGODlhDgBIAMIEAAAAAKrI8cLa9tru/////////////////yH5BAEKAAIALAAAAAAOAEgAAANfGCPczupJEaerFq6sefdYFlrjVErnk14btzbv57YiTdomjuoqz3oUH0woqwFjwSMxCVoiS4CeBBAdTqnWBzbrqHKNTaU4TJ6NzWUweq1u387uHPydprPt8d1cXuffJwkAOw==")
}

.x-btn-menu-active.x-breadcrumb-btn .x-btn-wrap-default-toolbar-small.x-btn-split:after {
    background-image: url("data:image/gif;R0lGODlhDgBIAMIEAAAAAKrI8cLa9tru/////////////////yH5BAEKAAIALAAAAAAOAEgAAANdGCPczupJEaerFq6sefdYFlrjVErnk14btzbv57YiTdomjuoqz3oUH0woqwFjwSMxCVoinzaAVFpkTIcTwK+p7HK/M28YbCTfxOWxOs0+m3No91rehr93cftcn0kAADs=")
}

.x-breadcrumb-default-scroller .x-box-scroller-body-horizontal {
    margin-left: 14px
}

.x-breadcrumb-default-vertical-scroller .x-box-scroller-body-vertical {
    margin-top: 26px
}

.x-box-scroller-breadcrumb-default {
    cursor: pointer
}

.x-box-scroller-breadcrumb-default.x-box-scroller-disabled {
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=50)";
    opacity: 0.5;
    cursor: default
}

.x-box-scroller-breadcrumb-default.x-box-scroller-left, .x-box-scroller-breadcrumb-default.x-box-scroller-right {
    width: 14px;
    height: 22px;
    border-style: solid;
    border-color: #8db2e3;
    border-width: 0 0 1px;
    top: 50%;
    margin-top: -11px
}

.x-box-scroller-breadcrumb-default.x-box-scroller-left {
    margin-left: 0;
    margin-right: 0;
    margin-bottom: 0;
    background-image: url("data:image/gif;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");
    background-position: -14px 0
}

.x-box-scroller-breadcrumb-default.x-box-scroller-left.x-box-scroller-hover {
    background-position: 0 0
}

.x-box-scroller-breadcrumb-default.x-box-scroller-right {
    margin-left: 0;
    margin-right: 0;
    margin-bottom: 0;
    background-image: url("data:image/gif;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");
    background-position: 0 0
}

.x-box-scroller-breadcrumb-default.x-box-scroller-right.x-box-scroller-hover {
    background-position: -14px 0
}

.x-tree-expander {
    cursor: pointer
}

.x-tree-arrows .x-tree-expander {
    background-image: url("data:image/gif;R0lGODlhQAAUAMZaACYmJllZWRzE9y3I9y3J9y7I9y7J92HW+Xfc+oWFhYiIiJiYmKGhoaampqmpqby8vILf+6Xk+aXm+6fk+abm+6jn+6nn+67n+q/n+q7o+rDo+7Po+7Pp+8nJyd/f38Xu/Mfv/Mjv/M3u+8rw/NDv+9Dy/dXw+tfx/Nfy/Nny/Nry/Nzy+93y+9/z+9zz/N70/eLi4unp6ezs7O3t7e7u7uDz++H0++P0++L1/eP2/eX1++b1++f2++T2/eX2/eb3/ef3/ej2++j3/er3/Ov3/O33/On4/er4/ev4/ev4/u/4++34/Oz5/u35/u74/O/4/O75/u/5/u/6/vLy8vH4+/L5+/P5+/D4/PD6/vH6/v///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////yH5BAEKAH8ALAAAAABAABQAAAfIgH+Cg4SFhoeIiYqLjI2Oj5CRkpOUlZaXmJmahkxCm4QdU59/PQgfo38NDjCRDwqJLwIEEpEZBzuJDTMMHo8PAACJKgIYAxSPEwICNrl/Mgs0jb8BwYgoAiIXBCCNEQIQAi3NfzEJM4vT1Ikn2CQcAiWLyRDgNc3P0Yrp6ogpAiQaDIRYlOEbPQE3cu3qtUgBMGCvELkQsIFABUYHlCk7ECTXqk84BBSw0GiHjRY1bgR5kijUKCMIRqCamQXKzJs4c+rcybNnoUAAOw==")
}

.x-tree-arrows .x-tree-expander-over .x-tree-expander {
    background-position: -32px center
}

.x-tree-arrows .x-grid-tree-node-expanded .x-tree-expander {
    background-position: -16px center
}

.x-tree-arrows .x-grid-tree-node-expanded .x-tree-expander-over .x-tree-expander {
    background-position: -48px center
}

.x-tree-lines .x-tree-elbow {
    /*  background-image:url("data:image/gif;R0lGODlhEAAUAKECAEL/QsbGxv///////yH5BAEAAAAALAAAAAAQABQAAAIahG+By+2gnpxxWlavhrurz3VOJkpkOaLWKRYAOw==") */
    background-image:  url("data:image/gif;base64,R0lGODlhEAAUAKECAEL/QsbGxv///////yH5BAEAAAAALAAAAAAQABQAAAIahG+By+2gnpxxWlavhrurz3VOJkpkOaLWKRYAOw==") 
}

.x-tree-lines .x-tree-elbow-end {
    /* background-image: url("data:image/gif;R0lGODlhEAAUAKECAEL/QsbGxv///////yH5BAEAAAAALAAAAAAQABQAAAIXhG+By+2gnpxxWlavhrurz3XiSJbmORUAOw==") */
    background-image:  url("data:image/gif;base64,R0lGODlhEAAUAKECAEL/QsbGxv///////yH5BAEAAAAALAAAAAAQABQAAAIXhG+By+2gnpxxWlavhrurz3XiSJbmORUAOw==")
}

.x-tree-lines .x-tree-elbow-plus {
    /* background-image: url("data:image/gif;R0lGODlhEAAUAOMOADFKY0L/QpSlvZylvZytxqW11qm92r3GxrXI48bGxsbS59Te8efv9+vz/////////yH5BAEAAA8ALAAAAAAQABQAAARN8MkpE70462e3/90nSgthDoMgHBnhvG/DAC0MyAqNuS/ALAbdZeAAGI1BzkXgkAEWioKQIpAtAAqENCNgZA2F8HRyOJpZo1EonV6zKREAOw==") */
    background-image:  url("data:image/gif;base64,R0lGODlhEAAUAOMOADFKY0L/QpSlvZylvZytxqW11qm92r3GxrXI48bGxsbS59Te8efv9+vz/////////yH5BAEAAA8ALAAAAAAQABQAAARN8MkpE70462e3/90nSgthDoMgHBnhvG/DAC0MyAqNuS/ALAbdZeAAGI1BzkXgkAEWioKQIpAtAAqENCNgZA2F8HRyOJpZo1EonV6zKREAOw==")
}

.x-tree-lines .x-tree-elbow-end-plus {
    /* background-image: url("data:image/gif;R0lGODlhEAAUAOMOADFKY0L/QpSlvZylvZytxqW11qm92r3GxrXI48bGxsbS59Te8efv9+vz/////////yH5BAEAAA8ALAAAAAAQABQAAARM8MkpE70462e3/90nSgthDoMgHBnhvG/DAC0MyAqNuS/ALAbdZeAAGI1BzkXgkAEWioKQIpAtAAqENCNgZA2F8HRyOJpZo7R6zc5EAAA7") */
    background-image:  url("data:image/gif;base64,R0lGODlhEAAUAOMOADFKY0L/QpSlvZylvZytxqW11qm92r3GxrXI48bGxsbS59Te8efv9+vz/////////yH5BAEAAA8ALAAAAAAQABQAAARM8MkpE70462e3/90nSgthDoMgHBnhvG/DAC0MyAqNuS/ALAbdZeAAGI1BzkXgkAEWioKQIpAtAAqENCNgZA2F8HRyOJpZo7R6zc5EAAA7")
}

.x-tree-lines .x-grid-tree-node-expanded .x-tree-elbow-plus {
   /*  background-image: url("data:image/gif;R0lGODlhEAAUAOMOADFKY0L/QpSlvZylvZytxqW11qm92r3GxrnK5MbGxsbW69jh8efv9+vz/////////yH5BAEAAA8ALAAAAAAQABQAAARM8MkpE70462e3/90nSgthDoMgHBnhvG/DAC3syAiNuTGzGLrLwAEoFoGci+DmWygKQYpAtnAioBkBQ4EwFL7RycFIZo1GofM5raZEAAA7") */
   background-image:  url("data:image/gif;base64,R0lGODlhEAAUAOMOADFKY0L/QpSlvZylvZytxqW11qm92r3GxrnK5MbGxsbW69jh8efv9+vz/////////yH5BAEAAA8ALAAAAAAQABQAAARM8MkpE70462e3/90nSgthDoMgHBnhvG/DAC3syAiNuTGzGLrLwAEoFoGci+DmWygKQYpAtnAioBkBQ4EwFL7RycFIZo1GofM5raZEAAA7")
}

.x-tree-lines .x-grid-tree-node-expanded .x-tree-elbow-end-plus {
    background-image: url("data:image/gif;R0lGODlhEAAUAOMOADFKY0L/QpSlvZylvZytxqW11qm92r3GxrnK5MbGxsbW69jh8efv9+vz/////////yH5BAEAAA8ALAAAAAAQABQAAARK8MkpE70462e3/90nSgthDoMgHBnhvG/DAC3syAiNuTGzGLrLwAEoFoGci+DmWygKQYpAtnAioBkBQ4EwFL7RycFIZo3O6LQ6EwEAOw==")
}

.x-tree-lines .x-tree-elbow-line {
    background-image: url("data:image/gif;R0lGODlhEAAUAKECAEL/QsbGxv///////yH5BAEAAAAALAAAAAAQABQAAAIZhG+By+2gnpxxWlavhrvnToHaJzpkiaFHAQA7")
}

.x-tree-no-lines .x-tree-expander {
    background-image: url("data:image/gif;R0lGODlhEAAUAOMOADFKY0L/QpSlvZylvZytxqW11qm92r3GxrXI48bGxsbS59Te8efv9+vz/////////yH5BAEAAA8ALAAAAAAQABQAAARF8MlJq7046817XkQ4DIJwXISjqg0DoCvQKq+VqgCzGHU1OIBgkHcROFqAhaLQowhaC4ACwSwypoaCtjk5CL8nj3hMLksiADs=")
}

.x-tree-no-lines .x-grid-tree-node-expanded .x-tree-expander {
    background-image: url("data:image/gif;R0lGODlhEAAUAOMOADFKY0L/QpSlvZylvZytxqW11qm92r3GxrnK5MbGxsbW69jh8efv9+vz/////////yH5BAEAAA8ALAAAAAAQABQAAARE8MlJq7046817XkQ4DIJwXISjqg0DoKvTIq+Vssxi1NXgAEDg7iKQ5RaKAo8iaC2QCCWRoUAYCtjl5BDsnjzgsHgsiQAAOw==")
}

.x-tree-icon {
    width: 16px;
    height: 20px;
    line-height: 20px;
    color: gray;
    font-size: 16px
}

.x-tree-elbow-img {
    width: 16px;
    height: 20px;
    line-height: 20px;
    margin-right: 0
}

.x-tree-icon, .x-tree-elbow-img, .x-tree-checkbox {
    margin-top: -3px;
    margin-bottom: -4px
}

.x-tree-icon-leaf {
   /*  background-image: url("data:image/gif;R0lGODlhEAAQAIcAAAAAADVJYzZKZC9iyDFlzTly4j5240B240Z75Ep940D/QE6B5FaG5ViH5WKO5myU526X52WV82qZ9Xab6Hqf6XGd9X+h6Xei9n2n+ICAgJOit5alupqpvp6uw4Sl6Yam6ouq6oSr+Yuw+pC1+5a5/Jq9/aOyyKe2zJ/A/qLC/9Dg8ODg8ODo8PDw8PDw//D4///4/////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAMAAAoALAAAAAAQABAAAAiOABUIHEiwoMGDBUEoBPHBwoQHDhosQGCggEAQKVCUIDFCRAgMFypIiEDgokIPFCA4YJDgQIGXAwSeiEGzZs0XL1wIEGgiBoCfP2nidMEigMAONm/mZFFUIIeaGaJKjbrCqIINSW0OtarBJ1AAQpdyzRpjKNOxNKdOrSqwq00YOVuwWKGCa4C7ePPiRcg3IAA7") */
   background-image: url("data:image/gif;base64,R0lGODlhEAAQAIcAAAAAADVJYzZKZC9iyDFlzTly4j5240B240Z75Ep940D/QE6B5FaG5ViH5WKO5myU526X52WV82qZ9Xab6Hqf6XGd9X+h6Xei9n2n+ICAgJOit5alupqpvp6uw4Sl6Yam6ouq6oSr+Yuw+pC1+5a5/Jq9/aOyyKe2zJ/A/qLC/9Dg8ODg8ODo8PDw8PDw//D4///4/////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAMAAAoALAAAAAAQABAAAAiOABUIHEiwoMGDBUEoBPHBwoQHDhosQGCggEAQKVCUIDFCRAgMFypIiEDgokIPFCA4YJDgQIGXAwSeiEGzZs0XL1wIEGgiBoCfP2nidMEigMAONm/mZFFUIIeaGaJKjbrCqIINSW0OtarBJ1AAQpdyzRpjKNOxNKdOrSqwq00YOVuwWKGCa4C7ePPiRcg3IAA7")  
}

.x-tree-icon-parent {
    background-image: url("data:image/gif;R0lGODlhEAAQAKU2ADFKY0L/QplnAZpoApxqBJ5sBqBuCKNxC6VzDad1D6h2EKt5E6x6FK58FrB+GLOBG7WCHbeEH7qHIr2KJcCNKMKPKsWSLceUL8iVMMmWMcuYM8yZNNu3Utu3cf/Ub//bdf/kf5SlvZylvZytxqW11qm92r3GxrnK5P/vif/4k///mf//nP//usDAwMvLy8zMzNPT09bW1sbW69jh8efv9+vz/////////////////////////////////////////yH5BAEAAD8ALAAAAAAQABAAAAZ8wJ9wSCwSNxtNBmM82p4sVqX523Q4WGxnIolAHg6h5kkukxmxX0a1arvfqsTrd1HZ73j7wfWzqFKAgYIqBnwVKiiJiosqBXwUKiCSk5QqBHwTKh+bnJ0qA3wSKh6kpaYqAnM/Xw4NCwoIBwYFBAItMEMwLru8vbhUwMFFQQA7")
}

.x-tree-icon-parent-expanded {
    background-image: url("data:image/gif;R0lGODlhEAAQAKU9ADFKY0L/QplnAZpoApxqBJ5sBqBuCKJwCqNxC6RyDKVzDad1D6x6FLB+GLOBG7WCHbeEH7qHIr2KJcaaGcaaGsKPKsiVMMmWMcuYM8yZNMmgIc+iJte4QNq/bOKzQ+LBUP3VcP/bdfDkev/kf5SlvZylvbe3t5ytxqW11qm92r3GxrnK5P/XhP/rhP/viffwif/4k///mf//nP//pcTExMXFxc3NzdHR0cbW69jh8efv9+vz//r7/P///////////yH5BAEAAD8ALAAAAAAQABAAAAaBwJ9wSCwSMxnMxWI89p48XqX5y/RkWGxPEoE8HA0h5prNPp+M2+/Sg7nfcNmiNqnb7/VPC0GbxMplMR0TLAZ9f3BvMi8TIAU0P34uk5STMxoeBJB+MiOenyMzHBsDkJExIamqqSIUAjVCEwqzswkHBgUEAyY2QzY0wMHCvVTFxkVBADs=")
}

.x-tree-icon-custom {
    background-image: none
}

.x-tree-checkbox {
    margin-right: 3px;
    top: 4px;
    width: 13px;
    height: 13px;
    background-image: url("data:image/gif;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")
}

.x-tree-checkbox-checked {
    background-position: 0 -13px
}

.x-grid-tree-loading .x-tree-icon {
    background-image: url("data:image/gif;R0lGODlhEAAQALMMAKqooJGOhp2bk7e1rZ2bkre1rJCPhqqon8PBudDOxXd1bISCef///wAAAAAAAAAAACH/C05FVFNDQVBFMi4wAwEAAAAh+QQFAAAMACwAAAAAEAAQAAAET5DJyYyhmAZ7sxQEs1nMsmACGJKmSaVEOLXnK1PuBADepCiMg/DQ+/2GRI8RKOxJfpTCIJNIYArS6aRajWYZCASDa41Ow+Fx2YMWOyfpTAQAIfkEBQAADAAsAAAAABAAEAAABE6QyckEoZgKe7MEQMUxhoEd6FFdQWlOqTq15SlT9VQM3rQsjMKO5/n9hANixgjc9SQ/CgKRUSgw0ynFapVmGYkEg3v1gsPibg8tfk7CnggAIfkEBQAADAAsAAAAABAAEAAABE2QycnOoZjaA/IsRWV1goCBoMiUJTW8A0XMBPZmM4Ug3hQEjN2uZygahDyP0RBMEpmTRCKzWGCkUkq1SsFOFQrG1tr9gsPc3jnco4A9EQAh+QQFAAAMACwAAAAAEAAQAAAETpDJyUqhmFqbJ0LMIA7McWDfF5LmAVApOLUvLFMmlSTdJAiM3a73+wl5HYKSEET2lBSFIhMIYKRSimFriGIZiwWD2/WCw+Jt7xxeU9qZCAAh+QQFAAAMACwAAAAAEAAQAAAETZDJyRCimFqbZ0rVxgwF9n3hSJbeSQ2rCWIkpSjddBzMfee7nQ/XCfJ+OQYAQFksMgQBxumkEKLSCfVpMDCugqyW2w18xZmuwZycdDsRACH5BAUAAAwALAAAAAAQABAAAARNkMnJUqKYWpunUtXGIAj2feFIlt5JrWybkdSydNNQMLaND7pC79YBFnY+HENHMRgyhwPGaQhQotGm00oQMLBSLYPQ9QIASrLAq5x0OxEAIfkEBQAADAAsAAAAABAAEAAABE2QycmUopham+da1cYkCfZ94UiW3kmtbJuRlGF0E4Iwto3rut6tA9wFAjiJjkIgZAYDTLNJgUIpgqyAcTgwCuACJssAdL3gpLmbpLAzEQA7")
}

.x-tree-node-text {
    padding-left: 3px
}

.x-grid-cell-inner-treecolumn {
    padding: 3px 6px 4px 0
}

.x-tree-drop-ok-append .x-dd-drop-icon {
    background-image: url("data:image/gif;R0lGODlhEAAQAIcAAD2GNUKNNkOPOESMO0WNPEmPP0iNQUmPQlOVTFWWTVCZQVeeRV6cVmGeWGSgVWSgV2aiWGejW2WrVWirU2uqWGqsW2yqWm61WG+1WG+1WXS3W3S3XHC4WXK5W3O6XHG+X3asZ3iuaHe8YHi0ZH+yany6ZH28Zn2+Z3m9bn25an25a3+5bXDBY3nBZHrGa3zDa37BaX7Hb4K1boO1boa3cYi4d4y7doq5eYm+eI2+e5O/f4HMdYbJeobJfIXNeYrCeY/CfYnIf4rPfZW/gozLgY7MhI7Sg5LFgJXAgpfHhZfMhZPNiJjLhpjMh5jMipvBl5vBmJTTipbTiZXUipbUi5fVi5nRi53YkqTOlKbPlqbQlqDZlaDZlqXbm6rUnavUnKbIoKfJoa/fpa/fprPZpbTZpbTaprLbqLPdqbXbqLfaqrTdqrXfrLbdrLjVr7jdr7vcr7rWsbzVubfgr77itr3ktsTcuMXducnexMrexcXowMvmw8zgxs3gx87pydTrz9fu0tnp0dzx2ODy3OPt4ePu4ufw5ejx5uvz6e/27P///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAMAAIsALAAAAAAQABAAAAjGABcJHEiwoME7SGjIuBHHoMBAOrDs+ePnzYoQfQoGsgFnUJ0uXMTo+QEhD0EdagRdWVKEyhQjc1REGGgnCaAtUYIoUuTjRQw2C8IIHNJmDJEeKHZWEOHBypEGAmfQqcJjp1VFHGB4KSCQBBohO67u5HDiywCBNZxIccFCwlgOHZTkSCDQzYQ1LT6IGHthgxkBTwaCSHGGKYcMGDSQsXCAIB8HI9I0MVGCSRkKAOQUxPNAARAtWXAEMKDZIRgGBQgggOKwtcGAADs=")
}

.x-tree-drop-ok-above .x-dd-drop-icon {
    background-image: url("data:image/gif;R0lGODlhEAAQAIcAADVJY0Y3K0g5LFJBM1ZENSBIoGd6lWt+mXSFn3yNpo9+YJyMaqGQbq2dd7GgeNfFYOPUbO/ieKikn72tgq+vr7+/v5upwMGwhM/Pz9/f3////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAAAAP8ALAAAAAAQABAAAAhsADUIHDgQQwGCCAkaPEjQQkINBSJKpPBQYIWIAjMcdPjw4kCGDS1IEIjhowaOAh0CqEjwggMGCxQ8dOhwQgQIDwhoSIDggIGEDQYMEBBgJsujJ0VWRHlSw0qkLmHKTEhTg02cOnn6BCqU6MOAADs=")
}

.x-tree-drop-ok-below .x-dd-drop-icon {
    background-image: url("data:image/gif;R0lGODlhEAAQAIcAADVJY0Y3K0g5LFJBM1ZENSBIoGd6lWt+mXSFn3yNpo9+YJyMaqGQbq2dd7GgeNfFYOPUbO/ieKikn72tgq+vr7+/v5upwMGwhM/Pz9/f3////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAAAAP8ALAAAAAAQABAAAAhsADUIFGjBgoSBCDVYQLgQQMKHGi44YLBAgYYECA4YIKhQw4QIEB4QgIiwwYABAgJAXEiyJUGDJFlydOgy4sSKFzNu7LjwY8iRLk2iVIlhYIGOECscFbg0aYGlGY4ulMn0qVUKLTE8rTlQa8KAADs=")
}

.x-tree-drop-ok-between .x-dd-drop-icon {
    background-image: url("data:image/gif;R0lGODlhEAAQAIcAADVJY0Y3K0g5LFJBM1ZENSBIoGd6lWt+mXSFn3yNpo9+YJyMaqGQbq2dd7GgeNfFYOPUbO/ieKikn72tgr+/v5upwMGwhM/Pz////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAAAAP8ALAAAAAAQABAAAAhoADEIFFihgoSBCDFUQLgQQMKHGCw4YLBAAYYECA4YIKgQw4QIEB4QgIiwwYABAgIIvMCQJAYKBVwihBlz4MKFCQvo3Cnzgs6WJH26LHhwJVCODmVGnFjxYsaNHRd+DDlSpkmUKpUqDQgAOw==")
}

.x-tree-ddindicator {
    height: 1px;
    border-width: 1px 0px 0px;
    border-style: dotted;
    border-color: green
}

.x-multiselector-remove {
    font-size: 110%;
    color: #eee;
    cursor: pointer
}

.x-multiselector-remove .x-grid-cell-inner {
    padding: 3px 4px 4px 4px
}

.x-grid-item-over .x-multiselector-remove {
    color: red
}

.x-toast-icon-information {
    background-image: url("data:image/gif;iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABGdBTUEAAK/INwWK6QAAABl0RVh0U29mdHdhcmUAQWRvYmUgSW1hZ2VSZWFkeXHJZTwAAALlSURBVHjapJNLTBNRFIb/mU4pbWlpeRSwIi9RUBMBA4lRICLxFeODDQkLdEOCGsXowmiMmrAyutAYo9EYEzUxxoVRNyZsDRoRROVRoJRSS3kULS3tdDrM3OsdSGqMGxPO4i7OPec/3znnXo5SitUYj1WaoB2+ST+v43lrKBo7Cl7/YFOpE5KsQoqJyMiwQ6Uq5kNxfP3muhvWWc9tW2chBqhwFuYDWgtuty/VO+GlkfACVYlKNdu88zSFoYLOzS9SQlfMG/hJ773tvzoy7i+f9PgELXe5helIosVoToPZko6YsoLWXF8P3nEMA34RogpEZMCZY8eOyuJrPX2uoVA4yidnYDEKj8x2O+JLFKkCh6BE0X65CTOjHXBYVIjMPxXVRDiU5FowNBOHlFCuJwWILCscx2NeZEEKh6XQL1Tu7oQjrx3PusYg8BxYZ5iNAd6gjCOHG+DyTp1NCkRYxRBDVxhqMEyRlZeJ/fu2gjNXwmq1YZHdJQgHiQAiFaCqBJ7xgJLcQjQWQSwOLGk0DFdD5dmUOV5iwZQlAyrz6/VMJC7DM8dQeP7POwhzZmHC42c+FsBchL2t4ILIxGQE5xeRYGRhRhBipCYTwZWTF5DvzBKSAlXZOl//oAse/wJ0IGDFoBAzHBXF6O4ZY7tmqBxBQo7h9uMuGE16HKir9Gm5nLbLuekZPHndPZzQG8q4jAKUFBVjvdOwXNlm1MEdkDAx7sbzF+8Q+NyN+zfPuDaWFpSXbChaEei88xLpacYUmzn1w3ScVLlHxtE77EdbWwvMmQV4eOsGQqEo8tM4nD/R1MfxKdsVlch7G2tWWmDJiMZluSA3vbau0Nra++n7noZyR2zAtwDoVHj7vuBUU/XHix0tTbYMW62iEFnQ8f9+JiYkmkzGp4NjP7pqqreUHCozSW/ejyJnbS5aWw66XGP+V0ZjivhfvzE7M33WpFPXXKq3JPbsqlHIEsk73tyIqCj9FfdbgAEAfnti+v0M9kAAAAAASUVORK5CYII=")
}

.x-toast-icon-error {
    background-image: url("data:image/gif;iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABGdBTUEAAK/INwWK6QAAABl0RVh0U29mdHdhcmUAQWRvYmUgSW1hZ2VSZWFkeXHJZTwAAAPmSURBVHjaYpzKyMjAA8QaTEwM/5iZGd4wMTEx/vihwPT/vy0LA4PKXwYGZgYGhiefGRiOs7GxXQOK/WQEqmMDqmcC0gABBORDwH8g/vv7tybH///T5KWlLQVNTdk5FRQYGNnZGX6/fs3w/tSpv89v3Ljz5vfvPCZOzl0wfQABxDgJSPACTVP69y9KgItrtlJSEhebtzfDf5CLfv4Emgw0moWFgYWLi+HvyZMMT/r6GO6+ft3PwMlZysrC8hcggJiT2NgYGP788Vfl4VkqV1bGweLqyvDzzh2Gf0CN/4Fy///9Y/j/5w/Dr9u3GRg0NBgEzM0Z2E+ftnz/4QMj0HX7AQKISYGNTUSTlXW6UEQEG6OxMcPPq1cZGN+8Yfh77x7YiUw8PAx/gQYyfvrE8OfSJYY/oqIMghkZDBLc3KX/vn83Bwgg5ojfv/PFVFQChBITGf4/eMDAzMvLwJOXx8AqJsbwfcUKhj9AA7kcHBi4gfIMnz8z/LlwgYFVW5uB6c0blve3bokCBBATBzOzL7+tLQMLMCb+XLvGwGZkxAAKZRZNTQaetDQGruBgBnY3N7BrWIHO//3sGQPj27cM3NbWDPzc3NYAAcTExsOjyC0ry/D/4UMGNnl5hi8TJjD8OHECokFXl4HDxQXMBml8X1HBwA4MzP8fPzJwAL3GJS8vBBBATGx8fCwswND+//IlA9O3bwycwBB/X13N8AfoXOQoflNUxMC0cSPD/2PHGP7u2MHABDSElZ+fESCAmP69ffv1PzCEGX/9YmACuuIL0Cb+iRMZWIBhAY9rIBaePJnhp4EBA9P9+wxMz58z/AMa9PvVq58AAcRwlZV12Rslpf9/TEz+PzU0/P/57t3/MPDp0qX/b3bt+v8Pyv/56dP/+/b2/3/KyPz/rqr6/ywX12WAAGL6zMQ0583bt78ZX7xg4AOa/nn5cgZg8mX4DHTNZ2CC+hMSwvB61y6wN97v28fAc/MmAzABMbwGeuH7//8rAAKI8RoHB8M3BoZVfFxcocrAZPsXGN9PIyIYOI4fZxAFRisTUOw9MEG9j4xkkFi8mIEbaNBjYCw9/vLlNh8jowlAADEuBkoaMTPzszIwHP7EzKyrCDSdBxiArKysDIygcAClSGAg//n6leEHMOQfAg348evXK8n//60f/ft3ByCAQOHDYAs0MZONTcCOmXnq53//Iv8wMzOyAjUyQmMA6H2GP8B0wgykmRkZz7L//h049/fvx0uByRwggBhhAc3KyPhfCEhHsLAYB7KxFfEwMNjx/P/PB1TA9I2R8evXf/8uXGZknDbt169td/78+f0LqBYUVgABBgCcL3mszjTFOQAAAABJRU5ErkJggg==")
}

.x-toast-window .x-window-body {
    padding: 15px 5px 15px 5px
}

.x-toast-light .x-window-header {
    background-color: transparent
}

.x-toast-light .x-tool-img {
    background-color: transparent
}

.x-toast-light {
    background-image: url("data:image/gif;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")
}

.x-toast-light .x-window-body {
    padding: 15px 5px 20px 5px;
    background-color: transparent;
    border: 0px solid white
}

.x-box-tl {
    background: transparent no-repeat 0 0
}

.x-box-tc {
    height: 8px;
    background: transparent repeat-x 0 0;
    overflow: hidden
}

.x-box-tr {
    background: transparent no-repeat right -8px
}

.x-box-ml {
    background: transparent repeat-y 0;
    padding-left: 4px;
    overflow: hidden
}

.x-box-mc {
    background: repeat-x 0 -16px;
    padding: 4px 10px
}

.x-box-mc h3 {
    margin: 0 0 4px 0
}

.x-box-mr {
    background: transparent repeat-y right;
    padding-right: 4px;
    overflow: hidden
}

.x-box-bl {
    background: transparent no-repeat 0 -16px
}

.x-box-bc {
    background: transparent repeat-x 0 -8px;
    height: 8px;
    overflow: hidden
}

.x-box-br {
    background: transparent no-repeat right -24px
}

.x-box-tl, .x-box-bl {
    padding-left: 8px;
    overflow: hidden
}

.x-box-tr, .x-box-br {
    padding-right: 8px;
    overflow: hidden
}

.x-box-tl {
    background-image: url("data:image/gif;R0lGODlhCAAgAIcAAMDAwMPDw8TExMXFxcbGxsnJycvLy8zMzM7Ozs/Pz9DQ0NHR0dLS0tPT09XV1dbW1tfX19jY2NnZ2dzc3N3d3d7e3uDg4OHh4eLi4uPj4+Tk5OXl5ebm5ufn5+np6erq6uvr6+zs7O3t7e7u7u/v7/Dw8PHx8fLy8vPz8/T09PX19fb29vf39/j4+Pn5+fv7+/z8/P39/f7+/v///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAED/QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAMAAIcALAAAAAAIACAAAAjKAA8JHEhwIIoRHgaqAGEBggKBKTg8OBAhxCEWHhw4mMHxUIkJCjh2/MAgg8gZhzgYgHGy4EAPI1AUVADBAggVA0NEOPCgQwqBIjV6YHHoZIIJJoqKxMDgg1KOLwxwOCSiwoATI7KOIKEBwYMVWlV4kCCAgoqsh0hsaABAxgoQAkNcWBAAwQaBJkJkiKCgAEGEGyy4LKE16wkCFURoZfEAgQYSWVVQECDBw8IVMgA02EDi0AYEARZcsHiogIIIGUIkPWRhA8y/JVwGBAA7")
}

.x-box-tc {
    background-image: url("data:image/gif;R0lGODlhAQAgAIcAAMHBwcjIyNvb2+Tk5Ozs7O7u7u/v7/Dw8PHx8fPz8/T09PX19fb29vf39/j4+Pn5+fr6+vz8/P39/f7+/v///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAAAAP8ALAAAAAABACAAAAgkABkMCCCBgkEKBRIWYABAAAEKEyREgPDAQQMGCxQkQHDAQIGAADs=")
}

.x-box-tr {
    background-image: url("data:image/gif;R0lGODlhCAAgAIcAAMDAwMPDw8TExMXFxcbGxsnJycvLy8zMzM7Ozs/Pz9DQ0NHR0dLS0tPT09XV1dbW1tfX19jY2NnZ2dzc3N3d3d7e3uDg4OHh4eLi4uPj4+Tk5OXl5ebm5ufn5+np6erq6uvr6+zs7O3t7e7u7u/v7/Dw8PHx8fLy8vPz8/T09PX19fb29vf39/j4+Pn5+fv7+/z8/P39/f7+/v///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAED/QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAMAAIcALAAAAAAIACAAAAjKAA8JHEhwIIoRHgaqAGEBggKBKTg8OBAhxCEWHhw4mMHxUIkJCjh2/MAgg8gZhzgYgHGy4EAPI1AUVADBAggVA0NEOPCgQwqBIjV6YHHoZIIJJoqKxMDgg1KOLwxwOCSiwoATI7KOIKEBwYMVWlV4kCCAgoqsh0hsaABAxgoQAkNcWBAAwQaBJkJkiKCgAEGEGyy4LKE16wkCFURoZfEAgQYSWVVQECDBw8IVMgA02EDi0AYEARZcsHiogIIIGUIkPWRhA8y/JVwGBAA7")
}

.x-box-ml {
    background-image: url("data:image/gif;R0lGODlhBAABAIcAAMHBwdzc3Ozs7P7+/gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAAAAP8ALAAAAAAEAAEAAAgHAAUEADAgIAA7")
}

.x-box-mc {
    background-color: #eee;
    background-image: url("data:image/gif;R0lGODlhAQAgAIcAAMHBwcjIyNvb2+Tk5Ozs7O7u7u/v7/Dw8PHx8fPz8/T09PX19fb29vf39/j4+Pn5+fr6+vz8/P39/f7+/v///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAAAAP8ALAAAAAABACAAAAgkABkMCCCBgkEKBRIWYABAAAEKEyREgPDAQQMGCxQkQHDAQIGAADs=");
    font-family: "Myriad Pro", "Myriad Web", "Tahoma", "Helvetica", "Arial", sans-serif;
    color: #393939;
    font-size: 15px
}

.x-box-mc h3 {
    font-size: 18px;
    font-weight: bold
}

.x-box-mr {
    background-image: url("data:image/gif;R0lGODlhBAABAIcAAMHBwdzc3Ozs7P///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAAAAP8ALAAAAAAEAAEAAAgHAAcACCAgIAA7")
}

.x-box-bl {
    background-image: url("data:image/gif;R0lGODlhCAAgAIcAAMDAwMPDw8TExMXFxcbGxsnJycvLy8zMzM7Ozs/Pz9DQ0NHR0dLS0tPT09XV1dbW1tfX19jY2NnZ2dzc3N3d3d7e3uDg4OHh4eLi4uPj4+Tk5OXl5ebm5ufn5+np6erq6uvr6+zs7O3t7e7u7u/v7/Dw8PHx8fLy8vPz8/T09PX19fb29vf39/j4+Pn5+fv7+/z8/P39/f7+/v///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAED/QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAMAAIcALAAAAAAIACAAAAjKAA8JHEhwIIoRHgaqAGEBggKBKTg8OBAhxCEWHhw4mMHxUIkJCjh2/MAgg8gZhzgYgHGy4EAPI1AUVADBAggVA0NEOPCgQwqBIjV6YHHoZIIJJoqKxMDgg1KOLwxwOCSiwoATI7KOIKEBwYMVWlV4kCCAgoqsh0hsaABAxgoQAkNcWBAAwQaBJkJkiKCgAEGEGyy4LKE16wkCFURoZfEAgQYSWVVQECDBw8IVMgA02EDi0AYEARZcsHiogIIIGUIkPWRhA8y/JVwGBAA7")
}

.x-box-bc {
    background-image: url("data:image/gif;R0lGODlhAQAgAIcAAMHBwcjIyNvb2+Tk5Ozs7O7u7u/v7/Dw8PHx8fPz8/T09PX19fb29vf39/j4+Pn5+fr6+vz8/P39/f7+/v///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAAAAP8ALAAAAAABACAAAAgkABkMCCCBgkEKBRIWYABAAAEKEyREgPDAQQMGCxQkQHDAQIGAADs=")
}

.x-box-br {
    background-image: url("data:image/gif;R0lGODlhCAAgAIcAAMDAwMPDw8TExMXFxcbGxsnJycvLy8zMzM7Ozs/Pz9DQ0NHR0dLS0tPT09XV1dbW1tfX19jY2NnZ2dzc3N3d3d7e3uDg4OHh4eLi4uPj4+Tk5OXl5ebm5ufn5+np6erq6uvr6+zs7O3t7e7u7u/v7/Dw8PHx8fLy8vPz8/T09PX19fb29vf39/j4+Pn5+fv7+/z8/P39/f7+/v///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAED/QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAMAAIcALAAAAAAIACAAAAjKAA8JHEhwIIoRHgaqAGEBggKBKTg8OBAhxCEWHhw4mMHxUIkJCjh2/MAgg8gZhzgYgHGy4EAPI1AUVADBAggVA0NEOPCgQwqBIjV6YHHoZIIJJoqKxMDgg1KOLwxwOCSiwoATI7KOIKEBwYMVWlV4kCCAgoqsh0hsaABAxgoQAkNcWBAAwQaBJkJkiKCgAEGEGyy4LKE16wkCFURoZfEAgQYSWVVQECDBw8IVMgA02EDi0AYEARZcsHiogIIIGUIkPWRhA8y/JVwGBAA7")
}

.x-box-blue .x-box-bl, .x-box-blue .x-box-br, .x-box-blue .x-box-tl, .x-box-blue .x-box-tr {
    background-image: url("data:image/gif;R0lGODlhCAAgAIcAAKLG9LDP9s7OztHR0dPT09XV1dbW1tjY2NnZ2dzc3N3d3d7e3sHZ+eDg4OHh4eLi4uPj4+Tk5OXl5ebm5ufn5+np6erq6uvr6+zs7O3t7e7u7u/v7+jy/PDw8PHx8fLy8vPz8/T09PX19fb29vf39/j4+Pn5+fv7+/z8/P39/f7+/v///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAED/QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAMAAJoALAAAAAAIACAAAAjPADUJHEhwIAgNFQaKuNAgAACBISYYAHBghSYSFQoEWLGCg6YOCQBw5ODRQgAIHUlqmgAABUmVBQVW0ACiBEEAARpcEDFwxQEABiiEEMiBY4ACFUhoIskRQAIPS5k+CGAhKskTACZoyrAAwAcGYBlsiBDAwIiwIiogAKBABFhNGyQQAKDirEAMDgYAECBBoAcMEA44JIhQQoOYHTSEZfABwIIMYUkYCBBhA1gRCgAgqOB2hAoABCRs0CRBAIABDjAIxHkAAgaomhpImEm4Q8yAADs=")
}

.x-box-blue .x-box-bc, .x-box-blue .x-box-mc, .x-box-blue .x-box-tc {
    background-image: url("data:image/gif;R0lGODlhAQAqAIcAAKLG9KTH9KfJ9anK9avM9a7N9rDP9rLQ9rXR97fT97rU+LzW+L7X+Nvb28HZ+cXb+cjd+czg+s/i+tLk+tbm+trp+9/s++Tk5Ozs7OPv/Ojy/Pb29v39/QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAAAAP8ALAAAAAABACoAAAgwADdcAMBBg0ENDhI62ACgAQYNGSxUoEBhgoQIEB44ABBAwAACBQwcQJBAwQIGDgICADs=")
}

.x-box-blue .x-box-mc {
    background-color: #c3daf9
}

.x-box-blue .x-box-mc h3 {
    color: #17385b
}

.x-box-blue .x-box-ml {
    background-image: url("data:image/gif;R0lGODlhBAABAIcAAKLG9Nzc3Ozs7P7+/gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAAAAP8ALAAAAAAEAAEAAAgHAAUEADAgIAA7")
}

.x-box-blue .x-box-mr {
    background-image: url("data:image/gif;R0lGODlhBAABAIcAAKLG9Nzc3Ozs7P///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAAAAP8ALAAAAAAEAAEAAAgHAAcACCAgIAA7")
}

.x-message-box .x-msg-box-wait {
    background-image: url("data:image/gif;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")
}

.x-html-editor-wrap .x-toolbar {
    border-left-color: #b5b8c8;
    border-top-color: #b5b8c8;
    border-right-color: #b5b8c8
}

.x-html-editor-input {
    border: 1px solid #b5b8c8;
    border-top-width: 0
}

.x-column-header-trigger {
    background-color: #c5c5c5
}

.x-sliderwidget-default-cell .x-slider {
    margin: 2px 0 1px 0
}

.x-accordion-hd {
    -webkit-box-shadow: inset 0 0 #d9e7f8;
    -moz-box-shadow: inset 0 0 #d9e7f8;
    box-shadow: inset 0 0 #d9e7f8
}

.x-accordion-hd-sibling-expanded {
    -webkit-box-shadow: inset 0 1px #f3f7fb;
    -moz-box-shadow: inset 0 1px #f3f7fb;
    box-shadow: inset 0 1px #f3f7fb
}

.x-resizable-handle-east-over, .x-resizable-handle-west-over {
    background-position: left
}

.x-resizable-handle-south-over, .x-resizable-handle-north-over {
    background-position: top
}

.x-resizable-handle-southeast-over {
    background-position: top left
}

.x-resizable-handle-northwest-over {
    background-position: bottom right
}

.x-resizable-handle-northeast-over {
    background-position: bottom left
}

.x-resizable-handle-southwest-over {
    background-position: top right
}

.x-resizable-pinned .x-resizable-handle-east, .x-resizable-pinned .x-resizable-handle-west {
    background-position: left
}

.x-resizable-pinned .x-resizable-handle-south, .x-resizable-pinned .x-resizable-handle-north {
    background-position: top
}

.x-resizable-pinned .x-resizable-handle-southeast {
    background-position: top left
}

.x-resizable-pinned .x-resizable-handle-northwest {
    background-position: bottom right
}

.x-resizable-pinned .x-resizable-handle-northeast {
    background-position: bottom left
}

.x-resizable-pinned .x-resizable-handle-southwest {
    background-position: top right
}

.x-slider-focus .x-slider-thumb {
    outline: 1px dotted #333
}
"""