# Spam form python

Questo progetto Python è composto da due script distinti per la registrazione di utenti e il caricamento di file su un sito web. Gli script sono progettati per essere utilizzati a scopo dimostrativo e educativo, e l'uso improprio è fortemente sconsigliato.

## Registrazione Utenti

Lo script `main.py` permette la registrazione di un gran numero di utenti su una pagina web di registrazione. Ecco come utilizzarlo:

### Prerequisiti

- Python installato sul sistema.
- La libreria `requests` installata. Puoi installarla eseguendo `pip install requests`.
- La libreria `concurrent.futures` installata. Puoi installarla con `pip install futures`.
- La libreria `Faker` installata. Puoi installarla con `pip install faker`.

### Utilizzo

1. Esegui lo script `main.py` fornendo l'URL del modulo di registrazione e il percorso di un file JSON contenente i dati di registrazione. Ad esempio:

```bash
python main.py -n 1000000 -t 1000 -v -r https://example/register.php data.json
```

- `-t` specifica il numero di thread.
- `-n` specifica il numero di utenti da registrare.
- `-r` abilita l'uso di dati casuali per la registrazione.
- `-l` specifica il percorso del file di log.
- `-v` abilita la visualizzazione dei messaggi di log sulla console.

## Caricamento File

Lo script `upload_file_form.py` consente di caricare file su una pagina web tramite richieste POST parallele. Ecco come utilizzarlo:

### Prerequisiti

- Python installato sul sistema.
- La libreria `requests` installata. Puoi installarla eseguendo `pip install requests`.

### Utilizzo

1. Esegui lo script `upload_file_form.py` fornendo l'URL del modulo di caricamento dei file, il numero di upload, e la dimensione dei file. Ad esempio:

```bash
python upload_file_form.py https://example.com/upload 1 10000000
```

- Il numero di thread è impostato internamente nello script.

## Avvertenze

- L'uso responsabile e legale di questi script è fondamentale.
- Assicurati di rispettare le leggi e le regolamentazioni locali quando utilizzi questi script.
- Questi script sono forniti solo a scopo educativo e dimostrativo.

## Contributi

Se desideri contribuire a migliorare questi script, sentiti libero di farlo tramite pull request.

## Licenza

Questi script sono concessi in licenza secondo i termini della licenza MIT.