from django import template

register = template.Library()

@register.filter('in_proteinsegment')
def in_proteinsegment(residuegenericnumbers, proteinsegment):
    return residuegenericnumbers.filter(protein_segment=proteinsegment)

@register.filter('in_domain')
def in_domain(residues, domain):
    return residues.filter(domain=domain)