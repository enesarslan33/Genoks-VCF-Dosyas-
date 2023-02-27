import json
import vcf


vcf_reader = vcf.Reader(open('ornek.vcf', 'r'))


vcf_data = []

for record in vcf_reader:
    alt_strs = [str(alt) for alt in record.ALT]
    vcf_data.append({
        'chromosome': record.CHROM,
        'position': record.POS,
        'id': record.ID,
        'reference': record.REF,
        'alternate': alt_strs,
        'quality': record.QUAL,
        'filter': record.FILTER,
        'info': record.INFO,
        'format':record.FORMAT,
        'NA00001':record.samples[0].data,
        'NA00002': record.samples[1].data,
        'NA00003':record.samples[2].data


    })


json_data = json.dumps(vcf_data)


print(json_data)

with open('example.json', 'w') as f:
    json.dump(vcf_data, f, indent=4)





















