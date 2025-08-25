#------------------------------------------------------------------------------
  Projekt: DLR Pilot ZiRa
#------------------------------------------------------------------------------
Hardware:
#------------------------------------------------------------------------------
LED-Belegung:
J401 -> Pin 2	-> LED-Stripe	-> Gitter-Rahmen
J402 -> Pin 3
J403 -> Pin 4
J404 -> Pin 5
J405 -> Pin 6
J406 -> Pin 7
J407 -> Pin 8
J408 -> Pin 9	-> LED-Stripe	-> Co2 Ausstoß Anzeige Balken
#------------------------------------------------------------------------------
IO-Belegung:
J301 -> I 0.0	-> Taster vorne 			-> Schliesser           -> Pull-Down, aktiv high
J302 -> I 0.1	-> Taster vorne 			-> Öffner               -> Pull-Down, aktiv low
J303 -> I 0.2	-> Taster hinten			-> Schliesser           -> Pull-Down, aktiv high
J304 -> I 0.3	-> Taster hinten			-> Öffner               -> Pull-Down, aktiv low
J305 -> I 0.4	-> Reed-Kontakt				-> Position Grüne       -> Pull-Down, aktiv high
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
