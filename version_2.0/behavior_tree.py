# The basics arguments are: (agend, territory, light, temperature)
# The derived arguments are: (whatever need)

class IntermediateNode(object):
    """Super clase para extender los nodos intermedios"""
    def __init__(self, nodes):
        self.nodes = nodes

    def run(self, basic_args, derived_args):
        pass


class LeafNode(object):
    """Super clase para extender los nodos hoja"""
    def run(self, basic_args, derived_args):
        pass

class SequenceNode(IntermediateNode):
    """Los nodos secuencia sólo retornan verdadero si todos sus nodos hoja retornan verdadero."""
    def __init__(self, nodes):
        super(SequenceNode, self).__init__(nodes)

    def run(self, basic_args, derived_args):
        answer = (True, derived_args)
        for node in self.nodes:
            answer = node.run(basic_args, answer[1])
            if not answer[0]:
                return (False, None)
        return answer
        
class SelectorNode(IntermediateNode):
    """Los nodos secuencia sólo retornan verdadero si todos sus nodos hoja retornan verdadero."""
    def __init__(self, nodes):
        super(SelectorNode, self).__init__(nodes)

    def run(self, basic_args, derived_args):
        answer = (True, derived_args)
        for node in self.nodes:
            answer = node.run(basic_args, answer[1])
            if answer[0]:
                return answer
        return (False, None)

# Nodos hoja
# Descansar
class Goodplace(LeafNode):
    def run(self, basic_args, derived_args):
        return (basic_args[0].is_good_place_to_rest(basic_args[1], basic_args[3]), None)

class GetPlaces(LeafNode):
    def run(self, basic_args, derived_args):
        places = basic_args[0].get_places(basic_args[1])
        return (bool(places), places)

class ChooseGoodPlace(LeafNode):
    def run(self, basic_args, derived_args):
        return (True, basic_args[0].to_choose_good_place(derived_args))

# Procrear
class TherePartners(LeafNode):
    def run(self, basic_args, derived_args):
        partners = basic_args[0].are_there_any_partners(basic_args[1])
        return (bool(partners), partners)

class ChoosePartner(LeafNode):
    def run(self, basic_args, derived_args):
        return (True, basic_args[0].to_choose_partner(derived_args))

class SearchPartner(LeafNode):
    def run(self, basic_args, derived_args):
        return (True, basic_args[0].to_search_partner(derived_args))

# Protegerse
class DetectDanger(LeafNode):
    def run(self, basic_args, derived_args):
        agressors = basic_args[0].to_detect_danger(basic_args[1])
        return (bool(agressors), agressors)

class EvaluatedConfrontation(LeafNode):
    def run(self, basic_args, derived_args):
        return (basic_args[0].to_evaluadted_confrontation(derived_args), derived_args)

class ChooseEnemy(LeafNode):
    def run(self, basic_args, derived_args):
        return (True, basic_args[0].to_choose_enemy_to_attack(derived_args))


# Recolectar
class HaveSpaceBag(LeafNode):
    def run(self, basic_args, derived_args):
        return (basic_args[0].have_space_in_bag(), None)

class ThereFood(LeafNode):
    def run(self, basic_args, derived_args):
        aliments = basic_args[0].are_there_any_food(basic_args[1])
        return (bool(aliments), aliments)

class ChooseFood(LeafNode):
    def run(self, basic_args, derived_args):
        return (True, basic_args[0].to_choose_food(derived_args))

class SearchFood(LeafNode):
    def run(self, basic_args, derived_args):
        return (True, basic_args[0].to_search_food(derived_args))

class TherePrey(LeafNode):
    def run(self, basic_args, derived_args):
        preys = basic_args[0].are_there_any_prey(basic_args[1])
        return (bool(preys), preys)

class ChoosePrey(LeafNode):
    def run(self, basic_args, derived_args):
        return (True, basic_args[0].to_choose_prey(derived_args))


# Comer
class HaveFood(LeafNode):
    def run(self, basic_args, derived_args):
        return (basic_args[0].to_have_food(), None)


# Alimentar
class ThereOffspring(LeafNode):
    def run(self, basic_args, derived_args):
        offspring = basic_args[0].are_there_any_offspring(basic_args[1])
        return (bool(offspring), offspring)

class ChooseOffspring(LeafNode):
    def run(self, basic_args, derived_args):
        return (True, basic_args[0].to_choose_offspring_to_feed(derived_args))


# Nodos Acción
class ToRest(LeafNode):
    def run(self, basic_args, derived_args):
        return (True, ("To Rest",))
        
class ToMove(LeafNode):
    def run(self, basic_args, derived_args):
        return (True, ("To Move", derived_args))

class ToProcreate(LeafNode):
    def run(self, basic_args, derived_args):
        return (True, ("To Procreate", derived_args))

class ToAttack(LeafNode):
    def run(self, basic_args, derived_args):
        return (True, ("To Attack", derived_args))

class ToEscape(LeafNode):
    def run(self, basic_args, derived_args):
        return (True, ("To Escape", derived_args))    

class ToCollect(LeafNode):
    def run(self, basic_args, derived_args):
        return (True, ("To Collect", derived_args))

class ToEat(LeafNode):
    def run(self, basic_args, derived_args):
        return (True, ("To Eat", derived_args))

class ToFeed(LeafNode):
    def run(self, basic_args, derived_args):
        return (True, ("To Feed", derived_args))

# need_to_rest_tree = SelectorNode([
#     SequenceNode([
#         Goodplace(),
#         ToRest()
#     ]),
#     SequenceNode([
#         GetPlaces(),
#         ChooseGoodPlace(),
#         ToMove()
#     ])
# ])

# need_to_procreate_tree = SelectorNode([
#     SequenceNode([
#         TherePartners(),
#         ChoosePartner(),
#         ToProcreate()
#     ]),
#     SequenceNode([
#         GetPlaces(),
#         SearchPartner(),
#         ToMove()
#     ])
# ])

# need_to_protect_oneself_tree = SelectorNode([
#     SequenceNode([
#         DetectDanger(),
#         EvaluatedConfrontation(),
#         ChooseEnemy(),
#         ToAttack()
#     ]),
#     SequenceNode([
#         GetPlaces(),
#         ChooseGoodPlace(),
#         ToEscape()
#     ])
# ])

# need_to_collect_tree = SelectorNode([
#     SequenceNode([
#         HaveSpaceBag(),
#         ThereFood(),
#         ChooseFood(),
#         ToCollect()
#     ]),
#     SequenceNode([
#         TherePrey(),
#         ChoosePrey(),
#         ToAttack()
#     ]),
#     SequenceNode([
#         GetPlaces(),
#         SearchFood(),
#         ToMove()
#     ])
# ])

# need_to_eat_tree = SelectorNode([
#     SequenceNode([
#         HaveFood(),
#         ToEat()
#     ]),
#     need_to_collect_tree
# ])

# need_to_feed_tree = SelectorNode([
#     SequenceNode([
#         HaveFood(),
#         ThereOffspring(),
#         ChooseOffspring(),
#         ToFeed()
#     ]),
#     need_to_collect_tree
# ])