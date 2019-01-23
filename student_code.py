import read, copy
from util import *
from logical_classes import *


class KnowledgeBase(object):
    def __init__(self, facts=[], rules=[]):
        self.facts = facts
        self.rules = rules

    def __repr__(self):
        return 'KnowledgeBase({!r}, {!r})'.format(self.facts, self.rules)

    def __str__(self):
        string = "Knowledge Base: \n"
        string += "\n".join((str(fact) for fact in self.facts)) + "\n"
        string += "\n".join((str(rule) for rule in self.rules))
        return string

    def kb_assert(self, fact):
        """Assert a fact or rule into the KB

        Args:
            fact (Fact or Rule): Fact or Rule we're asserting in the format produced by read.py
        """
        #Check that argument is a fact
        #Check if fact is already in the KB
        if factq(fact.name):
            if fact in self.facts: return
            else: self.facts.append(fact)
        else: return

        print("Asserting {!r}".format(fact))
        
    def kb_ask(self, fact):
        """Ask if a fact is in the KB

        Args:
            fact (Fact) - Fact to be asked

        Returns:
            ListOfBindings|False - ListOfBindings if result found, False otherwise
        """
        given_state = fact.statement
        new_list = ListOfBindings()

        #if fact in self.facts:
        for f in self.facts:
            bindings_found = match(given_state, f.statement)
            if not bindings_found: continue #if match returns False
            else:
                new_list.add_bindings(bindings_found,f)
        # Return False if there are no matching facts (thus ListOfBindings would be an empty list
        if len(new_list) == 0: return False
        else:
            return new_list
        #else:

        print("Asking {!r}".format(fact))
