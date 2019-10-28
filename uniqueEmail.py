class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for email in emails:
            part = email.split("@")
            local = part[0].split("+")
            local = local[0]
            local = local.replace(".","")
            unique.add(local+"@"+part[1])
        return len(unique)