import json
import glob
from acdh_tei_pyutils.tei import TeiReader


files = glob.glob("./mets/*/*_mets.xml")
data = {}
tr_url = "https://files.transkribus.eu/Get?id="
tr_param = "&fileType=view"

for x in files:
    doc = TeiReader(x)
    doc_id = doc.tree.xpath(".//title[1]/text()")[0].replace("grocerist-", "")
    print(doc_id)
    images = doc.tree.xpath(
        ".//mets:fileGrp[@ID='IMG']//mets:FLocat/@xlink:href",
        namespaces={
            "mets": "http://www.loc.gov/METS/",
            "xlink": "http://www.w3.org/1999/xlink",
        },
    )
    images = [i.replace(tr_url, "").replace(tr_param, "") for i in images]
    data[doc_id] = images

with open("data.json", "w", encoding="utf-8") as fp:
    json.dump(data, fp, ensure_ascii=False, indent=2)