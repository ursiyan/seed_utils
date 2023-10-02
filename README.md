# BIP39 Seed Phrase Restore
This application allows you to generate a BIP39 compatible seed phrase and derive EVM (ETH, BSC, etc) addresses from it.

# Features
**Restore Seed Phrase**:<br>
Enter the existing 11 seed words (use "?" for a missing word) and generate the full seed phrase.

**Find Derived Addresses**:<br>
Generate Ethereum addresses from the provided seed phrase.

# Getting Started
1. Clone the repository to your local machine.

2. Install the necessary dependencies:<br>
`pip install eth-account mnemonic`<br>

3. Run the GUI application:<br>
`python gui.py`<br>

4. Use the GUI to input seed words, generate the full seed phrase, and derive Ethereum addresses.

# Usage
**Restore Seed Phrase:**<br>
Enter the existing seed words (or use "?" for missing words) in the provided input boxes.
Click the "Generate Seed" button to generate the full seed phrase.
The generated seed phrase will be displayed in the text box below.

**Find Derived Addresses:**<br>

Enter the seed phrase and the number of addresses to generate.
Click the "Generate Addresses" button to derive Ethereum addresses.
The addresses and corresponding private keys will be displayed in the text box below.
Optionally, check the "Save Addresses to File" checkbox to save the addresses to a file.
Contributing
If you'd like to contribute to this project, feel free to fork the repository and submit a pull request.
