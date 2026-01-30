# Ticketmaster Automation Guide

This guide explains how to interact with Ticketmaster's services responsibly and legally using their official API.

## ⚠️ Important Warning: Unauthorized Bots

Creating bots to automate ticket purchasing (often called "scalping bots" or "spinner bots") is generally against Ticketmaster's Terms of Service and can lead to severe consequences, including:
- **Account Bans:** Your account and IP address may be permanently banned.
- **Legal Action:** In many jurisdictions, including the United States (under the BOTS Act of 2016), using automated software to bypass security measures on ticket selling websites is **illegal**.
- **Ethical Concerns:** Scalping bots unfairly disadvantage legitimate fans.

**This guide does NOT provide instructions for bypassing queues, CAPTCHAs, or purchasing tickets automatically.**

## 🛡️ Internal Testing & Simulation

For users conducting authorized internal testing or ethical verification of ticket availability:

- **Use the API:** The most reliable way to simulate "monitoring" or "checking" for tickets is via the API. This avoids the brittleness of browser automation and provides structured data.
- **Monitoring vs. Buying:** While the API allows you to find tickets instantly, the actual purchase should be completed by following the `url` provided in the API response.
- **Rate Limits:** Be mindful of API rate limits. Polling too frequently can result in 429 (Too Many Requests) errors.

## ✅ Legitimate Alternative: The Ticketmaster Discovery API

Ticketmaster provides an official **Discovery API** that allows developers to search for events, attractions, and venues. This is the approved way to build applications that integrate with Ticketmaster data.

### What you can do with the Discovery API:
- Search for events by keyword, location, or date.
- Get details about venues and attractions.
- Find legitimate ticket links.

### Prerequisites

1.  **Ticketmaster Developer Account:** You need to register for a developer account at [developer.ticketmaster.com](https://developer.ticketmaster.com/).
2.  **API Key:** Once registered, create an app to get your unique API Key (Consumer Key).
3.  **Python:** You need Python installed on your computer.

## Using the Python Script

We have provided a script `ticket_search.py` that demonstrates how to use the Discovery API to search for events.

### Running the Script

Open your terminal or command prompt and run:

```bash
python3 ticket_search.py
```

Follow the prompts to enter a keyword (e.g., "Taylor Swift" or "New York"). The script will display a list of matching events with their dates, venues, and ticket links.

### Note on API Endpoint
The script uses the standard Discovery API endpoint: `https://app.ticketmaster.com/discovery/v2/events.json`.
Please refer to the [official documentation](https://developer.ticketmaster.com/products-and-docs/apis/discovery-api/v2/) if you encounter issues or if the API version changes.
