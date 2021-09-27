def calculate_total_weight(doc, method):
	from frappe.utils import flt
	total_weight = 0.0
	for d in doc.items:
		d.weight = flt(d.weight_per_unit1) * flt(d.qty)
		total_weight += d.weight

	doc.total_weight = total_weight