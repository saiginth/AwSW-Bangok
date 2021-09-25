from modloader import modinfo
from modloader.modclass import Mod, loadable_mod

def bryce1_afterparty(ml):
    wake_menu = ml.find_label('waitmenu') \
        .search_menu("I would, but I don't think I can beat someone like you.") \
        .search_menu("I'm not buzzed.") \
        .search_menu("I'm having a drinking contest with a dragon. How could I not love this?") \
        .search_menu("That's my tactic, make you think that I'm struggling so you'll let your guard down.") \
        .search_menu("Maybe. Having a lil' fun doesn't hurt, right?") \
        .search_menu("Why are you so damn attractive?") \
        .search_menu("Mine.") \
        .search_menu("S-Suck on this, you ssscaly bastard.") \
        .search_menu("If you think I'm giving up, you're mistaken. This isn't over.") \
        .search_menu("I know when I've had enough, and it's now.") \
        .search_menu("Fine...") \
        .search_menu("Put some pepper on his nose.")
    
    wake_menu.add_choice("Poke him someplace special.",jump='bangok_four_bryce1_poke',condition='persistent.nsfwtoggle == True')

    wake_menu.link_behind_from('bangok_four_bryce1_nevermind')

class AWSWModNew(Mod):
    @classmethod
    def mod_info(cls):
        if not all(hasattr(cls,attr) for attr in ['name','author','version']):
            raise NotImplementedError("One of name, author, or version fields is missing!")
        return (cls.name, cls.author, cls.version, getattr(cls,'nsfw',False))

@loadable_mod
class BangOk(AWSWModNew):
    name = "BangOk?"
    version = "v0.0"
    author = "4onen"
    nsfw = True

    def mod_load(self):
        ml = modinfo.get_mods()["MagmaLink"].import_ml()
        bryce1_afterparty(ml)

    @staticmethod
    def mod_complete():
        pass