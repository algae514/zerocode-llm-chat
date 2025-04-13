# API Keys Guide

This guide explains how to obtain and configure API keys for the ZeroCode LLM Chat Client.

## Table of Contents
- [OpenAI API Keys](#openai-api-keys)
- [Anthropic API Keys](#anthropic-api-keys)
- [Setting Up Your Keys](#setting-up-your-keys)
- [Managing Costs](#managing-costs)
- [Security Considerations](#security-considerations)

## OpenAI API Keys

OpenAI provides the GPT family of models (gpt-3.5-turbo, gpt-4, etc.).

### Getting an OpenAI API Key

1. Go to [OpenAI Platform](https://platform.openai.com/)
2. Create an account or sign in
3. Navigate to the [API Keys section](https://platform.openai.com/api-keys)
4. Click "Create new secret key"
5. Enter a name for your key (e.g., "ZeroCode LLM Chat")
6. Copy the key immediately (you won't be able to see it again)

### OpenAI Pricing

OpenAI charges based on the number of tokens used:
- Input tokens (your messages to the AI)
- Output tokens (the AI's responses)

Prices vary by model:
- gpt-3.5-turbo: Lower cost, suitable for most use cases
- gpt-4: Higher cost, more capable for complex tasks

For current pricing, visit the [OpenAI Pricing page](https://openai.com/pricing).

## Anthropic API Keys

Anthropic provides the Claude family of models (claude-3-opus, claude-3-sonnet, claude-3-haiku).

### Getting an Anthropic API Key

1. Go to [Anthropic Console](https://console.anthropic.com/)
2. Create an account or sign in
3. Navigate to the [API Keys section](https://console.anthropic.com/settings/keys)
4. Click "Create Key"
5. Enter a name for your key (e.g., "ZeroCode LLM Chat")
6. Set appropriate permissions and expiration
7. Copy the key immediately (you won't be able to see it again)

### Anthropic Pricing

Anthropic also charges based on tokens used, with different rates for:
- Input tokens (your messages to the AI)
- Output tokens (the AI's responses)

Prices vary by model:
- claude-3-haiku: Lowest cost, fastest
- claude-3-sonnet: Mid-tier pricing and capabilities
- claude-3-opus: Highest cost, most capable

For current pricing, visit the [Anthropic Pricing page](https://www.anthropic.com/api).

## Setting Up Your Keys

### In the .env File

1. Create a file named `.env` in the root directory of the application
2. Add your API keys in the following format:
   ```
   OPENAI_API_KEY=your_openai_key_here
   ANTHROPIC_API_KEY=your_anthropic_key_here
   ```
3. Save the file
4. Restart the application if it's already running

You only need one key to use the application, but adding both gives you access to all supported models.

### Key Security

- Never share your API keys with others
- Don't commit your .env file to version control
- Consider setting expiration dates on your keys if possible
- Rotate keys periodically for better security

## Managing Costs

### Cost Control Tips

1. **Monitor usage**: Both OpenAI and Anthropic provide dashboards to track API usage
2. **Set spending limits**: Configure spending caps in your OpenAI/Anthropic account settings
3. **Use efficient models**: For simpler tasks, use gpt-3.5-turbo or claude-3-haiku
4. **Optimize message length**: Shorter messages use fewer tokens

### Estimating Costs

As a rough estimate:
- 1,000 tokens is approximately 750 words
- A typical conversation might use 2,000-5,000 tokens

For specific pricing, check the providers' websites as pricing may change.

## Security Considerations

### Local Storage

ZeroCode stores:
- API keys in the .env file
- Conversations in a local SQLite database

None of your data is sent to any servers except the AI provider you choose (OpenAI or Anthropic).

### Best Practices

1. Keep your operating system and Python updated
2. Don't share your API keys
3. Be cautious about what information you share in conversations
4. Consider using API keys with limited permissions

### Rate Limits

Both OpenAI and Anthropic have rate limits to prevent abuse. If you encounter errors about exceeding rate limits, wait a few minutes before trying again.
