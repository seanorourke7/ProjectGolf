from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.template.defaultfilters import slugify



choices = [
    ('Abbeyleix Golf Club', 'Abbeyleix Golf Club'),
    ('Ardglass Golf Club', 'Ardglass Golf Club'),
    ('Ashford Castle Golf Club', 'Ashford Castle Golf Club'),
    ('Achill Island Golf Club', 'Achill Island Golf Club'),
    ('Ardminnan Golf Club', 'Ardminnan Golf Club'),
    ('Athenry Golf Club', 'Athenry Golf Club'),
    ('Adare Golf Club', 'Adare Golf Club'),
    ('Arklow Golf Club', 'Arklow Golf Club'),
    ('Athlone Golf Club', 'Athlone Golf Club'),
    ('Allen Park Golf Centre', 'Allen Park Golf Centre'),
    ('Ashbourne Golf Club', 'Ashbourne Golf Club'),
    ('Athy Golf Club', 'Athy Golf Club'),
    ('Ardeer Golf Club', 'Ardeer Golf Club'),
    ('Ashfield Golf Course', 'Ashfield Golf Course'),
    ('Aughnacloy Golf Club', 'Aughnacloy Golf Club'),
    ('Balbriggan Golf Club', 'Balbriggan Golf Club'),
    ('Ballyliffin - The Old Links', 'Ballyliffin - The Old Links'),
    ('Birr Golf Club', 'Birr Golf Club'),
    ('Balcarrick Golf Club', 'Balcarrick Golf Club'),
    ('Ballymena Golf Club', 'Ballymena Golf Club'),
    ('Black Bush - Black Bush Course', 'Black Bush - Black Bush Course'),
    ('Ballaghaderreen Golf Club', 'Ballaghaderreen Golf Club'),
    ('Ballymoney Golf Club', 'Ballymoney Golf Club'),
    ('Black Bush - Lagore Course', 'Black Bush - Lagore Course'),
    ('Ballina Golf Club', 'Ballina Golf Club'),
    ('Ballyneety Golf Club', 'Ballyneety Golf Club'),
    ('Black Bush - Thomaston Course', 'Black Bush - Thomaston Course'),
    ('Ballinamore Golf Club', 'Ballinamore Golf Club'),
    ('Ballyreagh Golf Club', 'Ballyreagh Golf Club'),
    ('Blacklion Golf Club', 'Blacklion Golf Club'),
    ('Ballinascorney Golf Club', 'Ballinascorney Golf Club'),
    ('Balmoral Golf Club', 'Balmoral Golf Club'),
    ('Blackwood - Hamilton Course', 'Blackwood - Hamilton Course'),
    ('Ballinasloe Golf Club', 'Ballinasloe Golf Club'),
    ('Baltinglass Golf Club', 'Baltinglass Golf Club'),
    ('Blackwood - Temple Course', 'Blackwood - Temple Course'),
    ('Ballinlough Castle Golf Club', 'Ballinlough Castle Golf Club'),
    ('Banbridge Golf Club', 'Banbridge Golf Club'),
    ('Blainroe Golf Club', 'Blainroe Golf Club'),
    ('Ballinrobe Golf Club', 'Ballinrobe Golf Club'),
    ('Bandon Golf Club', 'Bandon Golf Club'),
    ('Blarney Golf Club', 'Blarney Golf Club'),
    ('Ballybofey & Stranorlar Golf Club', 'Ballybofey & Stranorlar Golf Club'),
    ('Bangor Golf Club', 'Bangor Golf Club'),
    ('Borris Golf Club', 'Borris Golf Club'),
    ('Ballybunion - Cashen Course', 'Ballybunion - Cashen Course'),
    ('Bantry Bay Golf Club', 'Bantry Bay Golf Club'),
    ('Boyle Golf Club', 'Boyle Golf Club'),
    ('Ballybunion - Old Course', 'Ballybunion - Old Course'),
    ('Bearna Golf & Country Club', 'Bearna Golf & Country Club'),
    ('Bray Golf Club', 'Bray Golf Club'),
    ('Ballycastle Golf Club', 'Ballycastle Golf Club'),
    ('Beaufort Golf Resort', 'Beaufort Golf Resort'),
    ('Bright Castle Golf Club', 'Bright Castle Golf Club'),
    ('Ballyclare Golf Club', 'Ballyclare Golf Club'),
    ('Beaverstown Golf Club', 'Beaverstown Golf Club'),
    ('Brown Trout Golf Club', 'Brown Trout Golf Club'),
    ('Ballyearl Golf Club', 'Ballyearl Golf Club'),
    ('Beech Park Golf Club', 'Beech Park Golf Club'),
    ('Buncrana Golf Club', 'Buncrana Golf Club'),
    ('Ballyhaunis Golf Club', 'Ballyhaunis Golf Club'),
    ('Belturbet Golf Club', 'Belturbet Golf Club'),
    ('Bundoran Golf Club', 'Bundoran Golf Club'),
    ('Ballyheigue Castle Golf Club', 'Ballyheigue Castle Golf Club'),
    ('Belvoir Park Golf Club', 'Belvoir Park Golf Club'),
    ('Bushfoot Golf Club', 'Bushfoot Golf Club'),
    ('Ballykisteen Golf & Country Club', 'Ballykisteen Golf & Country Club'),
    ('Benone Golf Club', 'Benone Golf Club'),
    ('Ballyliffin - Glashedy Course', 'Ballyliffin - Glashedy Course'),
    ('Berehaven Golf Club', 'Berehaven Golf Club'),
    ('Cabra Castle Hotel', 'Cabra Castle Hotel'),
    ('Castletroy Golf Club', 'Castletroy Golf Club'),
    ('Connemara Isles Golf Club', 'Connemara Isles Golf Club'),
    ('Cahir Park Golf Club', 'Cahir Park Golf Club'),
    ('Castlewarden Golf Club', 'Castlewarden Golf Club'),
    ('Coollattin Golf Club', 'Coollattin Golf Club'),
    ('Cairndhu Golf Club', 'Cairndhu Golf Club'),
    ('Celbridge Elm Hall Golf Club', 'Celbridge Elm Hall Golf Club'),
    ('Coosheen Golf Club', 'Coosheen Golf Club'),
    ('Callan Golf Club', 'Callan Golf Club'),
    ('Charleville Golf Club', 'Charleville Golf Club'),
    ('Corballis Golf Club', 'Corballis Golf Club'),
    ('Carlow Golf Club', 'Carlow Golf Club'),
    ('Cill Dara Golf Club', 'Cill Dara Golf Club'),
    ('Cork Golf Club', 'Cork Golf Club'),
    ('Carnalea Golf Club', 'Carnalea Golf Club'),
    ('City of Belfast Golf Club', 'City of Belfast Golf Club'),
    ('Corrstown Golf Club', 'Corrstown Golf Club'),
    ('Carne Golf Links', 'Carne Golf Links'),
    ('City of Derry Golf Club', 'City of Derry Golf Club'),
    ('County Armagh Golf Club', 'County Armagh Golf Club'),
    ('Carrick-on-Shannon Golf Club', 'Carrick-on-Shannon Golf Club'),
    ('City of Derry Golf Course', 'City of Derry Golf Course'),
    ('County Cavan Golf Club', 'County Cavan Golf Club'),
    ('Carrick-on-Suir Golf Club', 'Carrick-on-Suir Golf Club'),
    ('Clandeboye - Ava Course', 'Clandeboye - Ava Course'),
    ('County Longford Golf Club', 'County Longford Golf Club'),
    ('Carrickfergus Golf Club', 'Carrickfergus Golf Club'),
    ('Clandeboye - Dufferin Course', 'Clandeboye - Dufferin Course'),
    ('County Meath(Trim) Golf Club', 'County Meath(Trim) Golf Club'),
    ('Carrickmines Golf Club', 'Carrickmines Golf Club'),
    ('Claremorris Golf Club', 'Claremorris Golf Club'),
    ('County Sligo Golf Club', 'County Sligo Golf Club'),
    ('Carton House Golf Club', 'Carton House Golf Club'),
    ('Cliftonville Golf Club', 'Cliftonville Golf Club'),
    ('County Tipperary Golf & Country Club',
     'County Tipperary Golf & Country Club'),
    ('Castle Golf Club', 'Castle Golf Club'),
    ('Clonakilty Golf Club', 'Clonakilty Golf Club'),
    ('Courtown Golf Club', 'Courtown Golf Club'),
    ('Castle Hume Golf Club', 'Castle Hume Golf Club'),
    ('Clones Golf Club', 'Clones Golf Club'),
    ('Craddockstown Golf Club', 'Craddockstown Golf Club'),
    ('Castlebar Golf Club', 'Castlebar Golf Club'),
    ('Clonmel Golf Club', 'Clonmel Golf Club'),
    ('Crossgar Golf Club', 'Crossgar Golf Club'),
    ('Castlecomer Golf Club', 'Castlecomer Golf Club'),
    ('Clontarf Golf Club', 'Clontarf Golf Club'),
    ('Cruit Island Golf Club', 'Cruit Island Golf Club'),
    ('Castlegregory Golf Club', 'Castlegregory Golf Club'),
    ('Cloverhill Golf Club', 'Cloverhill Golf Club'),
    ('Curragh Golf Club', 'Curragh Golf Club'),
    ('Castleisland Golf Club', 'Castleisland Golf Club'),
    ('Cobh Golf Club', 'Cobh Golf Club'),
    ('Cushendall Golf Club', 'Cushendall Golf Club'),
    ('Castlerea Golf Club', 'Castlerea Golf Club'),
    ('Concra Wood Golf & Country Club', 'Concra Wood Golf & Country Club'),
    ('Castlerock Golf Club', 'Castlerock Golf Club'),
    ('Connemara Golf Club', 'Connemara Golf Club'),
    ('Deer Park - Main Course', 'Deer Park - Main Course'),
    ('Doneraile Golf Club', 'Doneraile Golf Club'),
    ('Dundalk Golf Club', 'Dundalk Golf Club'),
    ('Deer Park - St Fintans', 'Deer Park - St Fintans'),
    ('Dooks Golf Club', 'Dooks Golf Club'),
    ('Dunfanaghy Golf Club', 'Dunfanaghy Golf Club'),
    ('Delgany Golf Club', 'Delgany Golf Club'),
    ('Douglas Golf Club', 'Douglas Golf Club'),
    ('Dungannon Golf Club', 'Dungannon Golf Club'),
    ('Dingle Golf Club', 'Dingle Golf Club'),
    ('Downpatrick Golf Club', 'Downpatrick Golf Club'),
    ('Dungarvan Golf Club', 'Dungarvan Golf Club'),
    ('Djouce Mountain Golf Club', 'Djouce Mountain Golf Club'),
    ('Dromoland Castle Golf Club', 'Dromoland Castle Golf Club'),
    ('Dunloe Golf Club', 'Dunloe Golf Club'),
    ('Donabate Golf Club', 'Donabate Golf Club'),
    ('Druids Glen Golf Club', 'Druids Glen Golf Club'),
    ('Dunmore Demesne Golf Club', 'Dunmore Demesne Golf Club'),
    ('Donaghadee Golf Club', 'Donaghadee Golf Club'),
    ('Dublin Mountain Golf Club', 'Dublin Mountain Golf Club'),
    ('Dunmore East Golf Club', 'Dunmore East Golf Club'),
    ('Donegal Golf Club', 'Donegal Golf Club'),
    ('Dun Lagohaire Golf Club', 'Dun Lagohaire Golf Club'),
    ('Dunmurry Golf Club', 'Dunmurry Golf Club'),
    ('East Clare Golf Club', 'East Clare Golf Club'),
    ('Elm Park Golf Club', 'Elm Park Golf Club'),
    ('Enniscrone Golf Club', 'Enniscrone Golf Club'),
    ('East Cork Golf Club', 'East Cork Golf Club'),
    ('Elmgreen Golf Club', 'Elmgreen Golf Club'),
    ('Enniskillen Golf Club', 'Enniskillen Golf Club'),
    ('Edenderry Golf Club', 'Edenderry Golf Club'),
    ('Ennis Golf Club', 'Ennis Golf Club'),
    ('Esker Hills Golf Club', 'Esker Hills Golf Club'),
    ('Edenmore Golf Club', 'Edenmore Golf Club'),
    ('Enniscorthy Golf Club', 'Enniscorthy Golf Club'),
    ('Edmondstown Golf Club', 'Edmondstown Golf Club'),
    ('Enniscrone Golf Club', 'Enniscrone Golf Club'),
    ('Faithlegg Golf Club', 'Faithlegg Golf Club'),
    ('Forest Little Golf Club', 'Forest Little Golf Club'),
    ('Foyle International', 'Foyle International'),
    ('Fermoy Golf Club', 'Fermoy Golf Club'),
    ('Fortwilliam Golf Club', 'Fortwilliam Golf Club'),
    ('Fernhill Golf Club', 'Fernhill Golf Club'),
    ('Fota Island Golf Club', 'Fota Island Golf Club'),
    ('Frankfield Golf Club', 'Frankfield Golf Club'),
    ('Fintona Golf Club', 'Fintona Golf Club'),
    ('Foxrock Golf Club', 'Foxrock Golf Club'),
    ('Galgorm Castle Golf Club', 'Galgorm Castle Golf Club'),
    ('Glenlo Abbey Golf Club', 'Glenlo Abbey Golf Club'),
    ('Greenacres Golf Centre', 'Greenacres Golf Centre'),
    ('Galway Bay Golf & Country Club', 'Galway Bay Golf & Country Club'),
    ('Gold Coast Golf Club', 'Gold Coast Golf Club'),
    ('Greencastle Golf Club', 'Greencastle Golf Club'),
    ('Galway Golf Club', 'Galway Golf Club'),
    ('Gort Golf Club', 'Gort Golf Club'),
    ('Greenisland Golf Club', 'Greenisland Golf Club'),
    ('Gilnahirk Golf Club', 'Gilnahirk Golf Club'),
    ('Gowran Park Golf Club', 'Gowran Park Golf Club'),
    ('Greenore Golf Club', 'Greenore Golf Club'),
    ('Glasson Golf Club', 'Glasson Golf Club'),
    ('Gracehill Golf Club', 'Gracehill Golf Club'),
    ('Greystones Golf Club', 'Greystones Golf Club'),
    ('Glencullen Golf Club', 'Glencullen Golf Club'),
    ('Grange Castle Golf Club', 'Grange Castle Golf Club'),
    ('Gweedore Golf Club', 'Gweedore Golf Club'),
    ('Glengarriff Golf Club', 'Glengarriff Golf Club'),
    ('Grange Golf Club', 'Grange Golf Club'),
    ('Headfort Championship Course', 'Headfort Championship Course'),
    ('Hermitage Golf Club', 'Hermitage Golf Club'),
    ('Hollywood Lakes Golf Club', 'Hollywood Lakes Golf Club'),
    ('Headfort Golf Club - Old Course', 'Headfort Golf Club - Old Course'),
    ('Highfield Golf Club', 'Highfield Golf Club'),
    ('Holywood Golf Club', 'Holywood Golf Club'),
    ('Helens Bay Golf Club', 'Helens Bay Golf Club'),
    ('Hilton Belfast Templepatrick', 'Hilton Belfast Templepatrick'),
    ('Howth Golf Club', 'Howth Golf Club'),
    ('Kanturk Golf Club', 'Kanturk Golf Club'),
    ('Killarney - Mahonys Point Course', 'Killarney - Mahonys Point Course'),
    ('Kilmashogue Golf Club', 'Kilmashogue Golf Club'),
    ('Kenmare Golf Club', 'Kenmare Golf Club'),
    ('Killarney Golf & Fishing Club Academy Course',
     'Killarney Golf & Fishing Club Academy Course'),
    ('Kilrea Golf Club', 'Kilrea Golf Club'),
    ('Kilcock Golf Club', 'Kilcock Golf Club'),
    ('Killeen Golf Club', 'Killeen Golf Club'),
    ('Kilrush Golf Club', 'Kilrush Golf Club'),
    ('Kilkea Castle Golf Club', 'Kilkea Castle Golf Club'),
    ('Killerig Castle Golf Club', 'Killerig Castle Golf Club'),
    ('Kilternan Golf Club', 'Kilternan Golf Club'),
    ('Kilkee Golf Club', 'Kilkee Golf Club'),
    ('Killin Park Golf Club', 'Killin Park Golf Club'),
    ('Kinsale Golf Club', 'Kinsale Golf Club'),
    ('Kilkeel Golf Club', 'Kilkeel Golf Club'),
    ('Killiney Golf Club', 'Killiney Golf Club'),
    ('Kirkistown Castle Golf Club', 'Kirkistown Castle Golf Club'),
    ('Kilkenny Golf Club', 'Kilkenny Golf Club'),
    ('Killorglin Golf Club', 'Killorglin Golf Club'),
    ('Knightsbrook Golf Club', 'Knightsbrook Golf Club'),
    ('Killarney - Killeen Course', 'Killarney - Killeen Course'),
    ('Killymoon Golf Club', 'Killymoon Golf Club'),
    ('Knock Golf Club', 'Knock Golf Club'),
    ('Lahinch - Castle Course', 'Lahinch - Castle Course'),
    ('Leopardstown Golf Club', 'Leopardstown Golf Club'),
    ('Loughgall Country Park & golf course',
     'Loughgall Country Park & golf course'),
    ('Lahinch - Old Course', 'Lahinch - Old Course'),
    ('Letterkenny Golf Club', 'Letterkenny Golf Club'),
    ('Loughrea Golf Club', 'Loughrea Golf Club'),
    ('Lambeg Golf Club', 'Lambeg Golf Club'),
    ('Limerick Golf Club', 'Limerick Golf Club'),
    ('Lucan Golf Club', 'Lucan Golf Club'),
    ('Larne Golf Club', 'Larne Golf Club'),
    ('Lisburn Golf Club', 'Lisburn Golf Club'),
    ('Lurgan Golf Club', 'Lurgan Golf Club'),
    ('Laytown & Bettystown Golf Club', 'Laytown & Bettystown Golf Club'),
    ('Lismore Golf Club', 'Lismore Golf Club'),
    ('Luttrellstown Castle Golf Club', 'Luttrellstown Castle Golf Club'),
    ('Lee Valley Golf & Country Club', 'Lee Valley Golf & Country Club'),
    ('Listowel Golf Club', 'Listowel Golf Club'),
    ('Macroom Golf Club', 'Macroom Golf Club'),
    ('Massereene Golf Club', 'Massereene Golf Club'),
    ('Mountbellew Golf Club', 'Mountbellew Golf Club'),
    ('Mahee Island Golf Club', 'Mahee Island Golf Club'),
    ('Milltown Golf Club', 'Milltown Golf Club'),
    ('Mountrath Golf Club', 'Mountrath Golf Club'),
    ('Mahon Golf Club', 'Mahon Golf Club'),
    ('Mitchelstown Golf Club', 'Mitchelstown Golf Club'),
    ('Mourne Golf Club', 'Mourne Golf Club'),
    ('Malahide Golf Club', 'Malahide Golf Club'),
    ('Moate Golf Club', 'Moate Golf Club'),
    ('Moyola Park Golf Club', 'Moyola Park Golf Club'),
    ('Mallow Golf Club', 'Mallow Golf Club'),
    ('Monkstown Golf Club', 'Monkstown Golf Club'),
    ('Moyvalley Golf Club', 'Moyvalley Golf Club'),
    ('Malone Edenderry Course', 'Malone Edenderry Course'),
    ('Mount Juliet Golf & Country Club', 'Mount Juliet Golf & Country Club'),
    ('Mullingar Golf Club', 'Mullingar Golf Club'),
    ('Malone Golf Club', 'Malone Golf Club'),
    ('Mount Temple Golf Club', 'Mount Temple Golf Club'),
    ('Mulranny Golf Club', 'Mulranny Golf Club'),
    ('Mannan Castle Golf Club', 'Mannan Castle Golf Club'),
    ('Mount Wolseley Golf Hotel & Country Club',
     'Mount Wolseley Golf Hotel & Country Club'),
    ('Muskerry Golf Club', 'Muskerry Golf Club'),
    ('Manor Golf Club', 'Manor Golf Club'),
    ('Mountain View Golf Club', 'Mountain View Golf Club'),
    ('Naas Golf Club', 'Naas Golf Club'),
    ('Newbridge Golf Club', 'Newbridge Golf Club'),
    ('North West Golf Club', 'North West Golf Club'),
    ('Narin & Portnoo Golf Club', 'Narin & Portnoo Golf Club'),
    ('Newcastle West Golf Club', 'Newcastle West Golf Club'),
    ('Nuremore Hotel Golf & Country Club', 'Nuremore Hotel Golf & Country Club'),
    ('Nenagh Golf Club', 'Nenagh Golf Club'),
    ('Newlands Golf Club', 'Newlands Golf Club'),
    ('New Ross Golf Club', 'New Ross Golf Club'),
    ('Newtownstewart Golf Club', 'Newtownstewart Golf Club'),
    ('Old Conna Golf Club', 'Old Conna Golf Club'),
    ('Omagh Golf Club', 'Omagh Golf Club'),
    ('Otway Golf Club', 'Otway Golf Club'),
    ('Old Head of Kinsale Golf Club', 'Old Head of Kinsale Golf Club'),
    ('Ormeau Golf Club', 'Ormeau Golf Club'),
    ('Oughterard Golf Club', 'Oughterard Golf Club'),
    ('Palmerstown House Golf Club', 'Palmerstown House Golf Club'),
    ('Portmarnock Championship Course', 'Portmarnock Championship Course'),
    ('Portstewart - Riverside Golf Club', 'Portstewart - Riverside Golf Club'),
    ('Parknasilla Golf Club', 'Parknasilla Golf Club'),
    ('Portmarnock Hotel & Golf Links', 'Portmarnock Hotel & Golf Links'),
    ('Portstewart - Strand Golf Club', 'Portstewart - Strand Golf Club'),
    ('Portadown Golf Club', 'Portadown Golf Club'),
    ('Portsalon Golf Club', 'Portsalon Golf Club'),
    ('Portumna Golf Club', 'Portumna Golf Club'),
    ('Portarlington Golf Club', 'Portarlington Golf Club'),
    ('Portstewart - Old Course', 'Portstewart - Old Course'),
    ('Powerscourt Golf Club', 'Powerscourt Golf Club'),
    ('R & R Golf Course', 'R & R Golf Course'),
    ('Rockmount Golf Club', 'Rockmount Golf Club'),
    ('Roundwood Golf Club', 'Roundwood Golf Club'),
    ('Raffeen Creek Golf Club', 'Raffeen Creek Golf Club'),
    ('Roe Park Resort', 'Roe Park Resort'),
    ('Royal Belfast Golf Club', 'Royal Belfast Golf Club'),
    ('Rathbane Golf Club', 'Rathbane Golf Club'),
    ('Roganstown Hotel & CC', 'Roganstown Hotel & CC'),
    ('Royal County Down - Annesley Links', 'Royal County Down - Annesley Links'),
    ('Rathdowney Golf Club', 'Rathdowney Golf Club'),
    ('Rosapenna Golf Club', 'Rosapenna Golf Club'),
    ('Royal County Down - Championship Course',
     'Royal County Down - Championship Course'),
    ('Rathfarnham Golf Club', 'Rathfarnham Golf Club'),
    ('Roscommon Golf Club', 'Roscommon Golf Club'),
    ('Royal Dublin Golf Club', 'Royal Dublin Golf Club'),
    ('Rathmore Golf Club', 'Rathmore Golf Club'),
    ('Roscrea Golf Club', 'Roscrea Golf Club'),
    ('Royal Portrush - Dunluce Links', 'Royal Portrush - Dunluce Links'),
    ('Rathsallagh Golf Club', 'Rathsallagh Golf Club'),
    ('Ross Golf Club', 'Ross Golf Club'),
    ('Royal Portrush - Valley Links', 'Royal Portrush - Valley Links'),
    ('Redcastle Hotel & Golf Club', 'Redcastle Hotel & Golf Club'),
    ('Rosslare Golf Club', 'Rosslare Golf Club'),
    ('Royal Tara Golf Club', 'Royal Tara Golf Club'),
    ('Ring of Kerry Golf Club', 'Ring of Kerry Golf Club'),
    ('Rossmore Golf Club', 'Rossmore Golf Club'),
    ('Rush Golf Club', 'Rush Golf Club'),
    ('Scrabo Golf Club', 'Scrabo Golf Club'),
    ('Slievenamon Golf Club', 'Slievenamon Golf Club'),
    ('Stackstown Golf Club', 'Stackstown Golf Club'),
    ('Seapoint Golf Links', 'Seapoint Golf Links'),
    ('South County Golf Club', 'South County Golf Club'),
    ('Stepaside Golf Club', 'Stepaside Golf Club'),
    ('Shandon Park Golf Club', 'Shandon Park Golf Club'),
    ('South Meath Golf Club', 'South Meath Golf Club'),
    ('Strabane Golf Club', 'Strabane Golf Club'),
    ('Shannon Golf Club', 'Shannon Golf Club'),
    ('Spa Golf Club', 'Spa Golf Club'),
    ('Strandhill Golf Club', 'Strandhill Golf Club'),
    ('Silverwood Golf Centre', 'Silverwood Golf Centre'),
    ('Spanish Point Golf Club', 'Spanish Point Golf Club'),
    ('Strokestown Golf Club', 'Strokestown Golf Club'),
    ('Skellig Bay Golf Club', 'Skellig Bay Golf Club'),
    ('St Annes Golf Club', 'St Annes Golf Club'),
    ('Summerhill Golf Club', 'Summerhill Golf Club'),
    ('Skerries Golf Club', 'Skerries Golf Club'),
    ('St Helens Bay Golf Club', 'St Helens Bay Golf Club'),
    ('Sutton Golf Club', 'Sutton Golf Club'),
    ('Skibbereen and West Carbery Golf Club',
     'Skibbereen and West Carbery Golf Club'),
    ('St Margarets Golf Club', 'St Margarets Golf Club'),
    ('Swinford Golf Club', 'Swinford Golf Club'),
    ('Slieve Russell Golf Club', 'Slieve Russell Golf Club'),
    ('St Patricks Links Golf Club', 'St Patricks Links Golf Club'),
    ('Swords Open Golf Club', 'Swords Open Golf Club'),
    ('Tandragee Golf Club', 'Tandragee Golf Club'),
    ('The Island Golf Club', 'The Island Golf Club'),
    ('Trump International Golf Links & Hotel Doonbeg',
     'Trump International Golf Links & Hotel Doonbeg'),
    ('Tara Glen Golf Club', 'Tara Glen Golf Club'),
    ('The K Club', 'The K Club'),
    ('Tuam Golf Club', 'Tuam Golf Club'),
    ('Temple Golf Club', 'Temple Golf Club'),
    ('Thurles Golf Club', 'Thurles Golf Club'),
    ('Tubbercurry Golf Club', 'Tubbercurry Golf Club'),
    ('Templemore Golf Club', 'Templemore Golf Club'),
    ('Tipperary Golf Club', 'Tipperary Golf Club'),
    ('Tulfarris Golf Club', 'Tulfarris Golf Club'),
    ('The European Club', 'The European Club'),
    ('Traad Ponds Golf Club', 'Traad Ponds Golf Club'),
    ('Tullamore Golf Club', 'Tullamore Golf Club'),
    ('The Heath Golf Club', 'The Heath Golf Club'),
    ('Tralee Golf Club', 'Tralee Golf Club'),
    ('The Heritage Golf Resort', 'The Heritage Golf Resort'),
    ('Tramore Golf Club', 'Tramore Golf Club'),
    ('Virginia Golf Club', 'Virginia Golf Club'),
    ('Warrenpoint Golf Club', 'Warrenpoint Golf Club'),
    ('Westmanstown Golf Club', 'Westmanstown Golf Club'),
    ('Williamstown Golf Club', 'Williamstown Golf Club'),
    ('Waterford Castle Golf Club', 'Waterford Castle Golf Club'),
    ('Westport Golf Club', 'Westport Golf Club'),
    ('Woodbrook Golf Club', 'Woodbrook Golf Club'),
    ('Waterford Golf Club', 'Waterford Golf Club'),
    ('Wexford Golf Club', 'Wexford Golf Club'),
    ('Woodenbridge Golf Club', 'Woodenbridge Golf Club'),
    ('Waterville Golf Links', 'Waterville Golf Links'),
    ('Whitehead Golf Club', 'Whitehead Golf Club'),
    ('Woodstock Golf & Country Club', 'Woodstock Golf & Country Club'),
    ('West Waterford Golf Club', 'West Waterford Golf Club'),
    ('Wicklow Golf Club', 'Wicklow Golf Club'),
    ('Youghal Golf Club', 'Youghal Golf Club')

]

STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    course_name = models.CharField(
        max_length=200, choices=choices, default='Abbeyleix Golf Club')
    slug = models.SlugField(max_length=200, null=True,
                            blank=True, unique=True)
    author = models.ForeignKey(
        User, default=None, on_delete=models.CASCADE, related_name="blog_posts")
    featured_image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)
    review = models.TextField(blank=True)
    handicap = models.IntegerField(default=18)
    tees_played_off = models.CharField(max_length=10, default="white")
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.course_name

    def number_of_likes(self):
        return self.likes.count()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.id)
        super().save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
