from backend.context.log_schema import LogSchema


class LogAnalysisService:

    def analyze(
        self,
        connector_type: str,
        table_name: str,
        sample_logs: list[dict],
    ) -> LogSchema:

        if connector_type == "native":

            return LogSchema(

                table_name=table_name,

                platform="Microsoft Sentinel",

                parser="Native",

                columns=[],

            )

        if not sample_logs:

            return LogSchema(

                table_name=table_name,

                platform="Custom",

                parser="JSON",

            )

        sample = sample_logs[0]

        columns = []

        for key, value in sample.items():

            columns.append({

                "name": key,

                "type": type(value).__name__,

            })

        return LogSchema(

            table_name=table_name,

            platform="Custom",

            parser="AI",

            columns=columns,

            timestamp_field=self.find_timestamp(sample),

            event_field=self.find_event(sample),

            user_field=self.find_user(sample),

            ip_field=self.find_ip(sample),

            host_field=self.find_host(sample),

        )

    def find_timestamp(self, sample):

        fields = [
            "TimeGenerated",
            "Timestamp",
            "Time",
            "Date",
        ]

        return self.find(sample, fields)

    def find_event(self, sample):

        fields = [
            "EventID",
            "EventCode",
            "Status",
            "Action",
        ]

        return self.find(sample, fields)

    def find_user(self, sample):

        fields = [
            "User",
            "Account",
            "UserName",
        ]

        return self.find(sample, fields)

    def find_ip(self, sample):

        fields = [
            "IPAddress",
            "IP",
            "SourceIP",
        ]

        return self.find(sample, fields)

    def find_host(self, sample):

        fields = [
            "Computer",
            "Host",
            "Hostname",
        ]

        return self.find(sample, fields)

    def find(
        self,
        sample,
        fields,
    ):

        for field in fields:

            if field in sample:

                return field

        return ""


log_analysis_service = LogAnalysisService()