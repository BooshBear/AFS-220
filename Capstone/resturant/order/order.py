from django.conf import settings

from meal.models import Meal

class Order(object):
    def __init__(self, request):
        self.session = request.session
        order = self.session.get(settings.ORDER_SESSION_ID)
        
        if not order:
            order = self.session[settings.ORDER_SESSION_ID] = {}
            
        self.order = order
        
    def __iter__(self):
        for p in self.order.keys():
            self.order[str(p)]['meal'] = Meal.objects.get(pk=p)
            
        for item in self.order.values():
            item['total_price'] = int(item['meal'].price * item['quantity'])
            
            yield item
            
    def __len__(self):
        return sum(item['quantity'] for item in self.order.values())
    
    def save(self):
        self.session[settings.ORDER_SESSION_ID] = self.order
        self.session.modified = True
        
    def add(self, meal_id, quantity=1, update_quantity=False):
        meal_id = str(meal_id)
        
        if meal_id not in self.order:
            self.order[meal_id] = {'quantity': 1, 'id': meal_id}
            
        if update_quantity:
            self.order[meal_id]['quantity'] += int(quantity)
            
            if self.order[meal_id]['quantity'] == 0:
                self.remove(meal_id)
        
        self.save()
        
    def remove(self, meal_id):
        if meal_id in self.order:
            del self.order[meal_id]
            self.save()
            
    def get_total_cost(self):
        for p in self.order.keys():
            self.order[str(p)]['meal'] = Meal.objects.get(pk=p)
            
        return sum(item['meal'].price * item['quantity'] for item in self.order.values())
    
    def get_item(self, meal_id):
        return self.order[str(meal_id)]