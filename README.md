DLR Pilot ZiRa
#------------------------------------------------------------------------------
##################################################################

Hardware:

##################################################################

LED-Belegung:

J401	-> LED-Stripe	-> Gitter-Rahmen
J402
J403
J404
J405
J406
J407
J408	-> LED-Stripe	-> Co2 Ausstoß Anzeige Balken

##################################################################

IO-Belegung:

J301 -> I 0.0	-> Taster Schalter			-> Schliesser
J302 -> I 0.1	-> Taster Schalter			-> Öffner
J303 -> I 0.2	-> Reed-Kontakt				-> Position Grüne
J304 -> I 0.3	-> Reed-Kontakt				-> Position Rot
J305 -> I 0.4
J306 -> I 0.5
J307 -> I 0.6
J308 -> I 0.7

J301 -> Q 0.0	-> Taster LED				-> Grüne LED
J302 -> Q 0.1	-> Taster LED				-> Rote LED
J303 -> Q 0.2
J304 -> Q 0.3
J305 -> Q 0.4
J306 -> Q 0.5
J307 -> Q 0.6
J308 -> Q 0.7	-> Elektromagnet Ausgabe	-> Stromlos Türe öffnet

##################################################################

J201	-> RX/TX Connector
