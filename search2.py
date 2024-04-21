#https://webscrape2-dot-chunin.uc.r.appspot.com/login
# username: datathon_participant
# password: pagination!


from bs4 import BeautifulSoup

# The provided HTML content
html_content = """
<html lang="en"><head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rocket League Leaderboards</title>
    <link rel="stylesheet" href="/scrape.css">
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
    <table>
        <thead>
            <tr>
                <th>Player Name</th>
                <th>Shots</th>
                <th>Goals</th>
                <th>Saves</th>
                <th>Assists</th>
                <th>Game Score</th>
                <th>Score</th>
            </tr>
        </thead>
        <tbody id="data-body"><tr><td>AlphaKep</td><td>16.0</td><td>7</td><td>7.0</td><td>1.0</td><td>1655.0</td><td>3.0</td></tr><tr><td>Zineel</td><td>4.0</td><td>3</td><td>12.0</td><td>3.0</td><td>1578.0</td><td>1.0</td></tr><tr><td>Stealth</td><td>10.0</td><td>8</td><td>11.0</td><td>3.0</td><td>1827.0</td><td>1.0</td></tr><tr><td>2Piece</td><td>16.0</td><td>4</td><td>5.0</td><td>1.0</td><td>1514.0</td><td>1.0</td></tr><tr><td>Gyro.</td><td>6.0</td><td>4</td><td>7.0</td><td>0.0</td><td>1108.0</td><td>0.0</td></tr><tr><td>CorruptedG</td><td>4.0</td><td>0</td><td>4.0</td><td>1.0</td><td>900.0</td><td>0.0</td></tr><tr><td>Turinturo</td><td>6.0</td><td>4</td><td>7.0</td><td>2.0</td><td>1020.0</td><td>0.0</td></tr><tr><td>Lj</td><td>13.0</td><td>9</td><td>3.0</td><td>4.0</td><td>1210.0</td><td>3.0</td></tr><tr><td>Kraziks</td><td>8.0</td><td>6</td><td>3.0</td><td>1.0</td><td>978.0</td><td>3.0</td></tr><tr><td>Toastie</td><td>8.0</td><td>0</td><td>4.0</td><td>2.0</td><td>983.0</td><td>3.0</td></tr><tr><td>astro</td><td>16.0</td><td>0</td><td>8.0</td><td>2.0</td><td>2183.0</td><td>3.0</td></tr><tr><td>oath</td><td>6.0</td><td>3</td><td>3.0</td><td>4.0</td><td>1285.0</td><td>3.0</td></tr><tr><td>Fefe</td><td>9.0</td><td>6</td><td>9.0</td><td>1.0</td><td>1628.0</td><td>3.0</td></tr><tr><td>Memory</td><td>13.0</td><td>2</td><td>8.0</td><td>1.0</td><td>1676.0</td><td>2.0</td></tr><tr><td>rapid</td><td>7.0</td><td>1</td><td>7.0</td><td>3.0</td><td>1582.0</td><td>2.0</td></tr><tr><td>nexuhty</td><td>11.0</td><td>10</td><td>2.0</td><td>2.0</td><td>1247.0</td><td>2.0</td></tr><tr><td>Roll Dizz</td><td>10.0</td><td>4</td><td>8.0</td><td>1.0</td><td>1287.0</td><td>3.0</td></tr><tr><td>LionBlaze</td><td>14.0</td><td>10</td><td>8.0</td><td>5.0</td><td>1732.0</td><td>3.0</td></tr><tr><td>Shock</td><td>14.0</td><td>12</td><td>8.0</td><td>0.0</td><td>1787.0</td><td>3.0</td></tr><tr><td>tcorrell</td><td>15.0</td><td>3</td><td>10.0</td><td>1.0</td><td>1579.0</td><td>1.0</td></tr><tr><td>Andy</td><td>12.0</td><td>5</td><td>11.0</td><td>0.0</td><td>1825.0</td><td>1.0</td></tr><tr><td>ZPS.</td><td>11.0</td><td>10</td><td>5.0</td><td>2.0</td><td>1070.0</td><td>1.0</td></tr><tr><td>majicbear</td><td>17.0</td><td>1</td><td>8.0</td><td>1.0</td><td>2191.0</td><td>3.0</td></tr><tr><td>kinseh</td><td>13.0</td><td>6</td><td>7.0</td><td>5.0</td><td>1751.0</td><td>3.0</td></tr><tr><td>Jordan</td><td>12.0</td><td>9</td><td>6.0</td><td>2.0</td><td>1304.0</td><td>3.0</td></tr><tr><td>xpurt</td><td>10.0</td><td>0</td><td>9.0</td><td>1.0</td><td>1628.0</td><td>2.0</td></tr><tr><td>money</td><td>12.0</td><td>7</td><td>9.0</td><td>0.0</td><td>1567.0</td><td>2.0</td></tr><tr><td>Stokelyy</td><td>11.0</td><td>4</td><td>9.0</td><td>6.0</td><td>1699.0</td><td>2.0</td></tr><tr><td>Delta</td><td>13.0</td><td>3</td><td>5.0</td><td>1.0</td><td>1753.0</td><td>3.0</td></tr><tr><td>AlRaz</td><td>9.0</td><td>6</td><td>3.0</td><td>4.0</td><td>1317.0</td><td>3.0</td></tr><tr><td>Beastaboniam</td><td>5.0</td><td>3</td><td>4.0</td><td>3.0</td><td>845.0</td><td>3.0</td></tr><tr><td>Nitrous</td><td>9.0</td><td>2</td><td>2.0</td><td>0.0</td><td>750.0</td><td>0.0</td></tr><tr><td>Skillz.</td><td>4.0</td><td>3</td><td>12.0</td><td>1.0</td><td>1590.0</td><td>0.0</td></tr><tr><td>beeyu</td><td>10.0</td><td>0</td><td>2.0</td><td>3.0</td><td>1047.0</td><td>0.0</td></tr><tr><td>creamz</td><td>19.0</td><td>5</td><td>12.0</td><td>2.0</td><td>2603.0</td><td>2.0</td></tr><tr><td>Paarth</td><td>15.0</td><td>11</td><td>2.0</td><td>5.0</td><td>1543.0</td><td>2.0</td></tr><tr><td>Thundah</td><td>16.0</td><td>6</td><td>3.0</td><td>2.0</td><td>1538.0</td><td>2.0</td></tr><tr><td>Tool</td><td>12.0</td><td>8</td><td>6.0</td><td>1.0</td><td>2063.0</td><td>3.0</td></tr><tr><td>Bambii</td><td>12.0</td><td>10</td><td>13.0</td><td>5.0</td><td>2272.0</td><td>3.0</td></tr><tr><td>Jbot</td><td>11.0</td><td>4</td><td>8.0</td><td>6.0</td><td>1616.0</td><td>3.0</td></tr><tr><td>ayjacks</td><td>9.0</td><td>7</td><td>4.0</td><td>4.0</td><td>1085.0</td><td>3.0</td></tr><tr><td>SavvySeal</td><td>14.0</td><td>1</td><td>4.0</td><td>3.0</td><td>1315.0</td><td>3.0</td></tr><tr><td>.tristn</td><td>12.0</td><td>8</td><td>3.0</td><td>3.0</td><td>1695.0</td><td>3.0</td></tr><tr><td>Titoh</td><td>9.0</td><td>3</td><td>3.0</td><td>1.0</td><td>901.0</td><td>0.0</td></tr><tr><td>Monster442</td><td>6.0</td><td>5</td><td>8.0</td><td>2.0</td><td>1068.0</td><td>0.0</td></tr><tr><td>night.</td><td>4.0</td><td>0</td><td>7.0</td><td>0.0</td><td>1144.0</td><td>0.0</td></tr><tr><td>sosa</td><td>12.0</td><td>10</td><td>10.0</td><td>1.0</td><td>1778.0</td><td>2.0</td></tr><tr><td>ElOmarMaton</td><td>16.0</td><td>8</td><td>8.0</td><td>4.0</td><td>1908.0</td><td>2.0</td></tr><tr><td>AlphaKep</td><td>10.0</td><td>7</td><td>5.0</td><td>1.0</td><td>1799.0</td><td>2.0</td></tr><tr><td>Fefe</td><td>11.0</td><td>2</td><td>13.0</td><td>5.0</td><td>2210.0</td><td>3.0</td></tr></tbody>
    </table>
    <div class="buttons">
        <button id="1">1</button>
        <button id="2">2</button>
        <button id="3">3</button>
        <button id="4">4</button>
        <button id="5">5</button>
        <button id="6">6</button>
        <button id="7">7</button>
        <button id="8">8</button>
        <button id="9">9</button>
        <button id="10">10</button>
        <button id="11">11</button>
        <button id="12">12</button>
        <button id="13">13</button>
        <button id="14">14</button>
        <button id="15">15</button>
        <button id="16">16</button>
        <button id="17">17</button>
        <button id="18">18</button>
        <button id="19">19</button>
        <button id="20">20</button>
    </div>
    <script>
        document.addEventListener("DOMContentLoaded", () => {

            function fetchData(page) {
                const dataBody = document.getElementById("data-body");
                dataBody.innerHTML = ""; // Clear the table body before adding new data
                fetch(`/api/data?page=${page}`)
                    .then(response => response.json())
                    .then(data => {
                        data.forEach(row => {
                            const tr = document.createElement("tr");
                            const playerName = document.createElement("td");
                            playerName.textContent = row.player_tag;
                            const shots = document.createElement("td");
                            shots.textContent = row.core_shots;
                            const goals = document.createElement("td");
                            goals.textContent = row.core_goals;
                            const saves = document.createElement("td");
                            saves.textContent = row.core_saves;
                            const assists = document.createElement("td");
                            assists.textContent = row.core_assists;
                            const gameScore = document.createElement("td");
                            gameScore.textContent = row.core_score;
                            const score = document.createElement("td");
                            score.textContent = row.score;
                            tr.appendChild(playerName);
                            tr.appendChild(shots);
                            tr.appendChild(goals);
                            tr.appendChild(saves);
                            tr.appendChild(assists);
                            tr.appendChild(gameScore);
                            tr.appendChild(score);
                            dataBody.appendChild(tr);
                        })
                    })
                    .catch(error => {
                        console.error("Error:", error);
                    });
            }

            document.querySelectorAll('.buttons button').forEach(button => {
                button.addEventListener('click', () => {
                    console.log("Click")
                    const page = Number(button.id); // Get the page number from the button's ID
                    fetchData(page); // Fetch data for the selected page
                });
            });

            // Fetch data for the initial page when the page loads
            fetchData(1);
        });
    </script>


</body></html>
"""

# Parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Find the tbody element containing player data
tbody = soup.find('tbody', id='data-body')

# Initialize total goals
total_goals = 0

# Loop through each row in the tbody
for row in tbody.find_all('tr'):
    # Find the "Goals" column (the third column)
    goals_cell = row.find_all('td')[2]  # Index 2 corresponds to the third column (0-based index)

    # Extract the text and convert it to integer
    goals = int(goals_cell.get_text())

    # Add to total goals
    total_goals += goals

# Print the total goals
print("Total Goals:", total_goals)
