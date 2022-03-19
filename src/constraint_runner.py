from constraint_id import ConstraintManager

filePath = 'freecad_saves/sketcher_named_constraints.FCStd'

cm = ConstraintManager(filePath)

cm.print_constraints()
cm.save_constraints('./data/old_constraints.json')

cm.set_constraint('Rise', 50)
cm.set_constraint('Run', 100)

cm.print_constraints()
cm.save_doc('./freecad_saves/named_constraints_new.FCStd')
cm.save_constraints('./data/new_constraints.json')