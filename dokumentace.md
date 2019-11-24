# Domácí úkol 01: zobrazení

Dokumentace k souboru [du1_petr_janos.py](du1_petr_janos.py)

- [Zadání](Zadání)
- [Výsledek](Výsledek)
- [Autor](Autor)

#### Popis programu
Program, který ulehčí práci s výpočtem pro válcová tečná zobrazení. Uživatel si vybere z nabídky dané zobrazení a následně měřítko, poté se vypíší souřadnice rovnoběžek a poledníků, konkrétně jejich vzdálenost pro rýsování na papíře. Výchozí poloměr Země pro tento úkol je 6371,11 km, nicméně může být i zadán uživatelem. 
Program bude počítat Marinovo, Lambertovo, Braunovo a Mercatorovo zobrazení.



**Uživatelské vstupy:**
- Nejdříve se uživatele zeptá, jaké chce použít **zobrazení** 
(zobrazí se i nápověda, z kterých může vybírat). Pokud zadá něco jiného, než z výběru, program ho upozorní, 
a zeptá se ho znovu s nápovědou, které zobrazení má počítat. Pokud je výběr proveden malým písmenem, nevadí, 
program ho převede na velké.
- Uživatel dále zadá **měřítko**, které musí být kladné a nesmí se rovnat nule. Pokud se tomu tak nestane, 
program ho upozorní a znovu se ho zeptá.
- Posledním vstupem je **poloměr**. Ten nesmí být zadán záporným číslem (případně ho program opět upozorní). 
Když je zadána 0, program použije výchozí hodnotu pro Zemi, tedy 6371.11 km.

**Funkce:**
- **Poledníky:** Funkce založí seznam, poté dosadí do vzorce uživatelské vstupy. Stupně se dosazují pomocí funkce range od -180° do 180° po 10°. Vzorec jednak výsledek přepočítá pomocí měřítka na cm, ale zároveň jej zaokrouhlí pomocí funkce "round" na 1 desetinné místo. Následuje podmínka, která výsledek zapíše do seznamu, pokud přesahuje 1 m, zapíše "-". Funkce je ukončena vypsáním konečného seznamu.
- **Rovnoběžky:** 
Tato funkce je téměř stejná jako předchozí, liší se pouze rozsahem funkce "range" (pouze od -90° do 90°) a výběrem vzorce, který se použije - vybere se podle uživatele. U Mecatorova zobrazení musí být ošetřen vzorec vyjímkou (u 90°), protože by se dělilo 0, a to nelze. Opět je vzorec přepočítán a zaokrouhlen, funkce končí výpisem konečného seznamu.


**Jak program funguje?**

Při spuštění zadá uživatel požadované vstupy (vybere zobrazení, zvolí měřítko a poloměr), vyvolají se nadefinované funkce "rovnobezky" a "poledniky", které na základě zvolených vstupů vypočítají jednotlivé vzdálenosti a vypíší je v označeném seznamu.

**Poznámka:**

Dle zadání by měl program při chybném výběru zobrazení skončit, ale držel jsem se toho, že uživatel spouští program kvůli tomu, aby mu zobrazení vypočítal, proto se ho program ptá dokola, dokud nějaké nevybere. Jinak bych použil quit().

**Autor:**
- Petr Janoš
- třetí ročník BSGG
- obor Sociální geografie a geoinformatiky