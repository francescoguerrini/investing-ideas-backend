import yfinance as yf
import datetime as dt

def fetch_company_data(ticker: str) -> dict:
    """
    Recupera i dati di una compagnia dato il ticker, usando yfinance.
    Restituisce un dizionario con informazioni rilevanti, inclusa la performance rispetto al 31 dicembre dell'anno scorso rispetto a quello precedente.
    """
    try:
        # Ottieni il ticker tramite yfinance
        stock = yf.Ticker(ticker)
        
        # Recupera le informazioni principali della compagnia
        stock_info = stock.info

        # Se il ticker non è valido o i dati non sono disponibili
        if 'longName' not in stock_info:
            raise ValueError(f"Dati non trovati per il ticker {ticker}")

        # Recupera i dettagli rilevanti per l'azienda
        company_data = {
            "ticker": ticker,
            "name": stock_info.get("longName", "Nome non disponibile"),
            "current_price": stock_info.get("currentPrice", "Prezzo non disponibile"),
            "market_cap": stock_info.get("marketCap", "Non Disponibile"),
            "pe_ratio": stock_info.get("trailingPE", "-"),
            "dividend_yield": stock_info.get("dividendYield", "-"),
            "industry": stock_info.get("industry", "Generic"),
            "sector": stock_info.get("sector", "Generic"),
            "chart_link": f"https://finance.yahoo.com/chart/{ticker}"  # Link alla chart

        }

        # Calcolare la performance tra il 31 dicembre di due anni fa e il 31 dicembre dell'anno scorso
        today = dt.datetime.today()
        start_date = dt.datetime(today.year - 1, 1, 1).strftime('%Y-%m-%d')  # 1 gennaio anno precedente
        end_date = dt.datetime(today.year - 1, 12, 31).strftime('%Y-%m-%d')  # 31 dicembre anno precedente
        
        data = stock.history(start=start_date, end=end_date)

        # Verifica che ci siano dati storici per il periodo
        if data.empty:
            company_data["performance"] = "Dati non disponibili"
        else:
            # Prezzo di chiusura il 31 dicembre di due anni fa
            start_price = data.iloc[0]['Close']
            # Prezzo di chiusura il 31 dicembre dell'anno scorso
            end_price = data.iloc[-1]['Close']
            
            # Calcola la performance in percentuale
            performance_percent = ((end_price - start_price) / start_price) * 100
            company_data["performance"] = f"{performance_percent:.2f}%"

        return company_data

    except Exception as e:
        print(f"Errore nel recupero dei dati per {ticker}: {e}")
        return None
