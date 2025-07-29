# Fertilizer Dosage Pump

Ein Raspberry-Pi-basiertes System zur automatisierten Dosierung von Flüssigdünger mit präziser Mengensteuerung.  
Die Steuerung erfolgt über ein LCD-Display, einen Rotary Encoder und Taster.

---

## **Features**
- **Präzise Dosierung** über 3 Peristaltikpumpen  
- **Einfache Steuerung** per Rotary Encoder und Taster  
- **Kalibrierung** der Pumpenleistung (ml/Zeit) für höchste Genauigkeit  
- **Sicherheitsmechanismen**  
  - Relays starten standardmäßig immer **stromlos** (kein unbeabsichtigtes Dosieren nach Stromausfall)  
  - **Maximale Düngemenge pro Tag** festgelegt  
  - **Protokollierung** der Dosierintervalle zur Vermeidung von Überdosierung  
- **Persistente Speicherung** von Kalibrierungswerten und Einstellungen  
- **Display-Stromsparmodus**

---

## **Hardwareübersicht**
- **Raspberry Pi** (3 oder höher)  
- **3x Peristaltikpumpen** (12V)  
- **3x Relays** oder **3-fach Relay-Modul** (230V → 12V für Pumpen)  
- **12V Netzteil**  
- **Rotary Encoder** mit Taster  
- **2x Taster** (Navigation / Display)  
- **LCD Display**  
- **NYM-J 3x1,5mm² Installationskabel**  
- **Jumper Wires** (Verbindung Raspberry Pi zu Relays)  

---

## **Funktionsweise**
Der Raspberry Pi steuert die Signalgebung zu den Relays.  
Diese schalten die 12V-Spannung für die Peristaltikpumpen.  
Die Pumpen können individuell kalibriert werden, um eine genaue Dosierung in Millilitern pro Intervall sicherzustellen.

---

## **Kalibrierung**
1. **Gewünschte ml-Ausgabe** pro voreingestelltem Zeitintervall einstellen  
2. **Pumpen starten** im festgelegten Zeitintervall  
3. **Ausgegebene Menge messen** mit Messkolben  
4. **Zeitintervall-Variable proportional anpassen**  
   - Beispiel: 4,5 ml gemessen statt 5 ml → Anpassung um 1/9  
5. **Überprüfung wiederholen**  
6. **Zeitintervall speichern** (persistente Speicherung)  
7. **Pro Pumpe wiederholen**

---

## **Sicherheitsaspekte im Code**
- Beim Starten oder nach Stromausfall sind **alle Relays standardmäßig aus**  
- **Feste Begrenzung** der maximalen Düngemenge pro Tag  
- **Logging** der Auslösungen zur Überwachung und Fehlervermeidung  

---

## **Steuerung**
- **Programmbereiche wechseln** über Rotary Encoder  
- **Bestätigung/Auswahl** per Taster  
- **Kalibrierung**  
  - ml-Wert über Rotary Encoder einstellen  
  - Mit Taster bestätigen  
- **Reset-Funktion**  
  - Über Tastenkombination oder Doppelabfrage  
- **Displaysteuerung**  
  - Ein-/Ausschalten über Taster  
  - Optional Auto-Off nach 5 Minuten  
