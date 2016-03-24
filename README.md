tribeHacks2014
==============
# This program analyzes a CSV that contains data of how potential mentors (bigs)
# ranked mentees (littles) and vice versa. It assumes that the number of bigs is
# greater than or equal to the number of littles. Therefore, each little is 
# guaranteed a big. However, each potential big is not guaranteed to be matched 
# with a little. The maximum number of persons that can be preffed is 10, and 
# the minimum is 5. A form for creating the correctly formatted CSV can be found
# at https://docs.google.com/forms/d/17Cu4RSMUK2A_UN2OvHcysxIlv4rwVuZw0dvVqd5csMI/viewform

# Bigs and littles are both stored as instances of a Person class.
# Big and little objects are stored in two dictionaries respectively, so that
# their preferences are accessible by their name. A scores matrix totals the 
# mutual preference values, giving added weight to how a little ranked a big.
# In the case of a tie, matching is determined by how the little ranked the big.

# MentorMatch was developed with the Big/Little relationships associated with 
# sorority and fraternity life in mind. However, it can be used for mutually 
# preferenced mentor/mentee pairings in any organization, sports team, or 
# workplace. It allows for an anonymous submission of rankings by members and a 
# fair, mathematical matching process. 
