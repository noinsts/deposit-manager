
# Deposit Manager

**Deposit Manager** — це застосунок для керування депозитами. Він дозволяє додавати, редагувати, видаляти депозити, а також проводити обчислення, що стосуються депозитних процентних ставок на основі терміну. Усе це реалізовано через графічний інтерфейс на Python з використанням бібліотеки Tkinter. Данні про депозити зберігаються у базі даних SQLite.

## Особливості

- **Додавання депозитів**: Користувач може додавати депозити, вказуючи відсоткові ставки для різних термінів (3-6 місяців, 6-9 місяців, 9-12 місяців, 18 місяців, 24 місяці).
- **Редагування депозитів**: Можливість змінювати інформацію про існуючі депозити.
- **Видалення депозитів**: Легке видалення депозитів із бази даних.
- **Розрахунок депозиту**: Програма обчислює нарахування по депозиту на основі введених відсоткових ставок і терміну.
- **Ранні виводи**: Користувач може вказати, чи є депозит з можливістю дострокового виведення, і якщо так, вказати відповідну відсоткову ставку.

## Встановлення

1. Клонуйте репозиторій:

   ```bash
   git clone https://github.com/noinsts/deposit-manager.git
   ```

2. Перейдіть до директорії проекту:

   ```bash
   cd deposit-manager
   ```

## Використання

1. Запустіть застосунок:

   ```bash
   python main.py
   ```

2. Ви побачите головне вікно програми з кнопками для додавання, редагування та видалення депозитів.

3. Для кожного депозиту ви можете вказати:
   - Назву депозиту.
   - Назву банку.
   - Відсоткову ставку для різних термінів (3-6 місяців, 6-9 місяців, 9-12 місяців, 18 місяців, 24 місяці).
   - Чи є можливість дострокового виведення.

4. Додавайте депозити до бд та аналізуйте їх! 🙌

## Логіка роботи з базою даних

Всі дані про депозити зберігаються в базі даних SQLite. Це дає можливість зберігати велику кількість депозитів, а також здійснювати пошук, редагування і видалення даних.

## Плани на майбутнє

- Додавання підтримки кількох валют.
- Додавання можливості створення звітів про депозити
