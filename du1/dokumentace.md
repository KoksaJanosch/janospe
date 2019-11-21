<h1>Domácí úkol 01: zobrazení</h1>
<ul>
  <li>Zadání</li>
  <li>Výsledek</li>
  <li>Autor</li>
</ul>
<h3>Zadání</h3>
<p>Sestrojit program, který ulehčí práci s výpočtem pro válcová tečná zobrazení.
Uživatel si vybere z nabídky dané zobrazení a následně měřítko, poté se vypíší 
souřadnice rovnoběžek a poledníků, konkrétně jejich vzdálenost pro rýsování na papíře. Výchozí poloměr Země
pro tento úkol je 6371,11 km, nicméně může být i zadán uživatelem. <br>
Program bude počítat Marinovo, Lambertovo, Braunovo a Mercatorovo zobrazení.  

<h3>Výsledek</h3>
<b>Uživatelské vstupy:</b>
<ul style="list-style-type: square">
  <li>Program pracuje dle požadovaného zadání. Nejdříve se uživatele zeptá, 
jaké chce použít <b>zobrazení</b> (zobrazí se i nápověda, z kterých může vybírat). Pokud
zadá něco jiného, než z výběru, program ho upozorní, a zeptá se ho znovu s nápovědou, které 
zobrazení má počítat. Pokud je výběr proveden malým písmenem, nevadí, program ho převede na velké. </li>
  <li>Uživatel dále zadá <b>měřítko</b>, které musí být kladné a nesmí se rovnat nule. Pokud
se tomu tak nestane, program ho upozorní a znovu se ho zeptá. </li>
  <li>Posledním vstupem je <b>poloměr</b>. Ten nesmí být zadán záporným číslem (případně ho program opět upozorní).
Když je zadána 0, program použije výchozí hodnotu pro Zemi, tedy 6371.11 km. </li>
</ul>
<b>Funkce:</b>
<ul style="list-style-type: square">
  <li><u>Poledníky:</u>
  <br>Funkce založí seznam, poté dosadí do vzorce uživatelské vstupy.
  Stupně se dosazují pomocí funkce <i>range</i> od -180° do 180° po 10°. Vzorec jednak výsledek přepočítá
  pomocí měřítka na <i>cm</i>, ale zároveň jej zaokrouhlí pomocí funkce "<i>round</i>"
  na 1 desetinné místo. Následuje podmínka, která výsledek zapíše do seznamu, pokud přesahuje 1 m, zapíše "<i>-</i>".
  Funkce je ukončena vypsáním konečného seznamu.</li>
  <li><u>Rovnoběžky:</u>
  <br>Tato funkce je téměř stejná jako předchozí, liší se pouze rozsahem funkce "<i>range</i>" (pouze od -90° do 90°) 
  a výběrem vzorce, který se použije - vybere se podle uživatele. U Mecatorova zobrazení musí být ošetřen vzorec 
  vyjímkou (u 90°), protože by se dělilo 0, a to nelze. Opět je vzorec přepočítán a zaokrouhlen, funkce končí 
  výpisem konečného seznamu.
</li>
</ul>
<b>Jak program funguje?</b>
<p>Při spuštění zadá uživatel požadované vstupy (vybere zobrazení, zvolí měřítko a poloměr), vyvolají se nadefinované
funkce "<i>rovnobezky</i>" a "<i>poledniky</i>", které na základě zvolených vstupů vypočítají jednotlivé vzdálenosti
a vypíší je v označeném seznamu.</p>

<p>Poznámka:<br>
Dle zadání by měl program při chybném výběru zobrazení skončit, ale držel jsem se toho, že 
uživatel spouští program kvůli tomu, aby mu zobrazení vypočítal, proto se ho program ptá dokola, 
dokud nějaké nevybere. Jinak bych použil <i>quit()</i>.</p>