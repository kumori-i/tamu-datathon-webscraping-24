# https://webscrape1-dot-chunin.uc.r.appspot.com/login
# username: datathon_participant
# password: webscrape!

from bs4 import BeautifulSoup

html_content = """<html><head>
      <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
      <meta name="generator" content="PhpSpreadsheet, https://github.com/PHPOffice/PhpSpreadsheet">
      <title>Minor League Baseball Statistics</title>
      <meta name="author" content="Unknown Creator">
      <meta name="title" content="Untitled Spreadsheet">
      <meta name="company" content="Microsoft Corporation">
      <link rel="stylesheet" href="/scrape.css">
  <link href="data:text/css,%3Ais(%5Bid*%3D'google_ads_iframe'%5D%2C%5Bid*%3D'taboola-'%5D%2C.taboolaHeight%2C.taboola-placeholder%2C%23credential_picker_container%2C%23credentials-picker-container%2C%23credential_picker_iframe%2C%5Bid*%3D'google-one-tap-iframe'%5D%2C%23google-one-tap-popup-container%2C.google-one-tap-modal-div%2C%23amp_floatingAdDiv%2C%23ez-content-blocker-container)%20%7Bdisplay%3Anone!important%3Bmin-height%3A0!important%3Bheight%3A0!important%3B%7D" rel="stylesheet" type="text/css"><script src="moz-extension://a931a247-baa3-4405-8d8d-a95a659c5dd2/content/fido2/page-script.js" id="bw-fido2-page-script"></script><style>.rdp {
  --rdp-cell-size: 40px;
  --rdp-accent-color: #0000ff;
  --rdp-background-color: #e7edff;
  --rdp-accent-color-dark: #3003e1;
  --rdp-background-color-dark: #180270;
  --rdp-outline: 2px solid var(--rdp-accent-color); /* Outline border for focused elements */
  --rdp-outline-selected: 2px solid rgba(0, 0, 0, 0.75); /* Outline border for focused _and_ selected elements */

  margin: 1em;
}

/* Hide elements for devices that are not screen readers */
.rdp-vhidden {
  box-sizing: border-box;
  padding: 0;
  margin: 0;
  background: transparent;
  border: 0;
  -moz-appearance: none;
  -webkit-appearance: none;
  appearance: none;
  position: absolute !important;
  top: 0;
  width: 1px !important;
  height: 1px !important;
  padding: 0 !important;
  overflow: hidden !important;
  clip: rect(1px, 1px, 1px, 1px) !important;
  border: 0 !important;
}

/* Buttons */
.rdp-button_reset {
  appearance: none;
  position: relative;
  margin: 0;
  padding: 0;
  cursor: default;
  color: inherit;
  outline: none;
  background: none;
  font: inherit;

  -moz-appearance: none;
  -webkit-appearance: none;
}

.rdp-button {
  border: 2px solid transparent;
}

.rdp-button[disabled] {
  opacity: 0.25;
}

.rdp-button:not([disabled]) {
  cursor: pointer;
}

.rdp-button:focus:not([disabled]),
.rdp-button:active:not([disabled]) {
  color: inherit;
  border: var(--rdp-outline);
  background-color: var(--rdp-background-color);
}

.rdp-button:hover:not([disabled]) {
  background-color: var(--rdp-background-color);
}

.rdp-months {
  display: flex;
}

.rdp-month {
  margin: 0 1em;
}

.rdp-month:first-child {
  margin-left: 0;
}

.rdp-month:last-child {
  margin-right: 0;
}

.rdp-table {
  margin: 0;
  max-width: calc(var(--rdp-cell-size) * 7);
  border-collapse: collapse;
}

.rdp-with_weeknumber .rdp-table {
  max-width: calc(var(--rdp-cell-size) * 8);
  border-collapse: collapse;
}

.rdp-caption {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0;
  text-align: left;
}

.rdp-multiple_months .rdp-caption {
  position: relative;
  display: block;
  text-align: center;
}

.rdp-caption_dropdowns {
  position: relative;
  display: inline-flex;
}

.rdp-caption_label {
  position: relative;
  z-index: 1;
  display: inline-flex;
  align-items: center;
  margin: 0;
  padding: 0 0.25em;
  white-space: nowrap;
  color: currentColor;
  border: 0;
  border: 2px solid transparent;
  font-family: inherit;
  font-size: 140%;
  font-weight: bold;
}

.rdp-nav {
  white-space: nowrap;
}

.rdp-multiple_months .rdp-caption_start .rdp-nav {
  position: absolute;
  top: 50%;
  left: 0;
  transform: translateY(-50%);
}

.rdp-multiple_months .rdp-caption_end .rdp-nav {
  position: absolute;
  top: 50%;
  right: 0;
  transform: translateY(-50%);
}

.rdp-nav_button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: var(--rdp-cell-size);
  height: var(--rdp-cell-size);
  padding: 0.25em;
  border-radius: 100%;
}

/* ---------- */
/* Dropdowns  */
/* ---------- */

.rdp-dropdown_year,
.rdp-dropdown_month {
  position: relative;
  display: inline-flex;
  align-items: center;
}

.rdp-dropdown {
  appearance: none;
  position: absolute;
  z-index: 2;
  top: 0;
  bottom: 0;
  left: 0;
  width: 100%;
  margin: 0;
  padding: 0;
  cursor: inherit;
  opacity: 0;
  border: none;
  background-color: transparent;
  font-family: inherit;
  font-size: inherit;
  line-height: inherit;
}

.rdp-dropdown[disabled] {
  opacity: unset;
  color: unset;
}

.rdp-dropdown:focus:not([disabled]) + .rdp-caption_label,
.rdp-dropdown:active:not([disabled]) + .rdp-caption_label {
  border: var(--rdp-outline);
  border-radius: 6px;
  background-color: var(--rdp-background-color);
}

.rdp-dropdown_icon {
  margin: 0 0 0 5px;
}

.rdp-head {
  border: 0;
}

.rdp-head_row,
.rdp-row {
  height: 100%;
}

.rdp-head_cell {
  vertical-align: middle;
  text-transform: uppercase;
  font-size: 0.75em;
  font-weight: 700;
  text-align: center;
  height: 100%;
  height: var(--rdp-cell-size);
  padding: 0;
}

.rdp-tbody {
  border: 0;
}

.rdp-tfoot {
  margin: 0.5em;
}

.rdp-cell {
  width: var(--rdp-cell-size);
  height: 100%;
  height: var(--rdp-cell-size);
  padding: 0;
  text-align: center;
}

.rdp-weeknumber {
  font-size: 0.75em;
}

.rdp-weeknumber,
.rdp-day {
  display: flex;
  overflow: hidden;
  align-items: center;
  justify-content: center;
  box-sizing: border-box;
  width: var(--rdp-cell-size);
  max-width: var(--rdp-cell-size);
  height: var(--rdp-cell-size);
  margin: 0;
  border: 2px solid transparent;
  border-radius: 100%;
}

.rdp-day_today:not(.rdp-day_outside) {
  font-weight: bold;
}

.rdp-day_selected:not([disabled]),
.rdp-day_selected:focus:not([disabled]),
.rdp-day_selected:active:not([disabled]),
.rdp-day_selected:hover:not([disabled]) {
  color: white;
  background-color: var(--rdp-accent-color);
}

.rdp-day_selected:focus:not([disabled]) {
  border: var(--rdp-outline-selected);
}

.rdp:not([dir='rtl']) .rdp-day_range_start:not(.rdp-day_range_end) {
  border-top-right-radius: 0;
  border-bottom-right-radius: 0;
}

.rdp:not([dir='rtl']) .rdp-day_range_end:not(.rdp-day_range_start) {
  border-top-left-radius: 0;
  border-bottom-left-radius: 0;
}

.rdp[dir='rtl'] .rdp-day_range_start:not(.rdp-day_range_end) {
  border-top-left-radius: 0;
  border-bottom-left-radius: 0;
}

.rdp[dir='rtl'] .rdp-day_range_end:not(.rdp-day_range_start) {
  border-top-right-radius: 0;
  border-bottom-right-radius: 0;
}

.rdp-day_range_end.rdp-day_range_start {
  border-radius: 100%;
}

.rdp-day_range_middle {
  border-radius: 0;
}
</style></head>
  <body class="vsc-initialized"><div id="bit-notification-bar-spacer" style="height: 0px;"></div>
<style>
@page { margin-left: 0.7in; margin-right: 0.7in; margin-top: 0.75in; margin-bottom: 0.75in; }
body { margin-left: 0.7in; margin-right: 0.7in; margin-top: 0.75in; margin-bottom: 0.75in; }
</style>
    <table border="0" cellpadding="0" cellspacing="0" id="sheet0" class="sheet0 gridlines">
        <colgroup><col class="col0">
        <col class="col1">
        <col class="col2">
        <col class="col3">
        <col class="col4">
        <col class="col5">
        <col class="col6">
        <col class="col7">
        </colgroup><tbody>
          <tr class="row0">
            <td class="column0 style0 s">year</td>
            <td class="column1 style0 s">team</td>
            <td class="column2 style0 s">games</td>
            <td class="column3 style0 s">plate_appearances</td>
            <td class="column4 style0 s">runs</td>
            <td class="column5 style0 s">hits</td>
            <td class="column6 style0 s">homeruns</td>
            <td class="column7 style0 s">RBI</td>
          </tr>
          <tr class="row1">
            <td class="column0 style0 n">2023</td>
            <td class="column1 style0 s">Amarillo Sod Poodles</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4974</td>
            <td class="column4 style0 n">647</td>
            <td class="column5 style0 n">1198</td>
            <td class="column6 style0 n">68</td>
            <td class="column7 style0 n">598</td>
          </tr>
          <tr class="row2">
            <td class="column0 style0 n">2023</td>
            <td class="column1 style0 s">Binghamton Rumble Ponies</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">5003</td>
            <td class="column4 style0 n">632</td>
            <td class="column5 style0 n">1222</td>
            <td class="column6 style0 n">89</td>
            <td class="column7 style0 n">591</td>
          </tr>
          <tr class="row3">
            <td class="column0 style0 n">2023</td>
            <td class="column1 style0 s">Corpus Christi Hooks</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4890</td>
            <td class="column4 style0 n">624</td>
            <td class="column5 style0 n">1200</td>
            <td class="column6 style0 n">93</td>
            <td class="column7 style0 n">590</td>
          </tr>
          <tr class="row4">
            <td class="column0 style0 n">2023</td>
            <td class="column1 style0 s">Montgomery Biscuits</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4882</td>
            <td class="column4 style0 n">592</td>
            <td class="column5 style0 n">1086</td>
            <td class="column6 style0 n">120</td>
            <td class="column7 style0 n">566</td>
          </tr>
          <tr class="row5">
            <td class="column0 style0 n">2023</td>
            <td class="column1 style0 s">Down East Wood Ducks</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4858</td>
            <td class="column4 style0 n">557</td>
            <td class="column5 style0 n">1078</td>
            <td class="column6 style0 n">92</td>
            <td class="column7 style0 n">520</td>
          </tr>
          <tr class="row6">
            <td class="column0 style0 n">2023</td>
            <td class="column1 style0 s">Columbia Fireflies</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4831</td>
            <td class="column4 style0 n">503</td>
            <td class="column5 style0 n">1095</td>
            <td class="column6 style0 n">48</td>
            <td class="column7 style0 n">465</td>
          </tr>
          <tr class="row7">
            <td class="column0 style0 n">2023</td>
            <td class="column1 style0 s">Erie SeaWolves</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4834</td>
            <td class="column4 style0 n">499</td>
            <td class="column5 style0 n">1149</td>
            <td class="column6 style0 n">70</td>
            <td class="column7 style0 n">471</td>
          </tr>
          <tr class="row8">
            <td class="column0 style0 n">2023</td>
            <td class="column1 style0 s">Akron RubberDucks</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4742</td>
            <td class="column4 style0 n">468</td>
            <td class="column5 style0 n">1070</td>
            <td class="column6 style0 n">66</td>
            <td class="column7 style0 n">447</td>
          </tr>
          <tr class="row9">
            <td class="column0 style0 n">2022</td>
            <td class="column1 style0 s">Amarillo Sod Poodles</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4881</td>
            <td class="column4 style0 n">603</td>
            <td class="column5 style0 n">1118</td>
            <td class="column6 style0 n">112</td>
            <td class="column7 style0 n">568</td>
          </tr>
          <tr class="row10">
            <td class="column0 style0 n">2022</td>
            <td class="column1 style0 s">Binghamton Rumble Ponies</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4855</td>
            <td class="column4 style0 n">578</td>
            <td class="column5 style0 n">1103</td>
            <td class="column6 style0 n">78</td>
            <td class="column7 style0 n">543</td>
          </tr>
          <tr class="row11">
            <td class="column0 style0 n">2022</td>
            <td class="column1 style0 s">Corpus Christi Hooks</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4805</td>
            <td class="column4 style0 n">534</td>
            <td class="column5 style0 n">1050</td>
            <td class="column6 style0 n">104</td>
            <td class="column7 style0 n">502</td>
          </tr>
          <tr class="row12">
            <td class="column0 style0 n">2022</td>
            <td class="column1 style0 s">Montgomery Biscuits</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4894</td>
            <td class="column4 style0 n">533</td>
            <td class="column5 style0 n">1152</td>
            <td class="column6 style0 n">76</td>
            <td class="column7 style0 n">501</td>
          </tr>
          <tr class="row13">
            <td class="column0 style0 n">2022</td>
            <td class="column1 style0 s">Down East Wood Ducks</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4933</td>
            <td class="column4 style0 n">532</td>
            <td class="column5 style0 n">1160</td>
            <td class="column6 style0 n">78</td>
            <td class="column7 style0 n">508</td>
          </tr>
          <tr class="row14">
            <td class="column0 style0 n">2022</td>
            <td class="column1 style0 s">Columbia Fireflies</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4920</td>
            <td class="column4 style0 n">530</td>
            <td class="column5 style0 n">1154</td>
            <td class="column6 style0 n">96</td>
            <td class="column7 style0 n">507</td>
          </tr>
          <tr class="row15">
            <td class="column0 style0 n">2022</td>
            <td class="column1 style0 s">Erie SeaWolves</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4810</td>
            <td class="column4 style0 n">499</td>
            <td class="column5 style0 n">1080</td>
            <td class="column6 style0 n">73</td>
            <td class="column7 style0 n">465</td>
          </tr>
          <tr class="row16">
            <td class="column0 style0 n">2022</td>
            <td class="column1 style0 s">Akron RubberDucks</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4894</td>
            <td class="column4 style0 n">497</td>
            <td class="column5 style0 n">1062</td>
            <td class="column6 style0 n">86</td>
            <td class="column7 style0 n">469</td>
          </tr>
          <tr class="row17">
            <td class="column0 style0 n">2021</td>
            <td class="column1 style0 s">Amarillo Sod Poodles</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4798</td>
            <td class="column4 style0 n">547</td>
            <td class="column5 style0 n">1104</td>
            <td class="column6 style0 n">92</td>
            <td class="column7 style0 n">518</td>
          </tr>
          <tr class="row18">
            <td class="column0 style0 n">2021</td>
            <td class="column1 style0 s">Binghamton Rumble Ponies</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4779</td>
            <td class="column4 style0 n">538</td>
            <td class="column5 style0 n">1043</td>
            <td class="column6 style0 n">73</td>
            <td class="column7 style0 n">505</td>
          </tr>
          <tr class="row19">
            <td class="column0 style0 n">2021</td>
            <td class="column1 style0 s">Corpus Christi Hooks</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4769</td>
            <td class="column4 style0 n">511</td>
            <td class="column5 style0 n">1057</td>
            <td class="column6 style0 n">110</td>
            <td class="column7 style0 n">481</td>
          </tr>
          <tr class="row20">
            <td class="column0 style0 n">2021</td>
            <td class="column1 style0 s">Montgomery Biscuits</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4793</td>
            <td class="column4 style0 n">509</td>
            <td class="column5 style0 n">1059</td>
            <td class="column6 style0 n">99</td>
            <td class="column7 style0 n">488</td>
          </tr>
          <tr class="row21">
            <td class="column0 style0 n">2021</td>
            <td class="column1 style0 s">Down East Wood Ducks</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4765</td>
            <td class="column4 style0 n">488</td>
            <td class="column5 style0 n">1034</td>
            <td class="column6 style0 n">88</td>
            <td class="column7 style0 n">463</td>
          </tr>
          <tr class="row22">
            <td class="column0 style0 n">2021</td>
            <td class="column1 style0 s">Columbia Fireflies</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4754</td>
            <td class="column4 style0 n">476</td>
            <td class="column5 style0 n">1067</td>
            <td class="column6 style0 n">62</td>
            <td class="column7 style0 n">431</td>
          </tr>
          <tr class="row23">
            <td class="column0 style0 n">2021</td>
            <td class="column1 style0 s">Erie SeaWolves</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4723</td>
            <td class="column4 style0 n">457</td>
            <td class="column5 style0 n">1037</td>
            <td class="column6 style0 n">81</td>
            <td class="column7 style0 n">430</td>
          </tr>
          <tr class="row24">
            <td class="column0 style0 n">2021</td>
            <td class="column1 style0 s">Akron RubberDucks</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4706</td>
            <td class="column4 style0 n">455</td>
            <td class="column5 style0 n">1068</td>
            <td class="column6 style0 n">55</td>
            <td class="column7 style0 n">425</td>
          </tr>
          <tr class="row25">
            <td class="column0 style0 n">2020</td>
            <td class="column1 style0 s">Amarillo Sod Poodles</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4841</td>
            <td class="column4 style0 n">622</td>
            <td class="column5 style0 n">1163</td>
            <td class="column6 style0 n">159</td>
            <td class="column7 style0 n">594</td>
          </tr>
          <tr class="row26">
            <td class="column0 style0 n">2020</td>
            <td class="column1 style0 s">Binghamton Rumble Ponies</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4975</td>
            <td class="column4 style0 n">614</td>
            <td class="column5 style0 n">1134</td>
            <td class="column6 style0 n">111</td>
            <td class="column7 style0 n">575</td>
          </tr>
          <tr class="row27">
            <td class="column0 style0 n">2020</td>
            <td class="column1 style0 s">Corpus Christi Hooks</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4785</td>
            <td class="column4 style0 n">601</td>
            <td class="column5 style0 n">1098</td>
            <td class="column6 style0 n">105</td>
            <td class="column7 style0 n">554</td>
          </tr>
          <tr class="row28">
            <td class="column0 style0 n">2020</td>
            <td class="column1 style0 s">Montgomery Biscuits</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4922</td>
            <td class="column4 style0 n">596</td>
            <td class="column5 style0 n">1147</td>
            <td class="column6 style0 n">63</td>
            <td class="column7 style0 n">558</td>
          </tr>
          <tr class="row29">
            <td class="column0 style0 n">2020</td>
            <td class="column1 style0 s">Down East Wood Ducks</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4984</td>
            <td class="column4 style0 n">589</td>
            <td class="column5 style0 n">1139</td>
            <td class="column6 style0 n">122</td>
            <td class="column7 style0 n">559</td>
          </tr>
          <tr class="row30">
            <td class="column0 style0 n">2020</td>
            <td class="column1 style0 s">Columbia Fireflies</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4899</td>
            <td class="column4 style0 n">563</td>
            <td class="column5 style0 n">1071</td>
            <td class="column6 style0 n">134</td>
            <td class="column7 style0 n">529</td>
          </tr>
          <tr class="row31">
            <td class="column0 style0 n">2020</td>
            <td class="column1 style0 s">Erie SeaWolves</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4848</td>
            <td class="column4 style0 n">541</td>
            <td class="column5 style0 n">1102</td>
            <td class="column6 style0 n">99</td>
            <td class="column7 style0 n">507</td>
          </tr>
          <tr class="row32">
            <td class="column0 style0 n">2020</td>
            <td class="column1 style0 s">Akron RubberDucks</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4722</td>
            <td class="column4 style0 n">500</td>
            <td class="column5 style0 n">1058</td>
            <td class="column6 style0 n">83</td>
            <td class="column7 style0 n">470</td>
          </tr>
          <tr class="row33">
            <td class="column0 style0 n">2019</td>
            <td class="column1 style0 s">Amarillo Sod Poodles</td>
            <td class="column2 style0 n">133</td>
            <td class="column3 style0 n">5322</td>
            <td class="column4 style0 n">692</td>
            <td class="column5 style0 n">1233</td>
            <td class="column6 style0 n">134</td>
            <td class="column7 style0 n">653</td>
          </tr>
          <tr class="row34">
            <td class="column0 style0 n">2019</td>
            <td class="column1 style0 s">Binghamton Rumble Ponies</td>
            <td class="column2 style0 n">133</td>
            <td class="column3 style0 n">5253</td>
            <td class="column4 style0 n">655</td>
            <td class="column5 style0 n">1223</td>
            <td class="column6 style0 n">138</td>
            <td class="column7 style0 n">626</td>
          </tr>
          <tr class="row35">
            <td class="column0 style0 n">2019</td>
            <td class="column1 style0 s">Corpus Christi Hooks</td>
            <td class="column2 style0 n">133</td>
            <td class="column3 style0 n">5190</td>
            <td class="column4 style0 n">643</td>
            <td class="column5 style0 n">1182</td>
            <td class="column6 style0 n">143</td>
            <td class="column7 style0 n">610</td>
          </tr>
          <tr class="row36">
            <td class="column0 style0 n">2019</td>
            <td class="column1 style0 s">Montgomery Biscuits</td>
            <td class="column2 style0 n">133</td>
            <td class="column3 style0 n">5170</td>
            <td class="column4 style0 n">641</td>
            <td class="column5 style0 n">1215</td>
            <td class="column6 style0 n">132</td>
            <td class="column7 style0 n">600</td>
          </tr>
          <tr class="row37">
            <td class="column0 style0 n">2019</td>
            <td class="column1 style0 s">Down East Wood Ducks</td>
            <td class="column2 style0 n">133</td>
            <td class="column3 style0 n">5150</td>
            <td class="column4 style0 n">632</td>
            <td class="column5 style0 n">1213</td>
            <td class="column6 style0 n">140</td>
            <td class="column7 style0 n">605</td>
          </tr>
          <tr class="row38">
            <td class="column0 style0 n">2019</td>
            <td class="column1 style0 s">Columbia Fireflies</td>
            <td class="column2 style0 n">133</td>
            <td class="column3 style0 n">5109</td>
            <td class="column4 style0 n">606</td>
            <td class="column5 style0 n">1200</td>
            <td class="column6 style0 n">89</td>
            <td class="column7 style0 n">573</td>
          </tr>
          <tr class="row39">
            <td class="column0 style0 n">2019</td>
            <td class="column1 style0 s">Erie SeaWolves</td>
            <td class="column2 style0 n">133</td>
            <td class="column3 style0 n">5081</td>
            <td class="column4 style0 n">588</td>
            <td class="column5 style0 n">1150</td>
            <td class="column6 style0 n">102</td>
            <td class="column7 style0 n">554</td>
          </tr>
          <tr class="row40">
            <td class="column0 style0 n">2019</td>
            <td class="column1 style0 s">Akron RubberDucks</td>
            <td class="column2 style0 n">133</td>
            <td class="column3 style0 n">5075</td>
            <td class="column4 style0 n">533</td>
            <td class="column5 style0 n">1125</td>
            <td class="column6 style0 n">88</td>
            <td class="column7 style0 n">500</td>
          </tr>
          <tr class="row41">
            <td class="column0 style0 n">2018</td>
            <td class="column1 style0 s">Amarillo Sod Poodles</td>
            <td class="column2 style0 n">133</td>
            <td class="column3 style0 n">5241</td>
            <td class="column4 style0 n">769</td>
            <td class="column5 style0 n">1295</td>
            <td class="column6 style0 n">213</td>
            <td class="column7 style0 n">744</td>
          </tr>
          <tr class="row42">
            <td class="column0 style0 n">2018</td>
            <td class="column1 style0 s">Binghamton Rumble Ponies</td>
            <td class="column2 style0 n">133</td>
            <td class="column3 style0 n">5312</td>
            <td class="column4 style0 n">723</td>
            <td class="column5 style0 n">1280</td>
            <td class="column6 style0 n">175</td>
            <td class="column7 style0 n">673</td>
          </tr>
          <tr class="row43">
            <td class="column0 style0 n">2018</td>
            <td class="column1 style0 s">Corpus Christi Hooks</td>
            <td class="column2 style0 n">133</td>
            <td class="column3 style0 n">5126</td>
            <td class="column4 style0 n">657</td>
            <td class="column5 style0 n">1211</td>
            <td class="column6 style0 n">129</td>
            <td class="column7 style0 n">626</td>
          </tr>
          <tr class="row44">
            <td class="column0 style0 n">2018</td>
            <td class="column1 style0 s">Montgomery Biscuits</td>
            <td class="column2 style0 n">133</td>
            <td class="column3 style0 n">5157</td>
            <td class="column4 style0 n">644</td>
            <td class="column5 style0 n">1208</td>
            <td class="column6 style0 n">156</td>
            <td class="column7 style0 n">612</td>
          </tr>
          <tr class="row45">
            <td class="column0 style0 n">2018</td>
            <td class="column1 style0 s">Down East Wood Ducks</td>
            <td class="column2 style0 n">133</td>
            <td class="column3 style0 n">5198</td>
            <td class="column4 style0 n">577</td>
            <td class="column5 style0 n">1131</td>
            <td class="column6 style0 n">121</td>
            <td class="column7 style0 n">521</td>
          </tr>
          <tr class="row46">
            <td class="column0 style0 n">2018</td>
            <td class="column1 style0 s">Columbia Fireflies</td>
            <td class="column2 style0 n">133</td>
            <td class="column3 style0 n">5165</td>
            <td class="column4 style0 n">563</td>
            <td class="column5 style0 n">1251</td>
            <td class="column6 style0 n">90</td>
            <td class="column7 style0 n">541</td>
          </tr>
          <tr class="row47">
            <td class="column0 style0 n">2018</td>
            <td class="column1 style0 s">Erie SeaWolves</td>
            <td class="column2 style0 n">133</td>
            <td class="column3 style0 n">4963</td>
            <td class="column4 style0 n">509</td>
            <td class="column5 style0 n">1088</td>
            <td class="column6 style0 n">106</td>
            <td class="column7 style0 n">485</td>
          </tr>
          <tr class="row48">
            <td class="column0 style0 n">2018</td>
            <td class="column1 style0 s">Akron RubberDucks</td>
            <td class="column2 style0 n">133</td>
            <td class="column3 style0 n">4987</td>
            <td class="column4 style0 n">491</td>
            <td class="column5 style0 n">1143</td>
            <td class="column6 style0 n">73</td>
            <td class="column7 style0 n">451</td>
          </tr>
          <tr class="row49">
            <td class="column0 style0 n">2017</td>
            <td class="column1 style0 s">Amarillo Sod Poodles</td>
            <td class="column2 style0 n">133</td>
            <td class="column3 style0 n">5303</td>
            <td class="column4 style0 n">777</td>
            <td class="column5 style0 n">1321</td>
            <td class="column6 style0 n">191</td>
            <td class="column7 style0 n">731</td>
          </tr>
          <tr class="row50">
            <td class="column0 style0 n">2017</td>
            <td class="column1 style0 s">Binghamton Rumble Ponies</td>
            <td class="column2 style0 n">133</td>
            <td class="column3 style0 n">5140</td>
            <td class="column4 style0 n">658</td>
            <td class="column5 style0 n">1160</td>
            <td class="column6 style0 n">173</td>
            <td class="column7 style0 n">643</td>
          </tr>
          <tr class="row51">
            <td class="column0 style0 n">2017</td>
            <td class="column1 style0 s">Corpus Christi Hooks</td>
            <td class="column2 style0 n">133</td>
            <td class="column3 style0 n">5200</td>
            <td class="column4 style0 n">643</td>
            <td class="column5 style0 n">1230</td>
            <td class="column6 style0 n">120</td>
            <td class="column7 style0 n">611</td>
          </tr>
          <tr class="row52">
            <td class="column0 style0 n">2017</td>
            <td class="column1 style0 s">Montgomery Biscuits</td>
            <td class="column2 style0 n">133</td>
            <td class="column3 style0 n">5090</td>
            <td class="column4 style0 n">618</td>
            <td class="column5 style0 n">1207</td>
            <td class="column6 style0 n">158</td>
            <td class="column7 style0 n">587</td>
          </tr>
          <tr class="row53">
            <td class="column0 style0 n">2017</td>
            <td class="column1 style0 s">Down East Wood Ducks</td>
            <td class="column2 style0 n">133</td>
            <td class="column3 style0 n">5060</td>
            <td class="column4 style0 n">603</td>
            <td class="column5 style0 n">1148</td>
            <td class="column6 style0 n">170</td>
            <td class="column7 style0 n">570</td>
          </tr>
          <tr class="row54">
            <td class="column0 style0 n">2017</td>
            <td class="column1 style0 s">Columbia Fireflies</td>
            <td class="column2 style0 n">133</td>
            <td class="column3 style0 n">5083</td>
            <td class="column4 style0 n">587</td>
            <td class="column5 style0 n">1173</td>
            <td class="column6 style0 n">130</td>
            <td class="column7 style0 n">556</td>
          </tr>
          <tr class="row55">
            <td class="column0 style0 n">2017</td>
            <td class="column1 style0 s">Erie SeaWolves</td>
            <td class="column2 style0 n">133</td>
            <td class="column3 style0 n">5120</td>
            <td class="column4 style0 n">583</td>
            <td class="column5 style0 n">1173</td>
            <td class="column6 style0 n">100</td>
            <td class="column7 style0 n">541</td>
          </tr>
          <tr class="row56">
            <td class="column0 style0 n">2017</td>
            <td class="column1 style0 s">Akron RubberDucks</td>
            <td class="column2 style0 n">133</td>
            <td class="column3 style0 n">4985</td>
            <td class="column4 style0 n">463</td>
            <td class="column5 style0 n">1105</td>
            <td class="column6 style0 n">85</td>
            <td class="column7 style0 n">443</td>
          </tr>
          <tr class="row57">
            <td class="column0 style0 n">2016</td>
            <td class="column1 style0 s">Amarillo Sod Poodles</td>
            <td class="column2 style0 n">133</td>
            <td class="column3 style0 n">5279</td>
            <td class="column4 style0 n">739</td>
            <td class="column5 style0 n">1262</td>
            <td class="column6 style0 n">162</td>
            <td class="column7 style0 n">695</td>
          </tr>
          <tr class="row58">
            <td class="column0 style0 n">2016</td>
            <td class="column1 style0 s">Binghamton Rumble Ponies</td>
            <td class="column2 style0 n">133</td>
            <td class="column3 style0 n">5303</td>
            <td class="column4 style0 n">732</td>
            <td class="column5 style0 n">1266</td>
            <td class="column6 style0 n">130</td>
            <td class="column7 style0 n">688</td>
          </tr>
          <tr class="row59">
            <td class="column0 style0 n">2016</td>
            <td class="column1 style0 s">Corpus Christi Hooks</td>
            <td class="column2 style0 n">133</td>
            <td class="column3 style0 n">5308</td>
            <td class="column4 style0 n">718</td>
            <td class="column5 style0 n">1265</td>
            <td class="column6 style0 n">121</td>
            <td class="column7 style0 n">671</td>
          </tr>
          <tr class="row60">
            <td class="column0 style0 n">2016</td>
            <td class="column1 style0 s">Montgomery Biscuits</td>
            <td class="column2 style0 n">133</td>
            <td class="column3 style0 n">5225</td>
            <td class="column4 style0 n">711</td>
            <td class="column5 style0 n">1192</td>
            <td class="column6 style0 n">169</td>
            <td class="column7 style0 n">667</td>
          </tr>
          <tr class="row61">
            <td class="column0 style0 n">2016</td>
            <td class="column1 style0 s">Down East Wood Ducks</td>
            <td class="column2 style0 n">133</td>
            <td class="column3 style0 n">5189</td>
            <td class="column4 style0 n">683</td>
            <td class="column5 style0 n">1263</td>
            <td class="column6 style0 n">142</td>
            <td class="column7 style0 n">637</td>
          </tr>
          <tr class="row62">
            <td class="column0 style0 n">2016</td>
            <td class="column1 style0 s">Columbia Fireflies</td>
            <td class="column2 style0 n">133</td>
            <td class="column3 style0 n">5318</td>
            <td class="column4 style0 n">669</td>
            <td class="column5 style0 n">1247</td>
            <td class="column6 style0 n">85</td>
            <td class="column7 style0 n">630</td>
          </tr>
          <tr class="row63">
            <td class="column0 style0 n">2016</td>
            <td class="column1 style0 s">Erie SeaWolves</td>
            <td class="column2 style0 n">133</td>
            <td class="column3 style0 n">5259</td>
            <td class="column4 style0 n">659</td>
            <td class="column5 style0 n">1255</td>
            <td class="column6 style0 n">148</td>
            <td class="column7 style0 n">628</td>
          </tr>
          <tr class="row64">
            <td class="column0 style0 n">2016</td>
            <td class="column1 style0 s">Akron RubberDucks</td>
            <td class="column2 style0 n">133</td>
            <td class="column3 style0 n">5076</td>
            <td class="column4 style0 n">596</td>
            <td class="column5 style0 n">1143</td>
            <td class="column6 style0 n">113</td>
            <td class="column7 style0 n">555</td>
          </tr>
          <tr class="row65">
            <td class="column0 style0 n">2015</td>
            <td class="column1 style0 s">Amarillo Sod Poodles</td>
            <td class="column2 style0 n">133</td>
            <td class="column3 style0 n">5243</td>
            <td class="column4 style0 n">777</td>
            <td class="column5 style0 n">1245</td>
            <td class="column6 style0 n">208</td>
            <td class="column7 style0 n">736</td>
          </tr>
          <tr class="row66">
            <td class="column0 style0 n">2015</td>
            <td class="column1 style0 s">Binghamton Rumble Ponies</td>
            <td class="column2 style0 n">133</td>
            <td class="column3 style0 n">4904</td>
            <td class="column4 style0 n">694</td>
            <td class="column5 style0 n">1149</td>
            <td class="column6 style0 n">157</td>
            <td class="column7 style0 n">651</td>
          </tr>
          <tr class="row67">
            <td class="column0 style0 n">2015</td>
            <td class="column1 style0 s">Corpus Christi Hooks</td>
            <td class="column2 style0 n">133</td>
            <td class="column3 style0 n">5213</td>
            <td class="column4 style0 n">694</td>
            <td class="column5 style0 n">1325</td>
            <td class="column6 style0 n">150</td>
            <td class="column7 style0 n">661</td>
          </tr>
          <tr class="row68">
            <td class="column0 style0 n">2015</td>
            <td class="column1 style0 s">Montgomery Biscuits</td>
            <td class="column2 style0 n">133</td>
            <td class="column3 style0 n">5094</td>
            <td class="column4 style0 n">666</td>
            <td class="column5 style0 n">1191</td>
            <td class="column6 style0 n">107</td>
            <td class="column7 style0 n">604</td>
          </tr>
          <tr class="row69">
            <td class="column0 style0 n">2015</td>
            <td class="column1 style0 s">Down East Wood Ducks</td>
            <td class="column2 style0 n">133</td>
            <td class="column3 style0 n">4992</td>
            <td class="column4 style0 n">656</td>
            <td class="column5 style0 n">1224</td>
            <td class="column6 style0 n">172</td>
            <td class="column7 style0 n">628</td>
          </tr>
          <tr class="row70">
            <td class="column0 style0 n">2015</td>
            <td class="column1 style0 s">Columbia Fireflies</td>
            <td class="column2 style0 n">133</td>
            <td class="column3 style0 n">5178</td>
            <td class="column4 style0 n">603</td>
            <td class="column5 style0 n">1186</td>
            <td class="column6 style0 n">104</td>
            <td class="column7 style0 n">553</td>
          </tr>
          <tr class="row71">
            <td class="column0 style0 n">2015</td>
            <td class="column1 style0 s">Erie SeaWolves</td>
            <td class="column2 style0 n">133</td>
            <td class="column3 style0 n">4818</td>
            <td class="column4 style0 n">544</td>
            <td class="column5 style0 n">1068</td>
            <td class="column6 style0 n">82</td>
            <td class="column7 style0 n">512</td>
          </tr>
          <tr class="row72">
            <td class="column0 style0 n">2015</td>
            <td class="column1 style0 s">Akron RubberDucks</td>
            <td class="column2 style0 n">133</td>
            <td class="column3 style0 n">4586</td>
            <td class="column4 style0 n">542</td>
            <td class="column5 style0 n">1059</td>
            <td class="column6 style0 n">89</td>
            <td class="column7 style0 n">496</td>
          </tr>
          <tr class="row73">
            <td class="column0 style0 n">2014</td>
            <td class="column1 style0 s">Amarillo Sod Poodles</td>
            <td class="column2 style0 n">132</td>
            <td class="column3 style0 n">5186</td>
            <td class="column4 style0 n">753</td>
            <td class="column5 style0 n">1309</td>
            <td class="column6 style0 n">145</td>
            <td class="column7 style0 n">709</td>
          </tr>
          <tr class="row74">
            <td class="column0 style0 n">2014</td>
            <td class="column1 style0 s">Binghamton Rumble Ponies</td>
            <td class="column2 style0 n">132</td>
            <td class="column3 style0 n">5180</td>
            <td class="column4 style0 n">744</td>
            <td class="column5 style0 n">1287</td>
            <td class="column6 style0 n">145</td>
            <td class="column7 style0 n">700</td>
          </tr>
          <tr class="row75">
            <td class="column0 style0 n">2014</td>
            <td class="column1 style0 s">Corpus Christi Hooks</td>
            <td class="column2 style0 n">132</td>
            <td class="column3 style0 n">5148</td>
            <td class="column4 style0 n">740</td>
            <td class="column5 style0 n">1218</td>
            <td class="column6 style0 n">204</td>
            <td class="column7 style0 n">697</td>
          </tr>
          <tr class="row76">
            <td class="column0 style0 n">2014</td>
            <td class="column1 style0 s">Montgomery Biscuits</td>
            <td class="column2 style0 n">132</td>
            <td class="column3 style0 n">5050</td>
            <td class="column4 style0 n">727</td>
            <td class="column5 style0 n">1266</td>
            <td class="column6 style0 n">197</td>
            <td class="column7 style0 n">685</td>
          </tr>
          <tr class="row77">
            <td class="column0 style0 n">2014</td>
            <td class="column1 style0 s">Down East Wood Ducks</td>
            <td class="column2 style0 n">132</td>
            <td class="column3 style0 n">4865</td>
            <td class="column4 style0 n">720</td>
            <td class="column5 style0 n">1179</td>
            <td class="column6 style0 n">205</td>
            <td class="column7 style0 n">680</td>
          </tr>
          <tr class="row78">
            <td class="column0 style0 n">2014</td>
            <td class="column1 style0 s">Columbia Fireflies</td>
            <td class="column2 style0 n">132</td>
            <td class="column3 style0 n">5249</td>
            <td class="column4 style0 n">697</td>
            <td class="column5 style0 n">1207</td>
            <td class="column6 style0 n">142</td>
            <td class="column7 style0 n">651</td>
          </tr>
          <tr class="row79">
            <td class="column0 style0 n">2014</td>
            <td class="column1 style0 s">Erie SeaWolves</td>
            <td class="column2 style0 n">132</td>
            <td class="column3 style0 n">4997</td>
            <td class="column4 style0 n">691</td>
            <td class="column5 style0 n">1266</td>
            <td class="column6 style0 n">133</td>
            <td class="column7 style0 n">668</td>
          </tr>
          <tr class="row80">
            <td class="column0 style0 n">2014</td>
            <td class="column1 style0 s">Akron RubberDucks</td>
            <td class="column2 style0 n">132</td>
            <td class="column3 style0 n">4407</td>
            <td class="column4 style0 n">461</td>
            <td class="column5 style0 n">979</td>
            <td class="column6 style0 n">81</td>
            <td class="column7 style0 n">438</td>
          </tr>
          <tr class="row81">
            <td class="column0 style0 n">2013</td>
            <td class="column1 style0 s">Amarillo Sod Poodles</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4709</td>
            <td class="column4 style0 n">622</td>
            <td class="column5 style0 n">1107</td>
            <td class="column6 style0 n">141</td>
            <td class="column7 style0 n">584</td>
          </tr>
          <tr class="row82">
            <td class="column0 style0 n">2013</td>
            <td class="column1 style0 s">Binghamton Rumble Ponies</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4917</td>
            <td class="column4 style0 n">620</td>
            <td class="column5 style0 n">1143</td>
            <td class="column6 style0 n">143</td>
            <td class="column7 style0 n">576</td>
          </tr>
          <tr class="row83">
            <td class="column0 style0 n">2013</td>
            <td class="column1 style0 s">Corpus Christi Hooks</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4564</td>
            <td class="column4 style0 n">578</td>
            <td class="column5 style0 n">1081</td>
            <td class="column6 style0 n">99</td>
            <td class="column7 style0 n">545</td>
          </tr>
          <tr class="row84">
            <td class="column0 style0 n">2013</td>
            <td class="column1 style0 s">Montgomery Biscuits</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4677</td>
            <td class="column4 style0 n">528</td>
            <td class="column5 style0 n">1051</td>
            <td class="column6 style0 n">84</td>
            <td class="column7 style0 n">493</td>
          </tr>
          <tr class="row85">
            <td class="column0 style0 n">2013</td>
            <td class="column1 style0 s">Down East Wood Ducks</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4503</td>
            <td class="column4 style0 n">499</td>
            <td class="column5 style0 n">1042</td>
            <td class="column6 style0 n">102</td>
            <td class="column7 style0 n">467</td>
          </tr>
          <tr class="row86">
            <td class="column0 style0 n">2013</td>
            <td class="column1 style0 s">Columbia Fireflies</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4671</td>
            <td class="column4 style0 n">489</td>
            <td class="column5 style0 n">1066</td>
            <td class="column6 style0 n">94</td>
            <td class="column7 style0 n">466</td>
          </tr>
          <tr class="row87">
            <td class="column0 style0 n">2013</td>
            <td class="column1 style0 s">Erie SeaWolves</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4503</td>
            <td class="column4 style0 n">481</td>
            <td class="column5 style0 n">1012</td>
            <td class="column6 style0 n">120</td>
            <td class="column7 style0 n">455</td>
          </tr>
          <tr class="row88">
            <td class="column0 style0 n">2013</td>
            <td class="column1 style0 s">Akron RubberDucks</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4042</td>
            <td class="column4 style0 n">451</td>
            <td class="column5 style0 n">918</td>
            <td class="column6 style0 n">86</td>
            <td class="column7 style0 n">420</td>
          </tr>
          <tr class="row89">
            <td class="column0 style0 n">2012</td>
            <td class="column1 style0 s">Amarillo Sod Poodles</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4761</td>
            <td class="column4 style0 n">703</td>
            <td class="column5 style0 n">1158</td>
            <td class="column6 style0 n">163</td>
            <td class="column7 style0 n">653</td>
          </tr>
          <tr class="row90">
            <td class="column0 style0 n">2012</td>
            <td class="column1 style0 s">Binghamton Rumble Ponies</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4824</td>
            <td class="column4 style0 n">616</td>
            <td class="column5 style0 n">1081</td>
            <td class="column6 style0 n">133</td>
            <td class="column7 style0 n">578</td>
          </tr>
          <tr class="row91">
            <td class="column0 style0 n">2012</td>
            <td class="column1 style0 s">Corpus Christi Hooks</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4819</td>
            <td class="column4 style0 n">590</td>
            <td class="column5 style0 n">1109</td>
            <td class="column6 style0 n">83</td>
            <td class="column7 style0 n">549</td>
          </tr>
          <tr class="row92">
            <td class="column0 style0 n">2012</td>
            <td class="column1 style0 s">Montgomery Biscuits</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4451</td>
            <td class="column4 style0 n">569</td>
            <td class="column5 style0 n">1027</td>
            <td class="column6 style0 n">101</td>
            <td class="column7 style0 n">522</td>
          </tr>
          <tr class="row93">
            <td class="column0 style0 n">2012</td>
            <td class="column1 style0 s">Down East Wood Ducks</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4751</td>
            <td class="column4 style0 n">504</td>
            <td class="column5 style0 n">1012</td>
            <td class="column6 style0 n">82</td>
            <td class="column7 style0 n">462</td>
          </tr>
          <tr class="row94">
            <td class="column0 style0 n">2012</td>
            <td class="column1 style0 s">Columbia Fireflies</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4679</td>
            <td class="column4 style0 n">502</td>
            <td class="column5 style0 n">1052</td>
            <td class="column6 style0 n">84</td>
            <td class="column7 style0 n">473</td>
          </tr>
          <tr class="row95">
            <td class="column0 style0 n">2012</td>
            <td class="column1 style0 s">Erie SeaWolves</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4537</td>
            <td class="column4 style0 n">472</td>
            <td class="column5 style0 n">998</td>
            <td class="column6 style0 n">101</td>
            <td class="column7 style0 n">434</td>
          </tr>
          <tr class="row96">
            <td class="column0 style0 n">2012</td>
            <td class="column1 style0 s">Akron RubberDucks</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4457</td>
            <td class="column4 style0 n">424</td>
            <td class="column5 style0 n">938</td>
            <td class="column6 style0 n">75</td>
            <td class="column7 style0 n">405</td>
          </tr>
          <tr class="row97">
            <td class="column0 style0 n">2011</td>
            <td class="column1 style0 s">Amarillo Sod Poodles</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4812</td>
            <td class="column4 style0 n">566</td>
            <td class="column5 style0 n">1161</td>
            <td class="column6 style0 n">72</td>
            <td class="column7 style0 n">543</td>
          </tr>
          <tr class="row98">
            <td class="column0 style0 n">2011</td>
            <td class="column1 style0 s">Binghamton Rumble Ponies</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4799</td>
            <td class="column4 style0 n">545</td>
            <td class="column5 style0 n">1085</td>
            <td class="column6 style0 n">58</td>
            <td class="column7 style0 n">489</td>
          </tr>
          <tr class="row99">
            <td class="column0 style0 n">2011</td>
            <td class="column1 style0 s">Corpus Christi Hooks</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4736</td>
            <td class="column4 style0 n">522</td>
            <td class="column5 style0 n">999</td>
            <td class="column6 style0 n">90</td>
            <td class="column7 style0 n">498</td>
          </tr>
          <tr class="row100">
            <td class="column0 style0 n">2011</td>
            <td class="column1 style0 s">Montgomery Biscuits</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4484</td>
            <td class="column4 style0 n">515</td>
            <td class="column5 style0 n">970</td>
            <td class="column6 style0 n">89</td>
            <td class="column7 style0 n">490</td>
          </tr>
          <tr class="row101">
            <td class="column0 style0 n">2011</td>
            <td class="column1 style0 s">Down East Wood Ducks</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4609</td>
            <td class="column4 style0 n">504</td>
            <td class="column5 style0 n">992</td>
            <td class="column6 style0 n">93</td>
            <td class="column7 style0 n">473</td>
          </tr>
          <tr class="row102">
            <td class="column0 style0 n">2011</td>
            <td class="column1 style0 s">Columbia Fireflies</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4729</td>
            <td class="column4 style0 n">493</td>
            <td class="column5 style0 n">1001</td>
            <td class="column6 style0 n">106</td>
            <td class="column7 style0 n">462</td>
          </tr>
          <tr class="row103">
            <td class="column0 style0 n">2011</td>
            <td class="column1 style0 s">Erie SeaWolves</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4444</td>
            <td class="column4 style0 n">482</td>
            <td class="column5 style0 n">974</td>
            <td class="column6 style0 n">84</td>
            <td class="column7 style0 n">461</td>
          </tr>
          <tr class="row104">
            <td class="column0 style0 n">2011</td>
            <td class="column1 style0 s">Akron RubberDucks</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4653</td>
            <td class="column4 style0 n">446</td>
            <td class="column5 style0 n">1008</td>
            <td class="column6 style0 n">82</td>
            <td class="column7 style0 n">410</td>
          </tr>
          <tr class="row105">
            <td class="column0 style0 n">2010</td>
            <td class="column1 style0 s">Amarillo Sod Poodles</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4850</td>
            <td class="column4 style0 n">628</td>
            <td class="column5 style0 n">1154</td>
            <td class="column6 style0 n">106</td>
            <td class="column7 style0 n">585</td>
          </tr>
          <tr class="row106">
            <td class="column0 style0 n">2010</td>
            <td class="column1 style0 s">Binghamton Rumble Ponies</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4830</td>
            <td class="column4 style0 n">590</td>
            <td class="column5 style0 n">1071</td>
            <td class="column6 style0 n">65</td>
            <td class="column7 style0 n">553</td>
          </tr>
          <tr class="row107">
            <td class="column0 style0 n">2010</td>
            <td class="column1 style0 s">Corpus Christi Hooks</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4739</td>
            <td class="column4 style0 n">558</td>
            <td class="column5 style0 n">1046</td>
            <td class="column6 style0 n">94</td>
            <td class="column7 style0 n">516</td>
          </tr>
          <tr class="row108">
            <td class="column0 style0 n">2010</td>
            <td class="column1 style0 s">Montgomery Biscuits</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4752</td>
            <td class="column4 style0 n">527</td>
            <td class="column5 style0 n">1064</td>
            <td class="column6 style0 n">79</td>
            <td class="column7 style0 n">472</td>
          </tr>
          <tr class="row109">
            <td class="column0 style0 n">2010</td>
            <td class="column1 style0 s">Down East Wood Ducks</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4709</td>
            <td class="column4 style0 n">508</td>
            <td class="column5 style0 n">1028</td>
            <td class="column6 style0 n">96</td>
            <td class="column7 style0 n">475</td>
          </tr>
          <tr class="row110">
            <td class="column0 style0 n">2010</td>
            <td class="column1 style0 s">Columbia Fireflies</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4708</td>
            <td class="column4 style0 n">476</td>
            <td class="column5 style0 n">1054</td>
            <td class="column6 style0 n">83</td>
            <td class="column7 style0 n">438</td>
          </tr>
          <tr class="row111">
            <td class="column0 style0 n">2010</td>
            <td class="column1 style0 s">Erie SeaWolves</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4412</td>
            <td class="column4 style0 n">442</td>
            <td class="column5 style0 n">915</td>
            <td class="column6 style0 n">82</td>
            <td class="column7 style0 n">419</td>
          </tr>
          <tr class="row112">
            <td class="column0 style0 n">2010</td>
            <td class="column1 style0 s">Akron RubberDucks</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4634</td>
            <td class="column4 style0 n">431</td>
            <td class="column5 style0 n">989</td>
            <td class="column6 style0 n">75</td>
            <td class="column7 style0 n">397</td>
          </tr>
          <tr class="row113">
            <td class="column0 style0 n">2009</td>
            <td class="column1 style0 s">Amarillo Sod Poodles</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4885</td>
            <td class="column4 style0 n">655</td>
            <td class="column5 style0 n">1204</td>
            <td class="column6 style0 n">88</td>
            <td class="column7 style0 n">612</td>
          </tr>
          <tr class="row114">
            <td class="column0 style0 n">2009</td>
            <td class="column1 style0 s">Binghamton Rumble Ponies</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4706</td>
            <td class="column4 style0 n">560</td>
            <td class="column5 style0 n">1144</td>
            <td class="column6 style0 n">92</td>
            <td class="column7 style0 n">527</td>
          </tr>
          <tr class="row115">
            <td class="column0 style0 n">2009</td>
            <td class="column1 style0 s">Corpus Christi Hooks</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4801</td>
            <td class="column4 style0 n">541</td>
            <td class="column5 style0 n">1081</td>
            <td class="column6 style0 n">106</td>
            <td class="column7 style0 n">510</td>
          </tr>
          <tr class="row116">
            <td class="column0 style0 n">2009</td>
            <td class="column1 style0 s">Montgomery Biscuits</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4664</td>
            <td class="column4 style0 n">494</td>
            <td class="column5 style0 n">1025</td>
            <td class="column6 style0 n">87</td>
            <td class="column7 style0 n">455</td>
          </tr>
          <tr class="row117">
            <td class="column0 style0 n">2009</td>
            <td class="column1 style0 s">Down East Wood Ducks</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4710</td>
            <td class="column4 style0 n">489</td>
            <td class="column5 style0 n">1072</td>
            <td class="column6 style0 n">58</td>
            <td class="column7 style0 n">457</td>
          </tr>
          <tr class="row118">
            <td class="column0 style0 n">2009</td>
            <td class="column1 style0 s">Columbia Fireflies</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4637</td>
            <td class="column4 style0 n">485</td>
            <td class="column5 style0 n">988</td>
            <td class="column6 style0 n">91</td>
            <td class="column7 style0 n">453</td>
          </tr>
          <tr class="row119">
            <td class="column0 style0 n">2009</td>
            <td class="column1 style0 s">Erie SeaWolves</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4691</td>
            <td class="column4 style0 n">482</td>
            <td class="column5 style0 n">1002</td>
            <td class="column6 style0 n">68</td>
            <td class="column7 style0 n">444</td>
          </tr>
          <tr class="row120">
            <td class="column0 style0 n">2009</td>
            <td class="column1 style0 s">Akron RubberDucks</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4656</td>
            <td class="column4 style0 n">477</td>
            <td class="column5 style0 n">1013</td>
            <td class="column6 style0 n">75</td>
            <td class="column7 style0 n">459</td>
          </tr>
          <tr class="row121">
            <td class="column0 style0 n">2008</td>
            <td class="column1 style0 s">Amarillo Sod Poodles</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4772</td>
            <td class="column4 style0 n">606</td>
            <td class="column5 style0 n">1130</td>
            <td class="column6 style0 n">133</td>
            <td class="column7 style0 n">575</td>
          </tr>
          <tr class="row122">
            <td class="column0 style0 n">2008</td>
            <td class="column1 style0 s">Binghamton Rumble Ponies</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4704</td>
            <td class="column4 style0 n">513</td>
            <td class="column5 style0 n">1030</td>
            <td class="column6 style0 n">95</td>
            <td class="column7 style0 n">465</td>
          </tr>
          <tr class="row123">
            <td class="column0 style0 n">2008</td>
            <td class="column1 style0 s">Corpus Christi Hooks</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4730</td>
            <td class="column4 style0 n">496</td>
            <td class="column5 style0 n">1069</td>
            <td class="column6 style0 n">74</td>
            <td class="column7 style0 n">463</td>
          </tr>
          <tr class="row124">
            <td class="column0 style0 n">2008</td>
            <td class="column1 style0 s">Montgomery Biscuits</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4739</td>
            <td class="column4 style0 n">473</td>
            <td class="column5 style0 n">1066</td>
            <td class="column6 style0 n">59</td>
            <td class="column7 style0 n">441</td>
          </tr>
          <tr class="row125">
            <td class="column0 style0 n">2008</td>
            <td class="column1 style0 s">Down East Wood Ducks</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4707</td>
            <td class="column4 style0 n">454</td>
            <td class="column5 style0 n">979</td>
            <td class="column6 style0 n">81</td>
            <td class="column7 style0 n">426</td>
          </tr>
          <tr class="row126">
            <td class="column0 style0 n">2008</td>
            <td class="column1 style0 s">Columbia Fireflies</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4674</td>
            <td class="column4 style0 n">452</td>
            <td class="column5 style0 n">1013</td>
            <td class="column6 style0 n">29</td>
            <td class="column7 style0 n">422</td>
          </tr>
          <tr class="row127">
            <td class="column0 style0 n">2008</td>
            <td class="column1 style0 s">Erie SeaWolves</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4545</td>
            <td class="column4 style0 n">366</td>
            <td class="column5 style0 n">903</td>
            <td class="column6 style0 n">46</td>
            <td class="column7 style0 n">342</td>
          </tr>
          <tr class="row128">
            <td class="column0 style0 n">2008</td>
            <td class="column1 style0 s">Akron RubberDucks</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4532</td>
            <td class="column4 style0 n">342</td>
            <td class="column5 style0 n">913</td>
            <td class="column6 style0 n">35</td>
            <td class="column7 style0 n">314</td>
          </tr>
          <tr class="row129">
            <td class="column0 style0 n">2007</td>
            <td class="column1 style0 s">Amarillo Sod Poodles</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4903</td>
            <td class="column4 style0 n">701</td>
            <td class="column5 style0 n">1139</td>
            <td class="column6 style0 n">138</td>
            <td class="column7 style0 n">659</td>
          </tr>
          <tr class="row130">
            <td class="column0 style0 n">2007</td>
            <td class="column1 style0 s">Binghamton Rumble Ponies</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4903</td>
            <td class="column4 style0 n">663</td>
            <td class="column5 style0 n">1213</td>
            <td class="column6 style0 n">68</td>
            <td class="column7 style0 n">619</td>
          </tr>
          <tr class="row131">
            <td class="column0 style0 n">2007</td>
            <td class="column1 style0 s">Corpus Christi Hooks</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4866</td>
            <td class="column4 style0 n">658</td>
            <td class="column5 style0 n">1120</td>
            <td class="column6 style0 n">146</td>
            <td class="column7 style0 n">620</td>
          </tr>
          <tr class="row132">
            <td class="column0 style0 n">2007</td>
            <td class="column1 style0 s">Montgomery Biscuits</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4841</td>
            <td class="column4 style0 n">623</td>
            <td class="column5 style0 n">1110</td>
            <td class="column6 style0 n">123</td>
            <td class="column7 style0 n">578</td>
          </tr>
          <tr class="row133">
            <td class="column0 style0 n">2007</td>
            <td class="column1 style0 s">Down East Wood Ducks</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4830</td>
            <td class="column4 style0 n">547</td>
            <td class="column5 style0 n">1096</td>
            <td class="column6 style0 n">110</td>
            <td class="column7 style0 n">512</td>
          </tr>
          <tr class="row134">
            <td class="column0 style0 n">2007</td>
            <td class="column1 style0 s">Columbia Fireflies</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4435</td>
            <td class="column4 style0 n">518</td>
            <td class="column5 style0 n">1008</td>
            <td class="column6 style0 n">105</td>
            <td class="column7 style0 n">508</td>
          </tr>
          <tr class="row135">
            <td class="column0 style0 n">2007</td>
            <td class="column1 style0 s">Erie SeaWolves</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4578</td>
            <td class="column4 style0 n">495</td>
            <td class="column5 style0 n">981</td>
            <td class="column6 style0 n">90</td>
            <td class="column7 style0 n">447</td>
          </tr>
          <tr class="row136">
            <td class="column0 style0 n">2007</td>
            <td class="column1 style0 s">Akron RubberDucks</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4306</td>
            <td class="column4 style0 n">469</td>
            <td class="column5 style0 n">950</td>
            <td class="column6 style0 n">75</td>
            <td class="column7 style0 n">405</td>
          </tr>
          <tr class="row137">
            <td class="column0 style0 n">2006</td>
            <td class="column1 style0 s">Amarillo Sod Poodles</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4870</td>
            <td class="column4 style0 n">644</td>
            <td class="column5 style0 n">1155</td>
            <td class="column6 style0 n">136</td>
            <td class="column7 style0 n">608</td>
          </tr>
          <tr class="row138">
            <td class="column0 style0 n">2006</td>
            <td class="column1 style0 s">Binghamton Rumble Ponies</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4873</td>
            <td class="column4 style0 n">639</td>
            <td class="column5 style0 n">1138</td>
            <td class="column6 style0 n">108</td>
            <td class="column7 style0 n">592</td>
          </tr>
          <tr class="row139">
            <td class="column0 style0 n">2006</td>
            <td class="column1 style0 s">Corpus Christi Hooks</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4843</td>
            <td class="column4 style0 n">618</td>
            <td class="column5 style0 n">1069</td>
            <td class="column6 style0 n">144</td>
            <td class="column7 style0 n">594</td>
          </tr>
          <tr class="row140">
            <td class="column0 style0 n">2006</td>
            <td class="column1 style0 s">Montgomery Biscuits</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4812</td>
            <td class="column4 style0 n">583</td>
            <td class="column5 style0 n">1072</td>
            <td class="column6 style0 n">73</td>
            <td class="column7 style0 n">533</td>
          </tr>
          <tr class="row141">
            <td class="column0 style0 n">2006</td>
            <td class="column1 style0 s">Down East Wood Ducks</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4469</td>
            <td class="column4 style0 n">528</td>
            <td class="column5 style0 n">978</td>
            <td class="column6 style0 n">85</td>
            <td class="column7 style0 n">487</td>
          </tr>
          <tr class="row142">
            <td class="column0 style0 n">2006</td>
            <td class="column1 style0 s">Columbia Fireflies</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4787</td>
            <td class="column4 style0 n">501</td>
            <td class="column5 style0 n">1054</td>
            <td class="column6 style0 n">59</td>
            <td class="column7 style0 n">460</td>
          </tr>
          <tr class="row143">
            <td class="column0 style0 n">2006</td>
            <td class="column1 style0 s">Erie SeaWolves</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4680</td>
            <td class="column4 style0 n">472</td>
            <td class="column5 style0 n">1009</td>
            <td class="column6 style0 n">53</td>
            <td class="column7 style0 n">430</td>
          </tr>
          <tr class="row144">
            <td class="column0 style0 n">2006</td>
            <td class="column1 style0 s">Akron RubberDucks</td>
            <td class="column2 style0 n">126</td>
            <td class="column3 style0 n">4672</td>
            <td class="column4 style0 n">426</td>
            <td class="column5 style0 n">974</td>
            <td class="column6 style0 n">51</td>
            <td class="column7 style0 n">395</td>
          </tr>
        </tbody>
    </table>


<div aria-live="polite" id="bit-notification-bar" style="height: 0px; width: 100%; top: 0px; left: 0px; padding: 0px; position: fixed; z-index: 2147483647; visibility: visible;"><iframe style="height: 0px; width: 100%; border: 0px; min-height: initial;" id="bit-notification-bar-iframe" src="moz-extension://a931a247-baa3-4405-8d8d-a95a659c5dd2/notification/bar.html"></iframe></div></body></html>"""

# Parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Find the tbody element containing player data
# tbody = soup.find('tbody', id='data-body')

# Initialize total goals
hrs = 0

tr = soup.find_all('tr')

# Loop through each row in the tbody
for row in tr:
    td = row.find_all('td')
    if td[6].get_text() != "homeruns":
        hrs += int(td[6].get_text())

# Print the total goals
print("Total Goals:", hrs)
