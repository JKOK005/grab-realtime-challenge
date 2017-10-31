class SurgePriceCalculatorMixin(object):
	min_price 	= 0.50
	max_price 	= 40.0
	sp_constant = 1.5

	def __init__(self, *args, **kwargs):
		super(SurgePriceCalculatorMixin, self).__init__(*args, **kwargs)

	def getSurgePrice(self, sp_model_obj):
		dd 	= sp_model_obj.demand
		ss 	= sp_model_obj.supply
		if(ss <= 0):
			ss = 1
		sp 	= float(dd)/ss * self.sp_constant
		return max(self.min_price, min(self.max_price, sp))
