import pytz
import yfinance as yf

def get_yf_stock_info(ticker: str):
    stock = yf.Ticker(ticker)
    info = stock.info
    print(info)
    return str(info)

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_yf_stock_info",
            "description": "해당 종목의 Yahoo Finance 정보를 반환합니다.",
            "parameters": {
                "type": "object",
                "properties": {
                    'ticker': {
                        'type': 'string',
                        'description': 'Yahoo Finance 정보를 반환할 종목의 티커를 입력하세요. (예: AAPL)',
                    },
                },
                "required": ['ticker'],
            },
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_yf_stock_history",
            "description": "해당 종목의 Yahoo Finance 주가 정보를 반환합니다.",
            "parameters": {
                "type": "object",
                "properties": {
                    'ticker': {
                        'type': 'string',
                        'description': 'Yahoo Finance 주가 정보를 반환할 종목의 티커를 입력하세요. (예: AAPL)',
                    },
                    'period': {
                        'type': 'string',
                        'description': '주가 정보를 조회할 기간을 입력하세요. (예: 1d, 5d, 1mo, 1y, 5y)',
                    },
                },
                "required": ['ticker', 'period'],
            },
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_yf_stock_recommendations",
            "description": "해당 종목의 Yahoo Finance 추천 정보를 반환합니다.",
            "parameters": {
                "type": "object",
                "properties": {
                    'ticker': {
                        'type': 'string',
                        'description': 'Yahoo Finance 추천 정보를 반환할 종목의 티커를 입력하세요. (예: AAPL)',
                    },
                },
                "required": ['ticker'],
            },
        }
    },
]

if __name__ == '__main__':
    info = get_yf_stock_info('AAPL')
