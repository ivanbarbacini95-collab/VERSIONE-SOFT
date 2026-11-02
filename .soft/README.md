# INJ Node — Versione Soft

Versione sperimentale **Tech Soft** dell'intera applicazione INJ Node.

## Design

Ispirata alla pagina Lite: fondo continuo, pannelli dalle superfici morbide,
micro-bordi, colore d'accento discreto, font leggibili, dati con cifre tabulari,
controlli leggeri e comportamento responsive per telefono e desktop.

Il design viene applicato a tutte le pagine HTML tramite \`tech-soft.css\`, un
livello visivo condiviso caricato **dopo** i CSS delle singole sezioni.
La pagina Lite continua a funzionare con il proprio grafico e la propria logica;
la modalità Pro resta disponibile.

## Base applicativa

L'intero contenuto funzionale deriva dal commit ufficiale
\`f64aea751dc86dbbe0b071983924f41494f35c92\`
di \`ivanbarbacini95-collab/INJ-VERSIONE-UFFICIALE\`.
I flussi per wallet, market, live chart, Treasury, reward, workspace e PWA
non vengono sostituiti con dati simulati.

## Aggiornamento repository

La GitHub Action \`build-tech-soft.yml\` copia il commit ufficiale fissato,
preserva la cartella \`.soft\` e il workflow di questa variante, quindi
applica il sistema visivo con \`python3 .soft/install.py\`.
Il risultato viene pubblicato sul branch \`main\` di VERSIONE-SOFT.

**Non modifica INJ-VERSIONE-UFFICIALE.**

## Verifica

Controllare con dispositivo reale le pagine Market, Treasury, grafici,
Live Reward, navigazione mobile/Android e impostazioni.
L'aspetto grafico non costituisce una verifica della disponibilità delle API live.
