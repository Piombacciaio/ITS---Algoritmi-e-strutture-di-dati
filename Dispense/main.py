import webbrowser
import os

dispesa_link = {
    "Flowchart - Algoritmi- UniPV":"https://robot.unipv.it/toolleeo/teaching/docs_fdi/fdi_flowchart.pdf"

}



def dispensa():
    
    mappatura_id_chiave = {} 
    for i, chiave in enumerate(dispesa_link.keys()):
        mappatura_id_chiave[i + 1] = chiave



    while True:

        os.system('cls' if os.name == 'nt' else 'clear')
        print("Seleziona una dispensa:")
        for id_val, nome_dispensa in mappatura_id_chiave.items():
            print(f"{id_val}: {nome_dispensa}")
        try:
            scelta_id = int(input("Inserisci l'ID della dispensa che vuoi aprire (99 per uscire): "))
            
            if scelta_id == 99:
                break
            
            
            if scelta_id in mappatura_id_chiave:
                nome_dispensa = mappatura_id_chiave[scelta_id]
                link = dispesa_link[nome_dispensa]
                
                print(f"Apertura di '{nome_dispensa}'...")
                webbrowser.open(link)
                input("\n\nPremi per continuare")

                
        except ValueError:
            continue

