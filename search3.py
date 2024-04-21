# https://webscrape3-dot-chunin.uc.r.appspot.com/login
# username: datathon_participant
# password: interaction1234

from bs4 import BeautifulSoup

# HTML content
html_content = """
<html lang="en"><head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="/decrypt.css">
<script src="moz-extension://a931a247-baa3-4405-8d8d-a95a659c5dd2/content/fido2/page-script.js" id="bw-fido2-page-script"></script><link href="data:text/css,%3Ais(%5Bid*%3D'google_ads_iframe'%5D%2C%5Bid*%3D'taboola-'%5D%2C.taboolaHeight%2C.taboola-placeholder%2C%23credential_picker_container%2C%23credentials-picker-container%2C%23credential_picker_iframe%2C%5Bid*%3D'google-one-tap-iframe'%5D%2C%23google-one-tap-popup-container%2C.google-one-tap-modal-div%2C%23amp_floatingAdDiv%2C%23ez-content-blocker-container)%20%7Bdisplay%3Anone!important%3Bmin-height%3A0!important%3Bheight%3A0!important%3B%7D" rel="stylesheet" type="text/css"><style>.rdp {
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

<body class="vsc-initialized">
    <div class="decryptionForm">
        <h2>Decrypt the Messages</h2>
        <input type="text" id="decryptionBox" placeholder="Decryption Box">
        <button id="decrypt">Decrypt</button>
        <input type="text" id="decrypted" placeholder="Decrypted Text">
    </div>
    <div class="encryptedData">
        <p>726f746a6a6e7e76</p>
        <p>6f6e6c617c636e73</p>
        <p>607d6b6d676f6f6b</p>
        <p>6a7c716f7772746a</p>
        <p>696f7d6f736b6e72</p>
        <p>707160666b68777e</p>
        <p>6765616d756d6c7c</p>
        <p>68717e746c6c6769</p>
        <p>746765766860737e</p>
        <p>7468776e726c7c77</p>
        <p>656d767e6962776f</p>
        <p>7d7c656370756c74</p>
        <p>6368626b68757574</p>
        <p>776e767c6a6c7c6f</p>
        <p>7e60676c65657e65</p>
        <p>636e73767473626e</p>
        <p>6674686f7e7d7567</p>
        <p>696c7d637d6c6d6f</p>
        <p>746e76747d61686a</p>
        <p>706d7d7662686d7d</p>
        <p>777d696b666d6c6d</p>
        <p>6c777e686f6b6c7d</p>
        <p>7e726b72616e7c77</p>
        <p>7666636575746563</p>
        <p>6d6c7d777068757c</p>
        <p>6a7d736e69717c60</p>
        <p>6e7c626569627566</p>
        <p>6b7163636b72687c</p>
        <p>6660757266686f61</p>
        <p>6c7c6060686d7762</p>
        <p>6d6970766d687363</p>
        <p>696c727069617373</p>
        <p>6362676a686f766c</p>
        <p>6d6b6d70716c6370</p>
        <p>7e6765616f706067</p>
        <p>6e6363746a6b7475</p>
        <p>696f6a6867656874</p>
        <p>6e637d6f73717e72</p>
        <p>696877686e637574</p>
        <p>6577726177756a71</p>
        <p>6b6370747d716566</p>
        <p>7c6961617465666f</p>
        <p>656b60696c6e7471</p>
        <p>6b626b6a766f6b7c</p>
        <p>6166666572776571</p>
        <p>696176627c716170</p>
        <p>75727e6e68627074</p>
        <p>75776976757d6d73</p>
        <p>71636071766a6c73</p>
        <p>65637c6c6a777d68</p>
        <p>6b70756173686772</p>
        <p>6561637c667c6f6b</p>
        <p>637c7561637d7d67</p>
        <p>71627c657c77706f</p>
        <p>7e62626f6a63756b</p>
        <p>63637e6274666865</p>
        <p>756f746d6a716f6c</p>
        <p>6e766f6a677e7668</p>
        <p>7d606761747c6a7e</p>
        <p>607e7d7160707562</p>
        <p>7471736566756362</p>
        <p>7e60747167696868</p>
        <p>7462687d6a6c6a68</p>
        <p>656d726b7774626b</p>
        <p>76736f6567737677</p>
        <p>63767262626d7569</p>
        <p>726b63626d726662</p>
        <p>7c737372746a7c76</p>
        <p>6c63747d6c71717d</p>
        <p>616d63726b62757e</p>
        <p>69636c73617d7e67</p>
        <p>637c7e6275637465</p>
        <p>6a746e6261707766</p>
        <p>7175727772777e6b</p>
        <p>7d7d6765766e7e67</p>
        <p>7474626c63666c74</p>
        <p>7d636a667170666f</p>
        <p>71747171627e766d</p>
        <p>6a76666f7e7e676b</p>
        <p>7d7c756c7576766b</p>
        <p>77737d7460696174</p>
        <p>6b65667c606e7363</p>
        <p>6b7c676177777d66</p>
        <p>72616b656a636777</p>
        <p>6a6d6573716e6c69</p>
        <p>6c72776a72656f69</p>
        <p>7d6d71737674636d</p>
        <p>736d6c6269616d60</p>
        <p>756b75607e7d736f</p>
        <p>7c677d75626e6d65</p>
        <p>6976757c616c6161</p>
        <p>756e656d626d776c</p>
        <p>776c686f6f7e7673</p>
        <p>717e7d7e6c696e71</p>
        <p>666f6c617c767c72</p>
        <p>7266656f70747567</p>
        <p>6f707c7d6f6b6767</p>
        <p>716e7c6a72746066</p>
        <p>7d70686a6f707e77</p>
        <p>6d6069607d696170</p>
        <p>7362746977777262</p>
        <p>6d6d7d6063656868</p>
        <p>6c71756663716861</p>
        <p>7c736d74667e7473</p>
        <p>637170606a7e706b</p>
        <p>6a6f7776776e6171</p>
        <p>73676b676f6f6661</p>
        <p>777e7d7275726065</p>
        <p>73687267756a6f63</p>
        <p>7d68656667726a63</p>
        <p>726f687461737e62</p>
        <p>766d737e65737e63</p>
        <p>6260677676766e60</p>
        <p>6a727e7e706b726a</p>
        <p>686174667167747d</p>
        <p>6267706f627e6e69</p>
        <p>7763756d637e6873</p>
        <p>72666c77707c6b65</p>
        <p>6b696a6375607c6a</p>
        <p>746d62696d626a73</p>
        <p>6e636f6674706f72</p>
        <p>7069616a6770696c</p>
        <p>606d6e7077617571</p>
        <p>7360636365696b70</p>
        <p>636e696d7e72637d</p>
        <p>767765656f6e6074</p>
        <p>686a696374637c6f</p>
        <p>6e7d6a70776a7d6d</p>
        <p>726a716975737367</p>
        <p>6b7d726372746e68</p>
        <p>6066606161766e76</p>
        <p>607d757463716a7e</p>
        <p>6676616776616677</p>
        <p>77656a6268656f6f</p>
        <p>6f67626167737c67</p>
        <p>7466616a6f7d6160</p>
        <p>777275617167666e</p>
        <p>7c6a6c77706e6175</p>
        <p>626b6d677d68626e</p>
        <p>69606c6d6e697e71</p>
        <p>6e7577777076766b</p>
        <p>6860716771636b70</p>
        <p>686f7d666c606665</p>
        <p>746f6b7074687c66</p>
        <p>687662766277686f</p>
        <p>6b677e706c74757d</p>
        <p>6e7e6f656c627c75</p>
        <p>7570776a7063716b</p>
        <p>626b6763727d6575</p>
        <p>6d6770776e657768</p>
        <p>6171687c77637265</p>
        <p>7676687d626b7c67</p>
        <p>6771616b6267656d</p>
        <p>6c76737e6f736361</p>
        <p>667e746072636d6c</p>
        <p>667574737e636e6b</p>
        <p>726d60697475737d</p>
        <p>65687e75706f737c</p>
        <p>7d72606e61766d6c</p>
        <p>6e7c696d666c6677</p>
        <p>6a626f7e6274757c</p>
        <p>656d71747c616d6f</p>
        <p>6c6d71697e656072</p>
        <p>676c677562616674</p>
        <p>6d6b747e6e7d6d72</p>
        <p>69696b7463706b6b</p>
        <p>666e7d6c62696665</p>
        <p>6d77627476667c61</p>
        <p>7667767560757669</p>
        <p>6660776a77696962</p>
        <p>697c7c7663766a6f</p>
        <p>60696a60667d6b65</p>
        <p>6372606561657467</p>
        <p>776f687e66717570</p>
        <p>6376746a626f7676</p>
        <p>6c63747e7575736c</p>
        <p>6f6f766a71637d77</p>
        <p>757e6a677e696276</p>
        <p>627c6f606d686572</p>
        <p>666c707c70726c62</p>
        <p>68776e7d616e6f6d</p>
        <p>6971746c6e776a6b</p>
        <p>637c77617c717077</p>
        <p>74717768616c607d</p>
        <p>7e777474606b6766</p>
        <p>71777e7d61756c7e</p>
        <p>6c7d696065706d66</p>
        <p>69626861626e7e67</p>
        <p>7e746e7e7075767e</p>
        <p>666c6c6960706366</p>
        <p>767c62676b6d717d</p>
        <p>6569737566606368</p>
        <p>736872686d6e6c6b</p>
        <p>6f60766b65716570</p>
        <p>71707d6b72756074</p>
        <p>706d77676b6c6163</p>
        <p>737c6b7c71717d70</p>
        <p>7c636d70706f7373</p>
        <p>6e7c6a7e6c657266</p>
        <p>61607e7466666f72</p>
        <p>6c77617666757373</p>
        <p>766e766d70756963</p>
        <p>77637d606f73677d</p>
        <p>6a76636c70656a6a</p>
        <p>6561737469657165</p>
        <p>6f6374637c6d6b77</p>
        <p>776b737676676374</p>
        <p>666876706b75656f</p>
        <p>63616a65767d6b6c</p>
        <p>7c74687569657173</p>
        <p>746b736f626f7174</p>
        <p>73776d6871617c6b</p>
        <p>6b626e67756f6276</p>
        <p>7d777577716a6967</p>
        <p>7670717c60777c6a</p>
        <p>6a7c737e67776a6f</p>
        <p>7d627e76657c6b6d</p>
        <p>6e746e7e63636f75</p>
        <p>6e67606b73737576</p>
        <p>696d7566667c767d</p>
        <p>686a637270766265</p>
        <p>6e60736c7e6f7474</p>
        <p>676f707670606e67</p>
        <p>746f72696b667063</p>
        <p>68617c6d63706576</p>
        <p>697569657d657e75</p>
        <p>6b6761676873686a</p>
        <p>6f7c626a67736970</p>
        <p>606a636b7e636563</p>
        <p>63677262617d757c</p>
        <p>7177677e7e636d71</p>
        <p>6e7476736d766c7c</p>
        <p>6f717577607c7563</p>
        <p>616f7266606e7176</p>
        <p>6b657e766e657476</p>
        <p>756b63667c77776a</p>
        <p>636d707e697e6674</p>
        <p>6969636e736f7d62</p>
        <p>72687d60717e6a66</p>
        <p>7d6768677d746c6f</p>
        <p>7669736d6e777169</p>
        <p>706566776d696b66</p>
        <p>6e7361626969687c</p>
        <p>6076636b697d6171</p>
        <p>656c697761736176</p>
        <p>697e69687265757d</p>
        <p>767174667d77736c</p>
        <p>6f7267687c736c72</p>
        <p>746b7d697d636d65</p>
        <p>60666663776c707e</p>
        <p>77637165626f6160</p>
        <p>6068686f60687e75</p>
        <p>6769667e7070636f</p>
        <p>726f70606d6c7c6f</p>
        <p>7271686b73626176</p>
        <p>6c72716c7c657468</p>
        <p>6e6266656c686d7d</p>
        <p>6770697560746977</p>
        <p>63756a67767e6e6c</p>
        <p>7669627166616b67</p>
        <p>6c7760777677637c</p>
        <p>74637c766d666876</p>
        <p>637261607073726b</p>
        <p>73736b7574686e6d</p>
        <p>6e68696d776d6d77</p>
        <p>756a7260706e627d</p>
        <p>69776b6d6e6e657e</p>
        <p>63726b7567636a77</p>
        <p>6a7e7c7c716d7073</p>
        <p>68756f6d6a737260</p>
        <p>7266616c617c7575</p>
        <p>656f686e69667d69</p>
        <p>6d6f7c60726a6d63</p>
        <p>63656f63626f617e</p>
        <p>7363686275696f77</p>
        <p>66776a716d6c626d</p>
        <p>636f766f68657373</p>
        <p>6270637d7773687d</p>
        <p>7570706e7c6c7466</p>
        <p>7c66707d6c727e63</p>
        <p>746f627e60727275</p>
        <p>686c676b66707169</p>
        <p>736a7376607d6b60</p>
        <p>667765736f697460</p>
        <p>6a75637c7d706c6a</p>
        <p>756a6772696f6a68</p>
        <p>6677667760746d70</p>
        <p>6061637d69746f62</p>
        <p>6a7576756965746c</p>
        <p>6972696c68606f68</p>
        <p>65727d7e74746867</p>
        <p>6569717e756b707d</p>
        <p>63726861626c7d73</p>
        <p>756a626f757d6d6b</p>
        <p>636a68716e6a6770</p>
        <p>7273747569697c74</p>
        <p>6e6e726a73697665</p>
        <p>6f66607c67766576</p>
        <p>766c6d7376707167</p>
        <p>77666b637e6f7e71</p>
        <p>6e68656d6760726b</p>
        <p>7270677c6c7d6861</p>
        <p>7562606f726a6e73</p>
        <p>6c74716d69766b6e</p>
        <p>757c747d6d736b77</p>
        <p>7c6f7d7669616a68</p>
        <p>657e676a6a627d62</p>
        <p>6f686c616c717075</p>
        <p>717d7e706770697d</p>
        <p>677e737277616769</p>
        <p>687e616b65656769</p>
        <p>6b6a736e76626f60</p>
        <p>74707e72736e736d</p>
        <p>65687e6068686d6c</p>
        <p>75776b68627e6766</p>
        <p>606869666d6f716b</p>
        <p>666b7c6961666f7d</p>
        <p>766f657e716c7768</p>
        <p>6e7c6a7e6e6d7c69</p>
        <p>7d69776b6b636a68</p>
        <p>736e63616e607d6e</p>
        <p>74756f706c616a70</p>
        <p>60657065706c6b6a</p>
        <p>68606e7468606a66</p>
        <p>76746f636b657162</p>
        <p>6f657d6e6a756e7c</p>
        <p>7d77737571616075</p>
        <p>6e6b626765637165</p>
        <p>706d686e76716765</p>
        <p>75756e6f71697d6f</p>
        <p>7c6069746f727577</p>
        <p>7c7d74766b676571</p>
        <p>7263726a61756d6d</p>
        <p>6066656275626c75</p>
        <p>65766d7460627274</p>
        <p>617c6f657e736962</p>
        <p>6d6571717d696a6b</p>
        <p>6d6862766b706c6a</p>
        <p>6172736e6c7e6d6f</p>
        <p>606f77746075616e</p>
        <p>7d676a746c6a636a</p>
        <p>616b6f6271756c75</p>
        <p>776e7d746d626a6a</p>
        <p>606269747467767e</p>
        <p>6571667373676d6b</p>
        <p>726b74766a717270</p>
        <p>656863637d6b6267</p>
        <p>6e716a726b777773</p>
        <p>69766d676576747d</p>
        <p>6862686361617e76</p>
        <p>6d6b6a6f7460636c</p>
        <p>676a7e7d616e7663</p>
        <p>6b667c626a687c73</p>
        <p>6d6d7c6c6e7e6e75</p>
        <p>69776d7074656a7c</p>
        <p>6c73757572626975</p>
        <p>7670636763726874</p>
        <p>7069736b7d716073</p>
        <p>6877756a61776263</p>
        <p>6e7c7e706f6c7662</p>
        <p>666f6c767d6c7d70</p>
        <p>6965757e7e706373</p>
        <p>6663737d67636260</p>
        <p>7470736e6a716a6f</p>
        <p>6a7063676d7c6e70</p>
        <p>627e687567727560</p>
        <p>6870606e63697375</p>
        <p>6b766f68697e736f</p>
        <p>6c707d747e6a717c</p>
        <p>6d667372716e6a66</p>
        <p>7c716b696c6c7668</p>
        <p>6e6a616368606a6b</p>
        <p>70756f616c62616c</p>
        <p>767c707c60616e77</p>
        <p>75727e686974627c</p>
        <p>6f746f7c6e7d7568</p>
        <p>776d757e76626075</p>
        <p>7c637d736d686f61</p>
        <p>7d7375696665756a</p>
        <p>6a6577766b627273</p>
        <p>666e6b7177767672</p>
        <p>6c6867626c6d7c66</p>
        <p>7c6d696561757c60</p>
        <p>6e7c667d68776b73</p>
        <p>737e77637d76617d</p>
        <p>65637c6c65656d75</p>
        <p>6c7e617d7361696f</p>
        <p>65697e6b61737667</p>
        <p>607163607c6c6c6b</p>
        <p>6f72706675756668</p>
        <p>6e73636a6a6f7471</p>
        <p>6f766f7e667d6c66</p>
        <p>627e757e6f7d6774</p>
        <p>74706c697e687277</p>
        <p>6b6f7e60687e6c61</p>
        <p>616c70677e757072</p>
        <p>6976717e60677360</p>
        <p>6e626868766a6e76</p>
        <p>7e7d686268766071</p>
        <p>6b61667160687d6e</p>
        <p>656670757e7c6a71</p>
        <p>707466626b7c606a</p>
        <p>7c727c7268617d77</p>
        <p>61726e6e75736d70</p>
        <p>666c7e7163776a69</p>
        <p>766b6b6d76666b63</p>
        <p>71666b6577776d6f</p>
        <p>747576666e7d7676</p>
        <p>766a737d696d7468</p>
        <p>6266707166737567</p>
        <p>7e73636c6876717c</p>
        <p>71657e656c6c7673</p>
        <p>747072737461676c</p>
        <p>7c63776076747d66</p>
        <p>76746c6f6c717d74</p>
        <p>616c7566657e6767</p>
        <p>6e66636d66637c65</p>
        <p>74716e6877766061</p>
        <p>7e6866696e7e6d73</p>
        <p>706c6c657e716b74</p>
        <p>6761716862687066</p>
        <p>607e65746a75696b</p>
        <p>71606561676d6268</p>
        <p>716d616d6a6f6a74</p>
        <p>6b6168766c767167</p>
        <p>727563716273626d</p>
        <p>73697077736d6b7c</p>
        <p>75666e77636e6c73</p>
        <p>7e62757660637462</p>
        <p>7d6a6b686d6a6772</p>
        <p>7e7c776673727260</p>
        <p>6c626c7076757375</p>
        <p>606e72606c707c76</p>
        <p>6b73677673607c65</p>
        <p>7e7577606c7d7266</p>
        <p>7e6e7e7e7560667e</p>
        <p>7e6c726576697368</p>
        <p>6e6d66616d737361</p>
        <p>637d7c6971696e6b</p>
        <p>74677e696b657165</p>
        <p>6f667d627c6e7277</p>
        <p>6066707c74626b70</p>
        <p>7e6968677469726a</p>
        <p>6b6c63726f777e66</p>
        <p>6b746b65666d6876</p>
        <p>70737065606b7d7d</p>
        <p>7461627d66686766</p>
        <p>6a74656371707d6a</p>
        <p>676b6f626a626969</p>
        <p>737c60676d637c68</p>
        <p>72696b7574776069</p>
        <p>70766671626c7174</p>
        <p>6e716d6075656a7d</p>
        <p>75746574706f6d67</p>
        <p>72757c746d68766f</p>
        <p>6b6d6367726c736a</p>
        <p>607768616f676a68</p>
        <p>73726a73716e636d</p>
        <p>6c757e62666e6765</p>
        <p>606776717c736f6d</p>
        <p>72607065716f7d60</p>
        <p>76737d776b7d6b71</p>
        <p>676e7c666e717e6b</p>
        <p>6371667465636f75</p>
        <p>716b687d68636877</p>
        <p>74606b7e6f6a776c</p>
        <p>7671707d68707274</p>
        <p>7e7c617c67736073</p>
        <p>6373736a6b606f60</p>
        <p>777461697d706a6a</p>
        <p>616f7267636c7171</p>
        <p>6f616d61676d6363</p>
        <p>6e6e656d6d687762</p>
        <p>7073606e6767617d</p>
        <p>6d6b6b6574617c7c</p>
        <p>6b65747d6f6a7260</p>
        <p>6776626e66766f73</p>
        <p>776c756a7c7c6c77</p>
        <p>727c6b6b63746273</p>
        <p>7573637e757d7465</p>
        <p>6f6f76777e7c7c72</p>
        <p>7d657c717260696e</p>
        <p>7e77656f66606974</p>
        <p>6b756277627c626c</p>
        <p>7363696d6e776661</p>
        <p>706a74766c606562</p>
        <p>7e7663657e636572</p>
        <p>6a6c7e76747d6a63</p>
        <p>67637d746f60666a</p>
        <p>7d687c6e61706576</p>
        <p>7c61717e716d6166</p>
        <p>6b717d63747e7e67</p>
        <p>61677c6375706371</p>
        <p>637e6b67626b7677</p>
        <p>7e617263716a7662</p>
        <p>70617d6261707161</p>
        <p>607061756666637d</p>
        <p>716f7c7173666869</p>
        <p>7c67676d65747061</p>
        <p>636b686d70706a62</p>
    </div>

<script src="./encrypt.js"></script>

</body></html>
"""

# Encrypted data
encrypted_data = """
<p>726f746a6a6e7e76</p>
        <p>6f6e6c617c636e73</p>
        <p>607d6b6d676f6f6b</p>
        <p>6a7c716f7772746a</p>
        <p>696f7d6f736b6e72</p>
        <p>707160666b68777e</p>
        <p>6765616d756d6c7c</p>
        <p>68717e746c6c6769</p>
        <p>746765766860737e</p>
        <p>7468776e726c7c77</p>
        <p>656d767e6962776f</p>
        <p>7d7c656370756c74</p>
        <p>6368626b68757574</p>
        <p>776e767c6a6c7c6f</p>
        <p>7e60676c65657e65</p>
        <p>636e73767473626e</p>
        <p>6674686f7e7d7567</p>
        <p>696c7d637d6c6d6f</p>
        <p>746e76747d61686a</p>
        <p>706d7d7662686d7d</p>
        <p>777d696b666d6c6d</p>
        <p>6c777e686f6b6c7d</p>
        <p>7e726b72616e7c77</p>
        <p>7666636575746563</p>
        <p>6d6c7d777068757c</p>
        <p>6a7d736e69717c60</p>
        <p>6e7c626569627566</p>
        <p>6b7163636b72687c</p>
        <p>6660757266686f61</p>
        <p>6c7c6060686d7762</p>
        <p>6d6970766d687363</p>
        <p>696c727069617373</p>
        <p>6362676a686f766c</p>
        <p>6d6b6d70716c6370</p>
        <p>7e6765616f706067</p>
        <p>6e6363746a6b7475</p>
        <p>696f6a6867656874</p>
        <p>6e637d6f73717e72</p>
        <p>696877686e637574</p>
        <p>6577726177756a71</p>
        <p>6b6370747d716566</p>
        <p>7c6961617465666f</p>
        <p>656b60696c6e7471</p>
        <p>6b626b6a766f6b7c</p>
        <p>6166666572776571</p>
        <p>696176627c716170</p>
        <p>75727e6e68627074</p>
        <p>75776976757d6d73</p>
        <p>71636071766a6c73</p>
        <p>65637c6c6a777d68</p>
        <p>6b70756173686772</p>
        <p>6561637c667c6f6b</p>
        <p>637c7561637d7d67</p>
        <p>71627c657c77706f</p>
        <p>7e62626f6a63756b</p>
        <p>63637e6274666865</p>
        <p>756f746d6a716f6c</p>
        <p>6e766f6a677e7668</p>
        <p>7d606761747c6a7e</p>
        <p>607e7d7160707562</p>
        <p>7471736566756362</p>
        <p>7e60747167696868</p>
        <p>7462687d6a6c6a68</p>
        <p>656d726b7774626b</p>
        <p>76736f6567737677</p>
        <p>63767262626d7569</p>
        <p>726b63626d726662</p>
        <p>7c737372746a7c76</p>
        <p>6c63747d6c71717d</p>
        <p>616d63726b62757e</p>
        <p>69636c73617d7e67</p>
        <p>637c7e6275637465</p>
        <p>6a746e6261707766</p>
        <p>7175727772777e6b</p>
        <p>7d7d6765766e7e67</p>
        <p>7474626c63666c74</p>
        <p>7d636a667170666f</p>
        <p>71747171627e766d</p>
        <p>6a76666f7e7e676b</p>
        <p>7d7c756c7576766b</p>
        <p>77737d7460696174</p>
        <p>6b65667c606e7363</p>
        <p>6b7c676177777d66</p>
        <p>72616b656a636777</p>
        <p>6a6d6573716e6c69</p>
        <p>6c72776a72656f69</p>
        <p>7d6d71737674636d</p>
        <p>736d6c6269616d60</p>
        <p>756b75607e7d736f</p>
        <p>7c677d75626e6d65</p>
        <p>6976757c616c6161</p>
        <p>756e656d626d776c</p>
        <p>776c686f6f7e7673</p>
        <p>717e7d7e6c696e71</p>
        <p>666f6c617c767c72</p>
        <p>7266656f70747567</p>
        <p>6f707c7d6f6b6767</p>
        <p>716e7c6a72746066</p>
        <p>7d70686a6f707e77</p>
        <p>6d6069607d696170</p>
        <p>7362746977777262</p>
        <p>6d6d7d6063656868</p>
        <p>6c71756663716861</p>
        <p>7c736d74667e7473</p>
        <p>637170606a7e706b</p>
        <p>6a6f7776776e6171</p>
        <p>73676b676f6f6661</p>
        <p>777e7d7275726065</p>
        <p>73687267756a6f63</p>
        <p>7d68656667726a63</p>
        <p>726f687461737e62</p>
        <p>766d737e65737e63</p>
        <p>6260677676766e60</p>
        <p>6a727e7e706b726a</p>
        <p>686174667167747d</p>
        <p>6267706f627e6e69</p>
        <p>7763756d637e6873</p>
        <p>72666c77707c6b65</p>
        <p>6b696a6375607c6a</p>
        <p>746d62696d626a73</p>
        <p>6e636f6674706f72</p>
        <p>7069616a6770696c</p>
        <p>606d6e7077617571</p>
        <p>7360636365696b70</p>
        <p>636e696d7e72637d</p>
        <p>767765656f6e6074</p>
        <p>686a696374637c6f</p>
        <p>6e7d6a70776a7d6d</p>
        <p>726a716975737367</p>
        <p>6b7d726372746e68</p>
        <p>6066606161766e76</p>
        <p>607d757463716a7e</p>
        <p>6676616776616677</p>
        <p>77656a6268656f6f</p>
        <p>6f67626167737c67</p>
        <p>7466616a6f7d6160</p>
        <p>777275617167666e</p>
        <p>7c6a6c77706e6175</p>
        <p>626b6d677d68626e</p>
        <p>69606c6d6e697e71</p>
        <p>6e7577777076766b</p>
        <p>6860716771636b70</p>
        <p>686f7d666c606665</p>
        <p>746f6b7074687c66</p>
        <p>687662766277686f</p>
        <p>6b677e706c74757d</p>
        <p>6e7e6f656c627c75</p>
        <p>7570776a7063716b</p>
        <p>626b6763727d6575</p>
        <p>6d6770776e657768</p>
        <p>6171687c77637265</p>
        <p>7676687d626b7c67</p>
        <p>6771616b6267656d</p>
        <p>6c76737e6f736361</p>
        <p>667e746072636d6c</p>
        <p>667574737e636e6b</p>
        <p>726d60697475737d</p>
        <p>65687e75706f737c</p>
        <p>7d72606e61766d6c</p>
        <p>6e7c696d666c6677</p>
        <p>6a626f7e6274757c</p>
        <p>656d71747c616d6f</p>
        <p>6c6d71697e656072</p>
        <p>676c677562616674</p>
        <p>6d6b747e6e7d6d72</p>
        <p>69696b7463706b6b</p>
        <p>666e7d6c62696665</p>
        <p>6d77627476667c61</p>
        <p>7667767560757669</p>
        <p>6660776a77696962</p>
        <p>697c7c7663766a6f</p>
        <p>60696a60667d6b65</p>
        <p>6372606561657467</p>
        <p>776f687e66717570</p>
        <p>6376746a626f7676</p>
        <p>6c63747e7575736c</p>
        <p>6f6f766a71637d77</p>
        <p>757e6a677e696276</p>
        <p>627c6f606d686572</p>
        <p>666c707c70726c62</p>
        <p>68776e7d616e6f6d</p>
        <p>6971746c6e776a6b</p>
        <p>637c77617c717077</p>
        <p>74717768616c607d</p>
        <p>7e777474606b6766</p>
        <p>71777e7d61756c7e</p>
        <p>6c7d696065706d66</p>
        <p>69626861626e7e67</p>
        <p>7e746e7e7075767e</p>
        <p>666c6c6960706366</p>
        <p>767c62676b6d717d</p>
        <p>6569737566606368</p>
        <p>736872686d6e6c6b</p>
        <p>6f60766b65716570</p>
        <p>71707d6b72756074</p>
        <p>706d77676b6c6163</p>
        <p>737c6b7c71717d70</p>
        <p>7c636d70706f7373</p>
        <p>6e7c6a7e6c657266</p>
        <p>61607e7466666f72</p>
        <p>6c77617666757373</p>
        <p>766e766d70756963</p>
        <p>77637d606f73677d</p>
        <p>6a76636c70656a6a</p>
        <p>6561737469657165</p>
        <p>6f6374637c6d6b77</p>
        <p>776b737676676374</p>
        <p>666876706b75656f</p>
        <p>63616a65767d6b6c</p>
        <p>7c74687569657173</p>
        <p>746b736f626f7174</p>
        <p>73776d6871617c6b</p>
        <p>6b626e67756f6276</p>
        <p>7d777577716a6967</p>
        <p>7670717c60777c6a</p>
        <p>6a7c737e67776a6f</p>
        <p>7d627e76657c6b6d</p>
        <p>6e746e7e63636f75</p>
        <p>6e67606b73737576</p>
        <p>696d7566667c767d</p>
        <p>686a637270766265</p>
        <p>6e60736c7e6f7474</p>
        <p>676f707670606e67</p>
        <p>746f72696b667063</p>
        <p>68617c6d63706576</p>
        <p>697569657d657e75</p>
        <p>6b6761676873686a</p>
        <p>6f7c626a67736970</p>
        <p>606a636b7e636563</p>
        <p>63677262617d757c</p>
        <p>7177677e7e636d71</p>
        <p>6e7476736d766c7c</p>
        <p>6f717577607c7563</p>
        <p>616f7266606e7176</p>
        <p>6b657e766e657476</p>
        <p>756b63667c77776a</p>
        <p>636d707e697e6674</p>
        <p>6969636e736f7d62</p>
        <p>72687d60717e6a66</p>
        <p>7d6768677d746c6f</p>
        <p>7669736d6e777169</p>
        <p>706566776d696b66</p>
        <p>6e7361626969687c</p>
        <p>6076636b697d6171</p>
        <p>656c697761736176</p>
        <p>697e69687265757d</p>
        <p>767174667d77736c</p>
        <p>6f7267687c736c72</p>
        <p>746b7d697d636d65</p>
        <p>60666663776c707e</p>
        <p>77637165626f6160</p>
        <p>6068686f60687e75</p>
        <p>6769667e7070636f</p>
        <p>726f70606d6c7c6f</p>
        <p>7271686b73626176</p>
        <p>6c72716c7c657468</p>
        <p>6e6266656c686d7d</p>
        <p>6770697560746977</p>
        <p>63756a67767e6e6c</p>
        <p>7669627166616b67</p>
        <p>6c7760777677637c</p>
        <p>74637c766d666876</p>
        <p>637261607073726b</p>
        <p>73736b7574686e6d</p>
        <p>6e68696d776d6d77</p>
        <p>756a7260706e627d</p>
        <p>69776b6d6e6e657e</p>
        <p>63726b7567636a77</p>
        <p>6a7e7c7c716d7073</p>
        <p>68756f6d6a737260</p>
        <p>7266616c617c7575</p>
        <p>656f686e69667d69</p>
        <p>6d6f7c60726a6d63</p>
        <p>63656f63626f617e</p>
        <p>7363686275696f77</p>
        <p>66776a716d6c626d</p>
        <p>636f766f68657373</p>
        <p>6270637d7773687d</p>
        <p>7570706e7c6c7466</p>
        <p>7c66707d6c727e63</p>
        <p>746f627e60727275</p>
        <p>686c676b66707169</p>
        <p>736a7376607d6b60</p>
        <p>667765736f697460</p>
        <p>6a75637c7d706c6a</p>
        <p>756a6772696f6a68</p>
        <p>6677667760746d70</p>
        <p>6061637d69746f62</p>
        <p>6a7576756965746c</p>
        <p>6972696c68606f68</p>
        <p>65727d7e74746867</p>
        <p>6569717e756b707d</p>
        <p>63726861626c7d73</p>
        <p>756a626f757d6d6b</p>
        <p>636a68716e6a6770</p>
        <p>7273747569697c74</p>
        <p>6e6e726a73697665</p>
        <p>6f66607c67766576</p>
        <p>766c6d7376707167</p>
        <p>77666b637e6f7e71</p>
        <p>6e68656d6760726b</p>
        <p>7270677c6c7d6861</p>
        <p>7562606f726a6e73</p>
        <p>6c74716d69766b6e</p>
        <p>757c747d6d736b77</p>
        <p>7c6f7d7669616a68</p>
        <p>657e676a6a627d62</p>
        <p>6f686c616c717075</p>
        <p>717d7e706770697d</p>
        <p>677e737277616769</p>
        <p>687e616b65656769</p>
        <p>6b6a736e76626f60</p>
        <p>74707e72736e736d</p>
        <p>65687e6068686d6c</p>
        <p>75776b68627e6766</p>
        <p>606869666d6f716b</p>
        <p>666b7c6961666f7d</p>
        <p>766f657e716c7768</p>
        <p>6e7c6a7e6e6d7c69</p>
        <p>7d69776b6b636a68</p>
        <p>736e63616e607d6e</p>
        <p>74756f706c616a70</p>
        <p>60657065706c6b6a</p>
        <p>68606e7468606a66</p>
        <p>76746f636b657162</p>
        <p>6f657d6e6a756e7c</p>
        <p>7d77737571616075</p>
        <p>6e6b626765637165</p>
        <p>706d686e76716765</p>
        <p>75756e6f71697d6f</p>
        <p>7c6069746f727577</p>
        <p>7c7d74766b676571</p>
        <p>7263726a61756d6d</p>
        <p>6066656275626c75</p>
        <p>65766d7460627274</p>
        <p>617c6f657e736962</p>
        <p>6d6571717d696a6b</p>
        <p>6d6862766b706c6a</p>
        <p>6172736e6c7e6d6f</p>
        <p>606f77746075616e</p>
        <p>7d676a746c6a636a</p>
        <p>616b6f6271756c75</p>
        <p>776e7d746d626a6a</p>
        <p>606269747467767e</p>
        <p>6571667373676d6b</p>
        <p>726b74766a717270</p>
        <p>656863637d6b6267</p>
        <p>6e716a726b777773</p>
        <p>69766d676576747d</p>
        <p>6862686361617e76</p>
        <p>6d6b6a6f7460636c</p>
        <p>676a7e7d616e7663</p>
        <p>6b667c626a687c73</p>
        <p>6d6d7c6c6e7e6e75</p>
        <p>69776d7074656a7c</p>
        <p>6c73757572626975</p>
        <p>7670636763726874</p>
        <p>7069736b7d716073</p>
        <p>6877756a61776263</p>
        <p>6e7c7e706f6c7662</p>
        <p>666f6c767d6c7d70</p>
        <p>6965757e7e706373</p>
        <p>6663737d67636260</p>
        <p>7470736e6a716a6f</p>
        <p>6a7063676d7c6e70</p>
        <p>627e687567727560</p>
        <p>6870606e63697375</p>
        <p>6b766f68697e736f</p>
        <p>6c707d747e6a717c</p>
        <p>6d667372716e6a66</p>
        <p>7c716b696c6c7668</p>
        <p>6e6a616368606a6b</p>
        <p>70756f616c62616c</p>
        <p>767c707c60616e77</p>
        <p>75727e686974627c</p>
        <p>6f746f7c6e7d7568</p>
        <p>776d757e76626075</p>
        <p>7c637d736d686f61</p>
        <p>7d7375696665756a</p>
        <p>6a6577766b627273</p>
        <p>666e6b7177767672</p>
        <p>6c6867626c6d7c66</p>
        <p>7c6d696561757c60</p>
        <p>6e7c667d68776b73</p>
        <p>737e77637d76617d</p>
        <p>65637c6c65656d75</p>
        <p>6c7e617d7361696f</p>
        <p>65697e6b61737667</p>
        <p>607163607c6c6c6b</p>
        <p>6f72706675756668</p>
        <p>6e73636a6a6f7471</p>
        <p>6f766f7e667d6c66</p>
        <p>627e757e6f7d6774</p>
        <p>74706c697e687277</p>
        <p>6b6f7e60687e6c61</p>
        <p>616c70677e757072</p>
        <p>6976717e60677360</p>
        <p>6e626868766a6e76</p>
        <p>7e7d686268766071</p>
        <p>6b61667160687d6e</p>
        <p>656670757e7c6a71</p>
        <p>707466626b7c606a</p>
        <p>7c727c7268617d77</p>
        <p>61726e6e75736d70</p>
        <p>666c7e7163776a69</p>
        <p>766b6b6d76666b63</p>
        <p>71666b6577776d6f</p>
        <p>747576666e7d7676</p>
        <p>766a737d696d7468</p>
        <p>6266707166737567</p>
        <p>7e73636c6876717c</p>
        <p>71657e656c6c7673</p>
        <p>747072737461676c</p>
        <p>7c63776076747d66</p>
        <p>76746c6f6c717d74</p>
        <p>616c7566657e6767</p>
        <p>6e66636d66637c65</p>
        <p>74716e6877766061</p>
        <p>7e6866696e7e6d73</p>
        <p>706c6c657e716b74</p>
        <p>6761716862687066</p>
        <p>607e65746a75696b</p>
        <p>71606561676d6268</p>
        <p>716d616d6a6f6a74</p>
        <p>6b6168766c767167</p>
        <p>727563716273626d</p>
        <p>73697077736d6b7c</p>
        <p>75666e77636e6c73</p>
        <p>7e62757660637462</p>
        <p>7d6a6b686d6a6772</p>
        <p>7e7c776673727260</p>
        <p>6c626c7076757375</p>
        <p>606e72606c707c76</p>
        <p>6b73677673607c65</p>
        <p>7e7577606c7d7266</p>
        <p>7e6e7e7e7560667e</p>
        <p>7e6c726576697368</p>
        <p>6e6d66616d737361</p>
        <p>637d7c6971696e6b</p>
        <p>74677e696b657165</p>
        <p>6f667d627c6e7277</p>
        <p>6066707c74626b70</p>
        <p>7e6968677469726a</p>
        <p>6b6c63726f777e66</p>
        <p>6b746b65666d6876</p>
        <p>70737065606b7d7d</p>
        <p>7461627d66686766</p>
        <p>6a74656371707d6a</p>
        <p>676b6f626a626969</p>
        <p>737c60676d637c68</p>
        <p>72696b7574776069</p>
        <p>70766671626c7174</p>
        <p>6e716d6075656a7d</p>
        <p>75746574706f6d67</p>
        <p>72757c746d68766f</p>
        <p>6b6d6367726c736a</p>
        <p>607768616f676a68</p>
        <p>73726a73716e636d</p>
        <p>6c757e62666e6765</p>
        <p>606776717c736f6d</p>
        <p>72607065716f7d60</p>
        <p>76737d776b7d6b71</p>
        <p>676e7c666e717e6b</p>
        <p>6371667465636f75</p>
        <p>716b687d68636877</p>
        <p>74606b7e6f6a776c</p>
        <p>7671707d68707274</p>
        <p>7e7c617c67736073</p>
        <p>6373736a6b606f60</p>
        <p>777461697d706a6a</p>
        <p>616f7267636c7171</p>
        <p>6f616d61676d6363</p>
        <p>6e6e656d6d687762</p>
        <p>7073606e6767617d</p>
        <p>6d6b6b6574617c7c</p>
        <p>6b65747d6f6a7260</p>
        <p>6776626e66766f73</p>
        <p>776c756a7c7c6c77</p>
        <p>727c6b6b63746273</p>
        <p>7573637e757d7465</p>
        <p>6f6f76777e7c7c72</p>
        <p>7d657c717260696e</p>
        <p>7e77656f66606974</p>
        <p>6b756277627c626c</p>
        <p>7363696d6e776661</p>
        <p>706a74766c606562</p>
        <p>7e7663657e636572</p>
        <p>6a6c7e76747d6a63</p>
        <p>67637d746f60666a</p>
        <p>7d687c6e61706576</p>
        <p>7c61717e716d6166</p>
        <p>6b717d63747e7e67</p>
        <p>61677c6375706371</p>
        <p>637e6b67626b7677</p>
        <p>7e617263716a7662</p>
        <p>70617d6261707161</p>
        <p>607061756666637d</p>
        <p>716f7c7173666869</p>
        <p>7c67676d65747061</p>
        <p>636b686d70706a62</p>
"""

# Function to decode encrypted data
def decode_data(encrypted_data):
    decoded_messages = []
    for line in encrypted_data.strip().split('\n'):
        hex_string = line.strip().replace('<p>', '').replace('</p>', '')
        decoded_message = bytes.fromhex(hex_string).decode('utf-8')
        decoded_messages.append(decoded_message)
    return decoded_messages

# Parsing HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Extracting encrypted data
encrypted_data_tags = soup.find_all('p')

# Decoding encrypted data
for tag in encrypted_data_tags:
    decrypted_messages = decode_data(tag.text)
    if "6b" == tag.text[12:14]: #looks for an 'o'
        if "6c" == tag.text[10:12]: #looks for an 'h'
            print(tag.text)
    # print("\nDecrypted Messages:")
    # for message in decrypted_messages:
        # print(message + " : " + tag.text)
