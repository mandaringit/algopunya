class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:

        counter = {}

        for domain in cpdomains:
            count, website = domain.split(" ")
            parts = website.split(".")

            for i in range(len(parts) - 1, -1, -1):
                subdomain = ".".join(parts[i:])
                if subdomain in counter:
                    counter[subdomain] += int(count)
                else:
                    counter[subdomain] = int(count)

        return [f"{counter[key]} {key}" for key in counter]
