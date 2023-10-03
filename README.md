# BIP39 Seed Phrase Restore
This repository contains Python code that implements a graphical user interface (GUI) application for restoring a BIP39 seed phrase, generating Ethereum addresses, and checking their balances. The application leverages various Python libraries to achieve these functionalities.

# Features
**Restore Seed Phrase**:<br>
Enter the existing 11 seed words (use "?" for a missing word) and generate the full seed phrase.

**Find Derived Addresses**:<br>
Generate Ethereum addresses from the provided seed phrase.

**Check Address Balances**:<br>
Check the balances of Ethereum addresses derived from the seed phrase on different EVM-compatible networks (Ethereum, Arbitrum, Binance Smart Chain, Polygon).

# Getting Started
1. Clone the repository to your local machine.

2. Install the necessary dependencies:<br>
`pip install eth-account mnemonic requests web3`<br>

3. Run the GUI application:<br>
`python gui.py`<br>

4. Use the GUI to input seed words, generate the full seed phrase, derive Ethereum addresses, and check their balances.

# Usage
**Restore Seed Phrase:**<br>
1. Enter the existing seed words (or use "?" for missing words) in the provided input boxes.
2. Click the "Generate Seed" button to generate the full seed phrase.
3. The generated seed phrase will be displayed in the text box below.

**Find Derived Addresses:**<br>
1. Enter the seed phrase and the number of addresses to generate.
2. Click the "Generate Addresses" button to derive Ethereum addresses.
3. The addresses and corresponding private keys (if chosen) will be displayed in the text box below.
4. Optionally, check the "Save Addresses to File" checkbox to save the addresses to a file.

**Check Address Balances:**<br>
1. Click "Display Addresses" to show the addresses previously generated or manually input them.
2. Click "Check Balance" to retrieve and display the Ethereum balances of the provided addresses on various EVM-compatible networks.
