#------------------------------------------------------------------------------
- Projekt: DLR Pilot ZiRa
#------------------------------------------------------------------------------
--- Hardware:
#------------------------------------------------------------------------------
------LED-Belegung:
J401 -> Pin 2	-> LED-Stripe	-> Gitter-Rahmen
J402 -> Pin 3
J403 -> Pin 4
J404 -> Pin 5
J405 -> Pin 6
J406 -> Pin 7
J407 -> Pin 8
J408 -> Pin 9	-> LED-Stripe	-> Co2 Ausstoß Anzeige Balken
#------------------------------------------------------------------------------
------ IO-Belegung:
J301 -> I 0.0	-> Taster vorne 			-> Schliesser           -> Pull-Down, aktiv high
J302 -> I 0.1	-> Taster vorne 			-> Öffner               -> Pull-Down, aktiv low
J303 -> I 0.2	-> Taster hinten			-> Schliesser           -> Pull-Down, aktiv high
J304 -> I 0.3	-> Taster hinten			-> Öffner               -> Pull-Down, aktiv low
J305 -> I 0.4	-> Reed-Kontakt				-> Position Grün        -> Pull-Down, aktiv high
J306 -> I 0.5	-> Reed-Kontakt				-> Position Rot         -> Pull-Down, aktiv high
J307 -> I 0.6
J308 -> I 0.7
#------------------------------------------------------------------------------
J301 -> Q 0.0	-> Taster LED vorne			-> Grüne LED
J302 -> Q 0.1	-> Taster LED vorne			-> Rote LED
J303 -> Q 0.2	-> Taster LED hinten		-> Grüne LED
J304 -> Q 0.3	-> Taster LED vorne			-> Rote LED
J305 -> Q 0.4
J306 -> Q 0.5
J307 -> Q 0.6
J308 -> Q 0.7	-> Elektromagnet Ausgabe	-> Stromlos Türe öffnet -> über Relaismodul
#------------------------------------------------------------------------------
J201 -> Pin 0   -> Audio-Ausgang über PWM
J201 -> Pin 1   -> Audio-Ausgang über PWM
#------------------------------------------------------------------------------
--- Beschreibung:
State:
    0   ## Nach dem Einschalten
        -> Nach Reset oder Neustart
        --> Alle Merker auf aus
        --> Alle LED-Stripes aus
        --> Alles Taster-LEDs aus
        --> Relais aus
        --> Audio-Ausgang aus
        --> Starte Timer -> 3 Sekunden

    1   ## Tor schliessen, Befüllen und Freigabe
        -> Timer abgelaufen oder Einsprung auf 1 
        --> Alle LED-Stripes auf Blau 5%
        --> Relais an -> Tor kann geschlossen werden
        --> Taster-LED vorne aus
        --> Taster-LED hinten gelb blinken

    2   ## Warte auf Modul (Rot/Grün)
        -> Taster hinten betätigt
            -> Taster hinten gelb 
            -> Wenn I0.4 und nicht I0.5
                -> Merker 1 an     -> Modul Grün
            -> Wenn I0.5 und nicht I0.4
                -> Merker 1 aus    -> Modul Rot

    3   ## Warte auf Taster vorne
        -> I0.4 oder I0.5 an
            -> Wenn Merker 1 an    -> Modul Grün  
                -> Taster vorne LED grün blinken
                -> Wert für Ablauf Sequenz auf "30 Sekunden" setzen
            -> Wenn Merker 1 aus   -> Modul Rot
                -> Taster vorne LED rot  blinken
                -> Wert für Ablauf Sequenz auf "20 Sekunden" setzen

    4   ## Warte auf Sequenz-Ende
        -> Taster vorne betätigt
            -> Wenn Merker 1 an     -> Modul Grün
                -> Animation "Grün" Start
            -> Wenn Merker 1 aus    -> Modul Rot
                -> Animation "Rot" Start

    5   ## Co2 Anzeige
        -> Timer Sequenz Ende abgelaufen
            -> Wenn Merker 1 an     -> Modul Grün
                -> Animation "Grün" Stop
