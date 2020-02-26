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
    background-image: url(images/tree/loading.gif);
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
    background-image: url(images/grid/loading.gif);
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
    background-image: url(images/progress/progress-default-bg.gif)
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
    content: "x-slicer:, bg:url(images/progress/progress-default-bg.gif), stretch:bottom" !important
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
    background-image: url(images/btn/btn-default-small-fbg.gif);
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
    background-image: url(images/btn/btn-default-small-corners.gif)
}

.x-btn-default-small-ml, .x-btn-default-small-mr {
    background-image: url(images/btn/btn-default-small-sides.gif)
}

.x-btn-default-small-mc {
    padding: 0px 0px 0px 0px
}

.x-cmd-slicer.x-btn-default-small:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, frame-bg:url(images/btn/btn-default-small-fbg.gif), corners:url(images/btn/btn-default-small-corners.gif), sides:url(images/btn/btn-default-small-sides.gif)" !important
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
    background-image: url(images/button/arrow.gif);
    padding-right: 8px
}

.x-btn-wrap-default-small.x-btn-arrow-bottom:after {
    height: 8px;
    background-image: url(images/button/arrow.gif)
}

.x-btn-wrap-default-small.x-btn-split-right:after {
    width: 14px;
    background-image: url(images/button/s-arrow.gif);
    padding-right: 14px
}

.x-btn-wrap-default-small.x-btn-split-bottom:after {
    height: 14px;
    background-image: url(images/button/s-arrow-b.gif)
}

.x-btn-over > .x-btn-wrap-default-small.x-btn-split-right:after {
    background-image: url(images/button/s-arrow-o.gif)
}

.x-btn-over > .x-btn-wrap-default-small.x-btn-split-bottom:after {
    background-image: url(images/button/s-arrow-bo.gif)
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
    background-image: url(images/btn/btn-default-small-focus-corners.gif)
}

.x-btn-focus .x-btn-default-small-ml, .x-btn-focus .x-btn-default-small-mr {
    background-image: url(images/btn/btn-default-small-focus-sides.gif)
}

.x-btn-focus .x-btn-default-small-mc {
    background-color: #fff;
    background-image: url(images/btn/btn-default-small-focus-fbg.gif)
}

.x-btn-over .x-btn-default-small-tl, .x-btn-over .x-btn-default-small-bl, .x-btn-over .x-btn-default-small-tr, .x-btn-over .x-btn-default-small-br, .x-btn-over .x-btn-default-small-tc, .x-btn-over .x-btn-default-small-bc {
    background-image: url(images/btn/btn-default-small-over-corners.gif)
}

.x-btn-over .x-btn-default-small-ml, .x-btn-over .x-btn-default-small-mr {
    background-image: url(images/btn/btn-default-small-over-sides.gif)
}

.x-btn-over .x-btn-default-small-mc {
    background-color: #e4f3ff;
    background-image: url(images/btn/btn-default-small-over-fbg.gif)
}

.x-btn-focus.x-btn-over .x-btn-default-small-tl, .x-btn-focus.x-btn-over .x-btn-default-small-bl, .x-btn-focus.x-btn-over .x-btn-default-small-tr, .x-btn-focus.x-btn-over .x-btn-default-small-br, .x-btn-focus.x-btn-over .x-btn-default-small-tc, .x-btn-focus.x-btn-over .x-btn-default-small-bc {
    background-image: url(images/btn/btn-default-small-focus-over-corners.gif)
}

.x-btn-focus.x-btn-over .x-btn-default-small-ml, .x-btn-focus.x-btn-over .x-btn-default-small-mr {
    background-image: url(images/btn/btn-default-small-focus-over-sides.gif)
}

.x-btn-focus.x-btn-over .x-btn-default-small-mc {
    background-color: #e4f3ff;
    background-image: url(images/btn/btn-default-small-focus-over-fbg.gif)
}

.x-btn.x-btn-menu-active .x-btn-default-small-tl, .x-btn.x-btn-menu-active .x-btn-default-small-bl, .x-btn.x-btn-menu-active .x-btn-default-small-tr, .x-btn.x-btn-menu-active .x-btn-default-small-br, .x-btn.x-btn-menu-active .x-btn-default-small-tc, .x-btn.x-btn-menu-active .x-btn-default-small-bc, .x-btn.x-btn-pressed .x-btn-default-small-tl, .x-btn.x-btn-pressed .x-btn-default-small-bl, .x-btn.x-btn-pressed .x-btn-default-small-tr, .x-btn.x-btn-pressed .x-btn-default-small-br, .x-btn.x-btn-pressed .x-btn-default-small-tc, .x-btn.x-btn-pressed .x-btn-default-small-bc {
    background-image: url(images/btn/btn-default-small-pressed-corners.gif)
}

.x-btn.x-btn-menu-active .x-btn-default-small-ml, .x-btn.x-btn-menu-active .x-btn-default-small-mr, .x-btn.x-btn-pressed .x-btn-default-small-ml, .x-btn.x-btn-pressed .x-btn-default-small-mr {
    background-image: url(images/btn/btn-default-small-pressed-sides.gif)
}

.x-btn.x-btn-menu-active .x-btn-default-small-mc, .x-btn.x-btn-pressed .x-btn-default-small-mc {
    background-color: #b6cbe4;
    background-image: url(images/btn/btn-default-small-pressed-fbg.gif)
}

.x-btn-focus.x-btn-menu-active .x-btn-default-small-tl, .x-btn-focus.x-btn-menu-active .x-btn-default-small-bl, .x-btn-focus.x-btn-menu-active .x-btn-default-small-tr, .x-btn-focus.x-btn-menu-active .x-btn-default-small-br, .x-btn-focus.x-btn-menu-active .x-btn-default-small-tc, .x-btn-focus.x-btn-menu-active .x-btn-default-small-bc, .x-btn-focus.x-btn-pressed .x-btn-default-small-tl, .x-btn-focus.x-btn-pressed .x-btn-default-small-bl, .x-btn-focus.x-btn-pressed .x-btn-default-small-tr, .x-btn-focus.x-btn-pressed .x-btn-default-small-br, .x-btn-focus.x-btn-pressed .x-btn-default-small-tc, .x-btn-focus.x-btn-pressed .x-btn-default-small-bc {
    background-image: url(images/btn/btn-default-small-focus-pressed-corners.gif)
}

.x-btn-focus.x-btn-menu-active .x-btn-default-small-ml, .x-btn-focus.x-btn-menu-active .x-btn-default-small-mr, .x-btn-focus.x-btn-pressed .x-btn-default-small-ml, .x-btn-focus.x-btn-pressed .x-btn-default-small-mr {
    background-image: url(images/btn/btn-default-small-focus-pressed-sides.gif)
}

.x-btn-focus.x-btn-menu-active .x-btn-default-small-mc, .x-btn-focus.x-btn-pressed .x-btn-default-small-mc {
    background-color: #b6cbe4;
    background-image: url(images/btn/btn-default-small-focus-pressed-fbg.gif)
}

.x-btn.x-btn-disabled .x-btn-default-small-tl, .x-btn.x-btn-disabled .x-btn-default-small-bl, .x-btn.x-btn-disabled .x-btn-default-small-tr, .x-btn.x-btn-disabled .x-btn-default-small-br, .x-btn.x-btn-disabled .x-btn-default-small-tc, .x-btn.x-btn-disabled .x-btn-default-small-bc {
    background-image: url(images/btn/btn-default-small-disabled-corners.gif)
}

.x-btn.x-btn-disabled .x-btn-default-small-ml, .x-btn.x-btn-disabled .x-btn-default-small-mr {
    background-image: url(images/btn/btn-default-small-disabled-sides.gif)
}

.x-btn.x-btn-disabled .x-btn-default-small-mc {
    background-color: #f7f7f7;
    background-image: url(images/btn/btn-default-small-disabled-fbg.gif)
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
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url(images/btn/btn-default-small-focus-corners.gif), sides:url(images/btn/btn-default-small-focus-sides.gif), frame-bg:url(images/btn/btn-default-small-focus-fbg.gif)" !important
}

.x-cmd-slicer.x-btn-over.x-btn-default-small:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url(images/btn/btn-default-small-over-corners.gif), sides:url(images/btn/btn-default-small-over-sides.gif), frame-bg:url(images/btn/btn-default-small-over-fbg.gif)" !important
}

.x-cmd-slicer.x-btn-focus.x-btn-over.x-btn-default-small:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url(images/btn/btn-default-small-focus-over-corners.gif), sides:url(images/btn/btn-default-small-focus-over-sides.gif), frame-bg:url(images/btn/btn-default-small-focus-over-fbg.gif)" !important
}

.x-cmd-slicer.x-btn-pressed.x-btn-default-small:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url(images/btn/btn-default-small-pressed-corners.gif), sides:url(images/btn/btn-default-small-pressed-sides.gif), frame-bg:url(images/btn/btn-default-small-pressed-fbg.gif)" !important
}

.x-cmd-slicer.x-btn-focus.x-btn-pressed.x-btn-default-small:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url(images/btn/btn-default-small-focus-pressed-corners.gif), sides:url(images/btn/btn-default-small-focus-pressed-sides.gif), frame-bg:url(images/btn/btn-default-small-focus-pressed-fbg.gif)" !important
}

.x-cmd-slicer.x-btn-disabled.x-btn-default-small:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url(images/btn/btn-default-small-disabled-corners.gif), sides:url(images/btn/btn-default-small-disabled-sides.gif), frame-bg:url(images/btn/btn-default-small-disabled-fbg.gif)" !important
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
    background-image: url(images/btn/btn-default-medium-fbg.gif);
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
    background-image: url(images/btn/btn-default-medium-corners.gif)
}

.x-btn-default-medium-ml, .x-btn-default-medium-mr {
    background-image: url(images/btn/btn-default-medium-sides.gif)
}

.x-btn-default-medium-mc {
    padding: 1px 1px 1px 1px
}

.x-cmd-slicer.x-btn-default-medium:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, frame-bg:url(images/btn/btn-default-medium-fbg.gif), corners:url(images/btn/btn-default-medium-corners.gif), sides:url(images/btn/btn-default-medium-sides.gif)" !important
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
    background-image: url(images/button/arrow.gif);
    padding-right: 8px
}

.x-btn-wrap-default-medium.x-btn-arrow-bottom:after {
    height: 8px;
    background-image: url(images/button/arrow.gif)
}

.x-btn-wrap-default-medium.x-btn-split-right:after {
    width: 14px;
    background-image: url(images/button/s-arrow.gif);
    padding-right: 14px
}

.x-btn-wrap-default-medium.x-btn-split-bottom:after {
    height: 14px;
    background-image: url(images/button/s-arrow-b.gif)
}

.x-btn-over > .x-btn-wrap-default-medium.x-btn-split-right:after {
    background-image: url(images/button/s-arrow-o.gif)
}

.x-btn-over > .x-btn-wrap-default-medium.x-btn-split-bottom:after {
    background-image: url(images/button/s-arrow-bo.gif)
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
    background-image: url(images/btn/btn-default-medium-focus-corners.gif)
}

.x-btn-focus .x-btn-default-medium-ml, .x-btn-focus .x-btn-default-medium-mr {
    background-image: url(images/btn/btn-default-medium-focus-sides.gif)
}

.x-btn-focus .x-btn-default-medium-mc {
    background-color: #fff;
    background-image: url(images/btn/btn-default-medium-focus-fbg.gif)
}

.x-btn-over .x-btn-default-medium-tl, .x-btn-over .x-btn-default-medium-bl, .x-btn-over .x-btn-default-medium-tr, .x-btn-over .x-btn-default-medium-br, .x-btn-over .x-btn-default-medium-tc, .x-btn-over .x-btn-default-medium-bc {
    background-image: url(images/btn/btn-default-medium-over-corners.gif)
}

.x-btn-over .x-btn-default-medium-ml, .x-btn-over .x-btn-default-medium-mr {
    background-image: url(images/btn/btn-default-medium-over-sides.gif)
}

.x-btn-over .x-btn-default-medium-mc {
    background-color: #e4f3ff;
    background-image: url(images/btn/btn-default-medium-over-fbg.gif)
}

.x-btn-focus.x-btn-over .x-btn-default-medium-tl, .x-btn-focus.x-btn-over .x-btn-default-medium-bl, .x-btn-focus.x-btn-over .x-btn-default-medium-tr, .x-btn-focus.x-btn-over .x-btn-default-medium-br, .x-btn-focus.x-btn-over .x-btn-default-medium-tc, .x-btn-focus.x-btn-over .x-btn-default-medium-bc {
    background-image: url(images/btn/btn-default-medium-focus-over-corners.gif)
}

.x-btn-focus.x-btn-over .x-btn-default-medium-ml, .x-btn-focus.x-btn-over .x-btn-default-medium-mr {
    background-image: url(images/btn/btn-default-medium-focus-over-sides.gif)
}

.x-btn-focus.x-btn-over .x-btn-default-medium-mc {
    background-color: #e4f3ff;
    background-image: url(images/btn/btn-default-medium-focus-over-fbg.gif)
}

.x-btn.x-btn-menu-active .x-btn-default-medium-tl, .x-btn.x-btn-menu-active .x-btn-default-medium-bl, .x-btn.x-btn-menu-active .x-btn-default-medium-tr, .x-btn.x-btn-menu-active .x-btn-default-medium-br, .x-btn.x-btn-menu-active .x-btn-default-medium-tc, .x-btn.x-btn-menu-active .x-btn-default-medium-bc, .x-btn.x-btn-pressed .x-btn-default-medium-tl, .x-btn.x-btn-pressed .x-btn-default-medium-bl, .x-btn.x-btn-pressed .x-btn-default-medium-tr, .x-btn.x-btn-pressed .x-btn-default-medium-br, .x-btn.x-btn-pressed .x-btn-default-medium-tc, .x-btn.x-btn-pressed .x-btn-default-medium-bc {
    background-image: url(images/btn/btn-default-medium-pressed-corners.gif)
}

.x-btn.x-btn-menu-active .x-btn-default-medium-ml, .x-btn.x-btn-menu-active .x-btn-default-medium-mr, .x-btn.x-btn-pressed .x-btn-default-medium-ml, .x-btn.x-btn-pressed .x-btn-default-medium-mr {
    background-image: url(images/btn/btn-default-medium-pressed-sides.gif)
}

.x-btn.x-btn-menu-active .x-btn-default-medium-mc, .x-btn.x-btn-pressed .x-btn-default-medium-mc {
    background-color: #b6cbe4;
    background-image: url(images/btn/btn-default-medium-pressed-fbg.gif)
}

.x-btn-focus.x-btn-menu-active .x-btn-default-medium-tl, .x-btn-focus.x-btn-menu-active .x-btn-default-medium-bl, .x-btn-focus.x-btn-menu-active .x-btn-default-medium-tr, .x-btn-focus.x-btn-menu-active .x-btn-default-medium-br, .x-btn-focus.x-btn-menu-active .x-btn-default-medium-tc, .x-btn-focus.x-btn-menu-active .x-btn-default-medium-bc, .x-btn-focus.x-btn-pressed .x-btn-default-medium-tl, .x-btn-focus.x-btn-pressed .x-btn-default-medium-bl, .x-btn-focus.x-btn-pressed .x-btn-default-medium-tr, .x-btn-focus.x-btn-pressed .x-btn-default-medium-br, .x-btn-focus.x-btn-pressed .x-btn-default-medium-tc, .x-btn-focus.x-btn-pressed .x-btn-default-medium-bc {
    background-image: url(images/btn/btn-default-medium-focus-pressed-corners.gif)
}

.x-btn-focus.x-btn-menu-active .x-btn-default-medium-ml, .x-btn-focus.x-btn-menu-active .x-btn-default-medium-mr, .x-btn-focus.x-btn-pressed .x-btn-default-medium-ml, .x-btn-focus.x-btn-pressed .x-btn-default-medium-mr {
    background-image: url(images/btn/btn-default-medium-focus-pressed-sides.gif)
}

.x-btn-focus.x-btn-menu-active .x-btn-default-medium-mc, .x-btn-focus.x-btn-pressed .x-btn-default-medium-mc {
    background-color: #b6cbe4;
    background-image: url(images/btn/btn-default-medium-focus-pressed-fbg.gif)
}

.x-btn.x-btn-disabled .x-btn-default-medium-tl, .x-btn.x-btn-disabled .x-btn-default-medium-bl, .x-btn.x-btn-disabled .x-btn-default-medium-tr, .x-btn.x-btn-disabled .x-btn-default-medium-br, .x-btn.x-btn-disabled .x-btn-default-medium-tc, .x-btn.x-btn-disabled .x-btn-default-medium-bc {
    background-image: url(images/btn/btn-default-medium-disabled-corners.gif)
}

.x-btn.x-btn-disabled .x-btn-default-medium-ml, .x-btn.x-btn-disabled .x-btn-default-medium-mr {
    background-image: url(images/btn/btn-default-medium-disabled-sides.gif)
}

.x-btn.x-btn-disabled .x-btn-default-medium-mc {
    background-color: #f7f7f7;
    background-image: url(images/btn/btn-default-medium-disabled-fbg.gif)
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
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url(images/btn/btn-default-medium-focus-corners.gif), sides:url(images/btn/btn-default-medium-focus-sides.gif), frame-bg:url(images/btn/btn-default-medium-focus-fbg.gif)" !important
}

.x-cmd-slicer.x-btn-over.x-btn-default-medium:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url(images/btn/btn-default-medium-over-corners.gif), sides:url(images/btn/btn-default-medium-over-sides.gif), frame-bg:url(images/btn/btn-default-medium-over-fbg.gif)" !important
}

.x-cmd-slicer.x-btn-focus.x-btn-over.x-btn-default-medium:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url(images/btn/btn-default-medium-focus-over-corners.gif), sides:url(images/btn/btn-default-medium-focus-over-sides.gif), frame-bg:url(images/btn/btn-default-medium-focus-over-fbg.gif)" !important
}

.x-cmd-slicer.x-btn-pressed.x-btn-default-medium:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url(images/btn/btn-default-medium-pressed-corners.gif), sides:url(images/btn/btn-default-medium-pressed-sides.gif), frame-bg:url(images/btn/btn-default-medium-pressed-fbg.gif)" !important
}

.x-cmd-slicer.x-btn-focus.x-btn-pressed.x-btn-default-medium:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url(images/btn/btn-default-medium-focus-pressed-corners.gif), sides:url(images/btn/btn-default-medium-focus-pressed-sides.gif), frame-bg:url(images/btn/btn-default-medium-focus-pressed-fbg.gif)" !important
}

.x-cmd-slicer.x-btn-disabled.x-btn-default-medium:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url(images/btn/btn-default-medium-disabled-corners.gif), sides:url(images/btn/btn-default-medium-disabled-sides.gif), frame-bg:url(images/btn/btn-default-medium-disabled-fbg.gif)" !important
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
    background-image: url(images/btn/btn-default-large-fbg.gif);
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
    background-image: url(images/btn/btn-default-large-corners.gif)
}

.x-btn-default-large-ml, .x-btn-default-large-mr {
    background-image: url(images/btn/btn-default-large-sides.gif)
}

.x-btn-default-large-mc {
    padding: 1px 1px 1px 1px
}

.x-cmd-slicer.x-btn-default-large:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, frame-bg:url(images/btn/btn-default-large-fbg.gif), corners:url(images/btn/btn-default-large-corners.gif), sides:url(images/btn/btn-default-large-sides.gif)" !important
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
    background-image: url(images/button/arrow.gif);
    padding-right: 8px
}

.x-btn-wrap-default-large.x-btn-arrow-bottom:after {
    height: 8px;
    background-image: url(images/button/arrow.gif)
}

.x-btn-wrap-default-large.x-btn-split-right:after {
    width: 14px;
    background-image: url(images/button/s-arrow.gif);
    padding-right: 14px
}

.x-btn-wrap-default-large.x-btn-split-bottom:after {
    height: 14px;
    background-image: url(images/button/s-arrow-b.gif)
}

.x-btn-over > .x-btn-wrap-default-large.x-btn-split-right:after {
    background-image: url(images/button/s-arrow-o.gif)
}

.x-btn-over > .x-btn-wrap-default-large.x-btn-split-bottom:after {
    background-image: url(images/button/s-arrow-bo.gif)
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
    background-image: url(images/btn/btn-default-large-focus-corners.gif)
}

.x-btn-focus .x-btn-default-large-ml, .x-btn-focus .x-btn-default-large-mr {
    background-image: url(images/btn/btn-default-large-focus-sides.gif)
}

.x-btn-focus .x-btn-default-large-mc {
    background-color: #fff;
    background-image: url(images/btn/btn-default-large-focus-fbg.gif)
}

.x-btn-over .x-btn-default-large-tl, .x-btn-over .x-btn-default-large-bl, .x-btn-over .x-btn-default-large-tr, .x-btn-over .x-btn-default-large-br, .x-btn-over .x-btn-default-large-tc, .x-btn-over .x-btn-default-large-bc {
    background-image: url(images/btn/btn-default-large-over-corners.gif)
}

.x-btn-over .x-btn-default-large-ml, .x-btn-over .x-btn-default-large-mr {
    background-image: url(images/btn/btn-default-large-over-sides.gif)
}

.x-btn-over .x-btn-default-large-mc {
    background-color: #e4f3ff;
    background-image: url(images/btn/btn-default-large-over-fbg.gif)
}

.x-btn-focus.x-btn-over .x-btn-default-large-tl, .x-btn-focus.x-btn-over .x-btn-default-large-bl, .x-btn-focus.x-btn-over .x-btn-default-large-tr, .x-btn-focus.x-btn-over .x-btn-default-large-br, .x-btn-focus.x-btn-over .x-btn-default-large-tc, .x-btn-focus.x-btn-over .x-btn-default-large-bc {
    background-image: url(images/btn/btn-default-large-focus-over-corners.gif)
}

.x-btn-focus.x-btn-over .x-btn-default-large-ml, .x-btn-focus.x-btn-over .x-btn-default-large-mr {
    background-image: url(images/btn/btn-default-large-focus-over-sides.gif)
}

.x-btn-focus.x-btn-over .x-btn-default-large-mc {
    background-color: #e4f3ff;
    background-image: url(images/btn/btn-default-large-focus-over-fbg.gif)
}

.x-btn.x-btn-menu-active .x-btn-default-large-tl, .x-btn.x-btn-menu-active .x-btn-default-large-bl, .x-btn.x-btn-menu-active .x-btn-default-large-tr, .x-btn.x-btn-menu-active .x-btn-default-large-br, .x-btn.x-btn-menu-active .x-btn-default-large-tc, .x-btn.x-btn-menu-active .x-btn-default-large-bc, .x-btn.x-btn-pressed .x-btn-default-large-tl, .x-btn.x-btn-pressed .x-btn-default-large-bl, .x-btn.x-btn-pressed .x-btn-default-large-tr, .x-btn.x-btn-pressed .x-btn-default-large-br, .x-btn.x-btn-pressed .x-btn-default-large-tc, .x-btn.x-btn-pressed .x-btn-default-large-bc {
    background-image: url(images/btn/btn-default-large-pressed-corners.gif)
}

.x-btn.x-btn-menu-active .x-btn-default-large-ml, .x-btn.x-btn-menu-active .x-btn-default-large-mr, .x-btn.x-btn-pressed .x-btn-default-large-ml, .x-btn.x-btn-pressed .x-btn-default-large-mr {
    background-image: url(images/btn/btn-default-large-pressed-sides.gif)
}

.x-btn.x-btn-menu-active .x-btn-default-large-mc, .x-btn.x-btn-pressed .x-btn-default-large-mc {
    background-color: #b6cbe4;
    background-image: url(images/btn/btn-default-large-pressed-fbg.gif)
}

.x-btn-focus.x-btn-menu-active .x-btn-default-large-tl, .x-btn-focus.x-btn-menu-active .x-btn-default-large-bl, .x-btn-focus.x-btn-menu-active .x-btn-default-large-tr, .x-btn-focus.x-btn-menu-active .x-btn-default-large-br, .x-btn-focus.x-btn-menu-active .x-btn-default-large-tc, .x-btn-focus.x-btn-menu-active .x-btn-default-large-bc, .x-btn-focus.x-btn-pressed .x-btn-default-large-tl, .x-btn-focus.x-btn-pressed .x-btn-default-large-bl, .x-btn-focus.x-btn-pressed .x-btn-default-large-tr, .x-btn-focus.x-btn-pressed .x-btn-default-large-br, .x-btn-focus.x-btn-pressed .x-btn-default-large-tc, .x-btn-focus.x-btn-pressed .x-btn-default-large-bc {
    background-image: url(images/btn/btn-default-large-focus-pressed-corners.gif)
}

.x-btn-focus.x-btn-menu-active .x-btn-default-large-ml, .x-btn-focus.x-btn-menu-active .x-btn-default-large-mr, .x-btn-focus.x-btn-pressed .x-btn-default-large-ml, .x-btn-focus.x-btn-pressed .x-btn-default-large-mr {
    background-image: url(images/btn/btn-default-large-focus-pressed-sides.gif)
}

.x-btn-focus.x-btn-menu-active .x-btn-default-large-mc, .x-btn-focus.x-btn-pressed .x-btn-default-large-mc {
    background-color: #b6cbe4;
    background-image: url(images/btn/btn-default-large-focus-pressed-fbg.gif)
}

.x-btn.x-btn-disabled .x-btn-default-large-tl, .x-btn.x-btn-disabled .x-btn-default-large-bl, .x-btn.x-btn-disabled .x-btn-default-large-tr, .x-btn.x-btn-disabled .x-btn-default-large-br, .x-btn.x-btn-disabled .x-btn-default-large-tc, .x-btn.x-btn-disabled .x-btn-default-large-bc {
    background-image: url(images/btn/btn-default-large-disabled-corners.gif)
}

.x-btn.x-btn-disabled .x-btn-default-large-ml, .x-btn.x-btn-disabled .x-btn-default-large-mr {
    background-image: url(images/btn/btn-default-large-disabled-sides.gif)
}

.x-btn.x-btn-disabled .x-btn-default-large-mc {
    background-color: #f7f7f7;
    background-image: url(images/btn/btn-default-large-disabled-fbg.gif)
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
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url(images/btn/btn-default-large-focus-corners.gif), sides:url(images/btn/btn-default-large-focus-sides.gif), frame-bg:url(images/btn/btn-default-large-focus-fbg.gif)" !important
}

.x-cmd-slicer.x-btn-over.x-btn-default-large:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url(images/btn/btn-default-large-over-corners.gif), sides:url(images/btn/btn-default-large-over-sides.gif), frame-bg:url(images/btn/btn-default-large-over-fbg.gif)" !important
}

.x-cmd-slicer.x-btn-focus.x-btn-over.x-btn-default-large:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url(images/btn/btn-default-large-focus-over-corners.gif), sides:url(images/btn/btn-default-large-focus-over-sides.gif), frame-bg:url(images/btn/btn-default-large-focus-over-fbg.gif)" !important
}

.x-cmd-slicer.x-btn-pressed.x-btn-default-large:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url(images/btn/btn-default-large-pressed-corners.gif), sides:url(images/btn/btn-default-large-pressed-sides.gif), frame-bg:url(images/btn/btn-default-large-pressed-fbg.gif)" !important
}

.x-cmd-slicer.x-btn-focus.x-btn-pressed.x-btn-default-large:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url(images/btn/btn-default-large-focus-pressed-corners.gif), sides:url(images/btn/btn-default-large-focus-pressed-sides.gif), frame-bg:url(images/btn/btn-default-large-focus-pressed-fbg.gif)" !important
}

.x-cmd-slicer.x-btn-disabled.x-btn-default-large:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url(images/btn/btn-default-large-disabled-corners.gif), sides:url(images/btn/btn-default-large-disabled-sides.gif), frame-bg:url(images/btn/btn-default-large-disabled-fbg.gif)" !important
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
    background-image: url(images/button/arrow.gif);
    padding-right: 8px
}

.x-btn-wrap-default-toolbar-small.x-btn-arrow-bottom:after {
    height: 8px;
    background-image: url(images/button/arrow.gif)
}

.x-btn-wrap-default-toolbar-small.x-btn-split-right:after {
    width: 14px;
    background-image: url(images/button/s-arrow-noline.gif);
    padding-right: 14px
}

.x-btn-wrap-default-toolbar-small.x-btn-split-bottom:after {
    height: 14px;
    background-image: url(images/button/s-arrow-b-noline.gif)
}

.x-btn-over > .x-btn-wrap-default-toolbar-small.x-btn-split-right:after {
    background-image: url(images/button/s-arrow-o.gif)
}

.x-btn-over > .x-btn-wrap-default-toolbar-small.x-btn-split-bottom:after {
    background-image: url(images/button/s-arrow-bo.gif)
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
    background-image: url(images/btn/btn-default-toolbar-small-over-corners.gif)
}

.x-btn-over .x-btn-default-toolbar-small-ml, .x-btn-over .x-btn-default-toolbar-small-mr {
    background-image: url(images/btn/btn-default-toolbar-small-over-sides.gif)
}

.x-btn-over .x-btn-default-toolbar-small-mc {
    background-color: #dbeeff;
    background-image: url(images/btn/btn-default-toolbar-small-over-fbg.gif)
}

.x-btn-focus.x-btn-over .x-btn-default-toolbar-small-tl, .x-btn-focus.x-btn-over .x-btn-default-toolbar-small-bl, .x-btn-focus.x-btn-over .x-btn-default-toolbar-small-tr, .x-btn-focus.x-btn-over .x-btn-default-toolbar-small-br, .x-btn-focus.x-btn-over .x-btn-default-toolbar-small-tc, .x-btn-focus.x-btn-over .x-btn-default-toolbar-small-bc {
    background-image: url(images/btn/btn-default-toolbar-small-focus-over-corners.gif)
}

.x-btn-focus.x-btn-over .x-btn-default-toolbar-small-ml, .x-btn-focus.x-btn-over .x-btn-default-toolbar-small-mr {
    background-image: url(images/btn/btn-default-toolbar-small-focus-over-sides.gif)
}

.x-btn-focus.x-btn-over .x-btn-default-toolbar-small-mc {
    background-color: #dbeeff;
    background-image: url(images/btn/btn-default-toolbar-small-focus-over-fbg.gif)
}

.x-btn.x-btn-menu-active .x-btn-default-toolbar-small-tl, .x-btn.x-btn-menu-active .x-btn-default-toolbar-small-bl, .x-btn.x-btn-menu-active .x-btn-default-toolbar-small-tr, .x-btn.x-btn-menu-active .x-btn-default-toolbar-small-br, .x-btn.x-btn-menu-active .x-btn-default-toolbar-small-tc, .x-btn.x-btn-menu-active .x-btn-default-toolbar-small-bc, .x-btn.x-btn-pressed .x-btn-default-toolbar-small-tl, .x-btn.x-btn-pressed .x-btn-default-toolbar-small-bl, .x-btn.x-btn-pressed .x-btn-default-toolbar-small-tr, .x-btn.x-btn-pressed .x-btn-default-toolbar-small-br, .x-btn.x-btn-pressed .x-btn-default-toolbar-small-tc, .x-btn.x-btn-pressed .x-btn-default-toolbar-small-bc {
    background-image: url(images/btn/btn-default-toolbar-small-pressed-corners.gif)
}

.x-btn.x-btn-menu-active .x-btn-default-toolbar-small-ml, .x-btn.x-btn-menu-active .x-btn-default-toolbar-small-mr, .x-btn.x-btn-pressed .x-btn-default-toolbar-small-ml, .x-btn.x-btn-pressed .x-btn-default-toolbar-small-mr {
    background-image: url(images/btn/btn-default-toolbar-small-pressed-sides.gif)
}

.x-btn.x-btn-menu-active .x-btn-default-toolbar-small-mc, .x-btn.x-btn-pressed .x-btn-default-toolbar-small-mc {
    background-color: #bccfe5;
    background-image: url(images/btn/btn-default-toolbar-small-pressed-fbg.gif)
}

.x-btn-focus.x-btn-menu-active .x-btn-default-toolbar-small-tl, .x-btn-focus.x-btn-menu-active .x-btn-default-toolbar-small-bl, .x-btn-focus.x-btn-menu-active .x-btn-default-toolbar-small-tr, .x-btn-focus.x-btn-menu-active .x-btn-default-toolbar-small-br, .x-btn-focus.x-btn-menu-active .x-btn-default-toolbar-small-tc, .x-btn-focus.x-btn-menu-active .x-btn-default-toolbar-small-bc, .x-btn-focus.x-btn-pressed .x-btn-default-toolbar-small-tl, .x-btn-focus.x-btn-pressed .x-btn-default-toolbar-small-bl, .x-btn-focus.x-btn-pressed .x-btn-default-toolbar-small-tr, .x-btn-focus.x-btn-pressed .x-btn-default-toolbar-small-br, .x-btn-focus.x-btn-pressed .x-btn-default-toolbar-small-tc, .x-btn-focus.x-btn-pressed .x-btn-default-toolbar-small-bc {
    background-image: url(images/btn/btn-default-toolbar-small-focus-pressed-corners.gif)
}

.x-btn-focus.x-btn-menu-active .x-btn-default-toolbar-small-ml, .x-btn-focus.x-btn-menu-active .x-btn-default-toolbar-small-mr, .x-btn-focus.x-btn-pressed .x-btn-default-toolbar-small-ml, .x-btn-focus.x-btn-pressed .x-btn-default-toolbar-small-mr {
    background-image: url(images/btn/btn-default-toolbar-small-focus-pressed-sides.gif)
}

.x-btn-focus.x-btn-menu-active .x-btn-default-toolbar-small-mc, .x-btn-focus.x-btn-pressed .x-btn-default-toolbar-small-mc {
    background-color: #bccfe5;
    background-image: url(images/btn/btn-default-toolbar-small-focus-pressed-fbg.gif)
}

.x-btn.x-btn-disabled .x-btn-default-toolbar-small-tl, .x-btn.x-btn-disabled .x-btn-default-toolbar-small-bl, .x-btn.x-btn-disabled .x-btn-default-toolbar-small-tr, .x-btn.x-btn-disabled .x-btn-default-toolbar-small-br, .x-btn.x-btn-disabled .x-btn-default-toolbar-small-tc, .x-btn.x-btn-disabled .x-btn-default-toolbar-small-bc {
    background-image: url(images/btn/btn-default-toolbar-small-disabled-corners.gif)
}

.x-btn.x-btn-disabled .x-btn-default-toolbar-small-ml, .x-btn.x-btn-disabled .x-btn-default-toolbar-small-mr {
    background-image: url(images/btn/btn-default-toolbar-small-disabled-sides.gif)
}

.x-btn.x-btn-disabled .x-btn-default-toolbar-small-mc {
    background-color: transparent;
    background-image: url(images/btn/btn-default-toolbar-small-disabled-fbg.gif)
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
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url(images/btn/btn-default-toolbar-small-over-corners.gif), sides:url(images/btn/btn-default-toolbar-small-over-sides.gif), frame-bg:url(images/btn/btn-default-toolbar-small-over-fbg.gif)" !important
}

.x-cmd-slicer.x-btn-focus.x-btn-over.x-btn-default-toolbar-small:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url(images/btn/btn-default-toolbar-small-focus-over-corners.gif), sides:url(images/btn/btn-default-toolbar-small-focus-over-sides.gif), frame-bg:url(images/btn/btn-default-toolbar-small-focus-over-fbg.gif)" !important
}

.x-cmd-slicer.x-btn-pressed.x-btn-default-toolbar-small:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url(images/btn/btn-default-toolbar-small-pressed-corners.gif), sides:url(images/btn/btn-default-toolbar-small-pressed-sides.gif), frame-bg:url(images/btn/btn-default-toolbar-small-pressed-fbg.gif)" !important
}

.x-cmd-slicer.x-btn-focus.x-btn-pressed.x-btn-default-toolbar-small:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url(images/btn/btn-default-toolbar-small-focus-pressed-corners.gif), sides:url(images/btn/btn-default-toolbar-small-focus-pressed-sides.gif), frame-bg:url(images/btn/btn-default-toolbar-small-focus-pressed-fbg.gif)" !important
}

.x-cmd-slicer.x-btn-disabled.x-btn-default-toolbar-small:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url(images/btn/btn-default-toolbar-small-disabled-corners.gif), sides:url(images/btn/btn-default-toolbar-small-disabled-sides.gif), frame-bg:url(images/btn/btn-default-toolbar-small-disabled-fbg.gif)" !important
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
    background-image: url(images/button/arrow.gif);
    padding-right: 8px
}

.x-btn-wrap-default-toolbar-medium.x-btn-arrow-bottom:after {
    height: 8px;
    background-image: url(images/button/arrow.gif)
}

.x-btn-wrap-default-toolbar-medium.x-btn-split-right:after {
    width: 14px;
    background-image: url(images/button/s-arrow-noline.gif);
    padding-right: 14px
}

.x-btn-wrap-default-toolbar-medium.x-btn-split-bottom:after {
    height: 14px;
    background-image: url(images/button/s-arrow-b-noline.gif)
}

.x-btn-over > .x-btn-wrap-default-toolbar-medium.x-btn-split-right:after {
    background-image: url(images/button/s-arrow-o.gif)
}

.x-btn-over > .x-btn-wrap-default-toolbar-medium.x-btn-split-bottom:after {
    background-image: url(images/button/s-arrow-bo.gif)
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
    background-image: url(images/btn/btn-default-toolbar-medium-over-corners.gif)
}

.x-btn-over .x-btn-default-toolbar-medium-ml, .x-btn-over .x-btn-default-toolbar-medium-mr {
    background-image: url(images/btn/btn-default-toolbar-medium-over-sides.gif)
}

.x-btn-over .x-btn-default-toolbar-medium-mc {
    background-color: #dbeeff;
    background-image: url(images/btn/btn-default-toolbar-medium-over-fbg.gif)
}

.x-btn-focus.x-btn-over .x-btn-default-toolbar-medium-tl, .x-btn-focus.x-btn-over .x-btn-default-toolbar-medium-bl, .x-btn-focus.x-btn-over .x-btn-default-toolbar-medium-tr, .x-btn-focus.x-btn-over .x-btn-default-toolbar-medium-br, .x-btn-focus.x-btn-over .x-btn-default-toolbar-medium-tc, .x-btn-focus.x-btn-over .x-btn-default-toolbar-medium-bc {
    background-image: url(images/btn/btn-default-toolbar-medium-focus-over-corners.gif)
}

.x-btn-focus.x-btn-over .x-btn-default-toolbar-medium-ml, .x-btn-focus.x-btn-over .x-btn-default-toolbar-medium-mr {
    background-image: url(images/btn/btn-default-toolbar-medium-focus-over-sides.gif)
}

.x-btn-focus.x-btn-over .x-btn-default-toolbar-medium-mc {
    background-color: #dbeeff;
    background-image: url(images/btn/btn-default-toolbar-medium-focus-over-fbg.gif)
}

.x-btn.x-btn-menu-active .x-btn-default-toolbar-medium-tl, .x-btn.x-btn-menu-active .x-btn-default-toolbar-medium-bl, .x-btn.x-btn-menu-active .x-btn-default-toolbar-medium-tr, .x-btn.x-btn-menu-active .x-btn-default-toolbar-medium-br, .x-btn.x-btn-menu-active .x-btn-default-toolbar-medium-tc, .x-btn.x-btn-menu-active .x-btn-default-toolbar-medium-bc, .x-btn.x-btn-pressed .x-btn-default-toolbar-medium-tl, .x-btn.x-btn-pressed .x-btn-default-toolbar-medium-bl, .x-btn.x-btn-pressed .x-btn-default-toolbar-medium-tr, .x-btn.x-btn-pressed .x-btn-default-toolbar-medium-br, .x-btn.x-btn-pressed .x-btn-default-toolbar-medium-tc, .x-btn.x-btn-pressed .x-btn-default-toolbar-medium-bc {
    background-image: url(images/btn/btn-default-toolbar-medium-pressed-corners.gif)
}

.x-btn.x-btn-menu-active .x-btn-default-toolbar-medium-ml, .x-btn.x-btn-menu-active .x-btn-default-toolbar-medium-mr, .x-btn.x-btn-pressed .x-btn-default-toolbar-medium-ml, .x-btn.x-btn-pressed .x-btn-default-toolbar-medium-mr {
    background-image: url(images/btn/btn-default-toolbar-medium-pressed-sides.gif)
}

.x-btn.x-btn-menu-active .x-btn-default-toolbar-medium-mc, .x-btn.x-btn-pressed .x-btn-default-toolbar-medium-mc {
    background-color: #bccfe5;
    background-image: url(images/btn/btn-default-toolbar-medium-pressed-fbg.gif)
}

.x-btn-focus.x-btn-menu-active .x-btn-default-toolbar-medium-tl, .x-btn-focus.x-btn-menu-active .x-btn-default-toolbar-medium-bl, .x-btn-focus.x-btn-menu-active .x-btn-default-toolbar-medium-tr, .x-btn-focus.x-btn-menu-active .x-btn-default-toolbar-medium-br, .x-btn-focus.x-btn-menu-active .x-btn-default-toolbar-medium-tc, .x-btn-focus.x-btn-menu-active .x-btn-default-toolbar-medium-bc, .x-btn-focus.x-btn-pressed .x-btn-default-toolbar-medium-tl, .x-btn-focus.x-btn-pressed .x-btn-default-toolbar-medium-bl, .x-btn-focus.x-btn-pressed .x-btn-default-toolbar-medium-tr, .x-btn-focus.x-btn-pressed .x-btn-default-toolbar-medium-br, .x-btn-focus.x-btn-pressed .x-btn-default-toolbar-medium-tc, .x-btn-focus.x-btn-pressed .x-btn-default-toolbar-medium-bc {
    background-image: url(images/btn/btn-default-toolbar-medium-focus-pressed-corners.gif)
}

.x-btn-focus.x-btn-menu-active .x-btn-default-toolbar-medium-ml, .x-btn-focus.x-btn-menu-active .x-btn-default-toolbar-medium-mr, .x-btn-focus.x-btn-pressed .x-btn-default-toolbar-medium-ml, .x-btn-focus.x-btn-pressed .x-btn-default-toolbar-medium-mr {
    background-image: url(images/btn/btn-default-toolbar-medium-focus-pressed-sides.gif)
}

.x-btn-focus.x-btn-menu-active .x-btn-default-toolbar-medium-mc, .x-btn-focus.x-btn-pressed .x-btn-default-toolbar-medium-mc {
    background-color: #bccfe5;
    background-image: url(images/btn/btn-default-toolbar-medium-focus-pressed-fbg.gif)
}

.x-btn.x-btn-disabled .x-btn-default-toolbar-medium-tl, .x-btn.x-btn-disabled .x-btn-default-toolbar-medium-bl, .x-btn.x-btn-disabled .x-btn-default-toolbar-medium-tr, .x-btn.x-btn-disabled .x-btn-default-toolbar-medium-br, .x-btn.x-btn-disabled .x-btn-default-toolbar-medium-tc, .x-btn.x-btn-disabled .x-btn-default-toolbar-medium-bc {
    background-image: url(images/btn/btn-default-toolbar-medium-disabled-corners.gif)
}

.x-btn.x-btn-disabled .x-btn-default-toolbar-medium-ml, .x-btn.x-btn-disabled .x-btn-default-toolbar-medium-mr {
    background-image: url(images/btn/btn-default-toolbar-medium-disabled-sides.gif)
}

.x-btn.x-btn-disabled .x-btn-default-toolbar-medium-mc {
    background-color: transparent;
    background-image: url(images/btn/btn-default-toolbar-medium-disabled-fbg.gif)
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
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url(images/btn/btn-default-toolbar-medium-over-corners.gif), sides:url(images/btn/btn-default-toolbar-medium-over-sides.gif), frame-bg:url(images/btn/btn-default-toolbar-medium-over-fbg.gif)" !important
}

.x-cmd-slicer.x-btn-focus.x-btn-over.x-btn-default-toolbar-medium:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url(images/btn/btn-default-toolbar-medium-focus-over-corners.gif), sides:url(images/btn/btn-default-toolbar-medium-focus-over-sides.gif), frame-bg:url(images/btn/btn-default-toolbar-medium-focus-over-fbg.gif)" !important
}

.x-cmd-slicer.x-btn-pressed.x-btn-default-toolbar-medium:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url(images/btn/btn-default-toolbar-medium-pressed-corners.gif), sides:url(images/btn/btn-default-toolbar-medium-pressed-sides.gif), frame-bg:url(images/btn/btn-default-toolbar-medium-pressed-fbg.gif)" !important
}

.x-cmd-slicer.x-btn-focus.x-btn-pressed.x-btn-default-toolbar-medium:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url(images/btn/btn-default-toolbar-medium-focus-pressed-corners.gif), sides:url(images/btn/btn-default-toolbar-medium-focus-pressed-sides.gif), frame-bg:url(images/btn/btn-default-toolbar-medium-focus-pressed-fbg.gif)" !important
}

.x-cmd-slicer.x-btn-disabled.x-btn-default-toolbar-medium:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url(images/btn/btn-default-toolbar-medium-disabled-corners.gif), sides:url(images/btn/btn-default-toolbar-medium-disabled-sides.gif), frame-bg:url(images/btn/btn-default-toolbar-medium-disabled-fbg.gif)" !important
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
    background-image: url(images/button/arrow.gif);
    padding-right: 8px
}

.x-btn-wrap-default-toolbar-large.x-btn-arrow-bottom:after {
    height: 8px;
    background-image: url(images/button/arrow.gif)
}

.x-btn-wrap-default-toolbar-large.x-btn-split-right:after {
    width: 14px;
    background-image: url(images/button/s-arrow-noline.gif);
    padding-right: 14px
}

.x-btn-wrap-default-toolbar-large.x-btn-split-bottom:after {
    height: 14px;
    background-image: url(images/button/s-arrow-b-noline.gif)
}

.x-btn-over > .x-btn-wrap-default-toolbar-large.x-btn-split-right:after {
    background-image: url(images/button/s-arrow-o.gif)
}

.x-btn-over > .x-btn-wrap-default-toolbar-large.x-btn-split-bottom:after {
    background-image: url(images/button/s-arrow-bo.gif)
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
    background-image: url(images/btn/btn-default-toolbar-large-over-corners.gif)
}

.x-btn-over .x-btn-default-toolbar-large-ml, .x-btn-over .x-btn-default-toolbar-large-mr {
    background-image: url(images/btn/btn-default-toolbar-large-over-sides.gif)
}

.x-btn-over .x-btn-default-toolbar-large-mc {
    background-color: #dbeeff;
    background-image: url(images/btn/btn-default-toolbar-large-over-fbg.gif)
}

.x-btn-focus.x-btn-over .x-btn-default-toolbar-large-tl, .x-btn-focus.x-btn-over .x-btn-default-toolbar-large-bl, .x-btn-focus.x-btn-over .x-btn-default-toolbar-large-tr, .x-btn-focus.x-btn-over .x-btn-default-toolbar-large-br, .x-btn-focus.x-btn-over .x-btn-default-toolbar-large-tc, .x-btn-focus.x-btn-over .x-btn-default-toolbar-large-bc {
    background-image: url(images/btn/btn-default-toolbar-large-focus-over-corners.gif)
}

.x-btn-focus.x-btn-over .x-btn-default-toolbar-large-ml, .x-btn-focus.x-btn-over .x-btn-default-toolbar-large-mr {
    background-image: url(images/btn/btn-default-toolbar-large-focus-over-sides.gif)
}

.x-btn-focus.x-btn-over .x-btn-default-toolbar-large-mc {
    background-color: #dbeeff;
    background-image: url(images/btn/btn-default-toolbar-large-focus-over-fbg.gif)
}

.x-btn.x-btn-menu-active .x-btn-default-toolbar-large-tl, .x-btn.x-btn-menu-active .x-btn-default-toolbar-large-bl, .x-btn.x-btn-menu-active .x-btn-default-toolbar-large-tr, .x-btn.x-btn-menu-active .x-btn-default-toolbar-large-br, .x-btn.x-btn-menu-active .x-btn-default-toolbar-large-tc, .x-btn.x-btn-menu-active .x-btn-default-toolbar-large-bc, .x-btn.x-btn-pressed .x-btn-default-toolbar-large-tl, .x-btn.x-btn-pressed .x-btn-default-toolbar-large-bl, .x-btn.x-btn-pressed .x-btn-default-toolbar-large-tr, .x-btn.x-btn-pressed .x-btn-default-toolbar-large-br, .x-btn.x-btn-pressed .x-btn-default-toolbar-large-tc, .x-btn.x-btn-pressed .x-btn-default-toolbar-large-bc {
    background-image: url(images/btn/btn-default-toolbar-large-pressed-corners.gif)
}

.x-btn.x-btn-menu-active .x-btn-default-toolbar-large-ml, .x-btn.x-btn-menu-active .x-btn-default-toolbar-large-mr, .x-btn.x-btn-pressed .x-btn-default-toolbar-large-ml, .x-btn.x-btn-pressed .x-btn-default-toolbar-large-mr {
    background-image: url(images/btn/btn-default-toolbar-large-pressed-sides.gif)
}

.x-btn.x-btn-menu-active .x-btn-default-toolbar-large-mc, .x-btn.x-btn-pressed .x-btn-default-toolbar-large-mc {
    background-color: #bccfe5;
    background-image: url(images/btn/btn-default-toolbar-large-pressed-fbg.gif)
}

.x-btn-focus.x-btn-menu-active .x-btn-default-toolbar-large-tl, .x-btn-focus.x-btn-menu-active .x-btn-default-toolbar-large-bl, .x-btn-focus.x-btn-menu-active .x-btn-default-toolbar-large-tr, .x-btn-focus.x-btn-menu-active .x-btn-default-toolbar-large-br, .x-btn-focus.x-btn-menu-active .x-btn-default-toolbar-large-tc, .x-btn-focus.x-btn-menu-active .x-btn-default-toolbar-large-bc, .x-btn-focus.x-btn-pressed .x-btn-default-toolbar-large-tl, .x-btn-focus.x-btn-pressed .x-btn-default-toolbar-large-bl, .x-btn-focus.x-btn-pressed .x-btn-default-toolbar-large-tr, .x-btn-focus.x-btn-pressed .x-btn-default-toolbar-large-br, .x-btn-focus.x-btn-pressed .x-btn-default-toolbar-large-tc, .x-btn-focus.x-btn-pressed .x-btn-default-toolbar-large-bc {
    background-image: url(images/btn/btn-default-toolbar-large-focus-pressed-corners.gif)
}

.x-btn-focus.x-btn-menu-active .x-btn-default-toolbar-large-ml, .x-btn-focus.x-btn-menu-active .x-btn-default-toolbar-large-mr, .x-btn-focus.x-btn-pressed .x-btn-default-toolbar-large-ml, .x-btn-focus.x-btn-pressed .x-btn-default-toolbar-large-mr {
    background-image: url(images/btn/btn-default-toolbar-large-focus-pressed-sides.gif)
}

.x-btn-focus.x-btn-menu-active .x-btn-default-toolbar-large-mc, .x-btn-focus.x-btn-pressed .x-btn-default-toolbar-large-mc {
    background-color: #bccfe5;
    background-image: url(images/btn/btn-default-toolbar-large-focus-pressed-fbg.gif)
}

.x-btn.x-btn-disabled .x-btn-default-toolbar-large-tl, .x-btn.x-btn-disabled .x-btn-default-toolbar-large-bl, .x-btn.x-btn-disabled .x-btn-default-toolbar-large-tr, .x-btn.x-btn-disabled .x-btn-default-toolbar-large-br, .x-btn.x-btn-disabled .x-btn-default-toolbar-large-tc, .x-btn.x-btn-disabled .x-btn-default-toolbar-large-bc {
    background-image: url(images/btn/btn-default-toolbar-large-disabled-corners.gif)
}

.x-btn.x-btn-disabled .x-btn-default-toolbar-large-ml, .x-btn.x-btn-disabled .x-btn-default-toolbar-large-mr {
    background-image: url(images/btn/btn-default-toolbar-large-disabled-sides.gif)
}

.x-btn.x-btn-disabled .x-btn-default-toolbar-large-mc {
    background-color: transparent;
    background-image: url(images/btn/btn-default-toolbar-large-disabled-fbg.gif)
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
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url(images/btn/btn-default-toolbar-large-over-corners.gif), sides:url(images/btn/btn-default-toolbar-large-over-sides.gif), frame-bg:url(images/btn/btn-default-toolbar-large-over-fbg.gif)" !important
}

.x-cmd-slicer.x-btn-focus.x-btn-over.x-btn-default-toolbar-large:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url(images/btn/btn-default-toolbar-large-focus-over-corners.gif), sides:url(images/btn/btn-default-toolbar-large-focus-over-sides.gif), frame-bg:url(images/btn/btn-default-toolbar-large-focus-over-fbg.gif)" !important
}

.x-cmd-slicer.x-btn-pressed.x-btn-default-toolbar-large:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url(images/btn/btn-default-toolbar-large-pressed-corners.gif), sides:url(images/btn/btn-default-toolbar-large-pressed-sides.gif), frame-bg:url(images/btn/btn-default-toolbar-large-pressed-fbg.gif)" !important
}

.x-cmd-slicer.x-btn-focus.x-btn-pressed.x-btn-default-toolbar-large:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url(images/btn/btn-default-toolbar-large-focus-pressed-corners.gif), sides:url(images/btn/btn-default-toolbar-large-focus-pressed-sides.gif), frame-bg:url(images/btn/btn-default-toolbar-large-focus-pressed-fbg.gif)" !important
}

.x-cmd-slicer.x-btn-disabled.x-btn-default-toolbar-large:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:3px 3px 3px 3px, corners:url(images/btn/btn-default-toolbar-large-disabled-corners.gif), sides:url(images/btn/btn-default-toolbar-large-disabled-sides.gif), frame-bg:url(images/btn/btn-default-toolbar-large-disabled-fbg.gif)" !important
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
    background-image: url(images/tools/tool-sprites.gif)
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
    background-image: url(images/util/splitter/mini-left.gif)
}

.x-layout-split-right {
    background-image: url(images/util/splitter/mini-right.gif)
}

.x-layout-split-top {
    background-image: url(images/util/splitter/mini-top.gif)
}

.x-layout-split-bottom {
    background-image: url(images/util/splitter/mini-bottom.gif)
}

.x-splitter-collapsed .x-layout-split-left {
    background-image: url(images/util/splitter/mini-right.gif)
}

.x-splitter-collapsed .x-layout-split-right {
    background-image: url(images/util/splitter/mini-left.gif)
}

.x-splitter-collapsed .x-layout-split-top {
    background-image: url(images/util/splitter/mini-bottom.gif)
}

.x-splitter-collapsed .x-layout-split-bottom {
    background-image: url(images/util/splitter/mini-top.gif)
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
    background-image: url(images/toolbar/toolbar-default-bg.gif) !important;
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
    background-image: url(images/toolbar/default-scroll-left.gif);
    background-position: -14px 0
}

.x-box-scroller-toolbar-default.x-box-scroller-left.x-box-scroller-hover {
    background-position: 0 0
}

.x-box-scroller-toolbar-default.x-box-scroller-right {
    margin-left: 0;
    margin-right: 0;
    margin-bottom: 0;
    background-image: url(images/toolbar/default-scroll-right.gif);
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
    background-image: url(images/toolbar/default-scroll-top.gif);
    background-position: 0 -5px
}

.x-box-scroller-toolbar-default.x-box-scroller-top.x-box-scroller-hover {
    background-position: 0 0
}

.x-box-scroller-toolbar-default.x-box-scroller-bottom {
    margin-top: 5px;
    margin-right: 0;
    margin-bottom: 5px;
    background-image: url(images/toolbar/default-scroll-bottom.gif);
    background-position: 0 0
}

.x-box-scroller-toolbar-default.x-box-scroller-bottom.x-box-scroller-hover {
    background-position: 0 -5px
}

.x-ie8 .x-box-scroller-toolbar-default {
    background-color: #d3e1f1
}

.x-toolbar-more-icon {
    background-image: url(images/toolbar/default-more.gif)
}

.x-cmd-slicer.x-toolbar-default:before {
    display: none;
    content: "x-slicer:, bg:url(images/toolbar/toolbar-default-bg.gif), stretch:bottom" !important
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
    background-image: url(images/toolbar/footer-scroll-left.gif);
    background-position: -14px 0
}

.x-box-scroller-toolbar-footer.x-box-scroller-left.x-box-scroller-hover {
    background-position: 0 0
}

.x-box-scroller-toolbar-footer.x-box-scroller-right {
    margin-left: 0;
    margin-right: 0;
    margin-bottom: 0;
    background-image: url(images/toolbar/footer-scroll-right.gif);
    background-position: 0 0
}

.x-box-scroller-toolbar-footer.x-box-scroller-right.x-box-scroller-hover {
    background-position: -14px 0
}

.x-ie8 .x-box-scroller-toolbar-footer {
    background-color: transparent
}

.x-toolbar-more-icon {
    background-image: url(images/toolbar/footer-more.gif)
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
    background-image: url(images/dd/drop-yes.gif)
}

.x-dd-drop-ok-add .x-dd-drop-icon {
    background-image: url(images/dd/drop-add.gif)
}

.x-dd-drop-nodrop div.x-dd-drop-icon {
    background-image: url(images/dd/drop-no.gif)
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
    background: url(images/panel-header/panel-header-default-top-bg.gif)
}

.x-nlg .x-panel-header-default-bottom {
    background: url(images/panel-header/panel-header-default-bottom-bg.gif) bottom left
}

.x-nlg .x-panel-header-default-left {
    background: url(images/panel-header/panel-header-default-left-bg.gif) top left
}

.x-nlg .x-panel-header-default-right {
    background: url(images/panel-header/panel-header-default-right-bg.gif) top right
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
    content: "x-slicer:, bg:url(images/panel-header/panel-header-default-top-bg.gif), stretch:bottom" !important
}

.x-cmd-slicer.x-panel-header-default-bottom:before {
    display: none;
    content: "x-slicer:, bg:url(images/panel-header/panel-header-default-bottom-bg.gif), stretch:top" !important
}

.x-cmd-slicer.x-panel-header-default-left:before {
    display: none;
    content: "x-slicer:, bg:url(images/panel-header/panel-header-default-left-bg.gif), stretch:right" !important
}

.x-cmd-slicer.x-panel-header-default-right:before {
    display: none;
    content: "x-slicer:, bg:url(images/panel-header/panel-header-default-right-bg.gif), stretch:left" !important
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
    background-image: url(images/panel/panel-default-framed-corners.gif)
}

.x-panel-default-framed-ml, .x-panel-default-framed-mr {
    background-image: url(images/panel/panel-default-framed-sides.gif);
    background-repeat: repeat-y
}

.x-panel-default-framed-mc {
    padding: 1px 1px 1px 1px
}

.x-cmd-slicer.x-panel-default-framed:before {
    display: none;
    content: "x-slicer:, frame:4px 4px 4px 4px, corners:url(images/panel/panel-default-framed-corners.gif), sides:url(images/panel/panel-default-framed-sides.gif)" !important
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
    background-image: url(images/panel-header/panel-header-default-framed-top-fbg.gif);
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
    background-image: url(images/panel-header/panel-header-default-framed-top-corners.gif)
}

.x-panel-header-default-framed-top-ml, .x-panel-header-default-framed-top-mr {
    background-image: url(images/panel-header/panel-header-default-framed-top-sides.gif)
}

.x-panel-header-default-framed-top-mc {
    padding: 2px 2px 5px 2px
}

.x-cmd-slicer.x-panel-header-default-framed-top:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:4px 4px 0 4px, frame-bg:url(images/panel-header/panel-header-default-framed-top-fbg.gif), corners:url(images/panel-header/panel-header-default-framed-top-corners.gif), sides:url(images/panel-header/panel-header-default-framed-top-sides.gif)" !important
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
    background-image: url(images/panel-header/panel-header-default-framed-right-fbg.gif);
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
    background-image: url(images/panel-header/panel-header-default-framed-right-corners.gif)
}

.x-panel-header-default-framed-right-tc, .x-panel-header-default-framed-right-bc {
    background-image: url(images/panel-header/panel-header-default-framed-right-sides.gif);
    background-repeat: repeat-x
}

.x-panel-header-default-framed-right-mc {
    padding: 2px 2px 2px 5px
}

.x-cmd-slicer.x-panel-header-default-framed-right:before {
    display: none;
    content: "x-slicer:, stretch:left, frame:4px 4px 4px 0, frame-bg:url(images/panel-header/panel-header-default-framed-right-fbg.gif), corners:url(images/panel-header/panel-header-default-framed-right-corners.gif), sides:url(images/panel-header/panel-header-default-framed-right-sides.gif)" !important
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
    background-image: url(images/panel-header/panel-header-default-framed-bottom-fbg.gif);
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
    background-image: url(images/panel-header/panel-header-default-framed-bottom-corners.gif)
}

.x-panel-header-default-framed-bottom-ml, .x-panel-header-default-framed-bottom-mr {
    background-image: url(images/panel-header/panel-header-default-framed-bottom-sides.gif)
}

.x-panel-header-default-framed-bottom-mc {
    padding: 5px 2px 2px 2px
}

.x-cmd-slicer.x-panel-header-default-framed-bottom:before {
    display: none;
    content: "x-slicer:, stretch:top, frame:0 4px 4px 4px, frame-bg:url(images/panel-header/panel-header-default-framed-bottom-fbg.gif), corners:url(images/panel-header/panel-header-default-framed-bottom-corners.gif), sides:url(images/panel-header/panel-header-default-framed-bottom-sides.gif)" !important
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
    background-image: url(images/panel-header/panel-header-default-framed-left-fbg.gif);
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
    background-image: url(images/panel-header/panel-header-default-framed-left-corners.gif)
}

.x-panel-header-default-framed-left-tc, .x-panel-header-default-framed-left-bc {
    background-image: url(images/panel-header/panel-header-default-framed-left-sides.gif);
    background-repeat: repeat-x
}

.x-panel-header-default-framed-left-mc {
    padding: 2px 5px 2px 2px
}

.x-cmd-slicer.x-panel-header-default-framed-left:before {
    display: none;
    content: "x-slicer:, stretch:right, frame:4px 0 4px 4px, frame-bg:url(images/panel-header/panel-header-default-framed-left-fbg.gif), corners:url(images/panel-header/panel-header-default-framed-left-corners.gif), sides:url(images/panel-header/panel-header-default-framed-left-sides.gif)" !important
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
    background-image: url(images/panel-header/panel-header-default-framed-collapsed-top-fbg.gif);
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
    background-image: url(images/panel-header/panel-header-default-framed-collapsed-top-corners.gif)
}

.x-panel-header-default-framed-collapsed-top-ml, .x-panel-header-default-framed-collapsed-top-mr {
    background-image: url(images/panel-header/panel-header-default-framed-collapsed-top-sides.gif)
}

.x-panel-header-default-framed-collapsed-top-mc {
    padding: 2px 2px 2px 2px
}

.x-cmd-slicer.x-panel-header-default-framed-collapsed-top:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:4px 4px 4px 4px, frame-bg:url(images/panel-header/panel-header-default-framed-collapsed-top-fbg.gif), corners:url(images/panel-header/panel-header-default-framed-collapsed-top-corners.gif), sides:url(images/panel-header/panel-header-default-framed-collapsed-top-sides.gif)" !important
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
    background-image: url(images/panel-header/panel-header-default-framed-collapsed-right-fbg.gif);
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
    background-image: url(images/panel-header/panel-header-default-framed-collapsed-right-corners.gif)
}

.x-panel-header-default-framed-collapsed-right-tc, .x-panel-header-default-framed-collapsed-right-bc {
    background-image: url(images/panel-header/panel-header-default-framed-collapsed-right-sides.gif);
    background-repeat: repeat-x
}

.x-panel-header-default-framed-collapsed-right-mc {
    padding: 2px 2px 2px 2px
}

.x-cmd-slicer.x-panel-header-default-framed-collapsed-right:before {
    display: none;
    content: "x-slicer:, stretch:left, frame:4px 4px 4px 4px, frame-bg:url(images/panel-header/panel-header-default-framed-collapsed-right-fbg.gif), corners:url(images/panel-header/panel-header-default-framed-collapsed-right-corners.gif), sides:url(images/panel-header/panel-header-default-framed-collapsed-right-sides.gif)" !important
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
    background-image: url(images/panel-header/panel-header-default-framed-collapsed-bottom-fbg.gif);
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
    background-image: url(images/panel-header/panel-header-default-framed-collapsed-bottom-corners.gif)
}

.x-panel-header-default-framed-collapsed-bottom-ml, .x-panel-header-default-framed-collapsed-bottom-mr {
    background-image: url(images/panel-header/panel-header-default-framed-collapsed-bottom-sides.gif)
}

.x-panel-header-default-framed-collapsed-bottom-mc {
    padding: 2px 2px 2px 2px
}

.x-cmd-slicer.x-panel-header-default-framed-collapsed-bottom:before {
    display: none;
    content: "x-slicer:, stretch:top, frame:4px 4px 4px 4px, frame-bg:url(images/panel-header/panel-header-default-framed-collapsed-bottom-fbg.gif), corners:url(images/panel-header/panel-header-default-framed-collapsed-bottom-corners.gif), sides:url(images/panel-header/panel-header-default-framed-collapsed-bottom-sides.gif)" !important
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
    background-image: url(images/panel-header/panel-header-default-framed-collapsed-left-fbg.gif);
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
    background-image: url(images/panel-header/panel-header-default-framed-collapsed-left-corners.gif)
}

.x-panel-header-default-framed-collapsed-left-tc, .x-panel-header-default-framed-collapsed-left-bc {
    background-image: url(images/panel-header/panel-header-default-framed-collapsed-left-sides.gif);
    background-repeat: repeat-x
}

.x-panel-header-default-framed-collapsed-left-mc {
    padding: 2px 2px 2px 2px
}

.x-cmd-slicer.x-panel-header-default-framed-collapsed-left:before {
    display: none;
    content: "x-slicer:, stretch:right, frame:4px 4px 4px 4px, frame-bg:url(images/panel-header/panel-header-default-framed-collapsed-left-fbg.gif), corners:url(images/panel-header/panel-header-default-framed-collapsed-left-corners.gif), sides:url(images/panel-header/panel-header-default-framed-collapsed-left-sides.gif)" !important
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
    background-image: url(images/btn-group/btn-group-default-framed-corners.gif)
}

.x-btn-group-default-framed-ml, .x-btn-group-default-framed-mr {
    background-image: url(images/btn-group/btn-group-default-framed-sides.gif);
    background-repeat: repeat-y
}

.x-btn-group-default-framed-mc {
    padding: 0px 0px 0px 0px
}

.x-cmd-slicer.x-btn-group-default-framed:before {
    display: none;
    content: "x-slicer:, frame:2px 2px 2px 2px, corners:url(images/btn-group/btn-group-default-framed-corners.gif), sides:url(images/btn-group/btn-group-default-framed-sides.gif)" !important
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
    background-image: url(images/btn-group/btn-group-default-framed-notitle-corners.gif)
}

.x-btn-group-default-framed-notitle-ml, .x-btn-group-default-framed-notitle-mr {
    background-image: url(images/btn-group/btn-group-default-framed-notitle-sides.gif);
    background-repeat: repeat-y
}

.x-btn-group-default-framed-notitle-mc {
    padding: 0px 0px 0px 0px
}

.x-cmd-slicer.x-btn-group-default-framed-notitle:before {
    display: none;
    content: "x-slicer:, frame:2px 2px 2px 2px, corners:url(images/btn-group/btn-group-default-framed-notitle-corners.gif), sides:url(images/btn-group/btn-group-default-framed-notitle-sides.gif)" !important
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
    background-image: url(images/window/window-default-corners.gif)
}

.x-window-default-ml, .x-window-default-mr {
    background-image: url(images/window/window-default-sides.gif);
    background-repeat: repeat-y
}

.x-window-default-mc {
    padding: 0px 0px 0px 0px
}

.x-cmd-slicer.x-window-default:before {
    display: none;
    content: "x-slicer:, frame:5px 5px 5px 5px, corners:url(images/window/window-default-corners.gif), sides:url(images/window/window-default-sides.gif)" !important
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
    background-image: url(images/window-header/window-header-default-top-corners.gif)
}

.x-window-header-default-top-ml, .x-window-header-default-top-mr {
    background-image: url(images/window-header/window-header-default-top-sides.gif);
    background-repeat: repeat-y
}

.x-window-header-default-top-mc {
    padding: 1px 1px 1px 1px
}

.x-cmd-slicer.x-window-header-default-top:before {
    display: none;
    content: "x-slicer:, frame:5px 5px 0 5px, corners:url(images/window-header/window-header-default-top-corners.gif), sides:url(images/window-header/window-header-default-top-sides.gif)" !important
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
    background-image: url(images/window-header/window-header-default-right-corners.gif)
}

.x-window-header-default-right-ml, .x-window-header-default-right-mr {
    background-image: url(images/window-header/window-header-default-right-sides.gif);
    background-repeat: repeat-y
}

.x-window-header-default-right-mc {
    padding: 1px 1px 1px 1px
}

.x-cmd-slicer.x-window-header-default-right:before {
    display: none;
    content: "x-slicer:, frame:5px 5px 5px 0, corners:url(images/window-header/window-header-default-right-corners.gif), sides:url(images/window-header/window-header-default-right-sides.gif)" !important
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
    background-image: url(images/window-header/window-header-default-bottom-corners.gif)
}

.x-window-header-default-bottom-ml, .x-window-header-default-bottom-mr {
    background-image: url(images/window-header/window-header-default-bottom-sides.gif);
    background-repeat: repeat-y
}

.x-window-header-default-bottom-mc {
    padding: 1px 1px 1px 1px
}

.x-cmd-slicer.x-window-header-default-bottom:before {
    display: none;
    content: "x-slicer:, frame:0 5px 5px 5px, corners:url(images/window-header/window-header-default-bottom-corners.gif), sides:url(images/window-header/window-header-default-bottom-sides.gif)" !important
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
    background-image: url(images/window-header/window-header-default-left-corners.gif)
}

.x-window-header-default-left-ml, .x-window-header-default-left-mr {
    background-image: url(images/window-header/window-header-default-left-sides.gif);
    background-repeat: repeat-y
}

.x-window-header-default-left-mc {
    padding: 1px 1px 1px 1px
}

.x-cmd-slicer.x-window-header-default-left:before {
    display: none;
    content: "x-slicer:, frame:5px 0 5px 5px, corners:url(images/window-header/window-header-default-left-corners.gif), sides:url(images/window-header/window-header-default-left-sides.gif)" !important
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
    background-image: url(images/window-header/window-header-default-collapsed-top-corners.gif)
}

.x-window-header-default-collapsed-top-ml, .x-window-header-default-collapsed-top-mr {
    background-image: url(images/window-header/window-header-default-collapsed-top-sides.gif);
    background-repeat: repeat-y
}

.x-window-header-default-collapsed-top-mc {
    padding: 1px 1px 1px 1px
}

.x-cmd-slicer.x-window-header-default-collapsed-top:before {
    display: none;
    content: "x-slicer:, frame:5px 5px 5px 5px, corners:url(images/window-header/window-header-default-collapsed-top-corners.gif), sides:url(images/window-header/window-header-default-collapsed-top-sides.gif)" !important
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
    background-image: url(images/window-header/window-header-default-collapsed-right-corners.gif)
}

.x-window-header-default-collapsed-right-ml, .x-window-header-default-collapsed-right-mr {
    background-image: url(images/window-header/window-header-default-collapsed-right-sides.gif);
    background-repeat: repeat-y
}

.x-window-header-default-collapsed-right-mc {
    padding: 1px 1px 1px 1px
}

.x-cmd-slicer.x-window-header-default-collapsed-right:before {
    display: none;
    content: "x-slicer:, frame:5px 5px 5px 5px, corners:url(images/window-header/window-header-default-collapsed-right-corners.gif), sides:url(images/window-header/window-header-default-collapsed-right-sides.gif)" !important
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
    background-image: url(images/window-header/window-header-default-collapsed-bottom-corners.gif)
}

.x-window-header-default-collapsed-bottom-ml, .x-window-header-default-collapsed-bottom-mr {
    background-image: url(images/window-header/window-header-default-collapsed-bottom-sides.gif);
    background-repeat: repeat-y
}

.x-window-header-default-collapsed-bottom-mc {
    padding: 1px 1px 1px 1px
}

.x-cmd-slicer.x-window-header-default-collapsed-bottom:before {
    display: none;
    content: "x-slicer:, frame:5px 5px 5px 5px, corners:url(images/window-header/window-header-default-collapsed-bottom-corners.gif), sides:url(images/window-header/window-header-default-collapsed-bottom-sides.gif)" !important
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
    background-image: url(images/window-header/window-header-default-collapsed-left-corners.gif)
}

.x-window-header-default-collapsed-left-ml, .x-window-header-default-collapsed-left-mr {
    background-image: url(images/window-header/window-header-default-collapsed-left-sides.gif);
    background-repeat: repeat-y
}

.x-window-header-default-collapsed-left-mc {
    padding: 1px 1px 1px 1px
}

.x-cmd-slicer.x-window-header-default-collapsed-left:before {
    display: none;
    content: "x-slicer:, frame:5px 5px 5px 5px, corners:url(images/window-header/window-header-default-collapsed-left-corners.gif), sides:url(images/window-header/window-header-default-collapsed-left-sides.gif)" !important
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
    background: url(images/form/exclamation.gif) no-repeat
}

.x-form-invalid-under-default {
    padding: 2px 2px 2px 20px;
    color: #c0272b;
    font: normal 11px/16px tahoma, arial, verdana, sans-serif;
    background: no-repeat 0 2px;
    background-image: url(images/form/exclamation.gif)
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
    background: url(images/form/exclamation.gif) no-repeat
}

.x-form-invalid-under-toolbar {
    padding: 2px 2px 2px 20px;
    color: #c30;
    font: normal 12px/16px tahoma, arial, verdana, sans-serif;
    background: no-repeat 0 2px;
    background-image: url(images/form/exclamation.gif)
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
    background-image: url(images/form/text-bg.gif);
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
    background-image: url(images/grid/invalid_line.gif);
    background-repeat: repeat-x;
    background-position: bottom
}

.x-form-trigger-default {
    width: 17px;
    background: 0 0 transparent url(images/form/trigger.gif) no-repeat;
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
    background-image: url(images/form/text-bg.gif);
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
    background-image: url(images/grid/invalid_line.gif);
    background-repeat: repeat-x;
    background-position: bottom
}

.x-form-trigger-toolbar {
    width: 17px;
    background: 0 0 #fff url(images/form/trigger.gif) no-repeat;
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
    background-image: url(images/form/clear-trigger.gif)
}

.x-form-search-trigger {
    background-image: url(images/form/search-trigger.gif)
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
    background-image: url(images/shared/icon-info.gif)
}

.x-message-box-warning {
    background-image: url(images/shared/icon-warning.gif)
}

.x-message-box-question {
    background-image: url(images/shared/icon-question.gif)
}

.x-message-box-error {
    background-image: url(images/shared/icon-error.gif)
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
    background: url(images/form/radio.gif) no-repeat
}

.x-form-cb-checked .x-form-radio-default {
    background-position: 0 -13px
}

.x-form-checkbox-default {
    background: url(images/form/checkbox.gif) no-repeat
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
    background: url(images/form/radio.gif) no-repeat
}

.x-form-cb-checked .x-form-radio-toolbar {
    background-position: 0 -13px
}

.x-form-checkbox-toolbar {
    background: url(images/form/checkbox.gif) no-repeat
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
    background-image: url(images/grid/invalid_line.gif);
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
    background-image: url(images/form/spinner.gif);
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
    background-image: url(images/form/spinner-small.gif);
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
    background-image: url(images/grid/page-first.gif)
}

.x-btn-icon-el.x-tbar-page-prev {
    background-image: url(images/grid/page-prev.gif)
}

.x-btn-icon-el.x-tbar-page-next {
    background-image: url(images/grid/page-next.gif)
}

.x-btn-icon-el.x-tbar-page-last {
    background-image: url(images/grid/page-last.gif)
}

.x-btn-icon-el.x-tbar-loading {
    background-image: url(images/grid/refresh.gif)
}

.x-item-disabled .x-tbar-page-first {
    background-image: url(images/grid/page-first-disabled.gif)
}

.x-item-disabled .x-tbar-page-prev {
    background-image: url(images/grid/page-prev-disabled.gif)
}

.x-item-disabled .x-tbar-page-next {
    background-image: url(images/grid/page-next-disabled.gif)
}

.x-item-disabled .x-tbar-page-last {
    background-image: url(images/grid/page-last-disabled.gif)
}

.x-item-disabled .x-tbar-loading {
    background-image: url(images/grid/refresh-disabled.gif)
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
    background: url(images/shared/right-btn.gif) no-repeat 0 0
}

.x-datepicker-prev {
    left: 6px;
    background: url(images/shared/left-btn.gif) no-repeat 0 0
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
    background-image: url(images/button/s-arrow-light.gif);
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
    background: url(images/tools/tool-sprites.gif) no-repeat 0 -120px
}

.x-monthpicker-yearnav-next-over {
    background-position: -15px -120px
}

.x-monthpicker-yearnav-prev {
    background: url(images/tools/tool-sprites.gif) no-repeat 0 -105px
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
    background-image: url(images/datepicker/datepicker-header-bg.gif);
    background-repeat: repeat-x;
    background-position: top left
}

.x-nlg .x-datepicker-footer, .x-nlg .x-monthpicker-buttons {
    background-image: url(images/datepicker/datepicker-footer-bg.gif);
    background-repeat: repeat-x;
    background-position: top left
}

.x-cmd-slicer.x-datepicker-header:before {
    display: none;
    content: "x-slicer:, bg:url(images/datepicker/datepicker-header-bg.gif), stretch:bottom" !important
}

.x-cmd-slicer.x-datepicker-footer:before {
    display: none;
    content: "x-slicer:, bg:url(images/datepicker/datepicker-footer-bg.gif), stretch:bottom" !important
}

.x-form-field-date .x-form-date-trigger {
    background-image: url(images/form/date-trigger.gif)
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
    background-image: url(images/tip/tip-default-corners.gif)
}

.x-tip-default-ml, .x-tip-default-mr {
    background-image: url(images/tip/tip-default-sides.gif);
    background-repeat: repeat-y
}

.x-tip-default-mc {
    padding: 0px 0px 0px 0px
}

.x-cmd-slicer.x-tip-default:before {
    display: none;
    content: "x-slicer:, frame:3px 3px 3px 3px, corners:url(images/tip/tip-default-corners.gif), sides:url(images/tip/tip-default-sides.gif)" !important
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
    background-image: url(images/tip/tip-form-invalid-corners.gif)
}

.x-tip-form-invalid-ml, .x-tip-form-invalid-mr {
    background-image: url(images/tip/tip-form-invalid-sides.gif);
    background-repeat: repeat-y
}

.x-tip-form-invalid-mc {
    padding: 0px 0px 0px 0px
}

.x-cmd-slicer.x-tip-form-invalid:before {
    display: none;
    content: "x-slicer:, frame:5px 5px 5px 5px, corners:url(images/tip/tip-form-invalid-corners.gif), sides:url(images/tip/tip-form-invalid-sides.gif)" !important
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
    background-image: url(images/form/exclamation.gif)
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
    background-image: url(images/editor/tb-sprite.gif)
}

.x-html-editor-tb .x-edit-italic, .x-menu-item div.x-edit-italic {
    background-position: -16px 0;
    background-image: url(images/editor/tb-sprite.gif)
}

.x-html-editor-tb .x-edit-underline, .x-menu-item div.x-edit-underline {
    background-position: -32px 0;
    background-image: url(images/editor/tb-sprite.gif)
}

.x-html-editor-tb .x-edit-forecolor, .x-menu-item div.x-edit-forecolor {
    background-position: -160px 0;
    background-image: url(images/editor/tb-sprite.gif)
}

.x-html-editor-tb .x-edit-backcolor, .x-menu-item div.x-edit-backcolor {
    background-position: -176px 0;
    background-image: url(images/editor/tb-sprite.gif)
}

.x-html-editor-tb .x-edit-justifyleft, .x-menu-item div.x-edit-justifyleft {
    background-position: -112px 0;
    background-image: url(images/editor/tb-sprite.gif)
}

.x-html-editor-tb .x-edit-justifycenter, .x-menu-item div.x-edit-justifycenter {
    background-position: -128px 0;
    background-image: url(images/editor/tb-sprite.gif)
}

.x-html-editor-tb .x-edit-justifyright, .x-menu-item div.x-edit-justifyright {
    background-position: -144px 0;
    background-image: url(images/editor/tb-sprite.gif)
}

.x-html-editor-tb .x-edit-insertorderedlist, .x-menu-item div.x-edit-insertorderedlist {
    background-position: -80px 0;
    background-image: url(images/editor/tb-sprite.gif)
}

.x-html-editor-tb .x-edit-insertunorderedlist, .x-menu-item div.x-edit-insertunorderedlist {
    background-position: -96px 0;
    background-image: url(images/editor/tb-sprite.gif)
}

.x-html-editor-tb .x-edit-increasefontsize, .x-menu-item div.x-edit-increasefontsize {
    background-position: -48px 0;
    background-image: url(images/editor/tb-sprite.gif)
}

.x-html-editor-tb .x-edit-decreasefontsize, .x-menu-item div.x-edit-decreasefontsize {
    background-position: -64px 0;
    background-image: url(images/editor/tb-sprite.gif)
}

.x-html-editor-tb .x-edit-sourceedit, .x-menu-item div.x-edit-sourceedit {
    background-position: -192px 0;
    background-image: url(images/editor/tb-sprite.gif)
}

.x-html-editor-tb .x-edit-createlink, .x-menu-item div.x-edit-createlink {
    background-position: -208px 0;
    background-image: url(images/editor/tb-sprite.gif)
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
    background-image: url(images/form/tag-field-item-close.gif)
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
    background-image: url(images/form/tag-field-item-close.gif)
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
    background-image: url(images/grid/cell-special-bg.gif)
}

.x-nlg .x-grid-item-selected .x-grid-cell-special {
    background-image: url(images/grid/cell-special-selected-bg.gif)
}

.x-grid-cell-special .x-cmd-slicer.x-grid-cell-special:before {
    display: none;
    content: "x-slicer:, bg:url(images/grid/cell-special-bg.gif)" !important
}

.x-grid-cell-special .x-cmd-slicer.x-grid-cell-special-selected:before {
    display: none;
    content: "x-slicer:, bg:url(images/grid/cell-special-selected-bg.gif)" !important
}

.x-grid-dirty-cell {
    background: url(images/grid/dirty.gif) no-repeat 0 0
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
    background-image: url(images/grid/dd-insert-arrow-right.png);
    height: 16px;
    width: 16px
}

.x-grid-drop-indicator .x-grid-drop-indicator-right {
    position: absolute;
    top: -8px;
    right: -11px;
    background-image: url(images/grid/dd-insert-arrow-left.png);
    height: 16px;
    width: 16px
}

.x-col-move-top, .x-col-move-bottom {
    width: 9px;
    height: 9px
}

.x-col-move-top {
    background-image: url(images/grid/col-move-top.gif)
}

.x-col-move-bottom {
    background-image: url(images/grid/col-move-bottom.gif)
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
    background-image: url(images/grid/hmenu-asc.gif)
}

.x-hmenu-sort-desc {
    background-image: url(images/grid/hmenu-desc.gif)
}

.x-cols-icon {
    background-image: url(images/grid/columns.gif)
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
    background-image: url(images/grid/column-header-bg.gif)
}

.x-nlg .x-column-header-over, .x-nlg .x-column-header-sort-ASC, .x-nlg .x-column-header-sort-DESC {
    background-image: url(images/grid/column-header-over-bg.gif)
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
    background: transparent url(images/grid/grid3-hd-btn.gif) no-repeat 0 center
}

.x-column-header-align-right .x-column-header-text {
    margin-right: 9px
}

.x-column-header-sort-ASC .x-column-header-text-inner, .x-column-header-sort-DESC .x-column-header-text-inner {
    padding-right: 12px;
    background-position: right center
}

.x-column-header-sort-ASC .x-column-header-text-inner {
    background-image: url(images/grid/sort_asc.gif)
}

.x-column-header-sort-DESC .x-column-header-text-inner {
    background-image: url(images/grid/sort_desc.gif)
}

.x-no-header-borders .x-column-header {
    border: 0 none
}

.x-no-header-borders .x-column-header .x-column-header-inner {
    padding-top: 4px
}

.x-cmd-slicer.x-column-header:before {
    display: none;
    content: "x-slicer:, bg:url(images/grid/column-header-bg.gif), stretch:bottom" !important
}

.x-cmd-slicer.x-column-header-over:before {
    display: none;
    content: "x-slicer:, bg:url(images/grid/column-header-over-bg.gif), stretch:bottom" !important
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
    background-image: url(images/form/checkbox.gif);
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
    background-image: url(images/form/text-bg.gif);
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
    background-image: url(images/grid/invalid_line.gif);
    background-repeat: repeat-x;
    background-position: bottom
}

.x-form-trigger-grid-cell {
    width: 17px;
    background: 0 0 transparent url(images/form/trigger.gif) no-repeat;
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
    background-image: url(images/form/tag-field-item-close.gif)
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
    background-image: url(images/form/spinner-small.gif);
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
    background: url(images/form/radio.gif) no-repeat
}

.x-form-cb-checked .x-form-radio-grid-cell {
    background-position: 0 -13px
}

.x-form-checkbox-grid-cell {
    background: url(images/form/checkbox.gif) no-repeat
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
    background-image: url(images/button/arrow.gif);
    padding-right: 8px
}

.x-btn-wrap-grid-cell-small.x-btn-arrow-bottom:after {
    height: 8px;
    background-image: url(images/button/arrow.gif)
}

.x-btn-wrap-grid-cell-small.x-btn-split-right:after {
    width: 14px;
    background-image: url(images/button/s-arrow.gif);
    padding-right: 14px
}

.x-btn-wrap-grid-cell-small.x-btn-split-bottom:after {
    height: 14px;
    background-image: url(images/button/s-arrow-b.gif)
}

.x-btn-over > .x-btn-wrap-grid-cell-small.x-btn-split-right:after {
    background-image: url(images/button/s-arrow-o.gif)
}

.x-btn-over > .x-btn-wrap-grid-cell-small.x-btn-split-bottom:after {
    background-image: url(images/button/s-arrow-bo.gif)
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
    background: url(images/grid/group-collapse.gif) no-repeat left center
}

.x-grid-group-title {
    color: #3764a0;
    font: bold 11px/13px tahoma, arial, verdana, sans-serif
}

.x-grid-group-hd-collapsed .x-grid-group-title {
    background-image: url(images/grid/group-expand.gif)
}

.x-group-by-icon {
    background-image: url(images/grid/group-by.gif)
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
    background-image: url(images/menu/default-checked.gif)
}

.x-menu-item-unchecked .x-menu-item-icon-default.x-menu-item-checkbox {
    background-image: url(images/menu/default-unchecked.gif)
}

.x-menu-item-checked .x-menu-item-icon-default.x-menu-group-icon {
    background-image: url(images/menu/default-group-checked.gif)
}

.x-menu-item-unchecked .x-menu-item-icon-default.x-menu-group-icon {
    background-image: none
}

.x-menu-item-arrow-default {
    width: 12px;
    height: 9px;
    top: 6px;
    right: -1px;
    background-image: url(images/menu/default-menu-parent.gif)
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
    background-image: url(images/menu/default-scroll-top.gif);
    background-position: 0 -5px
}

.x-box-scroller-menu-default.x-box-scroller-top.x-box-scroller-hover {
    background-position: 0 0
}

.x-box-scroller-menu-default.x-box-scroller-bottom {
    margin-top: 4px;
    margin-right: 0;
    margin-bottom: 4px;
    background-image: url(images/menu/default-scroll-bottom.gif);
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
    background-image: url(images/menu/default-menubar-menu-parent.gif)
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
    background-image: url(images/grid/filters/find.png)
}

.x-grid-filters-gt {
    background-image: url(images/grid/filters/greater_than.png)
}

.x-grid-filters-lt {
    background-image: url(images/grid/filters/less_than.png)
}

.x-grid-filters-eq {
    background-image: url(images/grid/filters/equals.png)
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
    background-image: url(images/grid/hmenu-lock.gif)
}

.x-hmenu-unlock {
    background-image: url(images/grid/hmenu-unlock.gif)
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
    background-image: url(images/grid-row-editor-buttons/grid-row-editor-buttons-default-bottom-corners.gif)
}

.x-grid-row-editor-buttons-default-bottom-ml, .x-grid-row-editor-buttons-default-bottom-mr {
    background-image: url(images/grid-row-editor-buttons/grid-row-editor-buttons-default-bottom-sides.gif);
    background-repeat: repeat-y
}

.x-grid-row-editor-buttons-default-bottom-mc {
    padding: 4px 0px 0px 0px
}

.x-cmd-slicer.x-grid-row-editor-buttons-default-bottom:before {
    display: none;
    content: "x-slicer:, frame:0 5px 5px 5px, corners:url(images/grid-row-editor-buttons/grid-row-editor-buttons-default-bottom-corners.gif), sides:url(images/grid-row-editor-buttons/grid-row-editor-buttons-default-bottom-sides.gif)" !important
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
    background-image: url(images/grid-row-editor-buttons/grid-row-editor-buttons-default-top-corners.gif)
}

.x-grid-row-editor-buttons-default-top-ml, .x-grid-row-editor-buttons-default-top-mr {
    background-image: url(images/grid-row-editor-buttons/grid-row-editor-buttons-default-top-sides.gif);
    background-repeat: repeat-y
}

.x-grid-row-editor-buttons-default-top-mc {
    padding: 0px 0px 4px 0px
}

.x-cmd-slicer.x-grid-row-editor-buttons-default-top:before {
    display: none;
    content: "x-slicer:, frame:5px 5px 0 5px, corners:url(images/grid-row-editor-buttons/grid-row-editor-buttons-default-top-corners.gif), sides:url(images/grid-row-editor-buttons/grid-row-editor-buttons-default-top-sides.gif)" !important
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
    background-image: url(images/grid/group-collapse.gif)
}

.x-grid-row-collapsed .x-grid-row-expander {
    background-image: url(images/grid/group-expand.gif)
}

.x-grid-cell-inner-property-name {
    background-image: url(images/grid/property-cell-bg.gif);
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
    background-image: url(images/sizer/e-handle.gif)
}

.x-resizable-handle-south-over, .x-resizable-handle-north-over, .x-resizable-pinned > .x-resizable-handle-south, .x-resizable-pinned > .x-resizable-handle-north {
    background-image: url(images/sizer/s-handle.gif)
}

.x-resizable-handle-southeast-over, .x-resizable-pinned > .x-resizable-handle-southeast {
    background-position: top left;
    background-image: url(images/sizer/se-handle.gif)
}

.x-resizable-handle-northwest-over, .x-resizable-pinned > .x-resizable-handle-northwest {
    background-position: bottom right;
    background-image: url(images/sizer/nw-handle.gif)
}

.x-resizable-handle-northeast-over, .x-resizable-pinned > .x-resizable-handle-northeast {
    background-position: bottom left;
    background-image: url(images/sizer/ne-handle.gif)
}

.x-resizable-handle-southwest-over, .x-resizable-pinned > .x-resizable-handle-southwest {
    background-position: top right;
    background-image: url(images/sizer/sw-handle.gif)
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
    background-image: url(images/slider/slider-thumb.png)
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
    background-image: url(images/slider/slider-v-thumb.png)
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
    background-image: url(images/slider/slider-bg.png)
}

.x-slider-vert, .x-slider-vert .x-slider-end, .x-slider-vert .x-slider-inner {
    background-image: url(images/slider/slider-v-bg.png)
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
    background-image: url(images/tab/tab-default-top-fbg.gif);
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
    background-image: url(images/tab/tab-default-top-corners.gif)
}

.x-tab-default-top-ml, .x-tab-default-top-mr {
    background-image: url(images/tab/tab-default-top-sides.gif)
}

.x-tab-default-top-mc {
    padding: 0px 6px 3px 6px
}

.x-cmd-slicer.x-tab-default-top:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:4px 4px 0 4px, frame-bg:url(images/tab/tab-default-top-fbg.gif), corners:url(images/tab/tab-default-top-corners.gif), sides:url(images/tab/tab-default-top-sides.gif)" !important
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
    background-image: url(images/tab/tab-default-bottom-fbg.gif);
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
    background-image: url(images/tab/tab-default-bottom-corners.gif)
}

.x-tab-default-bottom-ml, .x-tab-default-bottom-mr {
    background-image: url(images/tab/tab-default-bottom-sides.gif)
}

.x-tab-default-bottom-mc {
    padding: 0px 6px 0px 6px
}

.x-cmd-slicer.x-tab-default-bottom:before {
    display: none;
    content: "x-slicer:, stretch:top, frame:4px 4px 4px 4px, frame-bg:url(images/tab/tab-default-bottom-fbg.gif), corners:url(images/tab/tab-default-bottom-corners.gif), sides:url(images/tab/tab-default-bottom-sides.gif)" !important
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
    background-image: url(images/tab/tab-default-left-fbg.gif);
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
    background-image: url(images/tab/tab-default-left-corners.gif)
}

.x-tab-default-left-ml, .x-tab-default-left-mr {
    background-image: url(images/tab/tab-default-left-sides.gif)
}

.x-tab-default-left-mc {
    padding: 0px 5px 0px 6px
}

.x-cmd-slicer.x-tab-default-left:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:4px 4px 4px 4px, frame-bg:url(images/tab/tab-default-left-fbg.gif), corners:url(images/tab/tab-default-left-corners.gif), sides:url(images/tab/tab-default-left-sides.gif)" !important
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
    background-image: url(images/tab/tab-default-right-fbg.gif);
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
    background-image: url(images/tab/tab-default-right-corners.gif)
}

.x-tab-default-right-ml, .x-tab-default-right-mr {
    background-image: url(images/tab/tab-default-right-sides.gif)
}

.x-tab-default-right-mc {
    padding: 0px 6px 0px 5px
}

.x-cmd-slicer.x-tab-default-right:before {
    display: none;
    content: "x-slicer:, stretch:bottom, frame:4px 4px 4px 4px, frame-bg:url(images/tab/tab-default-right-fbg.gif), corners:url(images/tab/tab-default-right-corners.gif), sides:url(images/tab/tab-default-right-sides.gif)" !important
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
    background-image: url(images/tab/tab-default-top-over-corners.gif)
}

.x-tab-over .x-tab-default-top-ml, .x-tab-over .x-tab-default-top-mr {
    background-image: url(images/tab/tab-default-top-over-sides.gif)
}

.x-tab-over .x-tab-default-top-mc {
    background-repeat: repeat-x;
    background-image: url(images/tab/tab-default-top-over-fbg.gif)
}

.x-tab-focus .x-tab-default-top-tl, .x-tab-focus .x-tab-default-top-bl, .x-tab-focus .x-tab-default-top-tr, .x-tab-focus .x-tab-default-top-br, .x-tab-focus .x-tab-default-top-tc, .x-tab-focus .x-tab-default-top-bc {
    background-image: url(images/tab/tab-default-top-focus-corners.gif)
}

.x-tab-focus .x-tab-default-top-ml, .x-tab-focus .x-tab-default-top-mr {
    background-image: url(images/tab/tab-default-top-focus-sides.gif)
}

.x-tab-focus .x-tab-default-top-mc {
    background-repeat: repeat-x;
    background-image: url(images/tab/tab-default-top-focus-fbg.gif)
}

.x-tab-focus.x-tab-over .x-tab-default-top-tl, .x-tab-focus.x-tab-over .x-tab-default-top-bl, .x-tab-focus.x-tab-over .x-tab-default-top-tr, .x-tab-focus.x-tab-over .x-tab-default-top-br, .x-tab-focus.x-tab-over .x-tab-default-top-tc, .x-tab-focus.x-tab-over .x-tab-default-top-bc {
    background-image: url(images/tab/tab-default-top-focus-over-corners.gif)
}

.x-tab-focus.x-tab-over .x-tab-default-top-ml, .x-tab-focus.x-tab-over .x-tab-default-top-mr {
    background-image: url(images/tab/tab-default-top-focus-over-sides.gif)
}

.x-tab-focus.x-tab-over .x-tab-default-top-mc {
    background-repeat: repeat-x;
    background-image: url(images/tab/tab-default-top-focus-over-fbg.gif)
}

.x-tab.x-tab-active .x-tab-default-top-tl, .x-tab.x-tab-active .x-tab-default-top-bl, .x-tab.x-tab-active .x-tab-default-top-tr, .x-tab.x-tab-active .x-tab-default-top-br, .x-tab.x-tab-active .x-tab-default-top-tc, .x-tab.x-tab-active .x-tab-default-top-bc {
    background-image: url(images/tab/tab-default-top-active-corners.gif)
}

.x-tab.x-tab-active .x-tab-default-top-ml, .x-tab.x-tab-active .x-tab-default-top-mr {
    background-image: url(images/tab/tab-default-top-active-sides.gif)
}

.x-tab.x-tab-active .x-tab-default-top-mc {
    background-repeat: repeat-x;
    background-image: url(images/tab/tab-default-top-active-fbg.gif)
}

.x-tab-focus.x-tab-active .x-tab-default-top-tl, .x-tab-focus.x-tab-active .x-tab-default-top-bl, .x-tab-focus.x-tab-active .x-tab-default-top-tr, .x-tab-focus.x-tab-active .x-tab-default-top-br, .x-tab-focus.x-tab-active .x-tab-default-top-tc, .x-tab-focus.x-tab-active .x-tab-default-top-bc {
    background-image: url(images/tab/tab-default-top-focus-active-corners.gif)
}

.x-tab-focus.x-tab-active .x-tab-default-top-ml, .x-tab-focus.x-tab-active .x-tab-default-top-mr {
    background-image: url(images/tab/tab-default-top-focus-active-sides.gif)
}

.x-tab-focus.x-tab-active .x-tab-default-top-mc {
    background-repeat: repeat-x;
    background-image: url(images/tab/tab-default-top-focus-active-fbg.gif)
}

.x-tab.x-tab-disabled .x-tab-default-top-tl, .x-tab.x-tab-disabled .x-tab-default-top-bl, .x-tab.x-tab-disabled .x-tab-default-top-tr, .x-tab.x-tab-disabled .x-tab-default-top-br, .x-tab.x-tab-disabled .x-tab-default-top-tc, .x-tab.x-tab-disabled .x-tab-default-top-bc {
    background-image: url(images/tab/tab-default-top-disabled-corners.gif)
}

.x-tab.x-tab-disabled .x-tab-default-top-ml, .x-tab.x-tab-disabled .x-tab-default-top-mr {
    background-image: url(images/tab/tab-default-top-disabled-sides.gif)
}

.x-tab.x-tab-disabled .x-tab-default-top-mc {
    background-repeat: repeat-x;
    background-image: url(images/tab/tab-default-top-disabled-fbg.gif)
}

.x-tab-over .x-tab-default-right-tl, .x-tab-over .x-tab-default-right-bl, .x-tab-over .x-tab-default-right-tr, .x-tab-over .x-tab-default-right-br, .x-tab-over .x-tab-default-right-tc, .x-tab-over .x-tab-default-right-bc {
    background-image: url(images/tab/tab-default-right-over-corners.gif)
}

.x-tab-over .x-tab-default-right-ml, .x-tab-over .x-tab-default-right-mr {
    background-image: url(images/tab/tab-default-right-over-sides.gif)
}

.x-tab-over .x-tab-default-right-mc {
    background-repeat: repeat-x;
    background-image: url(images/tab/tab-default-right-over-fbg.gif)
}

.x-tab-focus .x-tab-default-right-tl, .x-tab-focus .x-tab-default-right-bl, .x-tab-focus .x-tab-default-right-tr, .x-tab-focus .x-tab-default-right-br, .x-tab-focus .x-tab-default-right-tc, .x-tab-focus .x-tab-default-right-bc {
    background-image: url(images/tab/tab-default-right-focus-corners.gif)
}

.x-tab-focus .x-tab-default-right-ml, .x-tab-focus .x-tab-default-right-mr {
    background-image: url(images/tab/tab-default-right-focus-sides.gif)
}

.x-tab-focus .x-tab-default-right-mc {
    background-repeat: repeat-x;
    background-image: url(images/tab/tab-default-right-focus-fbg.gif)
}

.x-tab-focus.x-tab-over .x-tab-default-right-tl, .x-tab-focus.x-tab-over .x-tab-default-right-bl, .x-tab-focus.x-tab-over .x-tab-default-right-tr, .x-tab-focus.x-tab-over .x-tab-default-right-br, .x-tab-focus.x-tab-over .x-tab-default-right-tc, .x-tab-focus.x-tab-over .x-tab-default-right-bc {
    background-image: url(images/tab/tab-default-right-focus-over-corners.gif)
}

.x-tab-focus.x-tab-over .x-tab-default-right-ml, .x-tab-focus.x-tab-over .x-tab-default-right-mr {
    background-image: url(images/tab/tab-default-right-focus-over-sides.gif)
}

.x-tab-focus.x-tab-over .x-tab-default-right-mc {
    background-repeat: repeat-x;
    background-image: url(images/tab/tab-default-right-focus-over-fbg.gif)
}

.x-tab.x-tab-active .x-tab-default-right-tl, .x-tab.x-tab-active .x-tab-default-right-bl, .x-tab.x-tab-active .x-tab-default-right-tr, .x-tab.x-tab-active .x-tab-default-right-br, .x-tab.x-tab-active .x-tab-default-right-tc, .x-tab.x-tab-active .x-tab-default-right-bc {
    background-image: url(images/tab/tab-default-right-active-corners.gif)
}

.x-tab.x-tab-active .x-tab-default-right-ml, .x-tab.x-tab-active .x-tab-default-right-mr {
    background-image: url(images/tab/tab-default-right-active-sides.gif)
}

.x-tab.x-tab-active .x-tab-default-right-mc {
    background-repeat: repeat-x;
    background-image: url(images/tab/tab-default-right-active-fbg.gif)
}

.x-tab-focus.x-tab-active .x-tab-default-right-tl, .x-tab-focus.x-tab-active .x-tab-default-right-bl, .x-tab-focus.x-tab-active .x-tab-default-right-tr, .x-tab-focus.x-tab-active .x-tab-default-right-br, .x-tab-focus.x-tab-active .x-tab-default-right-tc, .x-tab-focus.x-tab-active .x-tab-default-right-bc {
    background-image: url(images/tab/tab-default-right-focus-active-corners.gif)
}

.x-tab-focus.x-tab-active .x-tab-default-right-ml, .x-tab-focus.x-tab-active .x-tab-default-right-mr {
    background-image: url(images/tab/tab-default-right-focus-active-sides.gif)
}

.x-tab-focus.x-tab-active .x-tab-default-right-mc {
    background-repeat: repeat-x;
    background-image: url(images/tab/tab-default-right-focus-active-fbg.gif)
}

.x-tab.x-tab-disabled .x-tab-default-right-tl, .x-tab.x-tab-disabled .x-tab-default-right-bl, .x-tab.x-tab-disabled .x-tab-default-right-tr, .x-tab.x-tab-disabled .x-tab-default-right-br, .x-tab.x-tab-disabled .x-tab-default-right-tc, .x-tab.x-tab-disabled .x-tab-default-right-bc {
    background-image: url(images/tab/tab-default-right-disabled-corners.gif)
}

.x-tab.x-tab-disabled .x-tab-default-right-ml, .x-tab.x-tab-disabled .x-tab-default-right-mr {
    background-image: url(images/tab/tab-default-right-disabled-sides.gif)
}

.x-tab.x-tab-disabled .x-tab-default-right-mc {
    background-repeat: repeat-x;
    background-image: url(images/tab/tab-default-right-disabled-fbg.gif)
}

.x-tab-over .x-tab-default-bottom-tl, .x-tab-over .x-tab-default-bottom-bl, .x-tab-over .x-tab-default-bottom-tr, .x-tab-over .x-tab-default-bottom-br, .x-tab-over .x-tab-default-bottom-tc, .x-tab-over .x-tab-default-bottom-bc {
    background-image: url(images/tab/tab-default-bottom-over-corners.gif)
}

.x-tab-over .x-tab-default-bottom-ml, .x-tab-over .x-tab-default-bottom-mr {
    background-image: url(images/tab/tab-default-bottom-over-sides.gif)
}

.x-tab-over .x-tab-default-bottom-mc {
    background-repeat: repeat-x;
    background-image: url(images/tab/tab-default-bottom-over-fbg.gif)
}

.x-tab-focus .x-tab-default-bottom-tl, .x-tab-focus .x-tab-default-bottom-bl, .x-tab-focus .x-tab-default-bottom-tr, .x-tab-focus .x-tab-default-bottom-br, .x-tab-focus .x-tab-default-bottom-tc, .x-tab-focus .x-tab-default-bottom-bc {
    background-image: url(images/tab/tab-default-bottom-focus-corners.gif)
}

.x-tab-focus .x-tab-default-bottom-ml, .x-tab-focus .x-tab-default-bottom-mr {
    background-image: url(images/tab/tab-default-bottom-focus-sides.gif)
}

.x-tab-focus .x-tab-default-bottom-mc {
    background-repeat: repeat-x;
    background-image: url(images/tab/tab-default-bottom-focus-fbg.gif)
}

.x-tab-focus.x-tab-over .x-tab-default-bottom-tl, .x-tab-focus.x-tab-over .x-tab-default-bottom-bl, .x-tab-focus.x-tab-over .x-tab-default-bottom-tr, .x-tab-focus.x-tab-over .x-tab-default-bottom-br, .x-tab-focus.x-tab-over .x-tab-default-bottom-tc, .x-tab-focus.x-tab-over .x-tab-default-bottom-bc {
    background-image: url(images/tab/tab-default-bottom-focus-over-corners.gif)
}

.x-tab-focus.x-tab-over .x-tab-default-bottom-ml, .x-tab-focus.x-tab-over .x-tab-default-bottom-mr {
    background-image: url(images/tab/tab-default-bottom-focus-over-sides.gif)
}

.x-tab-focus.x-tab-over .x-tab-default-bottom-mc {
    background-repeat: repeat-x;
    background-image: url(images/tab/tab-default-bottom-focus-over-fbg.gif)
}

.x-tab.x-tab-active .x-tab-default-bottom-tl, .x-tab.x-tab-active .x-tab-default-bottom-bl, .x-tab.x-tab-active .x-tab-default-bottom-tr, .x-tab.x-tab-active .x-tab-default-bottom-br, .x-tab.x-tab-active .x-tab-default-bottom-tc, .x-tab.x-tab-active .x-tab-default-bottom-bc {
    background-image: url(images/tab/tab-default-bottom-active-corners.gif)
}

.x-tab.x-tab-active .x-tab-default-bottom-ml, .x-tab.x-tab-active .x-tab-default-bottom-mr {
    background-image: url(images/tab/tab-default-bottom-active-sides.gif)
}

.x-tab.x-tab-active .x-tab-default-bottom-mc {
    background-repeat: repeat-x;
    background-image: url(images/tab/tab-default-bottom-active-fbg.gif)
}

.x-tab-focus.x-tab-active .x-tab-default-bottom-tl, .x-tab-focus.x-tab-active .x-tab-default-bottom-bl, .x-tab-focus.x-tab-active .x-tab-default-bottom-tr, .x-tab-focus.x-tab-active .x-tab-default-bottom-br, .x-tab-focus.x-tab-active .x-tab-default-bottom-tc, .x-tab-focus.x-tab-active .x-tab-default-bottom-bc {
    background-image: url(images/tab/tab-default-bottom-focus-active-corners.gif)
}

.x-tab-focus.x-tab-active .x-tab-default-bottom-ml, .x-tab-focus.x-tab-active .x-tab-default-bottom-mr {
    background-image: url(images/tab/tab-default-bottom-focus-active-sides.gif)
}

.x-tab-focus.x-tab-active .x-tab-default-bottom-mc {
    background-repeat: repeat-x;
    background-image: url(images/tab/tab-default-bottom-focus-active-fbg.gif)
}

.x-tab.x-tab-disabled .x-tab-default-bottom-tl, .x-tab.x-tab-disabled .x-tab-default-bottom-bl, .x-tab.x-tab-disabled .x-tab-default-bottom-tr, .x-tab.x-tab-disabled .x-tab-default-bottom-br, .x-tab.x-tab-disabled .x-tab-default-bottom-tc, .x-tab.x-tab-disabled .x-tab-default-bottom-bc {
    background-image: url(images/tab/tab-default-bottom-disabled-corners.gif)
}

.x-tab.x-tab-disabled .x-tab-default-bottom-ml, .x-tab.x-tab-disabled .x-tab-default-bottom-mr {
    background-image: url(images/tab/tab-default-bottom-disabled-sides.gif)
}

.x-tab.x-tab-disabled .x-tab-default-bottom-mc {
    background-repeat: repeat-x;
    background-image: url(images/tab/tab-default-bottom-disabled-fbg.gif)
}

.x-tab-over .x-tab-default-left-tl, .x-tab-over .x-tab-default-left-bl, .x-tab-over .x-tab-default-left-tr, .x-tab-over .x-tab-default-left-br, .x-tab-over .x-tab-default-left-tc, .x-tab-over .x-tab-default-left-bc {
    background-image: url(images/tab/tab-default-left-over-corners.gif)
}

.x-tab-over .x-tab-default-left-ml, .x-tab-over .x-tab-default-left-mr {
    background-image: url(images/tab/tab-default-left-over-sides.gif)
}

.x-tab-over .x-tab-default-left-mc {
    background-repeat: repeat-x;
    background-image: url(images/tab/tab-default-left-over-fbg.gif)
}

.x-tab-focus .x-tab-default-left-tl, .x-tab-focus .x-tab-default-left-bl, .x-tab-focus .x-tab-default-left-tr, .x-tab-focus .x-tab-default-left-br, .x-tab-focus .x-tab-default-left-tc, .x-tab-focus .x-tab-default-left-bc {
    background-image: url(images/tab/tab-default-left-focus-corners.gif)
}

.x-tab-focus .x-tab-default-left-ml, .x-tab-focus .x-tab-default-left-mr {
    background-image: url(images/tab/tab-default-left-focus-sides.gif)
}

.x-tab-focus .x-tab-default-left-mc {
    background-repeat: repeat-x;
    background-image: url(images/tab/tab-default-left-focus-fbg.gif)
}

.x-tab-focus.x-tab-over .x-tab-default-left-tl, .x-tab-focus.x-tab-over .x-tab-default-left-bl, .x-tab-focus.x-tab-over .x-tab-default-left-tr, .x-tab-focus.x-tab-over .x-tab-default-left-br, .x-tab-focus.x-tab-over .x-tab-default-left-tc, .x-tab-focus.x-tab-over .x-tab-default-left-bc {
    background-image: url(images/tab/tab-default-left-focus-over-corners.gif)
}

.x-tab-focus.x-tab-over .x-tab-default-left-ml, .x-tab-focus.x-tab-over .x-tab-default-left-mr {
    background-image: url(images/tab/tab-default-left-focus-over-sides.gif)
}

.x-tab-focus.x-tab-over .x-tab-default-left-mc {
    background-repeat: repeat-x;
    background-image: url(images/tab/tab-default-left-focus-over-fbg.gif)
}

.x-tab.x-tab-active .x-tab-default-left-tl, .x-tab.x-tab-active .x-tab-default-left-bl, .x-tab.x-tab-active .x-tab-default-left-tr, .x-tab.x-tab-active .x-tab-default-left-br, .x-tab.x-tab-active .x-tab-default-left-tc, .x-tab.x-tab-active .x-tab-default-left-bc {
    background-image: url(images/tab/tab-default-left-active-corners.gif)
}

.x-tab.x-tab-active .x-tab-default-left-ml, .x-tab.x-tab-active .x-tab-default-left-mr {
    background-image: url(images/tab/tab-default-left-active-sides.gif)
}

.x-tab.x-tab-active .x-tab-default-left-mc {
    background-repeat: repeat-x;
    background-image: url(images/tab/tab-default-left-active-fbg.gif)
}

.x-tab-focus.x-tab-active .x-tab-default-left-tl, .x-tab-focus.x-tab-active .x-tab-default-left-bl, .x-tab-focus.x-tab-active .x-tab-default-left-tr, .x-tab-focus.x-tab-active .x-tab-default-left-br, .x-tab-focus.x-tab-active .x-tab-default-left-tc, .x-tab-focus.x-tab-active .x-tab-default-left-bc {
    background-image: url(images/tab/tab-default-left-focus-active-corners.gif)
}

.x-tab-focus.x-tab-active .x-tab-default-left-ml, .x-tab-focus.x-tab-active .x-tab-default-left-mr {
    background-image: url(images/tab/tab-default-left-focus-active-sides.gif)
}

.x-tab-focus.x-tab-active .x-tab-default-left-mc {
    background-repeat: repeat-x;
    background-image: url(images/tab/tab-default-left-focus-active-fbg.gif)
}

.x-tab.x-tab-disabled .x-tab-default-left-tl, .x-tab.x-tab-disabled .x-tab-default-left-bl, .x-tab.x-tab-disabled .x-tab-default-left-tr, .x-tab.x-tab-disabled .x-tab-default-left-br, .x-tab.x-tab-disabled .x-tab-default-left-tc, .x-tab.x-tab-disabled .x-tab-default-left-bc {
    background-image: url(images/tab/tab-default-left-disabled-corners.gif)
}

.x-tab.x-tab-disabled .x-tab-default-left-ml, .x-tab.x-tab-disabled .x-tab-default-left-mr {
    background-image: url(images/tab/tab-default-left-disabled-sides.gif)
}

.x-tab.x-tab-disabled .x-tab-default-left-mc {
    background-repeat: repeat-x;
    background-image: url(images/tab/tab-default-left-disabled-fbg.gif)
}

.x-tab-default-tl, .x-tab-default-bl, .x-tab-default-tr, .x-tab-default-br {
    -ms-filter: "progid:DXImageTransform.Microsoft.gradient(startColorstr=#00FFFFFF,endColorstr=#00FFFFFF)"
}

.x-tab-default .x-tab-close-btn {
    top: 2px;
    right: 2px;
    width: 11px;
    height: 11px;
    background: url(images/tab/tab-default-close.gif) 0 0;
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
    content: "x-slicer:, corners:url(images/tab/tab-default-top-focus-corners.gif), sides:url(images/tab/tab-default-top-focus-sides.gif), frame-bg:url(images/tab/tab-default-top-focus-fbg.gif), frame:4px 4px 4px 4px, stretch:bottom" !important
}

.x-cmd-slicer.x-tab-focus.x-tab-default-right:before {
    display: none;
    content: "x-slicer:, corners:url(images/tab/tab-default-right-focus-corners.gif), sides:url(images/tab/tab-default-right-focus-sides.gif), frame-bg:url(images/tab/tab-default-right-focus-fbg.gif), frame:4px 4px 4px 4px, stretch:left" !important
}

.x-cmd-slicer.x-tab-focus.x-tab-default-bottom:before {
    display: none;
    content: "x-slicer:, corners:url(images/tab/tab-default-bottom-focus-corners.gif), sides:url(images/tab/tab-default-bottom-focus-sides.gif), frame-bg:url(images/tab/tab-default-bottom-focus-fbg.gif), frame:4px 4px 4px 4px, stretch:top" !important
}

.x-cmd-slicer.x-tab-focus.x-tab-default-left:before {
    display: none;
    content: "x-slicer:, corners:url(images/tab/tab-default-left-focus-corners.gif), sides:url(images/tab/tab-default-left-focus-sides.gif), frame-bg:url(images/tab/tab-default-left-focus-fbg.gif), frame:4px 4px 4px 4px, stretch:right" !important
}

.x-cmd-slicer.x-tab-over.x-tab-default-top:before {
    display: none;
    content: "x-slicer:, corners:url(images/tab/tab-default-top-over-corners.gif), sides:url(images/tab/tab-default-top-over-sides.gif), frame-bg:url(images/tab/tab-default-top-over-fbg.gif), frame:4px 4px 4px 4px, stretch:bottom" !important
}

.x-cmd-slicer.x-tab-over.x-tab-default-right:before {
    display: none;
    content: "x-slicer:, corners:url(images/tab/tab-default-right-over-corners.gif), sides:url(images/tab/tab-default-right-over-sides.gif), frame-bg:url(images/tab/tab-default-right-over-fbg.gif), frame:4px 4px 4px 4px, stretch:left" !important
}

.x-cmd-slicer.x-tab-over.x-tab-default-bottom:before {
    display: none;
    content: "x-slicer:, corners:url(images/tab/tab-default-bottom-over-corners.gif), sides:url(images/tab/tab-default-bottom-over-sides.gif), frame-bg:url(images/tab/tab-default-bottom-over-fbg.gif), frame:4px 4px 4px 4px, stretch:top" !important
}

.x-cmd-slicer.x-tab-over.x-tab-default-left:before {
    display: none;
    content: "x-slicer:, corners:url(images/tab/tab-default-left-over-corners.gif), sides:url(images/tab/tab-default-left-over-sides.gif), frame-bg:url(images/tab/tab-default-left-over-fbg.gif), frame:4px 4px 4px 4px, stretch:right" !important
}

.x-cmd-slicer.x-tab-active.x-tab-default-top:before {
    display: none;
    content: "x-slicer:, corners:url(images/tab/tab-default-top-active-corners.gif), sides:url(images/tab/tab-default-top-active-sides.gif), frame-bg:url(images/tab/tab-default-top-active-fbg.gif), frame:4px 4px 4px 4px, stretch:bottom" !important
}

.x-cmd-slicer.x-tab-active.x-tab-default-right:before {
    display: none;
    content: "x-slicer:, corners:url(images/tab/tab-default-right-active-corners.gif), sides:url(images/tab/tab-default-right-active-sides.gif), frame-bg:url(images/tab/tab-default-right-active-fbg.gif), frame:4px 4px 4px 4px, stretch:left" !important
}

.x-cmd-slicer.x-tab-active.x-tab-default-bottom:before {
    display: none;
    content: "x-slicer:, corners:url(images/tab/tab-default-bottom-active-corners.gif), sides:url(images/tab/tab-default-bottom-active-sides.gif), frame-bg:url(images/tab/tab-default-bottom-active-fbg.gif), frame:4px 4px 4px 4px, stretch:top" !important
}

.x-cmd-slicer.x-tab-active.x-tab-default-left:before {
    display: none;
    content: "x-slicer:, corners:url(images/tab/tab-default-left-active-corners.gif), sides:url(images/tab/tab-default-left-active-sides.gif), frame-bg:url(images/tab/tab-default-left-active-fbg.gif), frame:4px 4px 4px 4px, stretch:right" !important
}

.x-cmd-slicer.x-tab-focus.x-tab-over.x-tab-default-top:before {
    display: none;
    content: "x-slicer:, corners:url(images/tab/tab-default-top-focus-over-corners.gif), sides:url(images/tab/tab-default-top-focus-over-sides.gif), frame-bg:url(images/tab/tab-default-top-focus-over-fbg.gif), frame:4px 4px 4px 4px, stretch:bottom" !important
}

.x-cmd-slicer.x-tab-focus.x-tab-over.x-tab-default-right:before {
    display: none;
    content: "x-slicer:, corners:url(images/tab/tab-default-right-focus-over-corners.gif), sides:url(images/tab/tab-default-right-focus-over-sides.gif), frame-bg:url(images/tab/tab-default-right-focus-over-fbg.gif), frame:4px 4px 4px 4px, stretch:left" !important
}

.x-cmd-slicer.x-tab-focus.x-tab-over.x-tab-default-bottom:before {
    display: none;
    content: "x-slicer:, corners:url(images/tab/tab-default-bottom-focus-over-corners.gif), sides:url(images/tab/tab-default-bottom-focus-over-sides.gif), frame-bg:url(images/tab/tab-default-bottom-focus-over-fbg.gif), frame:4px 4px 4px 4px, stretch:top" !important
}

.x-cmd-slicer.x-tab-focus.x-tab-over.x-tab-default-left:before {
    display: none;
    content: "x-slicer:, corners:url(images/tab/tab-default-left-focus-over-corners.gif), sides:url(images/tab/tab-default-left-focus-over-sides.gif), frame-bg:url(images/tab/tab-default-left-focus-over-fbg.gif), frame:4px 4px 4px 4px, stretch:right" !important
}

.x-cmd-slicer.x-tab-focus.x-tab-active.x-tab-default-top:before {
    display: none;
    content: "x-slicer:, corners:url(images/tab/tab-default-top-focus-active-corners.gif), sides:url(images/tab/tab-default-top-focus-active-sides.gif), frame-bg:url(images/tab/tab-default-top-focus-active-fbg.gif), frame:4px 4px 4px 4px, stretch:bottom" !important
}

.x-cmd-slicer.x-tab-focus.x-tab-active.x-tab-default-right:before {
    display: none;
    content: "x-slicer:, corners:url(images/tab/tab-default-right-focus-active-corners.gif), sides:url(images/tab/tab-default-right-focus-active-sides.gif), frame-bg:url(images/tab/tab-default-right-focus-active-fbg.gif), frame:4px 4px 4px 4px, stretch:left" !important
}

.x-cmd-slicer.x-tab-focus.x-tab-active.x-tab-default-bottom:before {
    display: none;
    content: "x-slicer:, corners:url(images/tab/tab-default-bottom-focus-active-corners.gif), sides:url(images/tab/tab-default-bottom-focus-active-sides.gif), frame-bg:url(images/tab/tab-default-bottom-focus-active-fbg.gif), frame:4px 4px 4px 4px, stretch:top" !important
}

.x-cmd-slicer.x-tab-focus.x-tab-active.x-tab-default-left:before {
    display: none;
    content: "x-slicer:, corners:url(images/tab/tab-default-left-focus-active-corners.gif), sides:url(images/tab/tab-default-left-focus-active-sides.gif), frame-bg:url(images/tab/tab-default-left-focus-active-fbg.gif), frame:4px 4px 4px 4px, stretch:right" !important
}

.x-cmd-slicer.x-tab-disabled.x-tab-default-top:before {
    display: none;
    content: "x-slicer:, corners:url(images/tab/tab-default-top-disabled-corners.gif), sides:url(images/tab/tab-default-top-disabled-sides.gif), frame-bg:url(images/tab/tab-default-top-disabled-fbg.gif), frame:4px 4px 4px 4px, stretch:bottom" !important
}

.x-cmd-slicer.x-tab-disabled.x-tab-default-right:before {
    display: none;
    content: "x-slicer:, corners:url(images/tab/tab-default-right-disabled-corners.gif), sides:url(images/tab/tab-default-right-disabled-sides.gif), frame-bg:url(images/tab/tab-default-right-disabled-fbg.gif), frame:4px 4px 4px 4px, stretch:left" !important
}

.x-cmd-slicer.x-tab-disabled.x-tab-default-bottom:before {
    display: none;
    content: "x-slicer:, corners:url(images/tab/tab-default-bottom-disabled-corners.gif), sides:url(images/tab/tab-default-bottom-disabled-sides.gif), frame-bg:url(images/tab/tab-default-bottom-disabled-fbg.gif), frame:4px 4px 4px 4px, stretch:top" !important
}

.x-cmd-slicer.x-tab-disabled.x-tab-default-left:before {
    display: none;
    content: "x-slicer:, corners:url(images/tab/tab-default-left-disabled-corners.gif), sides:url(images/tab/tab-default-left-disabled-sides.gif), frame-bg:url(images/tab/tab-default-left-disabled-fbg.gif), frame:4px 4px 4px 4px, stretch:right" !important
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
    background: url(images/tab-bar/tab-bar-default-top-bg.gif)
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
    background: url(images/tab-bar/tab-bar-default-bottom-bg.gif) bottom 0
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
    background: url(images/tab-bar/tab-bar-default-left-bg.gif)
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
    background: url(images/tab-bar/tab-bar-default-right-bg.gif) 0 right
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
    background-image: url(images/tab-bar/default-more.gif)
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
    background-image: url(images/tab-bar/default-scroll-left-top.gif)
}

.x-tab-bar-default-top .x-box-scroller-right {
    background-image: url(images/tab-bar/default-scroll-right-top.gif)
}

.x-tab-bar-default-bottom .x-box-scroller-left {
    background-image: url(images/tab-bar/default-scroll-left-bottom.gif)
}

.x-tab-bar-default-bottom .x-box-scroller-right {
    background-image: url(images/tab-bar/default-scroll-right-bottom.gif)
}

.x-tab-bar-default-left .x-box-scroller-top {
    background-image: url(images/tab-bar/default-scroll-top-left.gif)
}

.x-tab-bar-default-left .x-box-scroller-bottom {
    background-image: url(images/tab-bar/default-scroll-bottom-left.gif)
}

.x-tab-bar-default-right .x-box-scroller-top {
    background-image: url(images/tab-bar/default-scroll-top-right.gif)
}

.x-tab-bar-default-right .x-box-scroller-bottom {
    background-image: url(images/tab-bar/default-scroll-bottom-right.gif)
}

.x-cmd-slicer.x-tab-bar-default-top:before {
    display: none;
    content: "x-slicer:, bg:url(images/tab-bar/tab-bar-default-top-bg.gif), stretch:bottom" !important
}

.x-cmd-slicer.x-tab-bar-default-bottom:before {
    display: none;
    content: "x-slicer:, bg:url(images/tab-bar/tab-bar-default-bottom-bg.gif), stretch:top" !important
}

.x-cmd-slicer.x-tab-bar-default-left:before {
    display: none;
    content: "x-slicer:, bg:url(images/tab-bar/tab-bar-default-left-bg.gif), stretch:right" !important
}

.x-cmd-slicer.x-tab-bar-default-right:before {
    display: none;
    content: "x-slicer:, bg:url(images/tab-bar/tab-bar-default-right-bg.gif), stretch:left" !important
}

.x-breadcrumb-btn-default {
    margin: 0 0 0 0px
}

.x-breadcrumb-icon-folder-default {
    background-image: url(images/tree/folder.gif)
}

.x-btn-menu-active .x-breadcrumb-icon-folder-default {
    background-image: url(images/tree/folder-open.gif)
}

.x-breadcrumb-icon-leaf-default {
    background-image: url(images/tree/leaf.gif)
}

.x-breadcrumb-btn .x-btn-wrap-default-toolbar-small.x-btn-arrow:after {
    width: 14px;
    background-image: url(images/breadcrumb/default-arrow.gif)
}

.x-btn-menu-active.x-breadcrumb-btn .x-btn-wrap-default-toolbar-small.x-btn-arrow:after {
    background-image: url(images/breadcrumb/default-arrow-open.gif)
}

.x-breadcrumb-btn .x-btn-wrap-default-toolbar-small.x-btn-split:after {
    width: 14px;
    background-image: url(images/breadcrumb/default-split-arrow.gif)
}

.x-btn-over.x-breadcrumb-btn .x-btn-wrap-default-toolbar-small.x-btn-split:after {
    background-image: url(images/breadcrumb/default-split-arrow-over.gif)
}

.x-btn-menu-active.x-breadcrumb-btn .x-btn-wrap-default-toolbar-small.x-btn-split:after {
    background-image: url(images/breadcrumb/default-split-arrow-open.gif)
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
    background-image: url(images/breadcrumb/default-scroll-left.gif);
    background-position: -14px 0
}

.x-box-scroller-breadcrumb-default.x-box-scroller-left.x-box-scroller-hover {
    background-position: 0 0
}

.x-box-scroller-breadcrumb-default.x-box-scroller-right {
    margin-left: 0;
    margin-right: 0;
    margin-bottom: 0;
    background-image: url(images/breadcrumb/default-scroll-right.gif);
    background-position: 0 0
}

.x-box-scroller-breadcrumb-default.x-box-scroller-right.x-box-scroller-hover {
    background-position: -14px 0
}

.x-tree-expander {
    cursor: pointer
}

.x-tree-arrows .x-tree-expander {
    background-image: url(images/tree/arrows.gif)
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
    background-image: url(images/tree/elbow.gif)
}

.x-tree-lines .x-tree-elbow-end {
    background-image: url(images/tree/elbow-end.gif)
}

.x-tree-lines .x-tree-elbow-plus {
    background-image: url(images/tree/elbow-plus.gif)
}

.x-tree-lines .x-tree-elbow-end-plus {
    background-image: url(images/tree/elbow-end-plus.gif)
}

.x-tree-lines .x-grid-tree-node-expanded .x-tree-elbow-plus {
    background-image: url(images/tree/elbow-minus.gif)
}

.x-tree-lines .x-grid-tree-node-expanded .x-tree-elbow-end-plus {
    background-image: url(images/tree/elbow-end-minus.gif)
}

.x-tree-lines .x-tree-elbow-line {
    background-image: url(images/tree/elbow-line.gif)
}

.x-tree-no-lines .x-tree-expander {
    background-image: url(images/tree/elbow-plus-nl.gif)
}

.x-tree-no-lines .x-grid-tree-node-expanded .x-tree-expander {
    background-image: url(images/tree/elbow-minus-nl.gif)
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
    background-image: url(images/tree/leaf.gif)
}

.x-tree-icon-parent {
    background-image: url(images/tree/folder.gif)
}

.x-tree-icon-parent-expanded {
    background-image: url(images/tree/folder-open.gif)
}

.x-tree-icon-custom {
    background-image: none
}

.x-tree-checkbox {
    margin-right: 3px;
    top: 4px;
    width: 13px;
    height: 13px;
    background-image: url(images/form/checkbox.gif)
}

.x-tree-checkbox-checked {
    background-position: 0 -13px
}

.x-grid-tree-loading .x-tree-icon {
    background-image: url(images/tree/loading.gif)
}

.x-tree-node-text {
    padding-left: 3px
}

.x-grid-cell-inner-treecolumn {
    padding: 3px 6px 4px 0
}

.x-tree-drop-ok-append .x-dd-drop-icon {
    background-image: url(images/tree/drop-append.gif)
}

.x-tree-drop-ok-above .x-dd-drop-icon {
    background-image: url(images/tree/drop-above.gif)
}

.x-tree-drop-ok-below .x-dd-drop-icon {
    background-image: url(images/tree/drop-below.gif)
}

.x-tree-drop-ok-between .x-dd-drop-icon {
    background-image: url(images/tree/drop-between.gif)
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
    background-image: url(images/window/toast/icon16_info.png)
}

.x-toast-icon-error {
    background-image: url(images/window/toast/icon16_error.png)
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
    background-image: url(images/window/toast/fader.png)
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
    background-image: url(images/box/corners.gif)
}

.x-box-tc {
    background-image: url(images/box/tb.gif)
}

.x-box-tr {
    background-image: url(images/box/corners.gif)
}

.x-box-ml {
    background-image: url(images/box/l.gif)
}

.x-box-mc {
    background-color: #eee;
    background-image: url(images/box/tb.gif);
    font-family: "Myriad Pro", "Myriad Web", "Tahoma", "Helvetica", "Arial", sans-serif;
    color: #393939;
    font-size: 15px
}

.x-box-mc h3 {
    font-size: 18px;
    font-weight: bold
}

.x-box-mr {
    background-image: url(images/box/r.gif)
}

.x-box-bl {
    background-image: url(images/box/corners.gif)
}

.x-box-bc {
    background-image: url(images/box/tb.gif)
}

.x-box-br {
    background-image: url(images/box/corners.gif)
}

.x-box-blue .x-box-bl, .x-box-blue .x-box-br, .x-box-blue .x-box-tl, .x-box-blue .x-box-tr {
    background-image: url(images/box/corners-blue.gif)
}

.x-box-blue .x-box-bc, .x-box-blue .x-box-mc, .x-box-blue .x-box-tc {
    background-image: url(images/box/tb-blue.gif)
}

.x-box-blue .x-box-mc {
    background-color: #c3daf9
}

.x-box-blue .x-box-mc h3 {
    color: #17385b
}

.x-box-blue .x-box-ml {
    background-image: url(images/box/l-blue.gif)
}

.x-box-blue .x-box-mr {
    background-image: url(images/box/r-blue.gif)
}

.x-message-box .x-msg-box-wait {
    background-image: url(images/shared/blue-loading.gif)
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