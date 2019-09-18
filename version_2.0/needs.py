from behavior_tree import *

need_to_rest_tree = SelectorNode([
    SequenceNode([
        Goodplace(),
        ToRest()
    ]),
    SequenceNode([
        GetPlaces(),
        ChooseGoodPlace(),
        ToMove()
    ])
])

need_to_procreate_tree = SelectorNode([
    SequenceNode([
        TherePartners(),
        ChoosePartner(),
        ToProcreate()
    ]),
    SequenceNode([
        GetPlaces(),
        SearchPartner(),
        ToMove()
    ])
])

need_to_protect_oneself_tree = SelectorNode([
    SequenceNode([
        DetectDanger(),
        EvaluatedConfrontation(),
        ChooseEnemy(),
        ToAttack()
    ]),
    SequenceNode([
        GetPlaces(),
        ChooseGoodPlace(),
        ToEscape()
    ])
])

need_to_collect_tree = SelectorNode([
    SequenceNode([
        HaveSpaceBag(),
        ThereFood(),
        ChooseFood(),
        ToCollect()
    ]),
    SequenceNode([
        TherePrey(),
        ChoosePrey(),
        ToAttack()
    ]),
    SequenceNode([
        GetPlaces(),
        SearchFood(),
        ToMove()
    ])
])

need_to_eat_tree = SelectorNode([
    SequenceNode([
        HaveFood(),
        ToEat()
    ]),
    need_to_collect_tree
])

need_to_feed_tree = SelectorNode([
    SequenceNode([
        HaveFood(),
        ThereOffspring(),
        ChooseOffspring(),
        ToFeed()
    ]),
    need_to_collect_tree
])