from requests_html import *
from ADME_scraper import Properties
class WebScarper:
    # Constructor
    def __init__(self):
        self.HtmlSession = HTMLSession()
        self.page = 1
    def db_pages(self, query):
        print('Counting')
        Db_search = self.HtmlSession.get(f'https://go.drugbank.com/unearth/q?c=_score&d=down&page={self.page}&query={query}&searcher=drugs')
        # Db_search = self.HtmlSession.get(f'https://go.drugbank.com/unearth/q?approved=1&c=_score&ca=0&d=down&eu=0&page={self.page}&query={query}&searcher=drugs&us=0')
        arr = Db_search.html.links   # Array of links
        new = []
        for n in arr:
            if n.find('page=')!=-1:
                n=n[n.find('page='):n.find('query=')]
                print(n)
                string = ''
                for s in list(n):
                    if s.isdigit():
                        string+=s
                        new.append(int(string))
        try:
            return int(max(new))
        except:
            return 1
    # ID Extraction
    def dbId_Extractor(self,query):
        print('Extracting')
        Db_result = []
        for pg in range(1,self.db_pages(query)+1):
            Db_search = self.HtmlSession.get(f'https://go.drugbank.com/unearth/q?c=_score&d=down&page={pg}&query={query}&searcher=drugs')
            arr = Db_search.html.absolute_links 
            for lnk in arr:
                if lnk.find('DB')!= -1:
                    LKlist = lnk.split('/')
                    for i in LKlist:
                        if i.startswith('DB'):
                            Db_result.append(i)
        return Db_result        
    # Scrap database
    def Scraper(self,query):
        adme_obj = Properties()
        print('Scraping')
        csv_data = []
        with open('Properties.txt','r') as Pro_file:
            Properties_txt = Pro_file.read().split('\n')
            Pro_file.close()
        for drug in self.dbId_Extractor(query):
            DB_URL = f'https://go.drugbank.com/drugs/{drug}'
            db_html = self.HtmlSession.get(DB_URL)
            all_text = db_html.html.text.split('\n')

            Mol_url = f'https://go.drugbank.com/drugs/{drug}.mol'
            mol_html = self.HtmlSession.get(Mol_url)
            mol = mol_html.html.text
            try:
                preADMET_data = adme_obj.PreADME(mol)
                smiles = all_text[all_text.index('SMILES')+1]
                Properties_data = adme_obj.SwissADME(smiles)
                Tox = adme_obj.Toxicity(mol)
                csv_data.append(smiles)
                csv_data.append(f"{','.join(Properties_data + preADMET_data + Tox)}\n")
            except:
                pass
        with open(f'Output\\{query}.csv','w',encoding='utf-8') as file:
            file.write(f"SMILES, {str(','.join(Properties_txt))}\n{','.join(csv_data)}")
            file.close()