class Event:


    def __init__(self, eventId, name, organizer, startDate, startTime, endDate, endTime, seatAvailable, registeredUserIds):
        self.eventId = eventId
        self.name = name
        self.organizer = organizer
        self.startDate = startDate
        self.startTime =  startTime
        self.endDate = endDate
        self.endTime = endTime
        self.seatAvailable = seatAvailable
        self.registeredUserIds = registeredUserIds

    def __str__(self):
        return f"eventId : {self.eventId} \nname : {self.name} \norganiser : {self.organizer} \nstartDate : {self.startDate} \nstartTime : {self.startTime} \nendDate : {self.endDate} \nendTime : {self.endTime} \ntotalRegisteredUsers : {self.totalRegisteredUsers} \nseatAvailable : {self.seatAvailable}"

    def set_eventId(self,eventId):
         self.eventId = eventId

    def get_eventId(self):
        return self.eventId

    def set_name(self,name):
        self.name = name

    def get_name(self):
        return self.name

    def set_organiser(self,organiser):
         self.organizer = organiser

    def get_organiser(self):
        return self.organizer

    def set_startDate(self,startDate):
         self.startDate = startDate

    def get_startDate(self):
        return self.startDate

    def set_startTime(self,startTime):
         self.startTime = startTime

    def get_startTime(self):
        return self.startDate

    def set_endDate(self,endDate):
         self.endDate = endDate

    def get_endDate(self):
        return self.endDate

    def set_endTime(self,endTime):
         self.endTime = endTime

    def get_endTime(self):
        return self.endTime

    # def set_totalRegisteredUsers(self,totalRegisteredUsers):
    #      self.totalRegisteredUsers = totalRegisteredUsers

    # def get_totalRegistyeredUsers(self):
    #     return self.totalRegisteredUsers

    def set_seatAvailable(self,seatAvailable):
         self.seatAvailable = seatAvailable

    def get_seatAvailble(self):
        return self.seatAvailable

    def set_registeredUserIds(self, registeredUserIds):
        self.registeredUserIds  = registeredUserIds
    
    def get_registeredUserIds(self):
        return self.registeredUserIds