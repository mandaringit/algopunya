class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()

        for email in emails:
            local, domain = email.split("@")
            local = local.split("+")[0].replace(".", "")
            unique_emails.add(local + "@" + domain)

        """
        for email in emails:
            local, domain = email.split("@")
            new_local = []
            for char in local:
                if char == ".":
                    continue
                elif char == "+":
                    break
                else:
                    new_local.append(char)

            filterd_email = "".join(new_local) + "@" + domain
            unique_emails.add(filterd_email)
        """

        return len(unique_emails)
