# Murajaah Shell (murosh) 📖

Murosh or Murajaah Shell is a Simple CLI for tracking and planning murojaah from terminal

**✨ Feature :**
- Provide Al-Qur'an in terminal version(coming soon)
- Create Al-Qur'an Memorization List
- Tracking memorization in surah or juz part form into 3 group: done, undone, and ongoing for comprehensive murajaah so nothing left
- Shuffling undone memorization to read for user when desired with `murosh read random`

## Installation ⚙️

```bash
git clone https://github.com/ilhamsadewarsa/murosh-cli
cd murosh-cli
pip install -e
```
## Available Command ✒️
- `murosh`
  - Coming soon interactive murosh
- `murosh add`
  - add multiple surah or memorization pieces in interactive mode
- `murosh add [group] [name]`
  - add 1 surah or memorization pieces to a specific group ( done , undone, or ongoing)
  - ex: `murosh add undone an-naas`
- `murosh remove [name]`
  - remove existing memorization pieces
  - ex: `murosh remove an-naas`
- `murosh show [group]`
  - show memorization pieces in spesific group
  - ex: `murosh show undone`
- `murosh check [name]`
  - Move ongoing or undone memorization piece to done group
  - ex: `murosh check an-naas`
- `murosh read [name]`
  - choose a spesific memorization piece to move to ongoing group
  - ex: `murosh read an-nass`
- `murosh read random`
  - choose undone memorization piece randomly to read and move it to ongoing group


**DISCLAIMER ⚠️**

This Project still in early development, documentation has not been created well and there is a possibility of error. So any feedbacks are very needed in development 

