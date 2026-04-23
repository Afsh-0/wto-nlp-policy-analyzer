#it takes structred input and returns human like insights 
def generate_insights(entities):
    insights = [] #store final “meaningful statements”

    countries = list(set(entities.get("GPE", [])))
    orgs = list(set(entities.get("ORG", [])))
    money = list(set(entities.get("MONEY", [])))

    # Insight 1: Country focus
    if countries:
        insights.append(f"Main countries discussed: {', '.join(countries[:5])}")
        #If countries exist, Show first 5 only and Convert into readable sentence

    # Insight 2: Trade organizations
    if orgs:
        insights.append(f"Key organizations involved: {', '.join(orgs[:5])}")

    # Insight 3: Trade intensity
    if money:
        insights.append(f"Trade/financial references detected: {len(money)} monetary mentions")

    # Insight 4: Complexity indicator
    if len(countries) > 5:
        insights.append("High geopolitical complexity detected (multiple countries involved)")

    return insights