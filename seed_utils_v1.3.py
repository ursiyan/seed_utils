import hashlib
import tkinter as tk
from tkinter import ttk,messagebox
from eth_account import Account
from mnemonic import Mnemonic

normal_seed = ""
seed_phrase = ""
word_list_str = "abandon ability able about above absent absorb abstract absurd abuse access accident account accuse achieve acid acoustic acquire across act action actor actress actual adapt add addict address adjust admit adult advance advice aerobic affair afford afraid again age agent agree ahead aim air airport aisle alarm album alcohol alert alien all alley allow almost alone alpha already also alter always amateur amazing among amount amused analyst anchor ancient anger angle angry animal ankle announce annual another answer antenna antique anxiety any apart apology appear apple approve april arch arctic area arena argue arm armed armor army around arrange arrest arrive arrow art artefact artist artwork ask aspect assault asset assist assume asthma athlete atom attack attend attitude attract auction audit august aunt author auto autumn average avocado avoid awake aware away awesome awful awkward axis baby bachelor bacon badge bag balance balcony ball bamboo banana banner bar barely bargain barrel base basic basket battle beach bean beauty because become beef before begin behave behind believe below belt bench benefit best betray better between beyond bicycle bid bike bind biology bird birth bitter black blade blame blanket blast bleak bless blind blood blossom blouse blue blur blush board boat body boil bomb bone bonus book boost border boring borrow boss bottom bounce box boy bracket brain brand brass brave bread breeze brick bridge brief bright bring brisk broccoli broken bronze broom brother brown brush bubble buddy budget buffalo build bulb bulk bullet bundle bunker burden burger burst bus business busy butter buyer buzz cabbage cabin cable cactus cage cake call calm camera camp can canal cancel candy cannon canoe canvas canyon capable capital captain car carbon card cargo carpet carry cart case cash casino castle casual cat catalog catch category cattle caught cause caution cave ceiling celery cement census century cereal certain chair chalk champion change chaos chapter charge chase chat cheap check cheese chef cherry chest chicken chief child chimney choice choose chronic chuckle chunk churn cigar cinnamon circle citizen city civil claim clap clarify claw clay clean clerk clever click client cliff climb clinic clip clock clog close cloth cloud clown club clump cluster clutch coach coast coconut code coffee coil coin collect color column combine come comfort comic common company concert conduct confirm congress connect consider control convince cook cool copper copy coral core corn correct cost cotton couch country couple course cousin cover coyote crack cradle craft cram crane crash crater crawl crazy cream credit creek crew cricket crime crisp critic crop cross crouch crowd crucial cruel cruise crumble crunch crush cry crystal cube culture cup cupboard curious current curtain curve cushion custom cute cycle dad damage damp dance danger daring dash daughter dawn day deal debate debris decade december decide decline decorate decrease deer defense define defy degree delay deliver demand demise denial dentist deny depart depend deposit depth deputy derive describe desert design desk despair destroy detail detect develop device devote diagram dial diamond diary dice diesel diet differ digital dignity dilemma dinner dinosaur direct dirt disagree discover disease dish dismiss disorder display distance divert divide divorce dizzy doctor document dog doll dolphin domain donate donkey donor door dose double dove draft dragon drama drastic draw dream dress drift drill drink drip drive drop drum dry duck dumb dune during dust dutch duty dwarf dynamic eager eagle early earn earth easily east easy echo ecology economy edge edit educate effort egg eight either elbow elder electric elegant element elephant elevator elite else embark embody embrace emerge emotion employ empower empty enable enact end endless endorse enemy energy enforce engage engine enhance enjoy enlist enough enrich enroll ensure enter entire entry envelope episode equal equip era erase erode erosion error erupt escape essay essence estate eternal ethics evidence evil evoke evolve exact example excess exchange excite exclude excuse execute exercise exhaust exhibit exile exist exit exotic expand expect expire explain expose express extend extra eye eyebrow fabric face faculty fade faint faith fall false fame family famous fan fancy fantasy farm fashion fat fatal father fatigue fault favorite feature february federal fee feed feel female fence festival fetch fever few fiber fiction field figure file film filter final find fine finger finish fire firm first fiscal fish fit fitness fix flag flame flash flat flavor flee flight flip float flock floor flower fluid flush fly foam focus fog foil fold follow food foot force forest forget fork fortune forum forward fossil foster found fox fragile frame frequent fresh friend fringe frog front frost frown frozen fruit fuel fun funny furnace fury future gadget gain galaxy gallery game gap garage garbage garden garlic garment gas gasp gate gather gauge gaze general genius genre gentle genuine gesture ghost giant gift giggle ginger giraffe girl give glad glance glare glass glide glimpse globe gloom glory glove glow glue goat goddess gold good goose gorilla gospel gossip govern gown grab grace grain grant grape grass gravity great green grid grief grit grocery group grow grunt guard guess guide guilt guitar gun gym habit hair half hammer hamster hand happy harbor hard harsh harvest hat have hawk hazard head health heart heavy hedgehog height hello helmet help hen hero hidden high hill hint hip hire history hobby hockey hold hole holiday hollow home honey hood hope horn horror horse hospital host hotel hour hover hub huge human humble humor hundred hungry hunt hurdle hurry hurt husband hybrid ice icon idea identify idle ignore ill illegal illness image imitate immense immune impact impose improve impulse inch include income increase index indicate indoor industry infant inflict inform inhale inherit initial inject injury inmate inner innocent input inquiry insane insect inside inspire install intact interest into invest invite involve iron island isolate issue item ivory jacket jaguar jar jazz jealous jeans jelly jewel job join joke journey joy judge juice jump jungle junior junk just kangaroo keen keep ketchup key kick kid kidney kind kingdom kiss kit kitchen kite kitten kiwi knee knife knock know lab label labor ladder lady lake lamp language laptop large later latin laugh laundry lava law lawn lawsuit layer lazy leader leaf learn leave lecture left leg legal legend leisure lemon lend length lens leopard lesson letter level liar liberty library license life lift light like limb limit link lion liquid list little live lizard load loan lobster local lock logic lonely long loop lottery loud lounge love loyal lucky luggage lumber lunar lunch luxury lyrics machine mad magic magnet maid mail main major make mammal man manage mandate mango mansion manual maple marble march margin marine market marriage mask mass master match material math matrix matter maximum maze meadow mean measure meat mechanic medal media melody melt member memory mention menu mercy merge merit merry mesh message metal method middle midnight milk million mimic mind minimum minor minute miracle mirror misery miss mistake mix mixed mixture mobile model modify mom moment monitor monkey monster month moon moral more morning mosquito mother motion motor mountain mouse move movie much muffin mule multiply muscle museum mushroom music must mutual myself mystery myth naive name napkin narrow nasty nation nature near neck need negative neglect neither nephew nerve nest net network neutral never news next nice night noble noise nominee noodle normal north nose notable note nothing notice novel now nuclear number nurse nut oak obey object oblige obscure observe obtain obvious occur ocean october odor off offer office often oil okay old olive olympic omit once one onion online only open opera opinion oppose option orange orbit orchard order ordinary organ orient original orphan ostrich other outdoor outer output outside oval oven over own owner oxygen oyster ozone pact paddle page pair palace palm panda panel panic panther paper parade parent park parrot party pass patch path patient patrol pattern pause pave payment peace peanut pear peasant pelican pen penalty pencil people pepper perfect permit person pet phone photo phrase physical piano picnic picture piece pig pigeon pill pilot pink pioneer pipe pistol pitch pizza place planet plastic plate play please pledge pluck plug plunge poem poet point polar pole police pond pony pool popular portion position possible post potato pottery poverty powder power practice praise predict prefer prepare present pretty prevent price pride primary print priority prison private prize problem process produce profit program project promote proof property prosper protect proud provide public pudding pull pulp pulse pumpkin punch pupil puppy purchase purity purpose purse push put puzzle pyramid quality quantum quarter question quick quit quiz quote rabbit raccoon race rack radar radio rail rain raise rally ramp ranch random range rapid rare rate rather raven raw razor ready real reason rebel rebuild recall receive recipe record recycle reduce reflect reform refuse region regret regular reject relax release relief rely remain remember remind remove render renew rent reopen repair repeat replace report require rescue resemble resist resource response result retire retreat return reunion reveal review reward rhythm rib ribbon rice rich ride ridge rifle right rigid ring riot ripple risk ritual rival river road roast robot robust rocket romance roof rookie room rose rotate rough round route royal rubber rude rug rule run runway rural sad saddle sadness safe sail salad salmon salon salt salute same sample sand satisfy satoshi sauce sausage save say scale scan scare scatter scene scheme school science scissors scorpion scout scrap screen script scrub sea search season seat second secret section security seed seek segment select sell seminar senior sense sentence series service session settle setup seven shadow shaft shallow share shed shell sheriff shield shift shine ship shiver shock shoe shoot shop short shoulder shove shrimp shrug shuffle shy sibling sick side siege sight sign silent silk silly silver similar simple since sing siren sister situate six size skate sketch ski skill skin skirt skull slab slam sleep slender slice slide slight slim slogan slot slow slush small smart smile smoke smooth snack snake snap sniff snow soap soccer social sock soda soft solar soldier solid solution solve someone song soon sorry sort soul sound soup source south space spare spatial spawn speak special speed spell spend sphere spice spider spike spin spirit split spoil sponsor spoon sport spot spray spread spring spy square squeeze squirrel stable stadium staff stage stairs stamp stand start state stay steak steel stem step stereo stick still sting stock stomach stone stool story stove strategy street strike strong struggle student stuff stumble style subject submit subway success such sudden suffer sugar suggest suit summer sun sunny sunset super supply supreme sure surface surge surprise surround survey suspect sustain swallow swamp swap swarm swear sweet swift swim swing switch sword symbol symptom syrup system table tackle tag tail talent talk tank tape target task taste tattoo taxi teach team tell ten tenant tennis tent term test text thank that theme then theory there they thing this thought three thrive throw thumb thunder ticket tide tiger tilt timber time tiny tip tired tissue title toast tobacco today toddler toe together toilet token tomato tomorrow tone tongue tonight tool tooth top topic topple torch tornado tortoise toss total tourist toward tower town toy track trade traffic tragic train transfer trap trash travel tray treat tree trend trial tribe trick trigger trim trip trophy trouble truck true truly trumpet trust truth try tube tuition tumble tuna tunnel turkey turn turtle twelve twenty twice twin twist two type typical ugly umbrella unable unaware uncle uncover under undo unfair unfold unhappy uniform unique unit universe unknown unlock until unusual unveil update upgrade uphold upon upper upset urban urge usage use used useful useless usual utility vacant vacuum vague valid valley valve van vanish vapor various vast vault vehicle velvet vendor venture venue verb verify version very vessel veteran viable vibrant vicious victory video view village vintage violin virtual virus visa visit visual vital vivid vocal voice void volcano volume vote voyage wage wagon wait walk wall walnut want warfare warm warrior wash wasp waste water wave way wealth weapon wear weasel weather web wedding weekend weird welcome west wet whale what wheat wheel when where whip whisper wide width wife wild will win window wine wing wink winner winter wire wisdom wise wish witness wolf woman wonder wood wool word work world worry worth wrap wreck wrestle wrist write wrong yard year yellow you young youth zebra zero zone zoo"
DERIVATION_PATH = "m/44'/60'/0'/0/{}"
seed_phrase_index = ""
seed_phrase_binary = ""
ethereum_addresses = ""

# Enable Mnemonic features
Account.enable_unaudited_hdwallet_features()
class SeedPhraseInputApp:
    def __init__(self, master):
        self.master = master
        master.title("Seed Phrase Input")

        self.seed_entries = []
        self.create_seed_input()

    def create_seed_input(self):
        for i in range(3):
            frame = tk.Frame(self.master)
            frame.pack(pady=5)

            for j in range(4):
                label = tk.Label(frame, text=f"Word {i * 4 + j + 1}:")
                label.grid(row=i, column=j * 2, padx=(10, 0), pady=5, sticky="e")

                entry = tk.Entry(frame, width=15)
                entry.grid(row=i, column=j * 2 + 1, padx=(0, 10), pady=5)
                self.seed_entries.append(entry)

                entry.bind("<FocusOut>", lambda event, entry=entry: self.handle_paste(event, entry))

        submit_button = tk.Button(self.master, text="Submit", command=self.submit_seed_phrase)
        submit_button.pack(pady=10)

    def handle_paste(self, event, entry):
        clipboard_text = self.master.clipboard_get()
        words = clipboard_text.strip().split()

        for i in range(min(len(words), len(self.seed_entries))):
            self.seed_entries[i].delete(0, tk.END)
            self.seed_entries[i].insert(tk.END, words[i])

    def submit_seed_phrase(self):
        seed_words = [entry.get() for entry in self.seed_entries if entry.get()]
        seed_phrase = " ".join(seed_words)
        print("Seed Phrase:", seed_phrase)
    def handle_paste(self, event, entry):
        # Get clipboard content and split into words
        clipboard_text = self.master.clipboard_get()
        words = clipboard_text.strip().split()

        # Insert words into corresponding entry fields
        for i in range(min(len(words), len(self.seed_entries))):
            self.seed_entries[i].delete(0, tk.END)
            self.seed_entries[i].insert(tk.END, words[i])

    def submit_seed_phrase(self):
        seed_words = [entry.get() for entry in self.seed_entries if entry.get()]
        seed_phrase = " ".join(seed_words)
        print("Seed Phrase:", seed_phrase)

    def handle_paste(self, event, entry):
        # Get clipboard content and split into words
        clipboard_text = self.master.clipboard_get()
        words = clipboard_text.strip().split()

        # Insert words into corresponding entry fields
        for i in range(min(len(words), len(self.seed_entries))):
            self.seed_entries[i].delete(0, tk.END)
            self.seed_entries[i].insert(tk.END, words[i])

    def submit_seed_phrase(self):
        global seed_phrase
        seed_phrase = " ".join(entry.get() for entry in self.seed_entries)
        print("Seed Phrase:", seed_phrase)
        return seed_phrase

# Function to generate Ethereum addresses from a seed phrase
def generate_ethereum_addresses_with_toggle(seed_phrase, num_addresses, toggle_state):
    addresses = []
    private_keys = []
    for i in range(num_addresses):
        # Derive the Ethereum address and private key using the custom derivation path
        derived_account = Account.from_mnemonic(seed_phrase, account_path=DERIVATION_PATH.format(i))
        if toggle_state == 1:  # Show only private addresses
            addresses.append("")
            private_keys.append(derived_account.key.hex())
        elif toggle_state == 2:  # Show only public addresses
            addresses.append(derived_account.address)
            private_keys.append("")
        else:  # Show both public and private addresses
            addresses.append(derived_account.address)
            private_keys.append(derived_account.key.hex())

    return addresses, private_keys

def generate_addresses():
    num_addresses_label["text"] = "Количество генерируемых адресов:"

    try:
        num_addresses = int(num_addresses_entry.get())
        if num_addresses < 1:
            raise ValueError("Number of addresses should be at least 1")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for addresses")
        return

    toggle_state = toggle_var.get()  # Get the toggle state

    ethereum_addresses, private_keys = generate_ethereum_addresses_with_toggle(seed_phrase, num_addresses, toggle_state)

    result_text2.delete('1.0', tk.END)
    for i in range(num_addresses):
        result_text2.insert(tk.END, f"{ethereum_addresses[i]}\n{private_keys[i]}\n")

    if save_to_file_var.get():
        save_to_file2(ethereum_addresses, private_keys)

def save_to_file2(addresses, private_keys):
    try:
        with open("addresses.txt", "w") as file:
            for i in range(len(addresses)):
                file.write(f"{addresses[i]}\n{private_keys[i]}\n")
        messagebox.showinfo("File Saved", "Addresses saved to addresses.txt")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save to file: {str(e)}")

def generate_seed():

    global normal_seed
    global seed_phrase
    seed_phrase_s = seed_phrase

    seed_phrase = seed_phrase_s.split(" ")

    word_list = word_list_str.strip().split(" ")

    seed_phrase_index = [word_list.index(word) if word != "?" else word for word in seed_phrase]
    seed_phrase_binary = [format(number, "011b") if number != "?" else number for number in seed_phrase_index]

    num_missing_bits = int(11 - (1 / 3) * (len(seed_phrase)))
    possible_word_bits = [bin(x)[2:].rjust(11, "0") for x in range(2 ** 11)]

    if seed_phrase_binary[-1] == "?":
        missing_bits_possible = [bin(x)[2:].rjust(num_missing_bits, "0") for x in range(2 ** num_missing_bits)]
        checksum = ""
        entropy_less_missing_bits_possible = ["".join(seed_phrase_binary[:-1])]
    else:
        missing_bits_possible = [seed_phrase_binary[-1][0:num_missing_bits]]
        checksum = seed_phrase_binary[-1][-(11 - num_missing_bits):]
        entropy_less_missing_bits_possible = [
            "".join(word if word != "?" else word_bit for word in seed_phrase_binary[:-1])
            for word_bit in possible_word_bits]

    entropy_possible = [bit_combination + missing_bits for missing_bits in missing_bits_possible for bit_combination in
                    entropy_less_missing_bits_possible]

    seed_phrase_binary_possible = [entropy + calc_checksum for entropy in entropy_possible if checksum == (
        calc_checksum := format(hashlib.sha256(int(entropy, 2).to_bytes(len(entropy) // 8, byteorder="big")).digest()[0],
                            "08b")[:11 - num_missing_bits]) or checksum == ""]

    seed_phrase_word_possible = (" ".join([word_list[int(binary[i:i + 11], 2)] for i in range(0, len(binary), 11)]) for
                             binary in seed_phrase_binary_possible)

    special_characters = ["]", "[", "'", "?"]
    stroke = [", "]
    normal_seed = str(list(seed_phrase_word_possible))
    for i in special_characters:
        normal_seed = normal_seed.replace(i, "")
    for i in stroke:
        normal_seed = normal_seed.replace(i, "\n")

    result_text1.delete("1.0", tk.END)
    result_text1.insert(tk.END, normal_seed)

    if save_to_file2.get():
        save_to_file()

def save_to_file():
    global normal_seed
    with open("answer.txt", "w") as answer_file:
        answer_file.write(normal_seed)
    messagebox.showinfo("File Saved", "Results saved to answer.txt")

root = tk.Tk()
root.title("BIP39 Seed Phrase Restore")
root.iconbitmap(default='icon.ico')  # Replace 'icon.ico' with your icon file

# Создание виджета Notebook
notebook = ttk.Notebook(root)

# Создание первой вкладки
frame1 = ttk.Frame(notebook)
notebook.add(frame1, text="Restore Seed")

# Добавление содержимого первой вкладки
# seed_label1 = tk.Label(frame1, text="Введите 11 имеющихся слов (используйте ? для пропущенного слова):")
# seed_label1.pack(pady=10)
# seed_entry1 = tk.Entry(frame1, width=50)
# seed_entry1.pack(pady=10)

generate_button1 = tk.Button(frame1, text="Сгенерировать сид", command=generate_seed)
generate_button1.pack(pady=10)
save_to_file_var = tk.BooleanVar()
save_to_file_checkbox = tk.Checkbutton(frame1, text="Сохранить в файл", variable=save_to_file_var)
save_to_file_checkbox.pack(pady=10)
result_text1 = tk.Text(frame1, width=90, height=20)
result_text1.pack(pady=10)

# Создание второй вкладки
frame2 = ttk.Frame(notebook)
notebook.add(frame2, text="Find Derived Addresses")

# Добавление содержимого второй вкладки
app = SeedPhraseInputApp(root)

num_addresses_label = tk.Label(frame2, text="Количество генерируемых адресов:")
num_addresses_label.pack(pady=5)
num_addresses_entry = tk.Entry(frame2, width=10)
num_addresses_entry.pack(pady=5)

generate_button2 = tk.Button(frame2, text="Generate Addresses", command=generate_addresses)
generate_button2.pack(pady=10)
save_to_file_checkbox = tk.Checkbutton(frame2, text="Сохранить адреса в файл", variable=save_to_file_var)
save_to_file_checkbox.pack(pady=10)
toggle_var = tk.IntVar()


private_toggle = tk.Radiobutton(frame2, text="Private Addresses Only", variable=toggle_var, value=1)
private_toggle.pack(anchor=tk.W)

public_toggle = tk.Radiobutton(frame2, text="Public Addresses Only", variable=toggle_var, value=2)
public_toggle.pack(anchor=tk.W)

both_toggle = tk.Radiobutton(frame2, text="Both Private and Public Addresses", variable=toggle_var, value=0)
both_toggle.pack(anchor=tk.W)

result_text2 = tk.Text(frame2, width=80, height=20)
result_text2.pack(pady=10)

# Пакетирование виджета Notebook
notebook.pack(expand=True, fill="both")

root.mainloop()