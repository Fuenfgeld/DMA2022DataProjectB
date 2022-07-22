# DMA2022DataProjectB

Brustkrebs ist eine der häufigsten Krebserkrankungen. Er macht 30 % aller Krebsfälle bei Frauen in Deutschland aus. In seltenen Fällen kann er auch Männer befallen (1 % aller Krebsfälle bei Männern).

## Projektbeschreibung

Im Rahmen unseres Projektes analysieren wir einen Datensatz  aus den USA der Informationen über demographische und medizinische Details von 1019 Brustkrebs Patienten aus den USA enthält. Die Daten werden zum beantworten unserer Forschungsfrage verwendet. In der Forschungsfrage gehen wir der Frage nach, ob Patienten, die an Brustkrebs erkrankt sind und vergleichbare Krankheitszustände vorweisen, auch die gleiche Behandlung bzw. Medikation erhalten.

Eine genaue Anleitung zum klonen der Daten und des Codes und deren Ausführung auf lokalen oder cloud bassierten Systemen findet sich in [Systemumgebung](https://github.com/Fuenfgeld/DMA2022DataProjectB/wiki/Systemumgebung).

## Daten 
Der genaue Aufbau der verwendeten Daten kann hier [Datenbanktabellen](https://github.com/Fuenfgeld/DMA2022DataProjectB/wiki/Datenbanktabellen) betrachtet werden.
Die von uns generierten Daten werden auf Google Drive zur Verfügung gestellt. Die Daten sind anonymisiert und erlauben somit keinerlei Rückschlüsse auf die Identität der Patienten, sie dienen jedoch dazu die von uns verwendeten Methoden vefifizierbar zu machen. Für genauere Details über die Verfügbarmachung unserer Daten siehe [Data Sharing](https://github.com/Fuenfgeld/DMA2022DataProjectB/wiki/Datenmanagementplan#34-data-sharing)

## Methodik
Bei der Bearbeitung der Daten wurde das [Sternschema](https://de.wikipedia.org/wiki/Sternschema) als Datenmodell genutzt.
Dei bearbeiteten Daten wurden in SQL-Datenbanken geladen und auf Google Drive gespeichert.
Zur Auswertung der Daten wurde das [K-means-Verfahren](https://de.wikipedia.org/wiki/K-Means-Algorithmus) genutzt.
Ausführlichere Informationen finden sich in den [Forschungsergebnissen](https://github.com/Fuenfgeld/DMA2022DataProjectB/wiki/Forschungsergebnisse) und im Notebook [Analysis.ipynb](https://github.com/Fuenfgeld/DMA2022DataProjectB/blob/main/Code/Analysis.ipynb).

## Konklusion
Die Forschungsfrage kann positiv beschieden werden. Nach Analyse der Medikamentengabe, wurde ersichtlich, dass Pateienten mit gleichem oder vergleichbarem Krankheitszustand tatsächlich die gleiche (bzw. relativ ähnliche) Medikation erhielten. Diese trifft zumindest auf Patienten mit Brustkrebserkrankungen zu.
<br>
<br>

![Flowchart](https://raw.githubusercontent.com/Fuenfgeld/DMA2022DataProjectB/493ea8d456411bd701861dd6dcc4463d59ee2c46/Daten_schema/Links.svg)
![Flowchart](https://raw.githubusercontent.com/Fuenfgeld/DMA2022DataProjectB/main/Daten_schema/Dataflowchart.png)
 
 ## Video
 
https://drive.google.com/file/d/1afKM5Bh_LqKhpOoPfO0PVRCV1dRY66Hw/view


### Disclaimer: In dem Projekt wurden synthetische Daten verwendet. Keine echten Patienten Data (siehe https://github.com/synthetichealth/synthea) ![image](https://user-images.githubusercontent.com/32547123/180417555-d8273ff9-efbb-43f1-9e4d-cfee5d89be52.png)
