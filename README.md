# Spam Form PHP

Questo progetto è un semplice script PHP per inviare spam a un modulo di registrazione su un sito web. È stato creato per scopi di dimostrazione e non deve essere utilizzato per scopi illegali o dannosi.

## Come funziona

Lo script PHP utilizza la libreria cURL per inviare richieste POST al modulo di registrazione del sito web di destinazione. L'obiettivo è inundare il modulo con dati di registrazione generati casualmente, creando un alto volume di richieste e sovraccaricando il server.

## Prerequisiti

Per utilizzare lo script, assicurati di avere:

- Un server web con PHP installato.
- L'estensione cURL abilitata in PHP.

## Utilizzo

1. Scarica il repository o clona il progetto sul tuo server web.
2. Apri il file `spam.php` in un editor di testo.
3. Modifica la variabile `$targetURL` con l'URL del modulo di registrazione del sito web di destinazione.
4. Modifica i parametri del modulo di registrazione nel corpo della richiesta POST in base alle specifiche del modulo di destinazione (es. `name`, `email`, `message`, ecc.).
5. Salva le modifiche al file `spam.php`.
6. Apri il file `spam.php` nel tuo browser o eseguilo da riga di comando utilizzando il comando `php spam.php`.

## Avvertenze

- L'utilizzo di questo script per scopi illegali o dannosi è strettamente vietato.
- L'autore e il repository declinano ogni responsabilità per un uso improprio dello script.
- Assicurati di rispettare le leggi e i regolamenti locali quando utilizzi questo script.
- Questo progetto è fornito solo a scopo educativo e di dimostrazione.

## Contributi

Se desideri contribuire a questo progetto, sei il benvenuto! Puoi creare una pull request per suggerire miglioramenti, risolvere problemi o aggiungere nuove funzionalità.

## Licenza

Questo progetto è concesso in licenza secondo i termini della licenza MIT.
