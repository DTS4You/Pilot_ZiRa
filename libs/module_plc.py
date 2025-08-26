class PLC:
    def __init__(self):
        self.state = 'STOP'                 # Zustand der Steuerung
        self.step_value = 0                 # Ablaufsteuerung Schrittwert
        self.step_max = 5                   # Maximale Schritte Anzahl
        self.inputs = {                     # Eingänge (z.B. Taster, Sensoren)
            'start': False,
            'stop': False,
            'sensor': False
        }
        self.outputs = {                    # Ausgänge (z.B. Motor, Relais)
            'motor': False,
            'alarm': False
        }

    def set_state(self, state='STOP'):
        if state == 'START':
            self.state = 'RUN'
            return self.state
        if state == 'RUN':
            self.state = 'RUN'
            return self.state
        self.state = 'STOP'
        return self.state
    

    def read_input(self):
        # Eingänge vom Benutzer simulieren
        self.inputs['start'] = input("Start-Taster drücken? (ja/nein): ").lower() == 'ja'
        self.inputs['stop'] = input("Stop-Taster drücken? (ja/nein): ").lower() == 'ja'
        self.inputs['sensor'] = input("Sensor aktiviert? (ja/nein): ").lower() == 'ja'
    
    def write_output(self):
        print(f"Motor: {'An' if self.outputs['motor'] else 'Aus'}")
        print(f"Alarm: {'An' if self.outputs['alarm'] else 'Aus'}")
        print(f"Aktueller Zustand: {self.state}")

    def cycle(self):
        self.read_input()
        self.logic()
        self.write_output()
        print("-" * 30)

    def logic(self):
        if self.state == 'RUN':
            if self.inputs['start']:
                print("Motor startet...")
                self.outputs['motor'] = True
                self.state = 'RUNNING'
        elif self.state == 'RUNNING':
            if self.inputs['stop']:
                print("Motor stoppt...")
                self.outputs['motor'] = False
                self.state = 'IDLE'
            elif self.inputs['sensor']:
                print("Sensor aktiviert! Alarm auslösen.")
                self.outputs['alarm'] = True
            else:
                self.outputs['alarm'] = False

def main():
    state = 'RUN'
    plc = PLC()
    print(plc.set_state(state))
    #plc.cycle()

# ###############################################################################
# ### Main                                                                    ###
# ###############################################################################

if __name__ == "__main__":

    main()
