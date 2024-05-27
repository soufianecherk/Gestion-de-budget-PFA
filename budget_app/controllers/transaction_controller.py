from models.transaction import Transaction

class TransactionController:
    def add_transaction(self, date, category, subcategory, amount, note):
        transaction = Transaction(date, category, subcategory, amount, note)
        transaction.save()
    
    def get_all_transactions(self):
        return Transaction.get_all()
