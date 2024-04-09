import uuid

from dagger import dag, function, object_type


@object_type
class DaggerIssue:
    @function
    async def container_echo(self) -> str:
        return await (
            dag.container()
            .from_("busybox:stable-uclibc")
            .with_env_variable("CACHE_BUSTER", uuid.uuid4().hex)
            .with_exec(["sh", "-c", "for i in $(seq 1 10); do echo $i; sleep 1; done"])
            .stdout()
        )
