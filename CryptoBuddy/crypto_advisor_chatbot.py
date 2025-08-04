import json
from datetime import datetime

class CryptoAdvisor:
    def __init__(self):
        self.crypto_db = {
            "Bitcoin": {
                "symbol": "BTC",
                "price_trend": "rising",
                "market_cap": "high",
                "energy_use": "high",
                "sustainability_score": 3/10,
                "risk_level": "high",
                "current_price": 45000
            },
            "Ethereum": {
                "symbol": "ETH",
                "price_trend": "stable",
                "market_cap": "high",
                "energy_use": "medium",
                "sustainability_score": 6/10,
                "risk_level": "medium",
                "current_price": 3000
            },
            "Cardano": {
                "symbol": "ADA",
                "price_trend": "rising",
                "market_cap": "medium",
                "energy_use": "low",
                "sustainability_score": 8/10,
                "risk_level": "medium",
                "current_price": 1.2
            },
            "Solana": {
                "symbol": "SOL",
                "price_trend": "rising",
                "market_cap": "medium",
                "energy_use": "low",
                "sustainability_score": 7/10,
                "risk_level": "medium",
                "current_price": 150
            },
            "Algorand": {
                "symbol": "ALGO",
                "price_trend": "stable",
                "market_cap": "low",
                "energy_use": "low",
                "sustainability_score": 9/10,
                "risk_level": "low",
                "current_price": 0.35
            },
            "Polkadot": {
                "symbol": "DOT",
                "price_trend": "rising",
                "market_cap": "medium",
                "energy_use": "low",
                "sustainability_score": 7/10,
                "risk_level": "medium",
                "current_price": 7.5
            },
            "Avalanche": {
                "symbol": "AVAX",
                "price_trend": "rising",
                "market_cap": "medium",
                "energy_use": "medium",
                "sustainability_score": 6/10,
                "risk_level": "high",
                "current_price": 40
            }
        }

        self.user_portfolio = {}
        self.news_sentiments = {
            "Bitcoin": 0.2,
            "Ethereum": 0.3,
            "Cardano": 0.4,
            "Solana": 0.35,
            "Algorand": 0.5,
            "Polkadot": 0.3,
            "Avalanche": 0.25
        }

    def get_live_price(self, coin_name):
        """Mock live price from dataset"""
        return self.crypto_db.get(coin_name, {}).get("current_price", "N/A")

    def get_news_sentiment(self, coin_name):
        """Mock news sentiment analysis"""
        return self.news_sentiments.get(coin_name, 0)

    def calculate_coin_score(self, coin_name):
        """Calculate a comprehensive score for a cryptocurrency"""
        coin = self.crypto_db[coin_name]

        trend_score = 0.7 if coin["price_trend"] == "rising" else 0.3
        cap_score = {"high": 0.8, "medium": 0.6, "low": 0.3}.get(coin["market_cap"], 0)
        sustain_score = coin["sustainability_score"]
        news_score = (self.get_news_sentiment(coin_name) + 1) / 2

        total_score = (
            (trend_score * 0.3) +
            (cap_score * 0.25) +
            (sustain_score * 0.25) +
            (news_score * 0.2)
        )

        return total_score

    def show_portfolio(self):
        """Display the user's portfolio"""
        if not self.user_portfolio:
            print("\nCryptoBuddy: Your portfolio is currently empty. Want to add some coins?")
            return

        print("\n📊 Your Portfolio:")
        total_value = 0

        for coin, details in self.user_portfolio.items():
            amount = details["amount"]
            buy_price = details["buy_price"]
            current_price = self.get_live_price(coin)

            value = amount * current_price
            profit = (current_price - buy_price) * amount
            roi = (profit / (buy_price * amount)) * 100 if buy_price > 0 else 0

            print(f"\n{coin} ({self.crypto_db[coin]['symbol']}):")
            print(f"- Amount: {amount} coins")
            print(f"- Buy Price: ${buy_price:.2f} each")
            print(f"- Current Price: ${current_price:.2f} each")
            print(f"- Value: ${value:.2f}")
            print(f"- Profit/Loss: ${profit:.2f} ({roi:.2f}%)")

            total_value += value

        print(f"\n💰 Total Portfolio Value: ${total_value:.2f}")

    def add_to_portfolio(self, coin_name, amount, buy_price):
        """Add or update coins in the portfolio"""
        if coin_name not in self.crypto_db:
            print(f"\nCryptoBuddy: Sorry, I don't have data for {coin_name}.")
            return False

        if coin_name in self.user_portfolio:
            existing = self.user_portfolio[coin_name]
            total_amount = existing["amount"] + amount
            avg_price = ((existing["amount"] * existing["buy_price"]) + (amount * buy_price)) / total_amount
            self.user_portfolio[coin_name] = {
                "amount": total_amount,
                "buy_price": avg_price,
                "added": existing["added"]
            }
        else:
            self.user_portfolio[coin_name] = {
                "amount": amount,
                "buy_price": buy_price,
                "added": datetime.now().strftime("%Y-%m-%d")
            }

        print(f"\nCryptoBuddy: Successfully added {amount} {coin_name} at ${buy_price:.2f} to your portfolio!")
        return True

    def get_recommendation(self, strategy="balanced"):
        """Get recommendation based on investment strategy"""
        strategies = {
            "growth": lambda x: (
                (0.5 if self.crypto_db[x]["price_trend"] == "rising" else 0) +
                (0.3 if self.crypto_db[x]["market_cap"] in ["high", "medium"] else 0) +
                (0.2 * self.crypto_db[x]["sustainability_score"])
            ),
            "sustainable": lambda x: self.crypto_db[x]["sustainability_score"],
            "balanced": lambda x: self.calculate_coin_score(x),
            "conservative": lambda x: (
                (0.3 if self.crypto_db[x]["price_trend"] == "rising" else 0) +
                (0.4 if self.crypto_db[x]["market_cap"] == "high" else 0.2) +
                (0.3 * self.crypto_db[x]["sustainability_score"])
            )
        }

        if strategy not in strategies:
            strategy = "balanced"

        scored_coins = sorted(
            [(coin, strategies[strategy](coin)) for coin in self.crypto_db],
            key=lambda x: x[1],
            reverse=True
        )

        return scored_coins

    def show_coin_details(self, coin_name):
        """Display detailed information about a specific cryptocurrency"""
        if coin_name not in self.crypto_db:
            print(f"\nCryptoBuddy: Sorry, I don't have data for {coin_name}.")
            return

        coin = self.crypto_db[coin_name]
        live_price = self.get_live_price(coin_name)

        print(f"\n📈 Detailed Analysis for {coin_name} ({coin['symbol']}):")
        print(f"- Current Price: ${live_price if live_price != 'N/A' else 'N/A'}")
        print(f"- Price Trend: {coin['price_trend'].capitalize()}")
        print(f"- Market Cap: {coin['market_cap'].capitalize()}")
        print(f"- Energy Use: {coin['energy_use'].capitalize()}")
        print(f"- Sustainability Score: {coin['sustainability_score']*10}/10")
        print(f"- Risk Level: {coin['risk_level'].capitalize()}")

        score = self.calculate_coin_score(coin_name)
        print(f"\n🌟 Overall Score: {score*100:.1f}/100")

        if score >= 0.7:
            print("💡 CryptoBuddy's Verdict: Strong potential - consider for your portfolio!")
        elif score >= 0.5:
            print("💡 CryptoBuddy's Verdict: Moderate potential - could be worth researching further")
        else:
            print("💡 CryptoBuddy's Verdict: Higher risk - proceed with caution")

    def start_chat(self):
        """Main chat interface"""
        print("\nWelcome to CryptoBuddy Pro! 🌟 Your Crypto Investment Assistant!")
        print("I can help you analyze cryptocurrencies, track your portfolio, and make informed decisions.")
        print("Type 'help' for options or 'exit' to quit.\n")

        print("⚠️ IMPORTANT: Cryptocurrency investments are volatile and risky. These are not financial recommendations.\n")
        print("Always conduct your own research before investing. Past performance ≠ future results. ⚠️\n")

        while True:
            user_input = input("You: ").lower().strip()

            if user_input == 'exit':
                print("\nCryptoBuddy: Happy investing! 🚀\n")
                break
                
            elif user_input == 'help':
                print("\nCryptoBuddy: Here's what I can help with:")
                print("- 'trending': Show cryptocurrencies with rising prices")
                print("- 'sustainable': Find eco-friendly cryptocurrencies")
                print("- 'growth': Get high-growth potential recommendations")
                print("- 'balanced': Find coins with good growth and sustainability")
                print("- 'conservative': Lower-risk investment options")
                print("- 'portfolio': View or update your investment portfolio")
                print("- 'details [coin]': Get detailed analysis of a specific cryptocurrency")
                print("- 'all': Display all cryptocurrencies in my database")
                print("- 'news [coin]': Get sentiment analysis for a cryptocurrency")
                print("- 'exit': End our conversation\n")
            
            elif 'trending' in user_input or 'rising' in user_input:
                trending_coins = [coin for coin in self.crypto_db if self.crypto_db[coin]["price_trend"] == "rising"]
                if trending_coins:
                    print("\nCryptoBuddy: These cryptocurrencies are currently trending up: 📈")
                    for coin in trending_coins:
                        score = self.calculate_coin_score(coin)
                        print(f"- {coin}: Market cap {self.crypto_db[coin]['market_cap']}, "
                              f"Sustainability {self.crypto_db[coin]['sustainability_score']*10}/10, "
                              f"Overall score {score*100:.1f}/100")
                    print("\nRemember: Trends can change quickly in crypto markets!\n")
                else:
                    print("\nCryptoBuddy: Currently no cryptocurrencies show a strong upward trend. Maybe check back later!\n")
                    
            elif 'sustain' in user_input or 'eco' in user_input or 'green' in user_input:
                sustainable_coins = self.get_recommendation("sustainable")
                print("\nCryptoBuddy: Here are cryptocurrencies ranked by sustainability: 🌱")
                for coin, score in sustainable_coins[:5]:  # Show top 5
                    print(f"- {coin}: Sustainability score {score*10:.1f}/10, "
                          f"Energy use is {self.crypto_db[coin]['energy_use']}, "
                          f"Risk level: {self.crypto_db[coin]['risk_level']}")
                print("\nTip: Sustainable coins often have better long-term viability but may have lower short-term gains!\n")
                
            elif 'growth' in user_input or 'profit' in user_input:
                growth_coins = self.get_recommendation("growth")
                print("\nCryptoBuddy: These cryptocurrencies show good growth potential: 💹")
                for coin, score in growth_coins[:5]:  # Show top 5
                    print(f"- {coin}: Growth score {score*100:.1f}/100, "
                          f"Price trend: {self.crypto_db[coin]['price_trend']}, "
                          f"Risk level: {self.crypto_db[coin]['risk_level']}")
                print("\nNote: Higher growth potential often comes with higher risk!\n")
                
            elif 'balance' in user_input:
                balanced_coins = self.get_recommendation("balanced")
                print("\nCryptoBuddy: Best balanced options (growth + sustainability): ⚖️")
                for coin, score in balanced_coins[:3]:
                    print(f"- {coin}: Balanced score {score*100:.1f}/100")
                    print(f"  Trend: {self.crypto_db[coin]['price_trend']}, "
                          f"Sustain: {self.crypto_db[coin]['sustainability_score']*10}/10, "
                          f"Risk: {self.crypto_db[coin]['risk_level']}")
                print("\nThese offer a mix of growth potential and responsible investing!\n")
                
            elif 'conservative' in user_input:
                conservative_coins = self.get_recommendation("conservative")
                print("\nCryptoBuddy: Lower-risk cryptocurrency options: 🛡️")
                for coin, score in conservative_coins[:3]:
                    print(f"- {coin}: Safety score {score*100:.1f}/100")
                    print(f"  Risk level: {self.crypto_db[coin]['risk_level']}, "
                          f"Market cap: {self.crypto_db[coin]['market_cap']}, "
                          f"Volatility: {self.crypto_db[coin]['price_trend']}")
                print("\nThese may provide more stable returns with lower risk!\n")
                
            elif 'portfolio' in user_input:
                if 'add' in user_input:
                    try:
                        parts = user_input.split()
                        coin_name = parts[parts.index('add')+1].capitalize()
                        amount = float(parts[parts.index('add')+2])
                        price = float(parts[parts.index('add')+3])
                        self.add_to_portfolio(coin_name, amount, price)
                    except:
                        print("\nCryptoBuddy: Please use format: 'portfolio add [coin] [amount] [price]'")
                else:
                    self.show_portfolio()
                    
            elif 'details' in user_input:
                coin_name = user_input.replace('details', '').strip().capitalize()
                if coin_name:
                    self.show_coin_details(coin_name)
                else:
                    print("\nCryptoBuddy: Please specify a coin, like 'details bitcoin'")
                    
            elif 'news' in user_input:
                coin_name = user_input.replace('news', '').strip().capitalize()
                if coin_name in self.crypto_db:
                    sentiment = self.get_news_sentiment(coin_name)
                    if sentiment > 0.2:
                        print(f"\nCryptoBuddy: Recent news sentiment for {coin_name} is positive! 😊")
                    elif sentiment < -0.2:
                        print(f"\nCryptoBuddy: Recent news sentiment for {coin_name} is negative. 😟")
                    else:
                        print(f"\nCryptoBuddy: Recent news sentiment for {coin_name} is neutral. 😐")
                    print(f"Sentiment score: {sentiment:.2f} (range -1 to 1)\n")
                else:
                    print("\nCryptoBuddy: Sorry, I don't have news data for that cryptocurrency.")
                    
            elif 'all' in user_input:
                print("\nCryptoBuddy: Here's my complete cryptocurrency database: 📊")
                for coin in sorted(self.crypto_db.keys()):
                    score = self.calculate_coin_score(coin)
                    print(f"\n{coin} ({self.crypto_db[coin]['symbol']}):")
                    print(f"- Price trend: {self.crypto_db[coin]['price_trend']}")
                    print(f"- Market cap: {self.crypto_db[coin]['market_cap']}")
                    print(f"- Energy use: {self.crypto_db[coin]['energy_use']}")
                    print(f"- Sustainability: {self.crypto_db[coin]['sustainability_score']*10}/10")
                    print(f"- Risk level: {self.crypto_db[coin]['risk_level']}")
                    print(f"- Overall score: {score*100:.1f}/100")
                print("\n")
                
            else:
                print("\nCryptoBuddy: I'm not sure I understand. Try asking about:")
                print("- 'trending' cryptos")
                print("- 'sustainable' investment options")
                print("- 'growth' opportunities")
                print("- Your 'portfolio'")
                print("Or type 'help' to see all options.\n")

if __name__ == "__main__":
    advisor = CryptoAdvisor()
    advisor.start_chat()